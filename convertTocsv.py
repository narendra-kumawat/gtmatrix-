import csv
i=0;j=0

def selectStrings(page):
    pageIssue=""    
    with open(page,"r") as f:
        line=f.readlines()
        seeker=1
        while(seeker<len(line)-1):             
            if line[seeker+1].find("C")!=-1 or line[seeker+1].find("F")!=-1 or line[seeker+1].find("D")!=-1 or line[seeker+1].find("E")!=-1 :
                print(line[seeker],line[seeker+1])
                pageIssue=pageIssue+line[seeker]+line[seeker+1]+","
                seeker+=3
            else:
                seeker+=3
        return pageIssue

def generateData(i):       
        page="./files/PageSpeed"+str(i)+".txt"
        PageSpeedIssues = selectStrings(page)
        page="./files/YSlow"+str(i)+".txt"
        YSlowIssues = selectStrings(page)
        print("---------------------------")
        return PageSpeedIssues,YSlowIssues
    

def generateCSV(data):
    global j
    if(j==0):
        mode="w"
    else:
        mode="a"
    with open('./report/report.csv',mode) as csvfile:
        fieldnames=['url','country','pageSpeedScore','ySlow','fullyLoadedTime','totalPageTime','request','pageSpeedIssues','YSlowIssues']
        writer=csv.DictWriter(csvfile, fieldnames=fieldnames)
        if(j==0):
            writer.writeheader()
            j+=1
        writer.writerow(data)
    

def dataStructure(url):
    global i
    countrycode=[1,3,4,5,6]    
    dictionary={0:'Dallas, USA',1:'London, UK',2:'Mumbai, India',3:'Sydney, Australia',4:'São Paulo, Brazil'}     
    with open("./files/data.txt","r") as f:
        line=f.readlines()
    issues=generateData(countrycode[i])
    data={
        "url":url,
        "country":dictionary[i],
        "pageSpeedScore":line[0],
        "ySlow":line[1],
        "fullyLoadedTime":line[2],
        "totalPageTime":line[3],
        "request":line[4],
        "pageSpeedIssues":issues[0],
        "YSlowIssues":issues[1]
    }
    generateCSV(data)
    i+=1
    if(i>4):
        i=0