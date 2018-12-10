# gtmatrix-
It is a `Scrapper and Automation Tool` that is deloped to check all the issues in the website like what kind of improvement can be made in the website so that google will rank your website up in the google serarch resulet. This tool is developed using `selenium` python model to get all the required metrics according to contrywise and generate a final CSV with all those metrics.
#Getting Started
Clone the library and copy into local system using `git clone` command
```
git clone https://github.com/narendra-kumawat/gtmatrix-.git
```
Create a virtula environment either using `virtualenv` or any oother python module. Using `virtualenv` create a virtual entironment such as following
 ```
 virtualenv venv -p python3.5 
 ```
 After creating virtual environment activate the virtualenv as follows
 ```
 source venv/bin/activate
 ```
Now install the rquired library using `pip`
```
pip install selenium pandas 
```
Download the `chromedriver` to control the chrome seesion. Set the global path to the chrome driver. 
After that, copy all the urls you wants to generate the report in the `urls.py` file
```
urlList=[
    "https://www.datamintelligence.com/research-report/active-pharmaceutical-ingredients-market/",
    "https://www.datamintelligence.com/research-report/asia-pacific-adhesives-sealants-market/",
    "https://www.datamintelligence.com/research-report/aqua-feed-market/",
    "https://www.datamintelligence.com/research-report/asia-compound-feed-market/",
    "https://www.datamintelligence.com/research-report/ancient-grains-market/",
    "https://www.datamintelligence.com/research-report/alcoholic-beverages-market/",    
    ]
```
After adding all the urls in the urls.py file now run the file `gtmetricxScrapper.py`.
Once the process is done then the csv will be placed inside the report directory and the csv will be named as report.csv
