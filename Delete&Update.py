def update_char(text, pos, new_char):
    new_text = text[:pos] + new_char + text[pos + 1:]
    return new_text


def delete_char(text, pos):
    new_text = text[:pos] + text[pos + 1:]
    return new_text


text = "HELLO"

print("Original:", text)


text = update_char(text, 0, "J")
print("After update:", text)

text = delete_char(text, 4)
print("After delete:", text)


text = "PYTHON"

print("\nOriginal:", text)

text = update_char(text, 2, "X")
print("After update:", text)

text = delete_char(text, 0)
print("After delete:", text)