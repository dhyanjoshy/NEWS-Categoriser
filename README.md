# RSS News Categorizer

This project is a Flask-based application that collects news articles from various RSS feeds, categorizes them using NLP models, and stores them in a MySQL database. It allows users to view categorized articles and download them in CSV format.

## Table of Contents
1. [Overview](#overview)
2. [Features](#features)
3. [Technologies Used](#technologies-used)
4. [Installation](#installation)
5. [Usage](#usage)
6. [Code Structure](#code-structure)
7. [API Endpoints](#api-endpoints)
8. [Dependencies](#dependencies)

## 1. Overview
The **RSS News Categorizer** allows users to input one or more RSS feed URLs, parse the feed for articles, and classify them into categories like:
- **Terrorism / Protest / Political Unrest / Riot**
- **Positive / Uplifting**
- **Natural Disasters**

The application uses a pre-trained DistilBERT model for article classification and stores the results in a MySQL database. Users can also download the stored articles in CSV format.

## 2. Features
- **Article Categorization**: Automatically categorizes articles into predefined categories using an NLP model.
- **Database Integration**: Stores the parsed articles into a MySQL database.
- **Article Fetching**: Fetches stored articles and displays them in a web interface.
- **CSV Export**: Allows users to download categorized articles in CSV format.
- **Logging**: Detailed logging using Python’s `logging` module.

## 3. Technologies Used
- **Backend**: Flask
- **Database**: MySQL
- **NLP Model**: DistilBERT (using Hugging Face Transformers)
- **Frontend**: HTML, CSS (via Jinja2 templates)
- **Other Tools**: Feedparser (for RSS parsing), MySQL Connector (for database interaction)

## 4. Installation
### Prerequisites:
- Python 3.x
- MySQL Server
  
### Steps:
1. Clone the repository:
   ```bash
   git clone https://github.com/dhyanjoshy/NEWS-Categoriser.git
   cd your-repo-name```
2.	Install dependencies:
    ```bash
    pip install -r requirements.txt
    ```
3.	Set up your MySQL database:
-  Create a database named news_categoriser.
-  Update the MySQL credentials in fetch_feeds.py and save_feeds.py:
4. Installation
Prerequisites:
-	Python 3.x
-	MySQL Server

Steps:
1.	Clone the repository:
bash
Copy code
https://github.com/dhyanjoshy/NEWS-Categoriser.git
cd your-repo-name
2.	Install dependencies:
```bash
pip install -r requirements.txt
```
3.	Set up your MySQL database:
-	Create a database named news_categoriser.
-	Update the MySQL credentials in fetch_feeds.py and save_feeds.py:
python
Copy code
host='localhost',
user='your_mysql_user',
password='your_mysql_password',
database='news_categoriser'
4.	Run the application:
```bash
python app.py
```
## 5. Usage
1.	Open the browser and navigate to http://localhost:5000.
2.	Enter an RSS feed URL or multiple URLs in the provided form.
3.	Click Submit to parse, categorize, and save the articles.
4.	Access the articles from the /data route and download them using the /download route.
## 6. Code Structure
-	app.py: Main Flask application, handles routing and requests.
-	fetch_feeds.py: Fetches articles stored in the MySQL database.
-	parse_feeder.py: Parses RSS feeds and categorizes articles using DistilBERT.
-	save_feeds.py: Saves parsed articles into the MySQL database.
-	templates/: Contains HTML templates for rendering web pages.
-	requirements.txt: Lists the dependencies required for the project.
## 7. API Endpoints
-	/ (GET/POST):
o	GET: Displays the main page with a form to enter RSS feed URLs.
o	POST: Parses the feed, categorizes articles, and saves them to the database.
-	/multiple_url (GET/POST):
o	GET: Displays a form for submitting multiple URLs.
o	POST: Processes the list of URLs and categorizes the articles.
-	/data (GET):
o	Fetches categorized articles from the database and displays them.
-	/download (GET):
o	Downloads the stored articles in CSV format.
## 8. Dependencies
All dependencies are listed in requirements.txt. Key dependencies include:
-	Flask: For handling HTTP requests.
-	MySQL Connector: For database interaction.
-	Feedparser: For parsing RSS feeds.
-	Transformers (Hugging Face): For using the DistilBERT NLP model.

