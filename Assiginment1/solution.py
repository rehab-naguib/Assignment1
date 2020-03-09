f=open("input.txt", "r")
if f.mode == 'r':
contents =f.read()
def encrypt(contents,s): 
    result = "" 
  
    # traverse text 
    for i in range(len(contents)): 
        char = contents[i] 
  
        # Encrypt uppercase characters 
        if (char.isupper()): 
            result += chr((ord(char) + s-65) % 26 + 65) 
  
        # Encrypt lowercase characters 
        else: 
            result += chr((ord(char) + s - 97) % 26 + 97) 
  
    return result 
  
#check the above function 
s = 4
print ("Text  : " + contents )
print ("Shift : " + str(s) )
print ("Cipher: " + encrypt(contents,s) 
