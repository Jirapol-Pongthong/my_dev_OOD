def encode_char(ch, rotor_position, n):
    if not ch.isalpha():
        return ch
    
    step = (rotor_position + n) % 26
    base = ord('a') if ch.islower() else ord('A')
    
    if step == 0 and rotor_position != 0:
        step = 1
    
    return chr((ord(ch) - base + step) % 26 + base)

def decode_char(ch, rotor_position, n):
    if not ch.isalpha():
        return ch
    
    step = (rotor_position + n) % 26
    base = ord('a') if ch.islower() else ord('A')
    
    if step == 0 and rotor_position != 0:
        step = 1
    
    return chr((ord(ch) - base - step) % 26 + base)

def encode_message(message, rotor_position, index=0, n=0):
    if index >= len(message):
        return ""
    return encode_char(message[index], rotor_position, n) + encode_message(message, rotor_position, index+1, n+1)

def decode_message(message, rotor_position, index=0, n=0):
    if index >= len(message):
        return ""
    return decode_char(message[index], rotor_position, n) + decode_message(message, rotor_position, index+1, n+1)

# Test cases
test_cases = [
    ("abc", 1),
    ("abc", 27),
    ("abc", 26),
    ("abc", 0),
    ("abc", -1),
    ("AbC", 2),
    ("a c", 1),
    ("a1c!", 1),
    ("xyz", 3),
    ("XYZ", 3),
    ("", 5),
    ("abcdefghijklmnopqrstuvwxyz", 1)
]

print("Testing Caesar Cipher encode/decode:")
for msg, rot in test_cases:
    encoded = encode_message(msg, rot)
    decoded = decode_message(encoded, rot)
    status = "PASS" if decoded == msg else "FAIL"
    print(f"Input: '{msg}' Rotor: {rot} -> Encoded: '{encoded}' Decoded: '{decoded}' [{status}]")
