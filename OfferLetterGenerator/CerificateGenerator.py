from PIL import Image, ImageDraw, ImageFont
from pathlib import Path
import sys


def makeCerti(name, topic=""):
    img = Image.open("./src/certi.png")
    draw = ImageDraw.Draw(img)
    spaces = " " * ((THRESHOLD - len(name)) // 2)
    draw.text((30, 150), spaces + f"Congratulations {name} !!", (0, 0, 0), FONT)
    impdf = img.convert("RGB")
    img.save("./certi/{}.png".format(name.strip()))
    impdf.save("./certi/{}.pdf".format(name.strip()))


def maintainThreshold(name):
    if len("".join(name)) < THRESHOLD:
        res = "".join(name)
    else:
        nameL = name.split()
        resL = []
        for i in nameL[:-1]:
            resL.append(i[0].upper())
        resL += [nameL[-1]]
        res = " ".join(resL)
    return res


def fromList():
    name = []
    with open("./list.in", "r") as f:
        lines = [x for x in f.readlines()]
        for res in lines:
            name.append(res.rstrip())
    if len(name) != 0:
        for i in range(len(name)):
            try:
                makeCerti(maintainThreshold(name[i]))
            except:
                pass
    else:
        print("Enter names in the list and try again.")


def fromName():
    name = input("\nEnter Name ::\t").strip().split()
    makeCerti(maintainThreshold(" ".join(name)))


def getHelp():
    print(
        "\n\
            '-l'\t:\tTo generate letters by reading from the file\n\
            -n [NAME]\t:\tTo generate a single letter.\n\
            '-h'\t:\tSee this page.\n\n\
    You can also run the scripts without any flags and use the menu to generate letters."
    )


def main():
    print("\n\t\t\tLETTER GENERATOR\t\t\t")
    print("-------------------------------------------------------------------")
    choice = eval(input(
        "\n\t[1]\tFor Single Name.\t\t[2]\tFor a List of Names\n\t[99]\tHelp\t\t\t\t[0]\tExit\n\nEnter::\t"
    ))
    if int(choice) == 1:
        fromName()
    elif int(choice) == 2:
        fromList()
    elif int(choice) == 99:
        getHelp()
        main()
    elif int(choice) == 0:
        exit()
    else:
        print("Invalid choice try again.")
        main()


if __name__ == "__main__":
    Path("./certi").mkdir(parents=True, exist_ok=True)
    FONT = ImageFont.truetype("./src/font.ttf", 16)
    FONT_TOPIC = ImageFont.truetype("./src/font.ttf", 100)
    THRESHOLD = 15
    if len(sys.argv) == 1:
        main()
    else:
        if sys.argv[1] == "-l":
            fromList()
        elif sys.argv[1] == "-n":
            name = sys.argv[2:]
            makeCerti(maintainThreshold(" ".join(name)))
        elif sys.argv[1] == "-h":
            getHelp()
        else:
            print("Error :: Run stript with '-h' to get help.")
