import requests


def download(url):
    f = open("file_name.jpg", "wb")
    f.write(requests.get(url).content)
    f.close()
    print("Succesfully Downloaded")


def download_2(url):
    try:
        response = requests.get(url)
    except Exception:
        print("Failed Download!")
    else:
        if response.status_code == 200:
            with open("file_name.jpg", "wb") as f:
                f.write(requests.get(url).content)
                print("Succesfully Downloaded")
        else:
            print("Failed Download!")


url = "https://avatars0.githubusercontent.com/u/29729380?s=400&v=4"
download(url)
