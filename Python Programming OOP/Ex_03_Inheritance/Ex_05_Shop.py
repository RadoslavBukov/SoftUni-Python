"""
Test Code	                            Output
food = Food("apple")                    [apple, water]
drink = Drink("water")                  water
repo = ProductRepository()              apple: 10
repo.add(food)                          water: 10
repo.add(drink)
print(repo.products)
print(repo.find("water"))
repo.find("apple").decrease(5)
print(repo)
"""
from Ex_05_project.drink import Drink
from Ex_05_project.food import Food
from Ex_05_project.product import Product
from Ex_05_project.product_repository import ProductRepository

food = Food("apple")
drink = Drink("water")
repo = ProductRepository()
repo.add(food)
repo.add(drink)
print(repo.products)
print(repo.find("water"))
repo.find("apple").decrease(15)
print(repo)
repo.remove("water")
print(repo)