import wxversion
wxversion.select("2.8")
import wx
import sys

class CustomerManager(wx.Frame):
    def __init__(self,parent):
		wx.Frame.__init__(self, None, title="Manage Customers", pos=(150,150), size=(350,400))
		self.parent = parent

		panel = wx.Panel(self)
		self.Bind(wx.EVT_CLOSE, self.OnClose)
		
		box = wx.BoxSizer(wx.VERTICAL)

		m_text = wx.StaticText(panel, -1, "Customers!")
		m_text.SetFont(wx.Font(14, wx.SWISS, wx.NORMAL, wx.BOLD))
		m_text.SetSize(m_text.GetBestSize())
		box.Add(m_text, 0, wx.ALL, 10)

		

		panel.SetSizer(box)
		panel.Layout()

    def OnClose(self, event):
        self.Destroy()
