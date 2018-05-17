import requests
from bs4 import BeautifulSoup
import re
r = requests.get("https://www.ebay.com/sch/i.html?_from=R40&_trksid=p2499334.m570.l1313.TR12.TRC2.A0.H0.Xiphone+x+unlocked.TRS0&_nkw=iphone+x+unlocked&_sacat=9355")
soup=BeautifulSoup(r.content,'html.parser')
source_code=soup.findAll("ul",{"id":"ListViewInner"})



for links in source_code:
    title_code=links.find_all("a",{"class":"vip"})
    price_code=links.find_all("span",{"class":"bold"})
title_list=[]
for lists in title_code:
    title_list.append(lists.text.strip('\r\n\t').encode('ascii','ignore'))
price_list=[]
for list in price_code:
    price_list.append(list.text.strip('\t\n').encode('ascii','ignore'))
final_list=map(None,title_list,price_list)
for item in final_list:

    print item

filename="ebayiphonex.csv"
file=open(filename,"w")
headers="phone model,price\n"
file.write(headers)
for final in final_list:
    file.write("{},{}\n".format( final[0],re.sub(',','',final[1])))

file.close()

#print title_list
#print price_list


#print len(source_code)
#print len(title_code)
#print len(price_code)

nextpage=soup.find_all("a",{"class":"gspr next"})
#print len(nextpage)
nexpagelink=nextpage[0].get("href")
#print nexpagelink