import  hashlib


def encrypt_password(password):
    h = hashlib.sha256()
    h.update(password.encode('utf8'))
    return h.hexdigest()