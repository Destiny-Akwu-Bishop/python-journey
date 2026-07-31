#Program designed to up-hold bank principle

greeting = input("Greetings: ")

if greeting.startswith("Hello"):
    print("$0")
elif greeting.startswith("H"):
    print("$20")
else:
    print("$100")