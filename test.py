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