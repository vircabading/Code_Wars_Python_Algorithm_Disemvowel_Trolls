############################################
#   Code Wars: DISEMVOWEL TROLLS
############################################

def disemvowel(string_):
    output = ""
    for char in string_:
        print(char)
        if not (char == 'a' or char == 'e' or char == 'i' or char == 'o' or char == 'u') :
            print ("not a vowel found")
            output += char
    return output

print(disemvowel("Hello World!"))