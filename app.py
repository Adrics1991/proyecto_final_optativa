import tkinter as tk
from chatbot import ChatbotPlantas

bot = ChatbotPlantas("plantas.json")

def enviar():
    pregunta = entrada.get()
    respuesta = bot.responder(pregunta)
    chat.insert(tk.END, "Tú: " + pregunta + "\n")
    chat.insert(tk.END, "Bot: " + respuesta + "\n\n")
    entrada.delete(0, tk.END)

ventana = tk.Tk()
ventana.title("Chatbot de Plantas")

chat = tk.Text(ventana, width=60, height=20)
chat.pack()

entrada = tk.Entry(ventana, width=50)
entrada.pack()

boton = tk.Button(ventana, text="Enviar", command=enviar)
boton.pack()

ventana.mainloop()
