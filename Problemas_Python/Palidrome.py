def is_palidrome(text):
    text = text.lower().replace(" ","")
    length = len(text)

    for i in range(length//2):
        if text[i] != text[length-1-i]:
            return False
        return True
    
print(is_palidrome("reconocer"))
print(is_palidrome("hola"))