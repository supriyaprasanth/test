f=[212,194,176,158,140]
c=[100,80,90,40,30]
print('Fahrenheit to Celsius')
print('Fahrenheit')
print(f)
print('Celsius')
ce=list(map(lambda f:int(5/9*(f-32)),f))
print(ce)
print('Celsius to Fahrenheit')
print('Celsius')
print(c)
print('Fahrenheit')
fa=list(map(lambda c:int((9/5*c))+32,c))
print(fa)
