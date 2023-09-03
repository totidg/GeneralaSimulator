import tkinter as tk
import random

def escalera(tupla):
    tupla_ordenada = sorted(tupla)
    i = 0
    if tupla_ordenada[0] == 1 or tupla_ordenada[0] == 2:
        while i < len(tupla) and tupla.count(tupla[i]) == 1:
            i+=1
    return len(tupla) == i

def generala(tupla):
    i=0
    while i < len(tupla) and  tupla.count(tupla[i]) != 5:
        i+=1
    return len(tupla) != i

def poker(tupla):
    i=0
    while i < len(tupla) and tupla.count(tupla[i]) != 4:
        i+=1
    return len(tupla) != i

def full(tupla):
    i=0     
    while i < len(tupla) and (tupla.count(tupla[i]) == 2 or tupla.count(tupla[i]) == 3):
        i+=1
    return len(tupla) == i

def porcentaje(cantidad, total):
    return cantidad / total * 100

def tirar_dados():
    tirada = random.choices([1, 2, 3, 4, 5, 6], k=5)
    return tirada

def actualizar_resultados():
    tirada = tirar_dados()
    resultado_escalera.config(text=f'Escalera: {escalera(tirada)}')
    resultado_generala.config(text=f'Generala: {generala(tirada)}')
    resultado_poker.config(text=f'Poker: {poker(tirada)}')
    resultado_full.config(text=f'Full: {full(tirada)}')
    resultado_tirada.config(text=f'Dados: {tirada}')


ventana = tk.Tk()
ventana.title("Simulador de Juegos de Dados")
ventana.geometry("400x300")  


estilo_etiqueta = {'font': ('Arial', 14), 'pady': 10}


resultado_escalera = tk.Label(ventana, text="Escalera: ", **estilo_etiqueta)
resultado_escalera.pack()

resultado_generala = tk.Label(ventana, text="Generala: ", **estilo_etiqueta)
resultado_generala.pack()

resultado_poker = tk.Label(ventana, text="Poker: ", **estilo_etiqueta)
resultado_poker.pack()

resultado_full = tk.Label(ventana, text="Full: ", **estilo_etiqueta)
resultado_full.pack()

resultado_tirada = tk.Label(ventana, text="Dados: ", **estilo_etiqueta)
resultado_tirada.pack()


boton_tirar = tk.Button(ventana, text="Tirar Dados", command=actualizar_resultados, width=20, height=2)
boton_tirar.pack()

ventana.mainloop()
