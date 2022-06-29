#Faça um Programa que peça a temperatura em graus Celsius, transforme e mostre em graus Fahrenheit.
#Fórumula = (C*1.8)+32
temperatura_c=float(input("Informe a temperatura em CELSIUS: \n")) #Em se tratando de temperatura, é preciso usar a conversão do input (strint) para float.
temperatura_f=(temperatura_c*1.8)+32
print("A temperatura", temperatura_c, "CELSIUS equivale a " "%.2f" % temperatura_f, "graus FAHRENHEIT")
