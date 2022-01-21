def f1(text: str, shift: int = 3) -> str:
    plain_text = ""
    for c in text:
        if c.isupper():
            c_unicode = ord(c)
            index = ord(c) - ord("A")
            new_index = (index + shift) % 26
            new_unicode = new_index + ord("A")
            new_character = chr(new_unicode)
            plain_text = plain_text + new_character
        else:
            c_unicode = ord(c)
            index = ord(c) - ord("a")
            new_index = (index + shift) % 26
            new_unicode = new_index + ord("a")
            new_character = chr(new_unicode)
            plain_text = plain_text + new_character
    return plain_text


def encrypt_caesar(encrypted_text: str, shift: int = -3) -> str:
    plain_text = ""
    for c in encrypted_text:
        if c.isupper():
            c_unicode = ord(c)
            c_index = ord(c) - ord("A")
            new_index = (c_index + shift) % 26
            new_unicode = new_index + ord("A")
            new_character = chr(new_unicode)
            plain_text = plain_text + new_character
        else:
            c_unicode = ord(c)
            c_index = ord(c) - ord("a")
            new_index = (c_index + shift) % 26
            new_unicode = new_index + ord("a")
            new_character = chr(new_unicode)
            plain_text = plain_text + new_character
    return plain_text


a = []
text: str = input("Сообщение для шифровки:")
for i in range(len(text)):
    if text[i].isalpha():
        a.append(f1(text[i]))
    else:
        a.append(text[i])
print(*a, sep="")

b = []
textt: str = input("Сообщение для дешифровки:")
for i in range(len(textt)):
    if textt[i].isalpha():
        b.append(encrypt_caesar(textt[i]))
    else:
        b.append(textt[i])
print(*b, sep="")
