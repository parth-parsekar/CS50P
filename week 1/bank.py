def main():
    g = input("Greeting: ").lower()
    print("$" + money(g))

def money(i):
    if "hello" in i:
        return "0"
    elif i[:1] == "h":
        return "20"
    else:
        return "100"

main()
