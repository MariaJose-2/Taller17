while True:
    try:
        a = int(input("Un numero:"))
        print(a)
        break
    except ValueError:
        print("Este no es un numero entero")# 
        
    
#division 
    
a = 9; b = 0
try:
    c = a/b
except ZeroDivisionError:
    print("Eror: no se ha podido realizar la división por cero")
    
#typeEror
    try:
        list = ["a,b,c"]
        list2 = list[7]
        print(list2)
    except TypeError:
        print("no se puede encontrar ese tipo de numero en la lista ")

    
        
    