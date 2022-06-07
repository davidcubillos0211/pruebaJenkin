# coding=utf-8


s="ma123454ñana a las 10 o a las 11"
def num(str):
    posicion=0
    contador=0
    for i in str:
            
        if i.isnumeric():
            
            inicio=contador
            
            for i in (str[contador:]):
                
                contador+=1
                if i.isnumeric():
                    final=contador
                else:
                    primernumero= int(str[inicio:final])
                    
                    return primernumero
                if contador==len(str):
                    primernumero= int(str[inicio:final])
                    
                    return primernumero
                    
        contador+=1

print(num(s))
