############################################
#   Code Wars: DISEMVOWEL TROLLS
############################################

def disemvowel(string_):
    output = ""
    for char in string_:
        if not (char.lower() == 'a' or char.lower() == 'e' or 
                char.lower() == 'i' or char.lower() == 'o' or 
                char.lower() == 'u') :
            output += char
    return output

print("DisEmVowel Hello World!:",disemvowel("Hello World!"))
print("This website is for losers LOL!:",disemvowel("This website is for losers LOL!"))
