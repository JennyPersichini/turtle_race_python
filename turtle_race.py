from turtle import Turtle, Screen                                                              # importo il modulo turtle, in particolare le classi Turtle e Schreen
from random import randint

screen = Screen()                                                                              # creo una istanza schreen della classe Schreen
screen.setup(width=500, height=400)                                                            # i parametri sono le musure in pixel della finestra
giocata = screen.textinput(title="Giocata", prompt="Scegli il colore della tua tartaruga:")    # chiedo all'utente la sua giocata
colori = ["red", "green", "yellow", "blue", "pink", "purple"]   
posizione_y = [0, -25, -50, 25, 50, 75]                               # creo una lista di colori, saranno poi i colori delle tartarughe in gara

# t = Turtle(shape = "turtle")                                                                 # creo una istanza t della classe Turtle / passando il parametro shape ottengo lo stesso risultato del metodo shape()
# t.shape("turtle")                                                                            # con il metodo shape() cambio la forma del "personaggio" che di default è una freccia verso dx 
# t.color("red")
# t.penup()                                                                                    # letteralmente "penna su", toglie la scia della tartaruga
# t.goto(x=-240, y=0)  

turtles = []
# per far si che siano più tartarughe diverse, uso il ciclo for:
for num in range(6):
    t = Turtle(shape = "turtle")                                                               # creo una istanza t della classe Turtle / passando il parametro shape ottengo lo stesso risultato del metodo shape()                                                                   
    t.color(colori[num])
    t.penup()                                                                                      
    t.goto(x=-240, y=posizione_y[num])  
    turtles.append (t)                                                                         

# usando un ciclo for, la tartaruga creerà un quadrato:
# for x in range(4):
    # t.forward(100)                                                                          
    # t.right(90)                                                                             
                
# usando sempre il ciclo for , sempre utilizzando forward e right:
# for x in range(10):
    # t.forward(randint(20, 50))                                                               # anzichè passare valori fissi, passo valori random, quindi utilizzo randint, e suppongo che la tartaruga si muova con step con lunghezza tra 20 e 50                   
    # t.right(randint(0, 360))                                                                 # anche qui, angolo variabile tra 0 e 360 

start = True
# per farle "gareggiare" userò un ciclo while:
while start:
    for turtle in turtles:
        if turtle.xcor() > 230:                                                                # essendo un ciclo infinito, dovrò inserire una condizione che quando si avvera, allora la gara si ferma
            start = False
            if giocata == turtle.pencolor():
                print("Hai vinto!!!")
            else:
                print("Hai perso :(")
                print(f"Ha vinto la tartaruga {turtle.pencolor()}")
        turtle.forward(randint(0, 10))                                 

screen.exitonclick()                                                                           # chiamo su di essa il metodo exitomclick() --> la finestra che creo rimane aperta finchè non la chiudo con la x



