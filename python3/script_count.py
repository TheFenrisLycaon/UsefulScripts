
import os

path = os.getenv("scripts")
dropbox = os.getenv("dropbox")


def clear_screen():
    if os.name == "posix":
        os.system("clear")
    elif os.name in ("nt", "dos", "ce"):
        os.system("CLS")


def count_files(path, extensions):
    counter = 0
    for root, dirs, files in os.walk(path):
        for file in files:
            counter += file.endswith(extensions)
    return counter


def github():
    github_dir = os.path.join(dropbox, "github")
    github_count = sum((len(f) for _, _, f in os.walk(github_dir)))
    if github_count > 5:
        print("\nYou have too many in here, start uploading !!!!!")
        print("You have: " + str(github_count) + " waiting to be uploaded to github!!")
    elif github_count == 0:
        print("\nGithub directory is all Clear")
    else:
        print(
            "\nYou have: " + str(github_count) + " waiting to be uploaded to github!!"
        )


def development():
    dev_dir = os.path.join(path, "development")
    dev_count = sum((len(f) for _, _, f in os.walk(dev_dir)))
    if dev_count > 10:
        print("\nYou have too many in here, finish them or delete them !!!!!")
        print("You have: " + str(dev_count) + " waiting to be finished!!")
    elif dev_count == 0:
        print("\nDevelopment directory is all clear")
    else:
        print("\nYou have: " + str(dev_count) + " waiting to be finished!!")


clear_screen()

print("\nYou have the following :\n")
print("AutoIT:\t" + str(count_files(path, ".au3")))
print("Batch:\t" + str(count_files(path, (".bat", ",cmd"))))
print("Perl:\t" + str(count_files(path, ".pl")))
print("PHP:\t" + str(count_files(path, ".php")))
print("Python:\t" + str(count_files(path, ".py")))
print("Shell:\t" + str(count_files(path, (".ksh", ".sh", ".bash"))))
print("SQL:\t" + str(count_files(path, ".sql")))

github()
development()
