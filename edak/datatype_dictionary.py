ORACLE_COLUMNS_TO_ENDECA = {'FULFILLMENT_DATE':'mdex:dateTime', 'GL_DATE' : 'mdex:dateTime',
				'SHIP_QUANTITY': 'mdex:int', 'UNIT_PRICE':'mdex:double', 'ORDERED_QUANTITY':'mdex:int',
				 'PROMISE_DATE': 'mdex:dateTime', 'SCHEDULE_SHIP_DATE' :'mdex:dateTime', 'REQUEST_DATE':'mdex:dateTime',
				 'SHIPPED_QUANTITY' : 'mdex:int', 'ACTUAL_SHIPMENT_DATE':'mdex:dateTime',
				 'ACTUAL_ARRIVAL_DATE' : 'mdex:dateTime', 'ULTIMATE_DROPOFF_DATE': 'mdex:dateTime', 'PROMISED_DATE':'mdex:dateTime',
				 'LEAD_TIME':'mdex:int', 'POSTPROCESSING_LEAD_TIME' : 'mdex:int', 'FULL_LEAD_TIME' : 'mdex:int', 
				 'PREPROCESSING_LEAD_TIME' : 'mdex:int', 'DELIVERY_LEAD_TIME':'mdex:int', 'SCHEDULE_ARRIVAL_DATE' : 'mdex:dateTime',
				 'TOTAL_UNSHIPPED_QTY' : 'mdex:int', 'CONVERSION_RATE' : 'mdex:double', 'BOOKED_DATE' : 'mdex:dateTime',
				 'OFFER_START_DATE' :'mdex:dateTime', 'OFFER_END_DATE': 'mdex:dateTime', 'ULTILIZED_AMOUNT' : 'mdex:double',
				 'COMMITTED_AMOUNT' : 'mdex:double','EARNED_AMOUNT' : 'mdex:double', 'UOM_CONVERSION_FACTOR' : 'mdex:double',
				 'INPUT_COST_FUNCTIONAL' : 'mdex:double', 'ITEM_COST' : 'mdex:double', 'CURRENCY_CONVERSION':'mdex:double',
				 'INPUT_COST_USD' :'mdex:double', 'TOTAL_COST_USD':'mdex:double', 'INPUT_COST_USD_PER_EA' : 'mdex:double',
				 'GLOBAL_COST_USD':'mdex:double', 'GLOBAL_COST_USD_PER_EA':'mdex:double', 'FINAL_COST_FUNCTIONAL':'mdex:double',
				 'FINAL_COST_USD': 'mdex:double', 'FINAL_COST_USD_PER_EA': 'mdex:double', 'ENTERED_DR':'mdex:double',
				 'ENTERED_CR':'mdex:double', 'NET_ENTERED_AMT':'mdex:double','ACCOUNTED_DR':'mdex:double', 'ACCOUNTED_CR':'mdex:double',
				 'NET_ACCTD_AMT':'mdex:double','ITEM_DATE':'mdex:dateTime', 'ACCOUNTING_DATE': 'mdex:dateTime', 'CURRENCY_CONVERSION_RATE':'mdex:double',
				 'RECEIPT_DATE': 'mdex:dateTime','ENTERED_PO_UNIT_PRICE':'mdex:double', 'RECEIPT_QUANTITY':'mdex:int','ENTERED_PO_EXT':'mdex:double',
				 'RECEIPT_AMOUNT':'mdex:int','FUNC_PO_EXTENSION':'mdex:double', 'FUNC_PO_UNIT_PRICE':'mdex:double',
				 'FUNC_STD_COST':'mdex:double', 'FUNC_STD_COST_EXTENSION':'mdex:double','FUNC_PURCHASE_VARIANCE':'mdex:double',
				 'PURCHASE_VARIANCE':'mdex:double', 'PROJECT_START_DATE':'mdex:dateTime', 'PROJECT_CLOSED_DATE':'mdex:dateTime',
				 'PROJECT_COMPLETETION_DATE':'mdex:dateTime', 'RAW_COST_PER_ITEM':'mdex:double','EXPENDITURE_ITD':'mdex:double',
				 'EXPENDITURE_PTD':'mdex:double','EXPENDITURE_YTD':'mdex:double', 'BUDGET_COST':'mdex:double',
				 'QUANTITY':'mdex:int', 'RAW_COST_RATE':'mdex:double', 'COST':'mdex:double', 'COST_IN_USD':'mdex:double',
				 'AP_INVOICE_AMOUNT':'mdex:double','COST_MARKUP_USD':'mdex:double', 'COST_MARKUP':'mdex:double',
				 'MARKUP':'mdex:double','MARKUP_USD':'mdex:double', 'AP_INVOICE_POSTED_DATE':'mdex:dateTime',
				 'ORDER_BRIDGED_DATE':'mdex:dateTime','REVENUE_VALUE' :'mdex:double','SHIPPED_REVENUE':'mdex:double','FORECAST_EQP_COST':'mdex:double',
				 'SHIPPED_FCST_EQP_COST':'mdex:double', 'EQP_ETC':'mdex:double','CONVERSION_COST_PERCENT':'mdex:double', 'CURRENT_SHIPPED_QUANTITY':'mdex:int',
				 'UNIT_DM_COST':'mdex:double','UNIT_LIST_PRICE':'mdex:double','UNIT_SELLING_PRICE':'mdex:double','UNIT_DM_COST_1':'mdex:double','TOTAL_PROJECT_CURRENCY_DM_COST':'mdex:double',
				 'ORIGINAL_BOOKED_DATE':'mdex:dateTime','ORDER_LAST_UPDATE_DATE':'mdex:dateTime','RELEASED_AMOUNT':'mdex:double','LAST_UPDATE_DATE':'mdex:dateTime',
				 'TOTAL_SHIPPED_FCST_EQP_COST':'mdex:double','EQP_ETC_PROJ_CURR':'mdex:double','SHIPPED_QUANTITY': 'mdex:int','UNIT_PROJECT_CURR_DM_COST':'mdex:double',
				 'SHIPPED_DATE':'mdex:dateTime','INVOICE_AMOUNT':'mdex:double', 'COUNT_OF_TICKETS':'mdex:int','TOTAL_INVOICE_AMOUNT':'mdex:double','REPAIR_COST':'mdex:double',
				 'TOTAL_REPAIR_COSTS':'mdex:double', 'SO_PROMISE_DATE':'mdex:dateTime', 'DAYS_LEFT_LATE':'mdex:int', 'LAST_SHIP_DATE':'mdex:dateTime', 'INCIDENT_DATE':'mdex:dateTime',
				 'OPEN_DATE':'mdex:dateTime', 'PART_AVAILABILITY_DATE':'mdex:dateTime', 'DAYS_SINCE_QUOTE':'mdex:int', 'INITIAL_PROMISE_DATE':'mdex:dateTime'}

ENDECA_TO_XML = {'mdex:double': 'number', 'mdex:string': 'string', 'mdex:boolean': 'boolean',
                            'mdex:dateTime': 'date', 'mdex:int': 'integer',
                            'mdex:long': 'long'}