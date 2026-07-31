#Program that tells the user what meal time it is
def main():
    time = input("What time is it? ")
    convert(time)
    

def convert(n):
    
    hours, minute = n.split(":")
    minute = float(minute) / 60
    n = float(hours) + minute
    if 7 <= n <= 8:
            print("breakfast time")
    elif  12 <= n <= 13:
            print("lunch time")
    elif 18 <= n <= 19:
            print("dinner time")


main()