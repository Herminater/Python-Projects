def vigenere_decode(message, keyword):
    alphabet = "abcdefghijklmnopqrstuvwxyz"
    new_message = ""
    offset_counter = 0
    
    for letter in message:
        #If letter is space
        if letter in ",.! '?":
            new_message = new_message + letter
            continue

        #calculate offsett
        
        if offset_counter > len(keyword)-1:
            offset_counter -= len(keyword)

        offset_letter = keyword[offset_counter]
        offset = alphabet.find(offset_letter)

        offset_counter += 1


        #find letter with ofsett
        index_letter = alphabet.find(letter)
        decoded_index_letter = index_letter + offset

        #If index is out of range
        if decoded_index_letter > len(alphabet)-1:
            decoded_index_letter -= len(alphabet)

        new_message = new_message + alphabet[decoded_index_letter]
    print(new_message)
    return new_message   

vigenere_decode("aee uwsiv. uah hvm hbvzo gbgz", "Kaffe")





def vigenere_encode(message, keyword):
    alphabet = "abcdefghijklmnopqrstuvwxyz"
    new_message = ""
    offset_counter = 0
    
    for letter in message:
        #If letter is space
        if letter in ",.! '?":
            new_message = new_message + letter
            continue

        #calculate offsett
        
        if offset_counter > len(keyword)-1:
            offset_counter -= len(keyword)

        offset_letter = keyword[offset_counter]
        offset = alphabet.find(offset_letter)

        offset_counter += 1


        #find letter with ofsett
        index_letter = alphabet.find(letter)
        decoded_index_letter = index_letter - offset

        #If index is out of range
        if decoded_index_letter < 0:
            decoded_index_letter += len(alphabet)

        new_message = new_message + alphabet[decoded_index_letter]
    #print(new_message)
    return new_message   

#vigenere_encode("Hej Maria. Jeg har lavet kage", "Kaffe")

