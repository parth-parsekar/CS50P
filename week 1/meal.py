def main():
    t = input("What time is it? ")
    n = convert(t)

    if 7.0 <= n <= 8.0:
        print("breakfast time")
    elif 12.0 <= n <= 13.0:
        print("lunch time")
    elif 18.0 <= n <= 19.0:
        print("dinner time")

def convert(time):
    n = time.split(":")
    f = float(n[0])
    b = float(n[1])/60
    return f+b

if __name__ == "__main__":
    main()
