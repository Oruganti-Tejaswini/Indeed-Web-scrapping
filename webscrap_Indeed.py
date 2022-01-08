
# pip install Beautifulsoup4
# pip install requests

from bs4 import BeautifulSoup
import requests

def html_data(URL):
    data =requests.get(URL).text
    return BeautifulSoup(data ,'html.parser')

def job_data(soup):
    job_data_list =[]
    company_data_list=[]
    td =soup.find_all('td' ,class_='resultContent')
    for i in td:
        h2 =i.find("h2" ,class_=['jobTitle jobTitle-color-purple','jobTitle jobTitle-color-purple jobTitle-newJob']).get_text()
        job_data_list.append(h2.replace("new",""))
        a = (i.find(["a", "span"], class_=[ "companyName"]).get_text())
        company_data_list.append(a)

    final_result = list(zip(job_data_list, company_data_list))
    return final_result



Job_Description='software%20developer'
Location='Buffalo%2C%20NY'
URL='https://www.indeed.com/jobs?q='+Job_Description+'&l='+Location
print(URL)

soup=html_data(URL)

final_result=job_data(soup)
for i in final_result:
    print(i)




