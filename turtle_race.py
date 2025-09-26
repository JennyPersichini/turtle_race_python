from turtle import Turtle, Screen      # importo il modulo turtle, in particolare le classi Turtle e Schreen

t = Turtle(shape = "turtle")                             # creo una istanza t della classe Turtle / passando il parametro shape ottengo lo stesso risultato del metodo shape()
# t.shape("turtle")                      # con il metodo shape() cambio la forma del "personaggio" che di default è una freccia verso dx 
t.color("red")

screen = Screen()                      # creo una istanza schreen della classe Schreen
screen.exitonclick()                   # chiamo su di essa il metodo exitomclick() --> la finestra che creo rimane aperta finchè non la chiudo con la x



