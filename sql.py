# attr_dict = {'endeca_instance_id' : '204',
# 			 'attribute_name' :'accounting_date'}

# sql_statement = """
SET DEFINE OFF;

-- define Accounting Date attr and ensure that it is associated with EID Instance ID 9


REM INSERTING into APPS.FND_EID_PDR_ATTRS_B
-- DELETE FROM APPS.FND_EID_PDR_ATTRS_B WHERE EID_INSTANCE_ID = '%s' AND EID_INSTANCE_ATTRIBUTE = 'accounting_date'
Insert into APPS.FND_EID_PDR_ATTRS_B (EID_INSTANCE_ID,EID_INSTANCE_ATTRIBUTE,ENDECA_DATATYPE,EID_ATTR_PROFILE_ID,EID_RELEASE_VERSION,ATTRIBUTE_SOURCE,MANAGED_ATTRIBUTE_FLAG,HIERARCHICAL_MGD_ATTR_FLAG,DIM_ENABLE_REFINEMENTS_FLAG,DIM_SEARCH_HIERARCHICAL_FLAG,REC_SEARCH_HIERARCHICAL_FLAG,MGD_ATTR_EID_RELEASE_VERSION,OBSOLETED_FLAG,OBSOLETED_EID_RELEASE_VERSION,CREATED_BY,CREATION_DATE,LAST_UPDATED_BY,LAST_UPDATE_DATE,LAST_UPDATE_LOGIN,ATTR_ENABLE_UPDATE_FLAG,VIEW_OBJECT_ATTR_NAME,ATTR_VALUE_SET_FLAG,VALUE_SET_NAME,ATTR_ENABLE_NULL_FLAG,DESCRIPTIVE_FLEXFIELD_NAME) values (204,'accounting_date','mdex:string',1,'2.3','MSI','N','N','N','N','N','N','N','0',0,SYSDATE,0,SYSDATE,0,null,null,null,null,null,null);



-- make Accounting Date available across all languages (will still be displayed in English)
SET DEFINE OFF;

REM INSERTING into APPS.FND_EID_PDR_ATTRS_TL

