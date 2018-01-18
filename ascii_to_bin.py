def ascii_to_bin(ascii_str):
    """Return binary string from ASCII."""
    bin_str = bin(int.from_bytes(ascii_str.encode(), 'big'))
    return bin_str
