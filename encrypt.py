import sys
import unittest
def encrypt(text,s):
    result = ""
 

    for i in range(len(text)):
        char = text[i]
 
        
        if (char.isupper()):
            result += chr((ord(char) + s-65) % 26 + 65)
        elif char.isdigit():
            result+=str((ord(char)+ s-48))    
 
        
        elif char.islower():
            result += chr((ord(char) + s - 97) % 26 + 97)
            
        else:
            value=ord(char)+s
            result += chr(value % 128)
 
    return result



def decrypt(text,s):
    result = ""
 
    
    for i in range(len(text)):
        b=text[i]
        char = b
 
        
        if (char.isupper()):
            result += chr((ord(char) - s-65) % 26 + 66)
 
        
        elif char.isdigit():
            result+=str((ord(char)- s-48))
        elif char.islower():
            result += chr((ord(char)  - s- 97) % 26 + 97)
        else:
            value=ord(char)-s
            result += chr(value % 128)
            
 
    return result   

class firsttest(unittest.TestCase):
 
    def test_encrypt(self):
        assert encrypt('12345',1)=='23456'

    def test_decrypt(self):
        assert decrypt('23456',1)=='12345'        
x= firsttest()
x.test_encrypt() 

   