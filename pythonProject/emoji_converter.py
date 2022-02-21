def emoji_converter(message):
    emojis = {
    ":)": "🙂",
    ":(": "☹"
    }
    output = ""
    for word in message:
        output += emojis.get(word, word) + " "
    return output


message = input("> ").split()
print(emoji_converter(message))