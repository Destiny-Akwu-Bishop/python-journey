#Program used for turning emoticons into emojis
def main():
    line = input("Input line of text: ")
    print(convert(line))
def convert(str):
    str = str.replace(":)", "🙂")
    str = str.replace(":(", "🙁")
    return str
main()