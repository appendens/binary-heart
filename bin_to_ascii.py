def bin_to_ascii(bin_str):
    """Return ASCII string from binary."""
    n = int(bin_str, 2)
    asc_str = n.to_bytes((n.bit_length() + 7) // 8, 'big').decode()
    return asc_str
