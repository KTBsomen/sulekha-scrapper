
#before running this script run the commented javascript code in your browser after selecting any catagory page on sulekha.com 

'''
var links=new Set();
var start;
function findlink(){

lists=document.getElementsByTagName("a")
for(let i=0;i<lists.length;i++){
let l=lists[i].href
if(l.endsWith("contact-address")){links.add(l)}

}
}

console.log(links)

function start(){
document.getElementById("btnviewmorebiz").onclick=()=>findlink()
start=setInterval(()=>{document.getElementById("btnviewmorebiz").click()},5000)
}
function stop(){
clearInterval(start)
}
function save(){
var pom = document.createElement('a');
var blob = new Blob([...links],{type: 'text/csv;charset=utf-8;'});
var url = URL.createObjectURL(blob);
pom.href = url;
pom.setAttribute('download', 'sulekha-links.csv');
pom.click();

}
'''

import requests
import bs4
import csv
link_list=set(open("sulekha-links.csv","r").read().split(","))
def getData(url):
	data=[]
	try:
		s=bs4.BeautifulSoup(requests.get(url).content,"html.parser")
		title=s.find('h1', attrs = {'class':'title-primary'}).text
		table = s.find('section', attrs = {'id':'socialMediaSection'})
		rows=table.find_all('a', attrs = {'class':'has-action'})
		data.append(title)
	
		for i in rows:
			link=i["href"]
			if(link.startswith("mailto")):
				data.append(link.replace("mailto:",""))
			else:data.append(link)
	except:pass
	return data

rows = []
wri=1
try:
	for url in link_list:
		rows.append(getData(url))
		print(f"[ {wri} ] files are fetched..",end="\r")
		wri+=1 
		

	# field names
	fields = ['Name', 'Email', 'website']

	filename = "sulekha_email_and_website_details.csv"
	
	# writing to csv file
	with open(filename, 'w') as csvfile:
	# creating a csv writer object
		csvwriter = csv.writer(csvfile)
		
	# writing the fields
		csvwriter.writerow(fields)
		
	# writing the data rows
		csvwriter.writerows(rows)
	
	print("writing successful.............\nthnks for usin sulekha scraper ")	
		
except KeyboardInterrupt:
		

	# field names
	fields = ['Name', 'Email', 'website']

	filename = "sulekha_email_and_website_details.csv"
	
	# writing to csv file
	with open(filename, 'w') as csvfile:
	# creating a csv writer object
		csvwriter = csv.writer(csvfile)
		
	# writing the fields
		csvwriter.writerow(fields)
		
	# writing the data rows
		csvwriter.writerows(rows)
	
	print("writing successful.............\nthnks for usin sulekha scraper ")	


