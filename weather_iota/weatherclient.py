import sys
import time
import json
from iota import iota

class weatherclient:
	def __init__(self, seed, address):
		self.seed=seed
		self.address=address
		self.node=iota(seed)
		self.txCounter=self.node.txCounter
	
	def requestWeather(self):
		try:
			print("Take a coffee, I am sendig the request...")
			self.respondAddress=self.node.genAddress()
			print("I have generate you an address where you will recive the weather infos."+self.respondAddress)
			print("I'm sending now the request to the weather node...")
			self.message="{'command':'getWeather','address':'"+self.respondAddress+"'}"
			self.node.searchNewTransaction()
			self.node.sendMessage(self.address, self.message, '1')
			print("Waiting until weather Infos recived.")
			self.txCounter=self.node.txCounter
			while True:
				time.sleep(5)
				self.transaction=self.node.searchNewTransaction()
				if self.txCounter+2==self.node.txCounter:
					break
			self.message=self.node.searchMessage(self.transaction).replace('\'','\"')
			print(self.message)
			return self.message
		except Exception as e:
			self.error="Can not run Weather Node. "+str(e)
			print(self.error)
			return None

	def sendPromotion(self, message):
		self.message="{'command':'sendPromotion','promotion':'"+message+"'}"
		try:
			print("Take a coffee, I am sendig the request...")
			self.node.sendMessage(self.address, self.message, '1')
			print("Succesfully send Promotion.")
		except Exception as e:
			self.error="Can not send a Promotion. " +str(e)
			print(self.error)
			return None


	def execute(self, jsonData):
		try:
			print("Temperatur: "+jsonData['temperature']+"Humidity: "+jsonData['humidity']+"Pressure: "+jsonData['pressure'])
		except Exception as e:
			self.error="Can't execute command. "+str(e)
			return None

	
