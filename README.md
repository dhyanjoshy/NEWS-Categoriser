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
9. [License](#license)

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
- **Task Queue**: Celery (planned)
- **Frontend**: HTML, CSS (via Jinja2 templates)
- **Other Tools**: Feedparser (for RSS parsing), MySQL Connector (for database interaction)

## 4. Installation
### Prerequisites:
- Python 3.x
- MySQL Server
- Redis (if using Celery for background tasks)
  
### Steps:
1. Clone the repository:
   ```bash
   git clone https://github.com/your-repo-name.git
   cd your-repo-name```bash
2.  
