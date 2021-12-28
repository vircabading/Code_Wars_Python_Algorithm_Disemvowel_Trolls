############################################
#   Code Wars: DISEMVOWEL TROLLS
############################################

def disemvowel(string_):
    output = ""
    for char in string_:
        print(char)
        if (char == 'a' or char == 'e' or char == 'i' or char == 'o' or char == 'u') :
            print ("Vowel found")
    return string_

print(disemvowel("Hello World!"))