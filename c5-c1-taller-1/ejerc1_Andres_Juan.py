
cantp = int(input("¿Cuántas personas desea registrar?: "))

for i in range(cantp):
    print("Participante #",i+1)
    nombre = input("Ingrese su nombre: ")
    edadbuena = 0
    while edadbuena == 0:
        edad = int(input("Ingrese su edad: "))
        if (edad > 0):
            edadbuena = 1
        else:
            print("Ingrese una edad válida")
    conocimiento = input("¿Tiene conocimientos básicos de computación? (si/no): ")
    if (edad >= 15) and (conocimiento == "si"):
        print("Puede participar en el taller")
    else:
        print("No cumple los requisitos")
print("Proceso finalizado")
print("Hola mundo, soy hub otra vez, otra vez")



