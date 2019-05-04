
class Cryptography:

    @staticmethod
    def encrypt(f_data, password):
        return password + " " + f_data

    @staticmethod
    def decrypt(f_cipher, password):
        return password + " " + f_cipher
