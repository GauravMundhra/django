import time
import pandas as pd 
 
def excel():
	df=pd.read_excel('test.xlsx')
	result=df.Values.values
	result=result.tolist()
	return result

def run():
	time.sleep(3)
	print('helo')

def bar():
	df=pd.read_excel('data.xlsx',sheet_name=0)
	result=[]
	result.append([])
	result.append([])
	result[0]=df['Unnamed: 1'].values.tolist()
	result[1]=df['Unnamed: 2'].values.tolist()
	return result
