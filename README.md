# news-notifications
News Desktop Notifications

![Alt text](demo/demo1.png?raw=true)

![Alt text](demo/demo2.png?raw=true)

![Alt text](demo/demo3.png?raw=true)


## Getting Started

### Get the API Keys

Visit https://developer.nytimes.com/get-started to get an api key for the NYT API. 

Visit https://open-platform.theguardian.com/access/ to get an api key for The Guardian API. 

### Modify Config

* Rename config.template.ini to config.ini
* Add the api keys to the config file
* Look over sections.txt which lists the available news categories for each api
* Add sections separated by comma to the config file for each api

### Run

`python3 notify.py`
