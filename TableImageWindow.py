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
		
		box = wx.BoxSizer(wx.HORIZONTAL)

		box.Add(self.CreateImageBox(), 0, wx.ALL, 10)
		
		
		
		self.panel.SetSizer(box)
		self.panel.Layout()
	def CreateImageBox(self):
		ImageBox = wx.BoxSizer(wx.VERTICAL)
		myPng = wx.Image("img1.png", wx.BITMAP_TYPE_PNG)
		myPng = wx.StaticBitmap(self, 0, wx.BitmapFromImage(myPng), (1, 1), (myPng.GetWidth(), myPng.GetHeight()))
		ImageBox.Add(myPng, 0, wx.ALL, 0)
		return ImageBox	
	def OnClose(self, event):
		self.parent.Destroy()
		self.Destroy()
		

