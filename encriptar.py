from cryptography.fernet import Fernet

def generar_key():
    key = Fernet.generate_key()
    with open('pass.key', 'wb') as file:
        file.write(key)

def cargar_key():
    return open('pass.key','rb').read()

generar_key()

key=cargar_key()

password = b'SimpleAnonimo21'

file = open('pass.enc','wb')

clave = Ferner(key)
pass_enc = clave.encrypt(password)
file.write('pass_enc')
file.close()