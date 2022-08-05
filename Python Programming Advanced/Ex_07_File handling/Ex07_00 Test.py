import os
from io import open

def print_contents(file_path):
    print(f' --- Opening {file_path} ---')
    file = open(file_path)
    print(file.read())

print_contents("Ex07_00 Test Demo.txt")

print_contents('/Users/bukov/PycharmProjects/pythonProject/Python Advanced/Ex_07_File Handling/Ex07_00 Test Demo.txt')

#Not working variant:
#print_contents('\Users\bukov\PycharmProjects\pythonProject\Python Advanced\Ex_07_File Handling\Ex07_00 Test Ex07_00 Test Demo.txt')

print_contents('C:/Users/bukov/PycharmProjects/pythonProject/Python Advanced/Ex_07_File Handling/Ex07_00 Test Demo')