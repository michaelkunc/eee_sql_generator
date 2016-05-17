import sys
import reader_writer
import sql_generator
import eql_generator
import xml_generator


def main(args=None):
	# print 'writing some sweet PLSQL for you........'
	# reader = reader_writer.Excel_Reader()
	# sql_writer = reader_writer.Text_Writer('sql.txt')
	# sql_writer.clear_file()
	# for r in reader.attribute_data:
	# 	sql = sql_generator.SQL(*r)
	# 	sql_writer.save_text(sql.file)

	# print 'beep, boop your PLSQL is ready!'
	# print '------------------------------------------------------'
	# print 'now writing some EQL for you..................................'
	# eql_writer = reader_writer.Text_Writer('eql.txt') 
	# eql = eql_generator.EQL(reader.attribute_names)
	# eql_writer.clear_file()
	# eql_writer.save_text(eql.generate_EQL())
	# print 'beep, boop your EQL is ready too!'

	print '------------------------------------------------------------'
	print 'now writing your XML file...........'
	xml_writer = reader_writer.Text_Writer('xml.txt')
	xml_writer.clear_file()
	xml = xml_generator.XML({'test' : 'dict'}, 'receiving')
	xml_writer.save_text(xml.file)
	print 'beep, boop your XML is ready as well!'



if __name__ == '__main__':
	main()
