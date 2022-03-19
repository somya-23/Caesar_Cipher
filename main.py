from logo import caesar_logo

alphabet=['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']

def caesar(start_text,shift_amount,operation):
    end_text=""
    if operation=='decode':
        shift_amount*=-1
    for letter in start_text:
        if letter not in alphabet:
            end_text+=letter
        else:
            end_text+= alphabet[(26+((alphabet.index(letter)+shift_amount)%26))%26]
    return end_text

def perform_encoding_decoding():
    operation=input("Type 'encode' to encrypt, Type 'decode' to decrypt: ")
    message = input("Type your message ").lower()
    shift = int(input("Type the shift number "))
    print(f"The {operation}d is: {caesar(message,shift,operation)}")

should_continue=True
print(caesar_logo)
while should_continue:
    perform_encoding_decoding()
    decision=input("type 'yes' if you like to continue or 'no' to stop ")
    if decision=='no':
        should_continue=False






