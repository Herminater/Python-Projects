def merge_the_tools(string, k):
    # your code goes here
    counter = 0
    while counter != len(string):
        
        stringPart = string[counter:counter+k]
        
        
        index = 0
        
        recursive(index, stringPart)
        
        counter += k


def recursive(index, stringpart):
    if index < len(stringpart):
        
        saveLetter = stringpart[index]
       
        workedString = stringpart[index+1:].replace(saveLetter, "")
        returnString = stringpart[:index+1] + workedString
        
        index += 1
        recursive(index, returnString)
        
    else:
        print(stringpart)
        
    
    



if __name__ == '__main__':
    string, k = 'AABCAAADA', 3
    merge_the_tools(string, k)