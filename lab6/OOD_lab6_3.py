def encode_char(char, rotor_position):
    #coding here

def decode_char(char, rotor_position):
    #coding here

def encode_message(message, rotor_position,index = 0):
    if rotor_position > 26 :
        if message[index].isupper():
            move = rotor_position - 26
            if ord(message[index]) + move > 122 :
                word = (ord(message[index]) + move) - 26

def decode_message(encoded_message, rotor_position):
    #coding here
    pass

# การใช้งาน
print("This is Caesar cipher")
message ,initial_rotor_position = input("Enter Input : ").split(',')
encoded = encode_message(message, int(initial_rotor_position))
print("Encoded Message:",encoded)
decoded = decode_message(encoded, int(initial_rotor_position))
print("Decoded Message:", decoded)