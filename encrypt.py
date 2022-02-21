import sys
import unittest
def encrypt(text,s):
    result = ""
 

    for i in range(len(text)):
        char = text[i]
 
        
        if (char.isupper()):
            result += chr((ord(char) + s-65) % 26 + 66)
        elif char.isdigit():
            result+=str((ord(char)+ s-48))    
 
        
        elif char.islower():
            result += chr((ord(char) + s - 97) % 26 + 97)
            
        else:
            value=ord(char)+s
            result += chr(value % 128)
 
    return result
   

class firsttest(unittest.TestCase):
 
    def test_encrypt(self):
        assert encrypt('12345',1)=='23456c'
x= firsttest()
x.test_encrypt()    
   