# Creators: Eric Mahoney & Anuruddha Karunaratne 
# Course: IT 209 
# Assignment: 8 [Project]
# Description: Cash register game using object oriented programming. Users are prompted with a customer's transaction and must provide the correct amount of change for that transaction. Users get one point for a correct answer and lose 1 point if incorrect.

# imports the random library that we will use to generate random customers and monetary values
import random

class Player:
	def __init__(self, name, score=0):
		self.name = name
		self.score = score

	def returnName(self):
		return name

	def setName(self,name):
		name = self.name
		return("Name changed to: ", name)

class Customer:
	def __init__(self, name, money):
		# list of different names for our customers
		self.name = ['John':, 'Bob', 'Linda', 'Tom', 'Richard', 'Hubert']
		
		# list of different amounts of money that our customers will buy food with.
		self.money = [9.25, 5.00, 10.00, 7.50, 20.00]
		
		# dictionary list of groceries from:
		# http://www.visualcapitalist.com/decade-grocery-prices/
		self.groceries = {
		'white bread': 1.34,
		'wheat bread': 1.99,
		'whole milk': 3.24,
		'salted butter': 3.38,
		'american cheese': 4.28,
		'eggs': 1.43,
		'apples': 1.29,
		'bananas': 0.56,
		'oranges': 1.33,
		'strawberries': 2.21,
		'lemons': 2.01,
		'tomatoes': 1.90,
		'broccoli': 1.81,
		'bacon': 5.79,
		'pasta': 1.28,
		'dried beans': 1.36,
		'ground beef': 4.12,
		'all purpose flour': 0.52,
		'creamy peanut butter': 2.56,
		'top round steak': 5.78,
		'potatoes': 0.72,
		'frozen turkey': 1.59,
		'sirloin steak': 8.07,
		'white rice': 0.72,
		'chocolate chip cookies': 3.47,
		'seedless grapes': 2.67,
		'sugar': 0.65,
		'ice cream': 4.70
		}

	def getCustomer(self):


class Register:
	def __init__(self,one,five,ten,twenty,fifty,oneHundred):
		self.one = one
		self.five = five
		self.ten = ten
		self.twenty = twenty
		self.fifty = fifty
		self.oneHundred = oneHundred

class Score:
	def __init__(self):
		self.score = score

	def addScore(self):
		score += 1
		return score

	def subScore(self):
		score -= 1
		return score

	def returnScore(self):
		return score

class Purchase:
	def __init__(self):
		self.price = price

	def calcTax(self):
		va_sales_tax = 0.043
		tax = price * va_sales_tax
		return tax

class Main:
	def __init__(self):
		self.main = main