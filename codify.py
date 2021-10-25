from cryptography.fernet import Fernet
import pyperclip
import os


# 1. Uncomment Lines 14-18 To Create A Fresh Key.
# --- Do Not Lose This Key!
# --- You Will NOT Be Able To Decrypt Your Messages If You Do
# 2. Store The Resulting b'' String Into The Commented "key" Variable On Line 21
# 3. Comment Out Lines 14-18
# 4. Uncomment Lines: 21, 22, 68, and 69. Now You're Ready To Record Secret Messages!


# def create_key():
#     key = Fernet.generate_key()
#     return key
# 
# print(create_key())


# key = 
# fernet = Fernet(key)

def encrypt(message=''):
    if message == '':
        message = input('Enter message to encrypt: ')
    
    message = message.encode()
    enc_message = fernet.encrypt(message).decode()
    
    return enc_message

def decrypt(message=''):
    if message == '':
        message = input('Enter message to decrypt: ')
    if type(message) == bytes:
        message = message.decode()
        
    message = str(message).encode()
    dec_message = fernet.decrypt(message)
    
    return dec_message.decode()

def main():
    flag = 1
    while flag == 1:
        task = input("Encrypt (e) or Decrypt (d) a message: ").lower().strip()
        if task not in  ['e' ,'d' , '']:
            print(f'Invalid Option! You put: {task}\n')
            continue
        if task.strip() == '':
            flag = 2
            break
        
        if task == 'e':
            enc_text = encrypt()
            pyperclip.copy(enc_text)
            os.system('cls')
            print('Encrypted text has been copied.')
            continue
        
        if task == 'd':
            text = decrypt()
            os.system('cls')
            print(f'Decrypted Message:\n\n{text}\n\n')
            continue

# if __name__ == '__main__':
#     main()
