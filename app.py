# Importa as bibliotecas necessárias
from tkinter import *
import tkinter as tk
from geopy.geocoders import Nominatim
from tkinter import ttk, messagebox
from timezonefinder import TimezoneFinder
from datetime import datetime
import requests
import pytz

# Cria a janela principal da GUI usando Tkinter
window=Tk()
window.title('Previsão do tempo')
window.geometry('900x500+300+200')
window.resizable(False,False)

def getWeather ():
    try:
        cidade=textfield.get()

        geolocator = Nominatim(user_agent='geoapiExercises')
        local = geolocator.geocode(cidade)
        obj = TimezoneFinder()
        resultado = obj.timezone_at(lng=local.longitude, lat=local.latitude)
        print(resultado)

        home=pytz.timezone(resultado)
        horario_local=datetime.now(home)
        horario_atual = horario_local.strftime('%I:%M %p')
        relogio.config(text=horario_atual)
        nome.config(text='HORÁRIO ATUAL')

        # Requests na API
        api = 'https://api.openweathermap.org/data/2.5/weather?q='+cidade+'&appid=451a5e7fa6ccbfa2c20ec000322a1fd5'

        json_data = requests.get(api).json()
        condicaoRequest = json_data['weather'][0]['main']
        descricaoRequest = json_data['weather'][0]['description']
        temperaturaRequest = int(json_data['main']['temp']-273.15)
        pressaoRequest = json_data['main']['pressure']
        umidadeRequest = json_data['main']['humidity']
        ventoRequest = json_data['wind']['speed']

        temperatura.config(text=(temperaturaRequest, 'º'))
        condicao.config(text=(condicaoRequest, '|', 'Sensação', 'Térmica', temperaturaRequest, 'º'))

        textoVento.config(text=(ventoRequest, 'KM/H'))
        textoUmidade.config(text=(umidadeRequest, '%'))
        textoDescricao.config(text=descricaoRequest)
        textoPressao.config(text=(pressaoRequest, 'hPa'))
    
    except Exception as e:
        messagebox.showerror('Previsão do Tempo', 'Entrada Inválida.')

# Define botão de pesquisa
Search_image=PhotoImage(file='assets/img/search.png')
myImage=Label(image=Search_image)
myImage.place(x=15,y=22)

# Cria campo de entrada de dados
textfield = tk.Entry(window, justify='center', width=17, font=('poppins', 25,'bold'), bg='#3b3b3b', borderwidth=0, highlightthickness=0, fg='white')
textfield.place(x=50,y=40)
textfield.focus()

Search_icon=PhotoImage(file='assets/img/search_icon.png')
myImage_icon=Button(image=Search_icon, borderwidth=0, highlightthickness=0, cursor='hand2', bg='#3b3b3b', activebackground='#3b3b3b', command=getWeather)
myImage_icon.place(x=395, y=33)

Logo_image=PhotoImage(file='assets/img/logo.png')
logo=Label(image=Logo_image)
logo.place(x=150, y=115)


# Setor inferior
Frame_image=PhotoImage(file='assets/img/box.png')
frame_myImage=Label(image=Frame_image)
frame_myImage.pack(padx=5, pady=5, side= BOTTOM)

# tempo
nome=Label(window, font=('arial', 15, 'bold'))
nome.place(x=30, y=100)
relogio=Label(window, font=('Helvetica', 20))
relogio.place(x=30, y=130)

# Textos e titulos inferiores
tituloVento = Label(window, text='VENTO', font=('Helvetica', 15, 'bold'), fg='white', bg='#1AB5EF')
tituloVento.place(x=120, y=405)

tituloUmidade = Label(window, text='UMIDADE', font=('Helvetica', 15, 'bold'), fg='white', bg='#1AB5EF')
tituloUmidade.place(x=270, y=405)

tituloDescricao = Label(window, text='DESCRIÇÂO', font=('Helvetica', 15, 'bold'), fg='white', bg='#1AB5EF')
tituloDescricao.place(x=460, y=405)

tituloPressao = Label(window, text='PRESSÂO', font=('Helvetica', 15, 'bold'), fg='white', bg='#1AB5EF')
tituloPressao.place(x=670, y=405)

temperatura=Label(font=("arial",70, 'bold'), fg='#EE666D')
temperatura.place(x=400, y=150)
condicao=Label(font=('arial', 15, 'bold'))
condicao.place(x=400, y=250)

textoVento=Label(text='', font=('arial', 20, 'bold'), bg='#1AB5EF')
textoVento.place(x=100, y=430)

textoUmidade=Label(text='', font=('arial', 20, 'bold'), bg='#1AB5EF')
textoUmidade.place(x=280, y=430)

textoDescricao=Label(text='', font=('arial', 20, 'bold'), bg='#1AB5EF')
textoDescricao.place(x=420, y=430)

textoPressao=Label(text='', font=('arial', 20, 'bold'), bg='#1AB5EF')
textoPressao.place(x=670, y=430)

window.mainloop()