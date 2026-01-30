import customtkinter as ctk
import string
import random

#El siguiente programa tiene como proposito generar claves de forma aleatoria, 
#en el que el usuario pueda usarlas dependiendo de la longitud que desee, además,
#se mostrará en pantalla si la contraseña generada es debil, media o fuerte.
#Se utiliza la tecnologia customtkinter para el apartado grafico de la app.

ctk.set_appearance_mode("Dark")
ctk.set_appearance_mode("Blue")


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
        return "Débil", "red"
    elif longitud < 12 or tipos < 3:
        return "Media", "orange"
    else:
        return "Fuerte", "green"
    
#Creacion de la funcion generar_contraseña, aquí se va a generar de forma
#aleatoria la contraseña, para hacer posible esto utilizamos la función 
#random.
def generar_contraseña(longitud):
    caracteres = string.ascii_letters + string.digits + string.punctuation
    contraseña = "".join(random.choice(caracteres) for _ in range(longitud))
    return contraseña

#Ventana principal
app = ctk.CTk()
app.title("Generador de Contraseñas")
app.geometry("420x450")
app.resizable(False, False)


#Interfaz
titulo = ctk.CTkLabel(
    app,
    text="Generador de Contraseñas",
    font=("Arial", 20, "bold")
)
titulo.pack(pady=20)


longitud_label = ctk.CTkLabel(app, text="Longitud de la contraseña: 12")
longitud_label.pack()

def actualizar_longitud(valor):
    longitud_label.configure(
        text=f"Longitud de la contraseña: {int(valor)}"
    )

slider = ctk.CTkSlider(
    app,
    from_=4,
    to=32,
    number_of_steps=28,
    command=actualizar_longitud
)
slider.set(12)
slider.pack(pady=10)


entrada_contraseña = ctk.CTkEntry(
    app,
    width=300,
    justify="center",
    font=("Arial", 14)
)
entrada_contraseña.pack(pady=15)


seguridad_label = ctk.CTkLabel(app, text="")
seguridad_label.pack(pady=5)


#Funcion para generar y evaluar la contraseña
def generar():
    longitud = int(slider.get())
    contraseña = generar_contraseña(longitud)
    nivel, color = evaluar_contraseña(contraseña)

    entrada_contraseña.delete(0, "end")
    entrada_contraseña.insert(0, contraseña)

    seguridad_label.configure(
        text=f"Nivel de seguridad: {nivel}",
        text_color=color
    )


boton_generar = ctk.CTkButton(
    app,
    text="Generar contraseña",
    command=generar
)
boton_generar.pack(pady=15)

app.mainloop()
