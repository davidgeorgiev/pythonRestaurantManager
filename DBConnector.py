import MySQLdb

class DBConnector():
	def __init__ (self,parent):
		self.parent = parent
		self.db = MySQLdb.connect(host="localhost", user="root", passwd="laputa", db="DBrestaurant")
		self.lastResult = list()
	def RunTest(self,event):
		self.GetCustomerInfo()
	def GetCustomerInfo(self):
		cur = self.db.cursor()
		cur.execute("select * from customers;")
		for row in cur.fetchall():
			self.lastResult = [str(row[0]),str(row[1]),str(row[2]),str(row[3]),str(row[4]),str(row[5]),str(row[6])]
	def PrintLastResult(self,event):
		print(self.lastResult)
	def AddCustomer(self,dataList):
		cur = self.db.cursor()
		cur.execute("INSERT INTO `DBrestaurant`.`customers` (`firstName`,`middleName`,`lastName`,`email`,`phone`,`address`) VALUES ("+dataList[0]+","+dataList[1]+","+dataList[2]+","+dataList[3]+","+dataList[4]+","+dataList[5]+");")
		self.db.commit()
		cur.close()
	def __exit__():
		self.db.close()
