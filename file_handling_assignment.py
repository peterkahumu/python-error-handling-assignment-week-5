
with open('my_file.txt', 'w+') as file: 
   file.write(['Hello World !\n', 'I am learning PHP at the moment\n', 'I am also learnig python and its real fun for me.' ])
   
   
# read the file contents and display them on the console.
with open('my_file.txt', 'r') as file:
   print(file.read)
   
# append lines to the file using python code.
with open('my_file.txt', 'a') as file:
   file.write('\n I am appending this line to the file usinh python code.')

# user error handling technique to handle the errors that might arise during progam execution.
# FileNotFound Error
# PermissionError
try:
   with open('my_file.txt', 'r') as file:
      print(file.read)
except FileNotFoundError:
   print('File not found. Please check for the existence of the file or try creating a new file.')
except PermissionError:
   print("Access to the file is denied to this user. Please check the file permissions and try again.")
except Exception as e:
   print("An error occured:", e)