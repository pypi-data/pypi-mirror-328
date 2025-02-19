import torch


@torch.library.register_fake("flute::qgemm_raw_simple")
def _qgemm_raw_simple_abstract(
    input: torch.Tensor,
    weight: torch.Tensor,
    scales: torch.Tensor,
    table: torch.Tensor,
    table2: torch.Tensor,
    workspace: torch.Tensor,
    num_bits: int,
    group_size: int,
    template_id: int,
    num_sms: int,
) -> torch.Tensor:
    if not all([
        input.ndim >= 2,
        weight.ndim == 2,
        scales.ndim == 2,
        table.ndim == 1,
        table2.ndim == 3,
        workspace.ndim == 1,
    ]):
        raise ValueError

    dtype = input.dtype
    if dtype not in [torch.float16, torch.bfloat16]:
        raise TypeError

    if not all([
        weight.dtype == torch.int16,
        scales.dtype == dtype,
        table.dtype == dtype,
        table2.dtype == torch.float32,
        workspace.dtype == torch.uint8,
    ]):
        raise TypeError

    if not all([
        weight.shape[1] == input.shape[-1],  # K
        weight.shape[1] == scales.shape[1] * group_size,  # K
        weight.shape[0] == int(num_bits * (scales.shape[0] / 16)),  # P
        table.shape[0] == 2 ** num_bits,
        table2.shape[0] == 2 ** num_bits,
        table2.shape[1] == 2 ** num_bits,
        table2.shape[2] == 1,
    ]):
        raise ValueError

    N = scales.shape[0]
    return torch.empty(
        input.shape[:-1] + (N,),
        dtype=input.dtype,
        device=input.device)


@torch.library.register_fake("flute::qgemm_raw_simple_hadamard")
def _qgemm_raw_simple_hadamard_abstract(
    input: torch.Tensor,
    weight: torch.Tensor,
    scales: torch.Tensor,
    table: torch.Tensor,
    table2: torch.Tensor,
    workspace: torch.Tensor,
    num_bits: int,
    group_size: int,
    hadamard_size: int,
    template_id: int,
    num_sms: int,
) -> torch.Tensor:
    return _qgemm_raw_simple_abstract(
        input=input,
        weight=weight,
        scales=scales,
        table=table,
        table2=table2,
        workspace=workspace,
        num_bits=num_bits,
        group_size=group_size,
        template_id=template_id,
        num_sms=num_sms,
    )
