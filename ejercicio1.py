peso = float(input("Ingrese su pes en kg: "))
altura = float(input("Ingrese su altura en metros: "))
imc = peso/(altura**2)
if imc<18.5:
    categoria="Bajo peso"
elif imc <25:
    categoria="Peso normal"
elif imc <30:
    categoria="Sobrepeso"
else :
    categoria="Obesidad"

print(f"Su IMC es :{imc:.2f}") 
print(f"Categoria: {categoria}")
print("Error: Ingrese valores numericos validos.")
print("Error: La altura no puede ser cero.")