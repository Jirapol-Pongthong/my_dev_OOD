def encode_char(ch, rotor_position, n):
    if not ch.isalpha():
        return ch
    step = (rotor_position + n) % 26
    if step == 0:
        step = 1
    base = ord('a') if ch.islower() else ord('A')
    return chr((ord(ch) - base + step) % 26 + base)

def decode_char(ch, rotor_position, n):
    if not ch.isalpha():
        return ch
    step = (rotor_position + n) % 26
    if step == 0:
        step = 1
    base = ord('a') if ch.islower() else ord('A')
    return chr((ord(ch) - base - step) % 26 + base)

def encode_message(message, rotor_position, index=0, n=0, carry=0):
    if index >= len(message):
        return ""

    step0 = (rotor_position + carry + n) % 26
    ch = encode_char(message[index], rotor_position + carry, n)
    
    next_carry = carry + 1 if message[index].isalpha() and step0 == 0 else carry
    return ch + encode_message(message, rotor_position, index + 1, n + 1, next_carry)

def decode_message(message, rotor_position, index=0, n=0, carry=0):
    if index >= len(message):
        return ""
    step0 = (rotor_position + carry + n) % 26
    ch = decode_char(message[index], rotor_position + carry, n)
    next_carry = carry + 1 if message[index].isalpha() and step0 == 0 else carry
    return ch + decode_message(message, rotor_position, index + 1, n + 1, next_carry)

# การใช้งาน
print("This is Caesar cipher")
message ,initial_rotor_position = input("Enter Input : ").split(',')
encoded = encode_message(message, int(initial_rotor_position))
print("Encoded Message:",encoded)
decoded = decode_message(encoded, int(initial_rotor_position))
print("Decoded Message:", decoded)