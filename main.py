import wxversion
wxversion.select("2.8")
import wx
import os
import sys
from DBConnector import DBConnector
from mySqlUpdater import mySqlUpdater
from CustomerManager import CustomerManager
from CustomerAdder import CustomerAdder
from TableAdder import TableAdder
from threading import Thread
from time import sleep

class Frame(wx.Frame):
	def __init__(self):
		wx.Frame.__init__(self, None, title="Restaurant Manager v0.1", pos=(150,150), size=(350,400))
		self.theDBConnector = DBConnector(self)
		self.mySqlUpdater = mySqlUpdater(self)

		panel = wx.Panel(self)
		self.Bind(wx.EVT_CLOSE, self.OnClose)
		self.statusbar = self.CreateStatusBar()

		menubar = wx.MenuBar()
		fileMenu = wx.Menu()
		menubar.Append(fileMenu, '&File')


		MenuQuitItem = fileMenu.Append(wx.ID_EXIT, 'Quit', 'Quit application')
		self.Bind(wx.EVT_MENU, self.OnClose, MenuQuitItem)
		
		MenuAddCustomerItem = fileMenu.Append(wx.ID_ANY, 'Add Customer', 'Adding new Customer')
		self.Bind(wx.EVT_MENU, self.OnAddCustomer, MenuAddCustomerItem)
		MenuAddTableItem = fileMenu.Append(wx.ID_ANY, 'Add Table', 'Adding new Table')
		self.Bind(wx.EVT_MENU, self.OnAddTable, MenuAddTableItem)

		sqlMenu = wx.Menu()
		menubar.Append(sqlMenu, '&Sql')

		MenuUpdateSqlItem = sqlMenu.Append(wx.ID_ANY, 'Update', 'Update Sql')
		self.Bind(wx.EVT_MENU, self.mySqlUpdater.UpdateMySql, MenuUpdateSqlItem)
		
		MenuPrintLastResultSqlItem = sqlMenu.Append(wx.ID_ANY, 'Print Last Result', 'Prints Last Result')
		self.Bind(wx.EVT_MENU, self.theDBConnector.PrintLastResult, MenuPrintLastResultSqlItem)

		self.SetMenuBar(menubar)

		box = wx.BoxSizer(wx.VERTICAL)

		m_text = wx.StaticText(panel, -1, "Information")
		m_text.SetFont(wx.Font(14, wx.SWISS, wx.NORMAL, wx.BOLD))
		m_text.SetSize(m_text.GetBestSize())
		box.Add(m_text, 0, wx.ALL, 10)
		
		self.num_of_customers_button = wx.Button(panel, wx.ID_ANY, "")
		self.num_of_customers_button.Bind(wx.EVT_BUTTON, self.theDBConnector.RunTest)
		box.Add(self.num_of_customers_button, 0, wx.ALL, 10)
		
		self.num_of_tables_button = wx.Button(panel, wx.ID_ANY, "")
		self.num_of_tables_button.Bind(wx.EVT_BUTTON, self.theDBConnector.RunTest)
		box.Add(self.num_of_tables_button, 0, wx.ALL, 10)

		languages = ['C', 'C++', 'Python', 'Java', 'Perl'] 
		self.combo = wx.ComboBox(panel,choices = languages) 
		box.Add(self.combo, 0, wx.ALL, 10)
		self.choice = wx.Choice(panel,choices = languages)
		box.Add(self.choice, 0, wx.ALL, 10)


		m_test_button = wx.Button(panel, wx.ID_ANY, "Test database")
		m_test_button.Bind(wx.EVT_BUTTON, self.theDBConnector.RunTest)
		box.Add(m_test_button, 0, wx.ALL, 10)
		
		

		panel.SetSizer(box)
		panel.Layout()
		
		thread = Thread(target = self.UpdateInformationThread, args = ())
		thread.start()
		
	def UpdateInformationThread(self):
		while(1):
			self.OnUpdateInformation()
			sleep(2)
	def OnUpdateInformation(self):
		self.num_of_customers_button.SetLabel('Number of customers: '+str(self.theDBConnector.GetNumOfCustomers()))
		self.num_of_tables_button.SetLabel('Number of tables: '+str(self.theDBConnector.GetNumOfTables()))

	def OnAddCustomer(self,event):
		theCustomerAdder = CustomerAdder(self)
		theCustomerAdder.Show()
		
	def OnAddTable(self,event):
		theTableAdder = TableAdder(self)
		theTableAdder.Show()

	def OnClose(self, event):
		self.Destroy()

os.system("export UBUNTU_MENUPROXY=0")
app = wx.App(redirect=False)   # Error messages go to popup window
top = Frame()
top.Show()
app.MainLoop()
