# Quiz ID: Z75101

def snake_to_camel(text: str) -> str:
    words = text.split('_')
    for i, word in enumerate(words):
        words[i] = word.capitalize()
    words[0] = words[0].lower()
    return''.join(words)

a = 'python'
print(snake_to_camel(a))

