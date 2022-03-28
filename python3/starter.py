import os

f = os.listdir("./")
inp = str(eval(input("Enter filename::\t")))
if inp in f:
    print("Found")
    if int(eval(input("[0]\tEdit\t\t[Anyting Else]\tRun"))) == 0:
        os.startfile(inp)
    else:
        os.system("python ./" + inp)
else:
    print("Error")
