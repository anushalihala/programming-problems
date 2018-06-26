#PROBLEM STATEMENT:
#http://www.pythonchallenge.com/pc/def/ocr.html

fh = open('2raw.txt','r')
raw_text=fh.read()

char_count=dict()
for ch in raw_text:
    char_count[ch]=char_count.get(ch,0)+1
   
str=''   
for k,v in char_count.items():
    if(v==1):
        str += k

print('answer:', str)
        

#sorting list to view least frequent characters
items_list = [(v,k) for k,v in char_count.items()]
items_list.sort()
print(items_list)
