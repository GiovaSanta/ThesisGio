import numpy as np
import ml_dtypes 

hexVal = 0x01

# Use uint8 to hold the raw byte
raw_byte = np.array([hexVal], dtype=np.uint8)

# Cast it to float8_e4m3
decoded_val1 = raw_byte.view(ml_dtypes.float8_e4m3)
decoded_val2 = raw_byte.view(ml_dtypes.float8_e3m4)

print('{:#04x} understood as FP8_e4m3: {} '.format(hexVal, decoded_val1[0]))  # This gives you the decimal interpretation
print('{:#04x} understood as FP8_e3m4: {} '.format(hexVal, decoded_val2[0]))  # This gives you the decimal interpretation

print('the multiplication between the decoded values: {}'.format( float(decoded_val1[0]) * float(decoded_val2[0])) )

# Your decimal number
decimal_number = 1.5 
# Encode: create a numpy array of float8_e4m3 type
encoded = np.array([decimal_number], dtype=ml_dtypes.float8_e4m3)

# Now view the bits (uint8) to see the actual 8-bit hex value
encoded_hex = encoded.view(np.uint8)[0]

print(f"Decimal {decimal_number} encoded as float8_e4m3 → hex: {encoded_hex:#04x}")


