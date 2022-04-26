import turtle

s = turtle.Screen()
t = turtle.Turtle()
turtle.shape("turtle")

print('Para onde vamos?')
# se movendo
x = float(input('Digite o valor x\n'))
y = float(input('Digite o valor y\n'))
t.goto(x, y)

print('Vamos girar!')
angulo = int(input('Digite o valor do angulo\n'))
t.left(angulo)
