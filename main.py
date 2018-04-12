
import requests # learn more: https://python.org/pypi/requests

text ="""Your question goes here?

Option 1
Option 2
Option 3
Option 4
 """
 
arr=text.splitlines(True)

question=arr[0].replace('\n','')

opt1=arr[2].replace('\n','')
opt2=arr[3].replace('\n','')
opt3=arr[4].replace('\n','')
opt4=arr[5].replace('\n','')

dataString="";

#create a query for search engine
req = requests.get('https://www.googleapis.com/customsearch/v1?q='+question+'&cx=<google-customsearch-id>&key=<google-cse-project-key>');
jsonResponse=req.json()
jsonData = jsonResponse["items"]

for item in jsonData:
    dataString += item.get("snippet")
   
print(dataString.lower().count(opt1.lower()))
print(dataString.lower().count(opt2.lower()))
print(dataString.lower().count(opt3.lower()))
print(dataString.lower().count(opt4.lower()))
