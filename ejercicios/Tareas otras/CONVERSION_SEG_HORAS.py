a = input ("Escriba una cantidad de segundos ")

b = int(a)

c = b//3600

d = b % 3600

e = d//60 

h = d%60

f = int(e)

print ( b , "segundos son ", c,  "horas ", f , "minutos y", h , "segundos")