def caesar_decode(message, offset):
    alphabet = "abcdefghijklmnopqrstuvwxyz"
    new_message = ""
    for letter in message:
        #If letter is space
        if letter in ",.! '":
            new_message = new_message + letter
            continue

        index_letter = alphabet.find(letter)
        decoded_index_letter = index_letter + offset

        #If index is out of range
        if decoded_index_letter > len(alphabet)-1:
            decoded_index_letter -= len(alphabet)

        new_message = new_message + alphabet[decoded_index_letter]

    print(new_message, offset)

def brute_force_decoder(message):
    for num in range(0, 26):
        caesar_decode(message, num)

brute_force_decoder("vhfinmxkl atox kxgwxkxw tee hy maxlx hew vbiaxkl hulhexmx. px'ee atox mh kxteer lmxi ni hnk ztfx by px ptgm mh dxxi hnk fxlltzxl ltyx.")




def encoder(message, key):
    alphabet = "abcdefghijklmnopqrstuvwxyz"
    new_message_send = ""
    for letter in message:
        #If letter is space
        if letter in ",.! ":
            new_message_send = new_message_send + letter
            continue

        index_letter = alphabet.find(letter)
        decoded_index_letter = index_letter - key

        #If index is out of range
        if decoded_index_letter < 0:
            decoded_index_letter += len(alphabet)

        new_message_send = new_message_send + alphabet[decoded_index_letter]

    print(new_message_send)


encoder("hey", 10)