try:
    file = open("test.txt", "r")
    if file.name == "test.txt":
        raise FileNotFoundError("File not found")
  
    # var = bad_var  # This will raise a NameError because bad_var is not defined.
except FileNotFoundError as e:
    print(e)
except Exception as e:
    print(e)
else:
    print(file.read())
    file.close()
finally:
    print("Executing finally block")
    # This block will always execute
