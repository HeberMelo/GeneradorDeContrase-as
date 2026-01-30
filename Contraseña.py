import customtkinter as ctk
import string
import random

#El siguiente programa tiene como proposito generar claves de forma aleatoria, 
#en el que el usuario pueda usarlas dependiendo de la longitud que desee, además,
#se mostrará en pantalla si la contraseña generada es debil, media o fuerte.
#Se utiliza la tecnologia customtkinter para el apartado grafico de la app

ctk.set_appearance_mode("Oscuro")
ctk.set_appearance_mode("Claro")

#Ventana principal
app = ctk.CTK()
# Este apartado es para el historial de contraseñas generadas
historial = []


def evaluar_seguridad(contraseña):
    longitud = len(contraseña)
    tiene_mayus = any(c.isupper() for c in contraseña)
    tiene_minus = any(c.islower() for c in contraseña)
    tiene_digito = any(c.isdigit() for c in contraseña)
    tiene_simbolo = any(c in string.punctuation for c in contraseña)

    tipos = sum([tiene_mayus, tiene_minus, tiene_digito, tiene_simbolo])

#Condicional para saber si la contraseña generada en base a los digitos 
#escogidos por el usuario son debiles, medios o fuertes.
    if longitud < 8 or tipos < 2:
        return "Débil"
    elif longitud < 12 or tipos < 3:
        return "Media"
    else:
        return "Fuerte"
    
#Creacion de la funcion generar_contraseña, aquí se va a generar de forma
#aleatoria la contraseña, para hacer posible esto utilizamos la función 
#random.
def generar_contraseña(longitud):
    caracteres = string.ascii_letters + string.digits + string.punctuation
    contraseña = "".join(random.choice(caracteres) for _ in range(longitud))
    return contraseña

#Creamos la funcion mostrar_historial para ver el historial de contraseñas
def mostrar_historial():
    if historial:
        print("\n Historial de contraseñas generadas:")
        for i, (pwd, nivel) in enumerate(historial, start=1):
            print(f"{i}. {pwd} ({nivel})")
    else:
        print("\n No se han generado contraseñas aún.")

# Menú principal del programa
while True:
    print("\n--- Generador de Contraseñas ---")
    print("1. Generar nueva contraseña")
    print("2. Ver historial")
    print("3. Salir")

    opcion = input("Seleccione una opción (1-3): ")

    if opcion == "1":
        try:
            longitud = int(input("Ingrese el tamaño de la contraseña: "))
            if longitud < 1:
                print(" La longitud debe ser mayor que 0.")
                continue
            contraseña = generar_contraseña(longitud)
            seguridad = evaluar_seguridad(contraseña)

            print(" Contraseña generada:", contraseña)
            print(" Nivel de seguridad:", seguridad)

            historial.append((contraseña, seguridad))
        except ValueError:
            print(" Ingrese un número válido.")
    elif opcion == "2":
        mostrar_historial()
    elif opcion == "3":
        print(" Saliendo del programa.")
        break
    else:
        print(" Opción inválida. Intente nuevamente.")
