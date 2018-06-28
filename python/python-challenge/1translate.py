#PROBLEM STATEMENT:
#http://www.pythonchallenge.com/pc/def/map.html

#HELPFUL RESOURCES
#https://www.tutorialspoint.com/python/string_maketrans.htm

import string 

def method1(text, shift):
    new_text=''
    for ch in text:
        if(ord(ch)<ord('a') or ord(ch)>ord('z')): #or use isalpha function
            new_ch=ch
        else:
            #character index is character value between 0 and 25
            ch_index = ord(ch)-ord('a')      
            new_index = (ch_index+shift)%26
            new_ch=chr(new_index+ord('a'))
        new_text=new_text+new_ch
    return new_text
    
def method2(text,shift):
    shift %= 26  # |shift| < 26 
    alphabet = string.ascii_lowercase # 'abcdefghijklmnopqrstuvwxyz' (note: for Python 2, use string.lowercase instead)
    shifted_alphabet = alphabet[shift:] + alphabet[:shift]
    transtab=str.maketrans(alphabet, shifted_alphabet)
    return text.translate(transtab)

    
#TEST CASE
#g fmnc wms bgblr rpylqjyrc gr zw fylb. rfyrq ufyr amknsrcpq ypc dmp. bmgle gr gl zw fylb gq glcddgagclr ylb rfyr'q ufw rfgq rcvr gq qm jmle. sqgle qrpgle.kyicrpylq() gq pcamkkclbcb. lmu ynnjw ml rfc spj.    
text = input("Enter text here: ")
text_shift=2
print()
print('new text by method 1 is')
print(method1(text,text_shift))
print()
print('new text by method 2 is')
print(method2(text,text_shift))
