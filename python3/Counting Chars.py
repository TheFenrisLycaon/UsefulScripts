def count_chars(filename):
    count = {}

    with open(filename) as info:
        readfile = info.read()
        for character in readfile.upper():
            count[character] = count.get(character, 0) + 1

    return count


def main():
    is_exist = True
    while is_exist:
        try:
            inpuFile = input("File Name / (0)exit : ").strip()
            if inpuFile == "0":
                break
            print((count_chars(inpuFile)))
        except FileNotFoundError:
            print("File not found...Try again!")


if __name__ == "__main__":
    main()
