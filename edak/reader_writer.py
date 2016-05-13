import openpyxl

class Excel_Reader(object):

	def __init__(self):
		wb = openpyxl.load_workbook('endeca_attributes.xlsx')
		sheet = wb.get_sheet_by_name('endeca_attributes')
		highest_row = str(sheet.get_highest_row())
		self.attribute_data = [[c.value for c in rowOfCellObjects] for rowOfCellObjects in sheet['A2':'E'+highest_row]]
# this puts the quick and dirty into quick and dirty
		self.attribute_names = []
		for col in sheet.columns[1]:
			self.attribute_names.append(col.value)
# 		del self.attribute_names[0]

class Text_Writer(object):

	def __init__(self, file):
		self.file = file


	def clear_file(self):
		open(self.file, 'w').close()


	def save_text(self, text):
		with open(self.file, 'a') as f:
			f.write(text)
