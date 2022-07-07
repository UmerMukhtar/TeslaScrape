
from urllib import response
from fileinput import close
import requests
import pandas as pd

url= ('https://www.govcagecodes.com/?code=&company=TESLA#results')
try:
    # Checking URL/website status for Error 
    response = requests.get(url,timeout=15)                                 
    response.raise_for_status()
except requests.exceptions.HTTPError as errh:
    print ("Error:",errh)

    #getting table data
df_table=pd.read_html(response.text)

df= df_table[-1]

print(df)
    #file in json and excel
df.to_csv('result.csv')
df.to_json('result.json')
