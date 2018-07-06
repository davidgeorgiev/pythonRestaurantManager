import wx.html
class HtmlViewer(wx.Frame):
    def __init__(self, parent):
        wx.Frame.__init__(self, parent, -1, "Html page", pos=(500,150), size=(650,400))
        html = wx.html.HtmlWindow(self)
        if "gtk2" in wx.PlatformInfo:
            html.SetStandardFonts()

        wx.CallAfter(html.LoadPage, "current.html")
	def OnClose(self, event):
		self.Destroy()
