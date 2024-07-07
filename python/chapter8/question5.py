# writer a python function to remove given word from a list and strip it at same time.
def remove_word(words: list[str], word_to_remove: str) -> list[str]:
    return [w.replace(word_to_remove, '').strip() for w in words]

word_list = ["apple", "banana", "cherry"]
word_to_remove = "banana"
result = remove_word(word_list, word_to_remove)
print(result)  # Output: ['apple', 'cherry']
