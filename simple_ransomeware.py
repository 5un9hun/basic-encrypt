from struct import pack
import os

cur_path = os.listdir()

def encrypt():
    for i in range(len(cur_path)):
        if(cur_path[i] == os.path.basename(__file__)): continue #except for this file
        print(cur_path[i])
        
        print("[*] \""+cur_path[i]+"\" Encrypting . . .")
        with open(cur_path[i],'rb+') as f:  #read data 
            data = f.read()
        with open(cur_path[i],'wb+') as f: #write data
            for j in range(len(data)): #encryt logic
                enc_data = data[j] ^ 30 #simple xor logic ^^;
                enc_data = pack('B', enc_data)
                f.write(enc_data)
        os.rename(cur_path[i], "Encrypt.file_"+ str(i+1))
        print("[*] \""+cur_path[i]+"\" Success Encrypt!")
        
def decrypt():
    for i in range(len(cur_path)):
        if(cur_path[i] == os.path.basename(__file__)): continue #except for this file
        print(cur_path[i])
        
        print("[*] \""+cur_path[i]+"\" Decrypting . . .")
        with open(cur_path[i],'rb+') as f:  #read data 
            data = f.read()
        with open(cur_path[i],'wb+') as f: #write data
            for j in range(len(data)): #encryt logic
                enc_data = data[j] ^ 30 #simple xor logic ^^; 
                enc_data = pack('B', enc_data)
                f.write(enc_data)
        os.rename("Encrypt.file_"+ str(i+1), "decrypt_"+str(i+1)+".exe") #not developing (maybe refer to file data)
        print("[*] \""+cur_path[i]+"\" Success Decrypt!")


if(__name__ == "__main__" ):
    print(cur_path)
    print("[1]Encrypt files of this folder")
    print("[2]Decrypt files of this folder")
    c = int(input(">> "))
    if(c == 1): encrypt()
    elif(c == 2): decrypt()
    else: print("quit")
