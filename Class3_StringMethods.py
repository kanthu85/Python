String='sreekanth reddy Lakkireddy'
print(String.capitalize()) #Converts the first character to upper case
print(String.casefold())#Converts string into lowercase
print(String.center(50))#Returns a centered string, with specified space length
print(String.count('r'))#returns the number of times a specified value appears in the string
print(String.encode())	#Returns an encoded version of the string,encode in single quotes
print(String.endswith("a")) #Returns true if the string ends with the specified value
expandtab="H\te\tl\tl\to"
print(expandtab.expandtabs())	   #Sets the tab size of the string
print(String.find("r"))	       #Searches the string for a specified value and returns the position of where it was found first occurance
string_format ="sreekanth {middlename} {lastname}"
print(string_format.format(middlename='reddy',lastname='Lakkireddy'))       #Formats specified values in a string
data = {"name": "Alice", "age": 30}
formatted_string = "My name is {name} and I am {age} years old.".format_map(data)
print(formatted_string) #Formats specified values in a string from dictionary
print(String.index('d')) #Searches the string for a specified value and returns the position of where it was found
print(String.isalnum())	#Returns True if all characters in the string are alphanumeric
print(String.isalpha())	#Returns True if all characters in the string are in the alphabet
print(String.isascii())	#Returns True if all characters in the string are ascii characters
print(String.isdecimal())	#Returns True if all characters in the string are decimals
print(String.isdigit())	#Returns True if all characters in the string are digits
print(String.isidentifier())	#Returns True if the string(contains alphanumeric letters (a-z) and (0-9), or underscores (_)) is an identifier(A valid identifier cannot start with a number, or contain any spaces.)
print(String.islower())	#Returns True if all characters in the string are lower case
print(String.isnumeric())	#Returns True if all characters in the string are numeric
print(String.isprintable())#Returns True if all characters in the string are printable
str1= " "
print(str1.isspace())	#Returns True if all characters in the string are whitespaces
print(String.istitle())	#Returns True if the string follows the rules of a title()The istitle() method returns True if all words in a text start with a upper case letter, AND the rest of the word are lower case letters, otherwise False.
print(String.isupper())	#Returns True if all characters in the string are upper case
print(String.join( 'la'))	#Converts the elements of an iterable into a string
txt = "banana"
x = txt.ljust(20)
print(x, "is my favorite fruit.") #Returns a left justified version of the string
print(String.lower())	#Converts a string into lower case
print(String.lstrip())	#Returns a left trim version of the string
#maketrans() - Create a mapping table, and use it in the translate() method to replace any "S" characters with a "P" character:
txt = "Hello Sam!"
mytable = str.maketrans("S", "P")
print(txt.translate(mytable))	#Returns a translation table to be used in translations
#partition() -Search for the word "bananas", and return a tuple with three elements:
#1 - everything before the "match"
#2 - the "match"
#3 - everything after the "match"
txt = "I could eat bananas all day"
x = txt.partition("bananas")
print(x)	#Returns a tuple where the string is parted into three parts
print(String.replace('s','S'))#	Returns a string where a specified value is replaced with a specified value
print(String.rfind('r'))	#Searches the string for a specified value and returns the last position of where it was found
print(String.rindex('r'))	#Searches the string for a specified value and returns the last position of where it was found
txt = "banana"
x = txt.rjust(20)
print(x, "is my favorite fruit.")	#Returns a right justified version of the string
txt = "I could eat bananas all day"
x = txt.rpartition("bananas")
print(x) #Returns a tuple where the string is parted into three parts
print(String.rsplit(' '))	#Splits the string at the specified separator, and returns a list
print(String.rstrip())	#Returns a right trim version of the string
print(String.split(' '))	#Splits the string at the specified separator, and returns a list
linebreak_string ='sreekanth \n reddy \n Lakkireddy'
print(linebreak_string.splitlines())	#Splits the string at line breaks and returns a list
print(String.startswith('s'))	#Returns true if the string starts with the specified value
print(String.strip())	#Returns a trimmed version of the string
print(String.swapcase())	#Swaps cases, lower case becomes upper case and vice versa
print(String.title())	#Converts the first character of each word to upper case
#use a dictionary with ascii codes to replace 83 (S) with 80 (P):
mydict = {83:  80}
txt = "Hello Sam!"
print(txt.translate(mydict))	#Returns a translated string
print(String.upper())	#Converts a string into upper case
txt = "50"
x = txt.zfill(10)
print(x) #Fills the string with a specified number of 0 values at the beginning
#
string_title='sreekanthreddyLakkireddy'
print((string_title.casefold()).capitalize().istitle())

# --------------Continue with Data Types i Next Class----------------