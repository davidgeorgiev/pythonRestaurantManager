import wxversion
wxversion.select("2.8")
import wx
import sys
from TableImageWindow import TableImageWindow

class TableAdder(wx.Frame):
	def __init__(self,parent):
		wx.Frame.__init__(self, None, title="New Table", pos=(150,150), size=(350,200))
		self.parent = parent
		self.theTableImageWindow = TableImageWindow(self)

		self.panel = wx.Panel(self)
		self.Bind(wx.EVT_CLOSE, self.OnClose)
		self.InputChoices = list()
		
		box = wx.BoxSizer(wx.VERTICAL)

		m_text = wx.StaticText(self.panel, -1, "Add new table")
		m_text.SetFont(wx.Font(14, wx.SWISS, wx.NORMAL, wx.BOLD))
		m_text.SetSize(m_text.GetBestSize())
		box.Add(m_text, 0, wx.ALL, 10)

		self.lists = list()
		self.lists.append(self.GetListOfChoicesForNumberOfTables(9))
		box.Add(self.GetNewChoiceField("number of chairs",0,self.lists[0]), 0, wx.ALL, 0)
		self.lists.append(["no","yes"])
		box.Add(self.GetNewChoiceField("smoking",1,self.lists[1]), 0, wx.ALL, 0)
		
		m_add_customer_button = wx.Button(self.panel, wx.ID_ANY, "Add table")
		m_add_customer_button.Bind(wx.EVT_BUTTON, self.OnAddTable)
		box.Add(m_add_customer_button, 0, wx.ALL, 10)
		
		
		
		self.panel.SetSizer(box)
		self.panel.Layout()
		self.theTableImageWindow.Show()
	def GetListOfChoicesForNumberOfTables(self,max_chairs):
		return_list = list()
		for i in range(1,max_chairs):
			return_list.append(str(i))
		return return_list
	def ReadCoiceFieldsAndGetResult(self):
		read_data = list()
		k = 0
		for i in self.InputChoices:
			read_data.append("\""+self.lists[k][i.GetSelection()]+"\"")
			k += 1
		return read_data
			
	def OnAddTable(self,event):
		self.parent.theDBConnector.AddTable(self.ReadCoiceFieldsAndGetResult())
		self.OnClose(None)
	def GetNewChoiceField(self,label,index,list_of_choices):
		FirstNamebox = wx.BoxSizer(wx.HORIZONTAL)
		m_text = wx.StaticText(self.panel, -1, label)
		m_text.SetFont(wx.Font(10, wx.SWISS, wx.NORMAL, wx.BOLD))
		m_text.SetSize(m_text.GetBestSize())
		FirstNamebox.Add(m_text, 0, wx.ALL, 10)
		myChoice = wx.Choice(self.panel,choices = list_of_choices)
		self.InputChoices.append(myChoice)
		myChoice.Bind(wx.EVT_CHOICE, lambda evt : self.theTableImageWindow.UpdateImageBox(evt,0))
		FirstNamebox.Add(self.InputChoices[index], 0, wx.ALL, 5)
		return FirstNamebox
	
	def OnClose(self, event):
		self.theTableImageWindow.Destroy()
		self.Destroy()
