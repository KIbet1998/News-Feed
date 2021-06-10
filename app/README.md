#  NEWS API
#### Author: [Ronald Rono](https://github.com/KIbet1998/News-Feed.git)
## Description
This is a flask application that provides users with various sources of information and displays news from various categories.
As a user of the web application you will be able to:
1. See various news sources on the homepage of the application.
2. Select a news source and see all news articles from the selected news source in the application.
3. See the image, description and the time a news article was created.
4. Click on an article and read the full article on the source website.
## Setup and installations
* Clone Project to your machine
* Activate a virtual environment on terminal: `source virtual/bin/activate`
* Install all the requirements found in requirements file.
* On your terminal run `python3.8 manage.py runserver`
* Access the live site using the local host provided
## Getting started
### Prerequisites
* python3.8
* virtual environment
* pip
#### Clone the Repo and rename it to suit your needs.
```bash
git clone https://github.com/KIbet1998/News-Feed.git
```
#### Initialize git and add the remote repository
```bash
git init
```
```bash
git remote add origin <your-repository-url>
```
#### Create and activate the virtual environment
```bash
python3.8 -m virtualenv virtual
```
```bash
source virtual/bin/activate
```
#### Setting up environment variables
Create a `.env` file and paste paste the following filling where appropriate:
```
SECRET_KEY = 'your secret key'
DEBUG=True
```
#### Install dependancies
Install dependancies that will create an environment for the app to run
`pip install -r requirements.txt`
#### Run the app
```bash
python3.8 run.py
```
Open [localhost:5000](http://127.0.0.1:5000/)
## Built With
* [Python3.8](https://docs.python.org/3/)
* Boostrap
* HTML
* CSS