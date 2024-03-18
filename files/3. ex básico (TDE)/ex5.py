"""Escreva um algoritmo que realize a conversão de °c para Fahrenheit"""
celcius = float(input("Digite a temperatura em °c desejada: "))
fahrenheit = (celcius * 1.8) + 32
print(f"{celcius:.1f}°c em Fahrenheit são {fahrenheit:.1f}F")
