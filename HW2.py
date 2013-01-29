stock_dictionary = {}
import random

class Portfolio(object):

	def __init__(self):
		self.cash = 0
		self.stock_list = {}
		self.fund_list = {}
		self.history_list = ['\nLog of Transactions:','New portfolio created']
		#print "New portfolio created."
		
	def printlist(self):
		line1 = "\nCash: $" + str(round(self.cash,2)) + "\nStocks: \n"
		for k, v in self.stock_list.items():
			line2 = str(k) + " " + str(round(v,0))
		line3 = "\nMutual funds: \n"
		for k, v in self.fund_list.items():
			line4 = str(k) + " " + str(round(v,2))
		return line1 + line2 + line3 + line4
		
	def addCash(self, cashamount):
		self.cashamount = cashamount
		self.cash = self.cash + cashamount
		self.history_list.append("$" + str(cashamount) + " cash added to portfolio.")
		#print "$" + str(cashamount) + " cash added to portfolio."
	
	def buyStock(self, stockamount, stockname):
		self.stockamount = stockamount
		self.stockname = stockname
		self.cash = self.cash - (stockamount * stock_dictionary[stockname.stocksymbol])
		self.history_list.append(str(stockamount) + " shares of stock " + stockname.stocksymbol + " added to portfolio.")
		if self.stockname.stocksymbol in self.stock_list:
			self.stock_list[self.stockname.stocksymbol] = self.stock_list[self.stockname.stocksymbol] + stockamount
		else:
			self.stock_list[self.stockname.stocksymbol] = stockamount
		#print str(stockamount) + " shares of stock " + stockname.stocksymbol + " added to portfolio."
	
	def buyMutualFund(self, fundamount, fundname):
		self.fundamount = fundamount
		self.fundname = fundname
		self.cash = self.cash - fundamount
		self.history_list.append(str(fundamount) + " shares of mutual fund " + fundname.fundsymbol + " added to portfolio.")
		if self.fundname.fundsymbol in self.fund_list:
			self.fund_list[self.fundname.fundsymbol] = self.fund_list[self.fundname.fundsymbol] + fundamount
		else:
			self.fund_list[self.fundname.fundsymbol] = fundamount
		#print str(fundamount) + " shares of mutual fund " + fundname.fundsymbol + " added to portfolio."
	
	def sellMutualFund(self, sellfundname, sellfundamount):
		self.sellfundamount = sellfundamount
		self.sellfundname = sellfundname
		sellfundprice = random.uniform(0.9, 1.2)
		self.fund_list[sellfundname] = self.fund_list[sellfundname] - sellfundamount
		self.cash = self.cash + (sellfundamount * sellfundprice)
		self.history_list.append(str(sellfundamount) + " shares of mutual fund " + sellfundname + " sold.")
		#print str(sellfundamount) + " shares of mutual fund " + sellfundname.fundsymbol + " sold."
	
	def sellStock(self, sellstockname, sellstockamount):
		self.sellstockname = sellstockname
		self.sellstockamount = sellstockamount
		sellstockprice = random.uniform(0.5 * stock_dictionary[sellstockname], 1.5 * stock_dictionary[sellstockname])
		self.stock_list[sellstockname] = self.stock_list[sellstockname] - sellstockamount
		self.cash = self.cash + (sellstockamount * sellstockprice)
		self.history_list.append(str(sellstockamount) + " shares of stock " + sellstockname + " sold.")
		#print str(sellstockamount) + " shares of stock " + sellstockname.stocksymbol + " sold."
	
	def withdrawCash(self, sellcashamount):
		self.sellcashamount = sellcashamount
		self.cash = self.cash - sellcashamount
		self.history_list.append("$" + str(sellcashamount) + " removed from portfolio.")
		#print "$" + str(sellcashamount) + "removed from portfolio."
	
	def history(self):
		print " " + "\n ".join(self.history_list)
		
	def __str__(self):
		return str(self.printlist())
	
class Stock(object):

	def __init__(self, price, stocksymbol):
		self.price = price
		self.stocksymbol = stocksymbol
		stock_dictionary[stocksymbol] = price
		#print "Stock " + stocksymbol + " created with price of $" + str(price)
	
class MutualFund(object):

	def __init__(self, fundsymbol):
		self.fundsymbol = fundsymbol
		#print "Mutual fund " + fundsymbol + " created."
	
	