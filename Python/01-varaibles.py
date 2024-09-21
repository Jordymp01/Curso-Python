#Estas son los tipos de variables o funciones que se tiene.
#Variables

my_string_varaible = "My String variable"
print(my_string_varaible)

my_int_varaible = 5
print(my_int_varaible)

my_int_to_str_variable = str(my_int_varaible)
print(my_int_to_str_variable)
print(type(my_int_to_str_variable))

my_bool_variable = False
print (my_bool_variable)

#Concatenación de variables en un print
print(my_string_varaible, my_int_to_str_variable, my_bool_variable)
print("Este es el valor de :", my_bool_variable)

#Algunas funciones del sistema 
print(len(my_bool_variable)) #len sirve para contar cuantos  caracteres tiene una variable

#Variables en una sola línea. !Cuidado con abusar de esta sintaxis!
name,surname, alias, age = "Jordan", "Pérez", "Jordy", "23"
print("Me llamo:", name,surname,"Mi edad es :", age, "Y mi apodo es :",alias)

#Inputs
"""
first_name = input("What's your name? ") 
age = input("How old are you ? ")

print(name)
print(age)
"""

#Cambiamos su tipo

name = 23
age = "Jordy"
print(name)
print(age)

#¿Forzamos el tipo? 
address : str = "Mi dirección "
address = 32
print(address)

