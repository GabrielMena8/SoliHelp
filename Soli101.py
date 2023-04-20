##Cosas basicas de python

#La sintaxis es muy sencilla, el asunto viene con prestarle atencion a la indentacion de los bloques de codigo, siempre que haya una instruccion que cambie su indentacion
#Todo lo demas cambia tambien


#1. No se necesita definir el tipo de variable al declararla
#2. Las strings se definen con cual tipo de comillas, simples o dobles

q = 10
p = 199
c=[q, "d" , 'f' ,3]

#2. Python tiene muchas funciones built in que salvan mucho tiempo al usuario, la sintaxis es case sensitive asi que 

#Print("Hola mundo!") ##Da error

print("Hola mundo!") ##Es la forma correcta

##Metodos de strings
#Hay un monton de metodos built in para manipular los datos de cada tipo de variable pero el mas extenso es con las strings aca esta la lista y lo que haces, you can go nuts probandolas

string="AguadDacate"
print(string.casefold()) ##Puedes encadenar distintos metodos

# capitalize()	Converts the first character to upper case
# casefold()	Converts string into lower case
# center()	Returns a centered string
# count()	Returns the number of times a specified value occurs in a string
# encode()	Returns an encoded version of the string
# endswith()	Returns true if the string ends with the specified value
# expandtabs()	Sets the tab size of the string
# find()	Searches the string for a specified value and returns the position of where it was found
# format()	Formats specified values in a string
# format_map()	Formats specified values in a string
# index()	Searches the string for a specified value and returns the position of where it was found
# isalnum()	Returns True if all characters in the string are alphanumeric
# isalpha()	Returns True if all characters in the string are in the alphabet
# isascii()	Returns True if all characters in the string are ascii characters
# isdecimal()	Returns True if all characters in the string are decimals
# isdigit()	Returns True if all characters in the string are digits
# isidentifier()	Returns True if the string is an identifier
# islower()	Returns True if all characters in the string are lower case
# isnumeric()	Returns True if all characters in the string are numeric
# isprintable()	Returns True if all characters in the string are printable
# isspace()	Returns True if all characters in the string are whitespaces
# istitle()	Returns True if the string follows the rules of a title
# isupper()	Returns True if all characters in the string are upper case
# join()	Converts the elements of an iterable into a string
# ljust()	Returns a left justified version of the string
# lower()	Converts a string into lower case
# lstrip()	Returns a left trim version of the string
# maketrans()	Returns a translation table to be used in translations
# partition()	Returns a tuple where the string is parted into three parts
# replace()	Returns a string where a specified value is replaced with a specified value
# rfind()	Searches the string for a specified value and returns the last position of where it was found
# rindex()	Searches the string for a specified value and returns the last position of where it was found
# rjust()	Returns a right justified version of the string
# rpartition()	Returns a tuple where the string is parted into three parts
# rsplit()	Splits the string at the specified separator, and returns a list
# rstrip()	Returns a right trim version of the string
# split()	Splits the string at the specified separator, and returns a list
# splitlines()	Splits the string at line breaks and returns a list
# startswith()	Returns true if the string starts with the specified value
# strip()	Returns a trimmed version of the string
# swapcase()	Swaps cases, lower case becomes upper case and vice versa
# title()	Converts the first character of each word to upper case
# translate()	Returns a translated string
# upper()	Converts a string into upper case
# zfill()	Fills the string with a specified number of 0 values at the beginning



#Bucles
# Los mismos bucles clasicos

# for i in range(100): ##Los bucles for lo puedes trabajar de distintas maneras usando la funcion range(), esta funcion toma hasta 3 parametros y se puede usar de distintas formas

##3.1 in range(n), va a recorrer n veces desde 0 hasta el extremo n, con un incremento unico de unidades entre iteracion
##3.2 in range(b,n) va a recorrer desde b a n incrementando en uno en uno
##3.2 in range(b,n,c) va a recorrer desde b a n incrementando c unidades en cada loop 
## Todas son validas y funcionan de forma similar

for x in range(10):
    print(x)

for a in range(0,9):
    print(a)

for d in range(0,10,2):
    print(d)
    
