
message = "Hello world"

print(message)
print(len(message)) #length of the string
print(message[0]) #prints the character at the index 0
print(message[0:5]) #prints the character from 0 to 4
print(message[6:])#prints the character from 6 to end
print(message.lower()) #prints the string in lower case
print(message.upper()) #prints the string in upper case
print(message.count('l')) #counts the number of l in the string
print(message.find('world')) #finds the index of the word world in the string

message = message.replace("world", "universe") #replaces the word world with universe in the string
print(message)

greeting = "Hello"
name = "Bishow"
new_message = "{}, {}. Welcome!".format(greeting, name) #concatenates the two strings
print(new_message)