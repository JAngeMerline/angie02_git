def addition(a,b):
    return a+b
def soustraction(a,b):
    return a-b
def multiplication(a, b):
    return a*b
def division(a,b):
    return a/b
nombre1=float(input("Entrer le premier nombre: "))
nombre2=float(input("Entrer le deuxieme nombre: "))
operation=input("Entrer l'opperation a effectuer (+, -, *, /): ")

#maimtenant creons les conditions
if operation== "+":
    result=addition(nombre1, nombre2)
elif operation=="-":
    result=soustraction(nombre1, nombre2)
elif operation=="*":
    result= multiplication(nombre1, nombre2)
elif operation=="/":
    result=division(nombre1, nombre2)
else:
    result="error"

print("le resultat est: ", result)