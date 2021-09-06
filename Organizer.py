import os
from pathlib import Path


DIRECTORIES = {
    "HTML": [".html5", ".html", ".htm", ".xhtml"],
    "Imgaes": [".jpeg", ".jpg", ".tiff", ".gif", ".bmp", ".png", ".bpg", "svg",
               ".heif", ".psd"],
    "Videos": [".avi", ".flv", ".wmv", ".mov", ".mp4", ".webm", ".vob", ".mng",
               ".qt", ".mpg", ".mpeg", ".3gp", ".mkv"],
    "Documents": [".oxps", ".epub", ".pages", ".docx", ".doc", ".fdf", ".ods",
                  ".odt", ".pwi", ".xsn", ".xps", ".dotx", ".docm", ".dox",
                  ".rvg", ".rtf", ".rtfd", ".wpd", ".xls", ".xlsx", ".ppt",
                  "pptx", ".pdf"],
    "Archives": [".a", ".ar", ".cpio", ".iso", ".tar", ".gz", ".rz", ".7z",
                 ".dmg", ".rar", ".xar", ".zip"],
    "Audio": [".aac", ".aa", ".aac", ".dvf", ".m4a", ".m4b", ".m4p", ".mp3",
              ".msv", "ogg", "oga", ".raw", ".vox", ".wav", ".wma"],
    "Text": [".txt", ".in", ".out"],
    "Python": [".py"],
    "XML": [".xml"],
    "Executables": [".exe"],
    "Shell": [".sh"],
    "Others": []
}

FILE_FORMATS = {entryFormat: directory
                for directory, FILE_FORMATS in DIRECTORIES.items()
                for entryFormat in FILE_FORMATS}


def organize_junk():
    for entry in os.scandir():
        if not entry.is_dir():
            completePath = Path(entry.name)
            entryFormat = completePath.suffix.lower()
            if entryFormat in FILE_FORMATS:
                dirPath = Path(FILE_FORMATS[entryFormat])
                dirPath.mkdir(exist_ok=True)
                completePath.rename(dirPath.joinpath(completePath))
    for dir in os.scandir():
        try:
            if dir.is_dir():
                os.rmdir(dir)
            else:
                os.rename(os.getcwd() + '/' + str(Path(dir)),
                          os.getcwd() + '/Other/' + str(Path(dir)))
        except:
            pass


if __name__ == "__main__":
    os.makedirs(DIRECTORIES.keys, exist_ok=True)
    organize_junk()
