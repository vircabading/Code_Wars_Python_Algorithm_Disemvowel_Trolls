############################################
#   Code Wars: DISEMVOWEL TROLLS
############################################

def disemvowel(string_):
    output = ""
    for char in string_:
        if not (char == 'a' or char == 'e' or char == 'i' or char == 'o' or char == 'u') :
            output += char
    return output

print("DisEmVowel Hello World!:",disemvowel("Hello World!"))
