def main():
    f = input("File name: ")
    if "." in f:
        a = 0
    else:
        a = -1
    f = f.split(".")
# f[1]
    extentions(f[a+1])

def extentions(n):
    match n:
        case "gif" | "jpeg" | "jpg" | "png":
            print(f"image/{n}")
        case "pdf" | "txt" | "zip":
            print(f"application/{n}")
        case _:
            print(f"application/octet-stream")


main()
