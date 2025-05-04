#File Object

# file = open('test.txt', 'r') #opens the file in read mode
# print(file.name) #prints the name of the file
# print(file.mode) #prints the mode of the file
# file.close() #closes the file

# #Context Manager
# with open('test2.txt','r') as f:
    
#     #f_contents = f.readlines() #reads the file and stores it in the variable as a list
#     #print(f_contents) #prints the contents of the file as a list
#     #f_contents = f.readline() #reads the file and stores it in the variable as a list
#     # for line in f: #reads the file and stores it in the variable as a list
#     #     print(line, end='') #prints the contents of the file as a list
#     size_of_file = 10
#     f_contents = f.read(size_of_file) #reads the file and stores it in the variable
#     print(f_contents, end='')
#     f.seek(0)
#     f_contents = f.read(size_of_file) #reads the file and stores it in the variable
#     print(f_contents)

#     # while len(f_contents) > 0:
#     #     print(f_contents, end='*')
#     #     f_contents = f.read(size_of_file)
    

 #Write File
# with open('test2.txt','w') as f:
#     f.write('Test')
#     f.seek(0)
#     f.write('R')

with open('test.txt','r') as rf:
    with open('test_copy.txt','w') as wf:
        for line in rf:
            wf.write(line)