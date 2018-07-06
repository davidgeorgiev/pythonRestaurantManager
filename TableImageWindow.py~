import wxversion
wxversion.select("2.8")
import wx
import sys

class TableImageWindow(wx.Frame):
	def __init__(self,parent):
		wx.Frame.__init__(self, None, title="Table Image", pos=(150,350), size=(350,200))
		self.parent = parent

		self.panel = wx.Panel(self)
		self.Bind(wx.EVT_CLOSE, self.OnClose)
		self.InputChoices = list()
		
		self.box = wx.BoxSizer(wx.HORIZONTAL)

		
		self.UpdateImageBox(None,1)
		self.ImageBox = wx.BoxSizer(wx.VERTICAL)
		self.ImageBox.Add(self.myPngBmp, 0, wx.ALL, 0)
		
		self.box.Add(self.ImageBox, 0, wx.ALL, 35)
		
		
		
		self.panel.SetSizer(self.box)
		self.panel.Layout()
	def UpdateImageBox(self,event,val):
		if(val == 1):
			address = "Tables/3/1.png"
		else:
			num_of_chairs = self.parent.ReadCoiceFieldsAndGetResult()
			address = "Tables/3/"+str(num_of_chairs[0])[1]+".png"
		
		self.myPng = wx.Image(address, wx.BITMAP_TYPE_PNG)
		self.myPngBmp = wx.StaticBitmap(self, 0, wx.BitmapFromImage(self.myPng), (35, 35), (self.myPng.GetWidth(), self.myPng.GetHeight()))
	def OnClose(self, event):
		self.parent.Destroy()
		self.Destroy()
		

