import numpy as np
from ml_dtypes import float8_e4m3

# --- Decode an 8-bit value (hex) to a decimal float ---
def decode_fp8(val):
    """
    Convert a raw 8-bit integer to its corresponding float8_e4m3 decimal value.
    
    Parameters:
        val (int): 8-bit value (0-255)

    Returns:
        float8_e4m3: The interpreted float value
    """
    return np.frombuffer(np.uint8(val).tobytes(), dtype=float8_e4m3)[0]

# --- Encode a decimal float to a raw 8-bit value (as hex) ---
def encode_fp8(f):
    """
    Convert a decimal value to its 8-bit float8_e4m3 representation.
    
    Parameters:
        f (float or float8_e4m3): The float to encode

    Returns:
        int: 8-bit representation (0-255)
    """
    return np.frombuffer(float8_e4m3(f).tobytes(), dtype=np.uint8)[0]


# --- Example usage ---
if __name__ == "__main__":
    # From raw byte to float
    raw = 0x10
    decoded = decode_fp8(raw)
    print(f"0x{raw:02X} → {decoded} (decoded)")

    # From float to raw byte
    value = 1.5
    encoded = encode_fp8(value)
    print(f"{value} → 0x{encoded:02X} (encoded)")

