import random #this is used to import module

def random_number_gen():
    random_number = random.randint(9999,9999999) #this is used to generate random number between 1 and 100
    return random_number

print(random_number_gen())