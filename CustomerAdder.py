import wxversion
wxversion.select("2.8")
import wx
import sys

class CustomerAdder(wx.Frame):
	def __init__(self,parent):
		wx.Frame.__init__(self, None, title="New Customer", pos=(150,150), size=(350,400))
		self.parent = parent

		self.panel = wx.Panel(self)
		self.Bind(wx.EVT_CLOSE, self.OnClose)
		self.InputVariables = list()

		box = wx.BoxSizer(wx.VERTICAL)


		m_text = wx.StaticText(self.panel, -1, "Add new customer")
		m_text.SetFont(wx.Font(14, wx.SWISS, wx.NORMAL, wx.BOLD))
		m_text.SetSize(m_text.GetBestSize())
		box.Add(m_text, 0, wx.ALL, 10)


		box.Add(self.GetNewInputField("first name",0), 0, wx.ALL, 0)
		box.Add(self.GetNewInputField("middle name",1), 0, wx.ALL, 0)
		box.Add(self.GetNewInputField("last name",2), 0, wx.ALL, 0)
		box.Add(self.GetNewInputField("e-mail",3), 0, wx.ALL, 0)
		box.Add(self.GetNewInputField("phone",4), 0, wx.ALL, 0)
		box.Add(self.GetNewInputField("address",5), 0, wx.ALL, 0)
		
		m_add_customer_button = wx.Button(self.panel, wx.ID_ANY, "Add customer")
		m_add_customer_button.Bind(wx.EVT_BUTTON, self.OnAddCustomer)
		box.Add(m_add_customer_button, 0, wx.ALL, 10)
		
		self.panel.SetSizer(box)
		self.panel.Layout()
	def ReadInputFieldsAndGetResult(self):
		read_data = list()
		for i in self.InputVariables:
			read_data.append("\""+i.GetValue()+"\"")
		return read_data
			
	def OnAddCustomer(self,event):
		self.parent.theDBConnector.AddCustomer(self.ReadInputFieldsAndGetResult())
		self.OnClose(None)
	def GetNewInputField(self,label,index):
		FirstNamebox = wx.BoxSizer(wx.HORIZONTAL)
		m_text = wx.StaticText(self.panel, -1, label)
		m_text.SetFont(wx.Font(10, wx.SWISS, wx.NORMAL, wx.BOLD))
		m_text.SetSize(m_text.GetBestSize())
		FirstNamebox.Add(m_text, 0, wx.ALL, 10)
		self.InputVariables.append(wx.TextCtrl(self.panel, -1, size=(140,-1)))
		self.InputVariables[index].SetValue('')
		FirstNamebox.Add(self.InputVariables[index], 0, wx.ALL, 5)
		return FirstNamebox
	
	def OnClose(self, event):
		self.Destroy()
