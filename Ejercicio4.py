def par_impar(a,b):
    if (a+b)%2==0:
        return True
    else:
        return False
    

a = int(input("Ingrese primer numero: "))
b = int(input("Ingrese segundo numero: "))

print(par_impar(a,b))
    