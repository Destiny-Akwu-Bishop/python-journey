# Program made to answer the great question of life

question = input("What is the answer to the great question of life, the universe, and everything? ")

match question:
    case "42":
        print("Yes")
    case "forty-two":
        print("Yes")
    case "forty two":
        print("Yes")
    case _:
        print("No")
