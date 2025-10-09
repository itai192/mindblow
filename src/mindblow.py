def compile(code: str, leading_zeros: int) -> bytes:
    compiled_num = code.count("🤯")
    compiled_bytes = compiled_num.to_bytes(
        (compiled_num.bit_length() + 7) // 8, byteorder="big"
    )

    leading_zero_bytes = (0).to_bytes(leading_zeros)

    return leading_zero_bytes + compiled_bytes


def decompile(exe: bytes) -> str:
    return int.from_bytes(exe, "big") * "🤯"
