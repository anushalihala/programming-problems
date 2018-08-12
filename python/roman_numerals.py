def old_roman_numerals(num):
    #Old Roman numerals are numerals without subtractions, for e.g. VIIII instead of IX
    
    #Reference: I = 1 V = 5 X = 10 L = 50 C = 100 D = 500 M = 1000
    roman_num=''
    while(num>0):
        if(num>=1000):
            roman_num+='M'
            num=num-1000
        elif(num>=500):0
            roman_num+='D'
            num=num-500
        elif(num>=100):
            roman_num+='C'
            num=num-100
        elif(num>=50):
            roman_num+='L'
            num=num-50
        elif(num>=10):
            roman_num+='X'
            num=num-10
        elif(num>=5):
            roman_num+='V'
            num=num-5
        else:
            roman_num+='I'
            num=num-1
    return roman_num
    
def roman_numerals(num):
    if(num<1):
        return ''
    
    roman_symbols_dict={'I':1, 'V':5, 'X':10, 'L':50, 'C':100, 'D':500, 'M':1000}
    roman_symbols=['I','V','X','L','C','D','M']
    
    old_roman_num=old_roman_numerals(num)
    largest_symbol=old_roman_num[0]
    largest_symbol_value=roman_symbols_dict[largest_symbol]
    
    ones_symbol_value=1
    temp_largest_symbol_value=largest_symbol_value
    while(temp_largest_symbol_value%10==0):
        temp_largest_symbol_value/=10
        ones_symbol_value*=10
    
    try:
        next_largest_symbol=roman_symbols[roman_symbols.index(largest_symbol)+1]
        next_largest_symbol_value=roman_symbols_dict[next_largest_symbol]
        diff=next_largest_symbol_value-num
    except:
        diff=ones_symbol_value+1 #execute else case of if condition below
       
    if(diff<=ones_symbol_value):
        roman_num = old_roman_numerals(ones_symbol_value)+next_largest_symbol 
        acc=next_largest_symbol_value-ones_symbol_value
    else:
        roman_num=largest_symbol
        acc=largest_symbol_value
        
    roman_num=roman_num+roman_numerals(num-acc)
    
    return roman_num
    
print('List of values')
values = list(range(0,151))+list(range(200,1001,100))+[1063,1500]
for i in values:
    print(roman_numerals(i))
print()
try:
    num=int(input("Enter a number: "))
    print("Number in Roman numerals =",roman_numerals(num))
except:
    print('Not a number')