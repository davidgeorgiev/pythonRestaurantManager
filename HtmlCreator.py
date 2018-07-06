
class HtmlCreator():
	def __init__(self,parent):
		self.parent = parent
	def CreateTablesHtml(self,TablesDataList):
		with open('current.html', 'w') as the_file:
			the_file.write('<!DOCTYPE html><html><body>')
			k = 0
			for i in TablesDataList:
				k += 1
				filename = str(i[1])+".png"
				if(i[2] == "yes"):
					folder = "Tables/4/"
				else:
					folder = "Tables/5/"
				the_file.write('<div style="float: left;">'+str(i[0])+'<img src="'+folder+filename+'" width="130" height="80"></div>')
				if(k%4==0):
					the_file.write("<br>")
			the_file.write('</body></html>')
