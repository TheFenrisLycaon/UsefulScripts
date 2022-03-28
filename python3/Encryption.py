import random


class XORCipher(object):
    def __init__(self, key=0):
        self.__key = key

    def encrypt(self, content, key):
        assert isinstance(key, int) and isinstance(content, str)
        key = key or self.__key or 0
        while key > 255:
            key -= 255
        ans = []
        for ch in content:
            ans.append(chr(ord(ch) ^ key))
        return ans

    def decrypt(self, content, key):
        assert isinstance(key, int) and isinstance(content, list)
        key = key or self.__key or 0
        while key > 255:
            key -= 255
        ans = []
        for ch in content:
            ans.append(chr(ord(ch) ^ key))
        return ans

    def encrypt_string(self, content, key=0):
        assert isinstance(key, int) and isinstance(content, str)
        key = key or self.__key or 0
        while key > 255:
            key -= 255
        ans = ""
        for ch in content:
            ans += chr(ord(ch) ^ key)
        return ans

    def decrypt_string(self, content, key=0):
        assert isinstance(key, int) and isinstance(content, str)
        key = key or self.__key or 0
        while key > 255:
            key -= 255
        ans = ""
        for ch in content:
            ans += chr(ord(ch) ^ key)
        return ans

    def encrypt_file(self, file, key=0):
        assert isinstance(file, str) and isinstance(key, int)
        try:
            with open(file, "r") as fin:
                with open("encrypt.out", "w+") as fout:
                    for line in fin:
                        fout.write(self.encrypt_string(line, key))
        except:
            return False
        return True

    def decrypt_file(self, file, key):
        assert isinstance(file, str) and isinstance(key, int)
        try:
            with open(file, "r") as fin:
                with open("decrypt.out", "w+") as fout:
                    for line in fin:
                        fout.write(self.decrypt_string(line, key))
        except:
            return False
        return True


if __name__ == "__main__":
    crypt = XORCipher()
    ch = int(
        eval(input(
            "Welcome to the encryption services by Lycaon Industries\n1. Encrypt Your Data\n2. Decrypt Your Data::\n"
        ))
    )
    if ch == 1:
        key = random.randint(0, 70)
        data = str(eval(input("Enter Your Data::\t")))
        print((crypt.encrypt_string(data, key), key))
    elif ch == 2:
        data = str(eval(input("Enter Your Data::\t")))
        key = int(eval(input("Enter Key ::\t")))
        print((crypt.encrypt_string(data, key)))
    else:
        print("Invalido !!!")
