import os 

print(dir(os))#prints all the functions in the os module
print(os.getcwd())#prints the current working directory
os.chdir(r'C:\Users\NITRO V15\OneDrive\Desktop')#changes the current working directory
#print(os.getcwd())
#print(os.listdir())#prints the list of files and folders in the current working directory
#os.mkdir('testy')#creates a new folder in the current working directory
#os.makedirs('test1/test2')#creates a new folder in the current working directory with subfolders
#os.rmdir('testy')#deletes the folder in the current working directory
#os.removedirs('test1/test2')#deletes the folder in the current working directory with subfolders
#os.rename('test.txt','demo.txt')#renames the file in the current working directory
#print(os.stat('demo.txt'))#prints the information of the file in the current working directory
# for dirpath, dirnames, filenames in os.walk(r'C:\Users\NITRO V15\OneDrive\Desktop'):
#     print('Current Path:', dirpath)
#     print('Directories:', dirnames)
#     print('Files:', filenames)
#     print()
#print(os.environ.get('HOME'))#prints the environment variable
#file_path = os.path.join(os.environ.get('HOME'),'test.txt')#joins the path of the file with the environment variable
#print(file_path)
print(os.path.basename('/tmp/test.txt'))#prints the basename of the file
print(os.path.dirname('/tmp/test.txt'))#prints the dirname of the file
print(os.path.split('/tmp/test.txt'))#prints the basename and dirname of the file
print(os.path.exists('/tmp/test.txt'))#prints the boolean value if the file exists or not
print(os.path.isdir('/tmp/test.txt'))#prints the boolean value if the file is directory or not
print(os.path.isfile('/tmp/test.txt'))#prints the boolean value if the file is file or not
print(os.path.splitext('/tmp/test.txt'))#prints the basename and extension of the file
