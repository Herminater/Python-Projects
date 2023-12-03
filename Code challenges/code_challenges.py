def unique_english_letters(word):
    unique_letters = ""
    for letter in word:
        if letter in unique_letters:
            continue
        else:
            unique_letters = unique_letters + letter
    
    return len(unique_letters)

        
unique_letters = unique_english_letters("DetteErentest")
#print(unique_letters)


def count_char_x(word, x):
    number_of_appearances = word.count(x)
    print(number_of_appearances)
    return number_of_appearances

count_char_x("enhed", "e")


def count_multi_char_x(word, x):
    number_of_appearances = word.count(x)
    print(number_of_appearances)
    return number_of_appearances

count_multi_char_x("mississippi", "iss")

def substring_between_letters(word, start, end):
    if start in word and end in word:
        start_index = word.find(start) + 1
        end_index = word.find(end)
        substring = word[start_index:end_index]
    else: 
        return word
    return substring

substring_word = substring_between_letters("mississippi", "i", "p")
print(substring_word)


def x_length_words(sentence, x):
    sentence_list = sentence.split(" ")
    for word in sentence_list:
        if len(word) >= x:
            continue
        else:
            return False
    return True

T_F = x_length_words("Jeg har en hat", 2)

print(T_F)


def check_for_name(sentence, name): 
    if name.lower() in sentence.lower():
        return True
    else:
        return False
    
name_variable1 = check_for_name("My name is Jamie", "Jamie")
name_variable2 = check_for_name("My name is jamie", "Jamie")
name_variable3 = check_for_name("My name is JAMIE", "Jamie")

print(name_variable1)
print(name_variable2)
print(name_variable3)


def every_other_letter(word):
    new_word = ""
    for index in range(len(word)):
        if index % 2 != 0:
            new_word += word[index]

    return new_word

print(every_other_letter("Herman"))


def reverse_string(word):
    reversed_word = ""
    for index in range(1,len(word)+1):
        reversed_word += word[-index]

    return reversed_word
print(reverse_string("Herman"))

def make_spoonerism(word1, word2):
    letter1 = ""
    letter2 = ""
    letter1_index = 0
    letter2_index = 0
    for letter in word1:
        if letter.lower() not in "aeiouy":
            letter1 = letter
            letter1_index = word1.find(letter)
            break
    for letter in word2:
        if letter.lower() not in "aeiouy":
            letter2 = letter
            letter2_index = word2.find(letter)
            break
    spoonerism = word1[:letter1_index] + letter2 + word1[letter1_index+1:] + " " + word2[:letter2_index] + letter1 + word2[letter2_index+1 :]
    print(spoonerism)
    return 

make_spoonerism("Abfabetet", "Ofie")

def add_exclamation(word):
    while len(word) < 20:
        word += "!"

    return word

print(add_exclamation("Testhhhhhhhhhhhhhhh"))


def sum_values(my_dictionary):
    sum = 0
    for value in my_dictionary.values():
        sum += value

    return sum


def sum_even_keys(my_dictionary):
    sum = 0 
    for key in my_dictionary.keys():
        if key % 2 == 0:
            sum += my_dictionary[key]
    return sum

test_dic= {"a": 2, "b": 3, "c": 3}
def add_ten(my_dictionary):
    for key in my_dictionary.keys():
        my_dictionary[key] += 10

    return my_dictionary

print(add_ten(test_dic))


#This one is weird. This should be the sollution though..
def values_that_are_keys(my_dictionary):
    value_keys = []
    for key in my_dictionary.keys():
        for value in my_dictionary.values():
            if key == value:
                value_keys.append(value)
    return value

test_dic= {"a": "a", "2": 3, "c": 3}

print(values_that_are_keys(test_dic))


def max_key(my_dictionary):
    mx_key = 0
    for key in my_dictionary.keys():
        if my_dictionary[key] > mx_key:
            max_key = key
    return max_key
    
test_dic2= {"a": 9, "f": 3, "c": 3}
print(max_key(test_dic2))


def word_length_dictionary(words):
    new_dic = {}
    for word in words:
        new_dic[word] = len[word]
    return new_dic

#Test sollution pls
def frequency_dictionary(words):
    new_dic = {}
    for element in words:
        if element in new_dic:
            continue
        else:
            new_dic[element] = words.count(element)
    return element

def unique_values(my_dictionary):
    unique_values = []
    for key in my_dictionary.keys():
        if key in unique_values:
            continue
        else:
            unique_values.append(key)
    return len(unique_values)


#Forstod ikke opgave 4 i advanced dictionaries...





