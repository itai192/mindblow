def compile(code: str) -> bytes:
    compiled_num = code.count("🤯")
    return compiled_num.to_bytes((compiled_num.bit_length() + 7) // 8, byteorder="big")


def decompile(exe: bytes) -> str:
    return int.from_bytes(exe, "big") * "🤯"
