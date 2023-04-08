#   Convert all vowels i.e., a,e,i,o,u into #
#   Example:    chetan --> ch#t#n
def translate(name):
    translated_str = ""
    for letter in name:
        if letter.lower() in "aeiou":
            if letter.isupper():
                translated_str = translated_str + "#"
        else:
            translated_str = translated_str + letter
    return translated_str


print(translate(input("Enter a phrase: ")))
