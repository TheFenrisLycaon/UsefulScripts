import zipfile
import os


def backupToZip(folder):
    folder = os.path.abspath(folder)
    number = 1
    while True:
        zipFilename = os.path.basename(folder) + "_" + str(number) + ".zip"
        if not os.path.exists(zipFilename):
            break
        number = number + 1
    print(("Creating %s..." % (zipFilename)))
    backupZip = zipfile.ZipFile(zipFilename, "w")
    for foldername, subfolders, filenames in os.walk(folder):
        print(("Adding files in %s..." % (foldername)))
        backupZip.write(foldername)
        for filename in filenames:
            if filename.startswith(
                os.path.basename(folder) + "_"
            ) and filename.endswith(".zip"):
                continue
            backupZip.write(os.path.join(foldername, filename))
    backupZip.close()
    exit()


backupToZip(eval(input("Enter path::\t")))
