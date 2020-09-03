#Python Basics

#defining variables
x = 5
y = "lalala"

#defining functions
def hello():
    print("Hello, hellooooooo")
hello()

#printing to stdout
print("Hello World!")
print(y)
print(f"Variables are {y} and {x}")

#arrays
array = [1,2,3,4]
print(array)
print(array[2])

#2D list
array = [[1,2,3],
         [4,5,6],
         [7,8,9]]
print(array)
print(array[2][2])

#hashmap
car = {
  "make": "Toyota",
  "model": "Prius",
  "year": 2008
}
print(car["model"])
for x in car:
    print(x)
for x in car.values():
    print(x)