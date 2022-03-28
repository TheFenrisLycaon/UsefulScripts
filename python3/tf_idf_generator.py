import math
import pickle
from colorama import Fore, Style

switcher = {
    "r": Fore.RED,
    "bk": Fore.BLACK,
    "b": Fore.BLUE,
    "g": Fore.GREEN,
    "y": Fore.YELLOW,
    "m": Fore.MAGENTA,
    "c": Fore.CYAN,
    "w": Fore.WHITE,
}


def paint(s, color="r"):
    """
    Utility func, for printing colorful logs in console...

    @args:
    --
    s : String to be modified.
    color : color code to which the string will be formed. default is 'r'=RED

    @returns:
    --
    s : final modified string with foreground color as per parameters.

    """
    if color in switcher:
        s = switcher[color] + s + Style.RESET_ALL
    return s


TAG = paint("TF-IDF-GENE/", "b")


def find_tf_idf(file_names=["./../test/testdata"], prev_file_path=None, dump_path=None):
    """
    Function to create a TF-IDF list of dictionaries for a corpus of docs.
    If you opt for dumping the data, you can provide a file_path with .tfidfpkl extension(standard made for better understanding)
    and also re-generate a new tfidf list which overrides over an old one by mentioning its path.

    @Args:
    --
    file_names : paths of files to be processed on, you can give many small sized file, rather than one large file.
    prev_file_path : path of old .tfidfpkl file, if available. (default=None)
    dump_path : directory-path where to dump generated lists.(default=None)

    @returns:
    --
    idf : a dict of unique words in corpus,with their document frequency as values.
    tf_idf : the generated tf-idf list of dictionaries for mentioned docs.

    """

    tf_idf = []
    idf = {}
    if prev_file_path:
        print((TAG, "modifying over exising file.. @", prev_file_path))
        idf, tf_idf = pickle.load(open(prev_file_path, "rb"))
        prev_doc_count = len(idf)
        prev_corpus_length = len(tf_idf)

    for f in file_names:
        file1 = open(f, "r")
        for line in file1:
            dict = {}
            for i in set(line.split()):
                if i in idf:
                    idf[i] += 1
                else:
                    idf[i] = 1
            for word in line.split():
                if word not in dict:
                    dict[word] = 1
                else:
                    dict[word] += 1

            tf_idf.append(dict)
        file1.close()

    for doc in tf_idf:
        for key in doc:
            true_idf = math.log(len(tf_idf) / idf[key])
            true_tf = doc[key] / len(doc)
            doc[key] = true_tf * true_idf

    print((
        TAG,
        "Total number of unique words in corpus",
        len(idf),
        "( " + paint("++" + str(len(idf) - prev_doc_count), "g") + " )"
        if prev_file_path
        else "",
    ))
    print((
        TAG,
        "Total number of docs in corpus:",
        len(tf_idf),
        "( " + paint("++" + str(len(tf_idf) - prev_corpus_length), "g") + " )"
        if prev_file_path
        else "",
    ))

    if dump_path:
        if dump_path[-8:] != "tfidfpkl":
            raise Exception(
                TAG
                + "Please provide a .tfidfpkl file_path, it is the standard format of this module."
            )

        pickle.dump(
            (idf, tf_idf), open(dump_path, "wb"), protocol=pickle.HIGHEST_PROTOCOL
        )
        print((TAG, "Dumping TF-IDF vars @", dump_path))

    return idf, tf_idf
