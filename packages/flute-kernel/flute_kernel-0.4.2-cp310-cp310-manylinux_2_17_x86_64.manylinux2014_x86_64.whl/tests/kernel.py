import copy
import click
import torch
import argparse
from tqdm.auto import tqdm

import flute
import flute.tune
import flute.utils
from tests.shapes import SUPPORTED_SHAPES

FP16_ERROR_THRESHOLD = 2.0e-3
BF16_ERROR_THRESHOLD = 1.1e-2


# 2/4
def test_integer(
    M: int,
    N: int,
    K: int,
    num_bits: int,
    group_size: int,
    dtype: torch.dtype,
    uniform: bool,
    identity: bool,
) -> None:
    device = torch.device("cuda")
    G = int(K / group_size)

    if identity is True:
        if M != K:
            raise ValueError
        A = torch.eye(
            M,
            dtype=dtype,
            device=device)
    else:
        A = torch.randn(
            (M, K),
            dtype=dtype,
            device=device) / 100.

    W = torch.randint(
        0, 2 ** num_bits - 1,
        (K, N),
        dtype=torch.int64,
        device=device)

    S = torch.randn(
        (N, G),
        dtype=dtype,
        device=device)

    if uniform is True:
        qmap = torch.arange(
            2 ** num_bits,
            dtype=dtype,
            device=device)
    else:
        qmap = torch.randn(
            2 ** num_bits,
            dtype=dtype,
            device=device)

    qmap2 = flute.utils.make_qmap2_from_qmap(qmap)
    workspace = flute.utils.make_workspace_streamk(device=device)

    # ground truth
    W_ = qmap[W]
    S_ = torch.repeat_interleave(S, group_size, dim=1).T
    D_ = torch.mm(A, W_ * S_)

    Q, tune_metadata = flute.tune.tune_and_pack(
        inputs=A,
        weight=W,
        num_bits=num_bits,
        group_size=group_size)

    D = flute.qgemm(
        A,
        Q,
        S,
        qmap,
        qmap2,
        workspace,
        num_bits,
        group_size,
        tune_metadata.template_id,
        tune_metadata.num_sms)

    equal = (D_ == D).all().item()
    error  = ((D_ - D).norm() / D .norm()).item()
    error_ = ((D_ - D).norm() / D_.norm()).item()
    message = (
        f"M={str(M):<5} "
        f"N={str(N):<5} "
        f"K={str(K):<5} "
        f"num_bits={str(num_bits):<5} "
        f"group_size={str(group_size):<5} "
        f"dtype={str(dtype):<15} "
        f"uniform={str(uniform):<5} "
        f"error={error:.3e} "
        f"error_={error_:.3e}")

    if identity is True:
        if equal is not True:
            click.secho(message, bg="red")
    else:
        if dtype == torch.float16:
            threshold = FP16_ERROR_THRESHOLD
        elif dtype == torch.bfloat16:
            threshold = BF16_ERROR_THRESHOLD
        else:
            raise NotImplementedError

        if error > threshold or error_ > threshold:
            data_to_save = {
                "A": A,
                "Q": Q,
                "S": S,
                "qmap": qmap,
                "qmap2": qmap2,
                # "workspace": workspace,
                "W": W,
                "W_": W_,
                "S_": S_,
                "D_": D_,
                "D": D,
                "D_": D_,
                "error": error,
                "error_": error_,
            }
            # torch.save(data_to_save, f"{message}.pth")
            click.secho(message, fg="red")


@torch.no_grad()
def run_tests(num: int) -> None:
    for index in range(num):
        torch.manual_seed(index)

        for N, K in tqdm(SUPPORTED_SHAPES):
            for num_bits in [2, 3, 4]:
                # for group_size in [32, 64, 128, 256]:
                for group_size in [64, 128, 256]:
                    for dtype in [torch.float16, torch.bfloat16]:
                        for uniform in [True, False]:

                            test_integer(
                                M=K,
                                N=N,
                                K=K,
                                num_bits=num_bits,
                                group_size=group_size,
                                dtype=dtype,
                                uniform=uniform,
                                identity=True)

                            for M in [1, 3, 32, 53, 64, 1024]:
                                test_integer(
                                    M=M,
                                    N=N,
                                    K=K,
                                    num_bits=num_bits,
                                    group_size=group_size,
                                    dtype=dtype,
                                    uniform=uniform,
                                    identity=False)


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--num", type=int, default=10)
    args = parser.parse_args()

    run_tests(num=args.num)
