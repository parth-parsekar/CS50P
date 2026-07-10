def main():
    s = input("What is the Answer to the Great Question of Life, the Universe, and Everything?").lower()
    deep(s)

def deep(n):
    match n:
        case "42" | "forty two" | "forty-two":
            print("Yes")
        case _:
            print("No")

main()