Insert into APPS.FND_EID_PDR_ATTRS_TL (EID_INSTANCE_ID,EID_INSTANCE_ATTRIBUTE,LANGUAGE,SOURCE_LANG,DISPLAY_NAME,ATTRIBUTE_DESC,USER_DISPLAY_NAME,USER_ATTRIBUTE_DESC,CREATED_BY,CREATION_DATE,LAST_UPDATED_BY,LAST_UPDATE_DATE,LAST_UPDATE_LOGIN) values (204,'accounting_date','D','US','Accounting Date','Accounting Date','Accounting Date','Accounting Date',0,SYSDATE,0,SYSDATE,0);
Insert into APPS.FND_EID_PDR_ATTRS_TL (EID_INSTANCE_ID,EID_INSTANCE_ATTRIBUTE,LANGUAGE,SOURCE_LANG,DISPLAY_NAME,ATTRIBUTE_DESC,USER_DISPLAY_NAME,USER_ATTRIBUTE_DESC,CREATED_BY,CREATION_DATE,LAST_UPDATED_BY,LAST_UPDATE_DATE,LAST_UPDATE_LOGIN) values (204,'accounting_date','DK','US','Accounting Date','Accounting Date','Accounting Date','Accounting Date',0,SYSDATE,0,SYSDATE,0);
Insert into APPS.FND_EID_PDR_ATTRS_TL (EID_INSTANCE_ID,EID_INSTANCE_ATTRIBUTE,LANGUAGE,SOURCE_LANG,DISPLAY_NAME,ATTRIBUTE_DESC,USER_DISPLAY_NAME,USER_ATTRIBUTE_DESC,CREATED_BY,CREATION_DATE,LAST_UPDATED_BY,LAST_UPDATE_DATE,LAST_UPDATE_LOGIN) values (204,'accounting_date','E','US','Accounting Date','Accounting Date','Accounting Date','Accounting Date',0,SYSDATE,0,SYSDATE,0);
Insert into APPS.FND_EID_PDR_ATTRS_TL (EID_INSTANCE_ID,EID_INSTANCE_ATTRIBUTE,LANGUAGE,SOURCE_LANG,DISPLAY_NAME,ATTRIBUTE_DESC,USER_DISPLAY_NAME,USER_ATTRIBUTE_DESC,CREATED_BY,CREATION_DATE,LAST_UPDATED_BY,LAST_UPDATE_DATE,LAST_UPDATE_LOGIN) values (204,'accounting_date','F','US','Accounting Date','Accounting Date','Accounting Date','Accounting Date',0,SYSDATE,0,SYSDATE,0);
Insert into APPS.FND_EID_PDR_ATTRS_TL (EID_INSTANCE_ID,EID_INSTANCE_ATTRIBUTE,LANGUAGE,SOURCE_LANG,DISPLAY_NAME,ATTRIBUTE_DESC,USER_DISPLAY_NAME,USER_ATTRIBUTE_DESC,CREATED_BY,CREATION_DATE,LAST_UPDATED_BY,LAST_UPDATE_DATE,LAST_UPDATE_LOGIN) values (204,'accounting_date','NL','US','Accounting Date','Accounting Date','Accounting Date','Accounting Date',0,SYSDATE,0,SYSDATE,0);
Insert into APPS.FND_EID_PDR_ATTRS_TL (EID_INSTANCE_ID,EID_INSTANCE_ATTRIBUTE,LANGUAGE,SOURCE_LANG,DISPLAY_NAME,ATTRIBUTE_DESC,USER_DISPLAY_NAME,USER_ATTRIBUTE_DESC,CREATED_BY,CREATION_DATE,LAST_UPDATED_BY,LAST_UPDATE_DATE,LAST_UPDATE_LOGIN) values (204,'accounting_date','PT','US','Accounting Date','Accounting Date','Accounting Date','Accounting Date',0,SYSDATE,0,SYSDATE,0);
Insert into APPS.FND_EID_PDR_ATTRS_TL (EID_INSTANCE_ID,EID_INSTANCE_ATTRIBUTE,LANGUAGE,SOURCE_LANG,DISPLAY_NAME,ATTRIBUTE_DESC,USER_DISPLAY_NAME,USER_ATTRIBUTE_DESC,CREATED_BY,CREATION_DATE,LAST_UPDATED_BY,LAST_UPDATE_DATE,LAST_UPDATE_LOGIN) values (204,'accounting_date','PTB','US','Accounting Date','Accounting Date','Accounting Date','Accounting Date',0,SYSDATE,0,SYSDATE,0);
Insert into APPS.FND_EID_PDR_ATTRS_TL (EID_INSTANCE_ID,EID_INSTANCE_ATTRIBUTE,LANGUAGE,SOURCE_LANG,DISPLAY_NAME,ATTRIBUTE_DESC,USER_DISPLAY_NAME,USER_ATTRIBUTE_DESC,CREATED_BY,CREATION_DATE,LAST_UPDATED_BY,LAST_UPDATE_DATE,LAST_UPDATE_LOGIN) values (204,'accounting_date','S','US','Accounting Date','Accounting Date','Accounting Date','Accounting Date',0,SYSDATE,0,SYSDATE,0);
Insert into APPS.FND_EID_PDR_ATTRS_TL (EID_INSTANCE_ID,EID_INSTANCE_ATTRIBUTE,LANGUAGE,SOURCE_LANG,DISPLAY_NAME,ATTRIBUTE_DESC,USER_DISPLAY_NAME,USER_ATTRIBUTE_DESC,CREATED_BY,CREATION_DATE,LAST_UPDATED_BY,LAST_UPDATE_DATE,LAST_UPDATE_LOGIN) values (204,'accounting_date','US','US','Accounting Date','Accounting Date','Accounting Date','Accounting Date',0,SYSDATE,0,SYSDATE,0);
Insert into APPS.FND_EID_PDR_ATTRS_TL (EID_INSTANCE_ID,EID_INSTANCE_ATTRIBUTE,LANGUAGE,SOURCE_LANG,DISPLAY_NAME,ATTRIBUTE_DESC,USER_DISPLAY_NAME,USER_ATTRIBUTE_DESC,CREATED_BY,CREATION_DATE,LAST_UPDATED_BY,LAST_UPDATE_DATE,LAST_UPDATE_LOGIN) values (204,'accounting_date','ZHS','US','Accounting Date','Accounting Date','Accounting Date','Accounting Date',0,SYSDATE,0,SYSDATE,0);




-- add Accounting Date to the existing group, Categories. 
SET DEFINE OFF;

REM INSERTING into APPS.FND_EID_ATTR_GROUPS
SET DEFINE OFF;
Insert into APPS.FND_EID_ATTR_GROUPS (EID_INSTANCE_ID,EID_INSTANCE_GROUP,EID_INSTANCE_ATTRIBUTE,EID_INSTANCE_GROUP_ATTR_SEQ,EID_INST_GROUP_ATTR_USER_SEQ,GROUP_ATTRIBUTE_SOURCE,EID_RELEASE_VERSION,OBSOLETED_FLAG,OBSOLETED_EID_RELEASE_VERSION,CREATED_BY,CREATION_DATE,LAST_UPDATED_BY,LAST_UPDATE_DATE,LAST_UPDATE_LOGIN) values (204,'Categories','accounting_date',1,1,'MSI','2.3','N','0',0,SYSDATE,0,SYSDATE,0);


COMMIT;
"""
group_update_statment = """
SET DEFINE OFF;

UPDATE APPS.FND_EID_ATTR_GROUPS
SET EID_INSTANCE_GROUP_ATTR_SEQ = 1, EID_INST_GROUP_ATTR_USER_SEQ = 1
WHERE EID_INSTANCE_ID = {0} AND EID_INSTANCE_ATTRIBUTE = {1};

COMMIT;
""".format(attr_dict['endeca_instance_id'], attr_dict['attribute_name'])

print group_update_statment