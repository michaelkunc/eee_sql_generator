import openpyxl


class SQL(object):
    DEFINE_OFF = 'SET DEFINE OFF;\n'
    COMMIT = 'COMMIT;'
#need to add an attribute source as a parameter

    def __init__(self, eid_instance_id, eid_instance_attribute, datatype, profile_id, display_name):
		self.eid_instance_id = str(eid_instance_id)
		profile_id = str(profile_id)
		self.insert_attrs_b = self.insert_attrs_b(self.eid_instance_id, eid_instance_attribute, datatype, profile_id)
		self.insert_attrs_tl_all = self.insert_attrs_tl_all(self.eid_instance_id, eid_instance_attribute, display_name)
		self.insert_attr_groups = self.insert_attr_groups(self.eid_instance_id, eid_instance_attribute)
		self.update_attr_groups = self.update_attr_groups(self.eid_instance_id, eid_instance_attribute)

    def insert_attrs_b(self, eid_instance_id, eid_instance_attribute, datatype, profile_id):
    	rem_insert_statement = 'REM INSERTING into APPS.FND_EID_PDR_ATTRS_B\n'
    	insert_statement = 'Insert into APPS.FND_EID_PDR_ATTRS_B (EID_INSTANCE_ID,EID_INSTANCE_ATTRIBUTE,ENDECA_DATATYPE, EID_ATTR_PROFILE_ID,EID_RELEASE_VERSION,ATTRIBUTE_SOURCE,MANAGED_ATTRIBUTE_FLAG,HIERARCHICAL_MGD_ATTR_FLAG, DIM_ENABLE_REFINEMENTS_FLAG,DIM_SEARCH_HIERARCHICAL_FLAG,REC_SEARCH_HIERARCHICAL_FLAG, MGD_ATTR_EID_RELEASE_VERSION,OBSOLETED_FLAG,OBSOLETED_EID_RELEASE_VERSION,CREATED_BY,CREATION_DATE, LAST_UPDATED_BY,LAST_UPDATE_DATE,LAST_UPDATE_LOGIN,ATTR_ENABLE_UPDATE_FLAG,VIEW_OBJECT_ATTR_NAME,ATTR_VALUE_SET_FLAG, VALUE_SET_NAME,ATTR_ENABLE_NULL_FLAG,DESCRIPTIVE_FLEXFIELD_NAME)\n values'
    	values =  "("+ eid_instance_id +",'" + eid_instance_attribute + "','" + datatype + "'," + profile_id + ",'2.3','MSI','N','N','N','N','N','N','N','0',0,SYSDATE,0,SYSDATE,0,null,null,null,null,null,null);\n"
    	statement = SQL.DEFINE_OFF + rem_insert_statement + insert_statement + values + SQL.COMMIT
    	return statement


    def insert_attrs_tl(self, eid_instance_id ,eid_instance_attribute, language_code, display_name):
    	insert_statement = 'Insert into APPS.FND_EID_PDR_ATTRS_TL (EID_INSTANCE_ID,EID_INSTANCE_ATTRIBUTE,LANGUAGE,SOURCE_LANG,DISPLAY_NAME,ATTRIBUTE_DESC,USER_DISPLAY_NAME,USER_ATTRIBUTE_DESC,CREATED_BY,CREATION_DATE,LAST_UPDATED_BY,LAST_UPDATE_DATE,LAST_UPDATE_LOGIN) values'
    	values = "(" + eid_instance_id + ",'"+eid_instance_attribute+"','" + language_code + "','US','" + display_name + "','" + display_name +"','" + display_name + "','" + display_name + "',0,SYSDATE,0,SYSDATE,0);" 
    	statement = insert_statement + values 
    	return statement

#this method could use some TLC.
    def insert_attrs_tl_all(self, eid_instance_id, eid_instance_attribute, display_name):
    	ebs_language_codes = ('D', 'DK', 'E', 'F', 'NL', 'PT', 'PTB', 'S', 'US', 'ZHS')
        rem_insert_statement = 'REM INSERTING into APPS.FND_EID_PDR_ATTRS_TL\n'
        statement = SQL.DEFINE_OFF + rem_insert_statement
        for l in ebs_language_codes:
        	language_statement = self.insert_attrs_tl(eid_instance_id, eid_instance_attribute, l, display_name)
        	statement += language_statement + '\n'
        return statement + '\n' + SQL.COMMIT 


    def insert_attr_groups(self, eid_instance_id, eid_instance_attribute):
    	rem_insert_statement = 'REM INSERTING into APPS.FND_EID_ATTR_GROUPS\n'
    	insert_statement = 'Insert into APPS.FND_EID_ATTR_GROUPS (EID_INSTANCE_ID,EID_INSTANCE_GROUP,EID_INSTANCE_ATTRIBUTE,EID_INSTANCE_GROUP_ATTR_SEQ,EID_INST_GROUP_ATTR_USER_SEQ,GROUP_ATTRIBUTE_SOURCE,EID_RELEASE_VERSION,OBSOLETED_FLAG,OBSOLETED_EID_RELEASE_VERSION,CREATED_BY,CREATION_DATE,LAST_UPDATED_BY,LAST_UPDATE_DATE,LAST_UPDATE_LOGIN) values '
    	values = "("+ eid_instance_id + ",'Categories','" +eid_instance_attribute + "',1,1,'MSI','2.3','N','0',0,SYSDATE,0,SYSDATE,0);"
    	statement = SQL.DEFINE_OFF + rem_insert_statement + insert_statement + values + SQL.COMMIT
    	return statement

    def update_attr_groups(self, eid_instance_id, eid_instance_attribute):
    	update = "UPDATE APPS.FND_EID_ATTR_GROUPS "
    	set_statement = "SET EID_INSTANCE_GROUP_ATTR_SEQ = 1, EID_INST_GROUP_ATTR_USER_SEQ = 1 WHERE EID_INSTANCE_ID = "+eid_instance_id+" AND EID_INSTANCE_ATTRIBUTE = '"+ eid_instance_attribute +"'; \n"
    	statement = SQL.DEFINE_OFF + update +  set_statement + SQL.COMMIT + '\n'
    	return statement

    def save_sql(self):
    	text = self.insert_attrs_b + '\n'+ self.insert_attrs_tl_all + '\n' + self.insert_attr_groups + '\n' + self.update_attr_groups
    	with open('attribute_sql.txt', 'a') as f:
    		f.write(text)


class Excel_Reader(object):

    def __init__(self):
        wb = openpyxl.load_workbook('endeca_attributes.xlsx')
        sheet = wb.get_sheet_by_name('endeca_attributes')
        highest_row = str(sheet.get_highest_row())
        self.attribute_data = []
        for rowOfCellObjects in sheet['A2': 'E'+ highest_row]:
            cell_data = [c.value for c in rowOfCellObjects]
            self.attribute_data.append(cell_data)

#not crazy about this at all. The idea is to clear the file prior to appending the sql statements
#totally a stopgap at the moment
    def clear_attribute_sql_file(self):
        open('attribute_sql.txt', 'w').close()


reader = Excel_Reader()

reader.clear_attribute_sql_file()


for r in reader.attribute_data:
    sql = SQL(*r)
    sql.save_sql()