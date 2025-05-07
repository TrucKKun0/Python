#LEGB(Local, Enclosing, Global, Built-in) rule
#LEGB rule is a rule that Python follows to resolve variable names.
import builtins
#Built-in functions are functions that are always available in Python.
def my_min():
    pass  # This is a built-in function, but we are defining a local function with the same name.

m = min([1,2,5,4])
print(m)  # This will print 1, which is the minimum value in the list.

x = 'Global x'  # Global variable

def test(z):
    #global x  # Declare x as global to modify the global variable
    #x = 'Local x'  # This will create a new local variable x
    #y = 'Local y'
    #print(x)  # This will print 'Global x' because x is defined in the global scope.
    # print(y)
    print(z)  # This will print the value of z passed to the function.

#test('local z')  # This will print 'Local y' because y is defined in the local scope of the test function.
#print(y)# This will raise a NameError because y is not defined in the global scope.
#print(x)

#Enclosing scope
def outer():
    x = 'outer x'
    def inner():
        
        x = 'inner x'  # This will modify the variable in the outer function's scope
        print(x)  # This will print 'inner x'
    inner()
    print(x)  # This will print 'outer x'
outer()
print(x)  # This will print 'Global x' because x is defined in the global scope.