"""
Output:

Product
coffee
2.5
Beverage
Product
coffee
2.5
50
Soup
Starter
fish soup
9.9
230
"""
from Ex_04_project.product import Product
from Ex_04_project.beverage.beverage import Beverage
from Ex_04_project.food.food import Food
from Ex_04_project.beverage.hot_beverage import HotBeverage
from Ex_04_project.beverage.cold_beverage import ColdBaverage
from Ex_04_project.beverage.tea import Tea
from Ex_04_project.beverage.coffee import Coffee
from Ex_04_project.food.dessert import Dessert
from Ex_04_project.food.starter import Starter
from Ex_04_project.food.soup import Soup
from Ex_04_project.food.main_dish import MainDish
from Ex_04_project.food.cake import Cake
from Ex_04_project.food.salomon import Salomon

product = Product("coffee", 2.5)
print(product.__class__.__name__)
print(product.name)
print(product.price)
beverage = Beverage("coffee", 2.5, 50)
print(beverage.__class__.__name__)
print(beverage.__class__.__bases__[0].__name__)
print(beverage.name)
print(beverage.price)
print(beverage.milliliters)
soup = Soup("fish soup", 9.90, 230)
print(soup.__class__.__name__)
print(soup.__class__.__bases__[0].__name__)
print(soup.name)
print(soup.price)
print(soup.grams)
