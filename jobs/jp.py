# jp.py
 
import requests
from bs4 import BeautifulSoup
 
#job = input('Enter job Tilte:')
#location = input('Enter Location:')
 
#print(job)
 
 
 
#url = 'https://www.indeed.co.in/jobs?q=python+developer&amp;l=Bengaluru&amp;sort=date'
 
#url ='https://www.indeed.co.in/jobs?q='+job+'&amp;l='+location+'&amp;sort=date'
 
 
 

 
 
def job_data(url,items):
    titles  =[]
    links = []
    companies = []
    summaries  = []
    k=[]
    h=0
    dates =[]
    for j in range(0,2,1):
        res = requests.get(url+str(j)).content
        soup = BeautifulSoup(res,'html.parser')
        data = soup.find_all('div',class_='jobsearch-SerpJobCard')
        
        
        for i in data:
    
            title = i.find('h2',class_='title')
    
            if items[0] in title.text:
                company = i.find('span',class_='company')
                link = title.find('a')
                summary  =i.find('div',class_='summary')
            
                url1='https://www.indeed.co.in'+link['href']
                res1 = requests.get(url1).content
                soup1 = BeautifulSoup(res1,'html.parser')
                
                k.append(h+1)
                h=h+1

                data3=soup1.find(lambda tag:tag.name=="a" and "Apply On Company Site" in tag.text)

                
            
                    
                
                    
                date = i.find('span',class_='date')
    
                titles.append(title.text.strip())
                if data3==None:
                    links.append('https://www.indeed.co.in'+link['href'])
                else:
                    links.append(data3['href'])

                

                companies.append(company.text.strip())
                dates.append(date.text.strip())
                summaries.append(summary.text.strip())
    
                # print('\nJob Title:',title.text)
                # #print('posted:',date.text)
                # print('Company Name:',company.text)
                # print('Job Summary:',summary.text)
                # print('posted:',date.text)
                # print('https://www.indeed.co.in'+link['href'])
                # print(10*'*****')
            
 
    return k,titles,companies,summaries,dates,links
 
#job_data(url)