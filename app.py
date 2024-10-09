from flask import Flask, render_template, request, make_response, redirect
from parse_feeder import parse_feed
from save_feeds import article_save
from fetch_feeds import fetch_feeds_from_db
import csv
import logging
from logging.handlers import RotatingFileHandler

# Logger
logger = logging.getLogger('MyCustomLogger')
logger.setLevel(logging.DEBUG)
handler = RotatingFileHandler('app.log', maxBytes=100000, backupCount=3)
handler.setLevel(logging.DEBUG)
formatter = logging.Formatter('%(asctime)s - %(levelname)s - %(message)s')
handler.setFormatter(formatter)
logger.addHandler(handler)

app = Flask(__name__)

# Sample sum function (replace with your actual function)
@app.route('/', methods=['GET', 'POST'])
def index():
    result = None
    if request.method == 'POST':
        url = request.form.get('link')
        logger.info(f'Recived URL : {url}')
        articles = parse_feed(url)
        logger.info(f'Articles parsed')
        logger.info(f'Articles saving session started')
        status = article_save(articles,logger)
        logger.info(f'Articles saving session ended')
        print(status)
        print("done done")
        return redirect('/data')
    return render_template('index.html', result=result)

@app.route('/multiple_url', methods=['GET', 'POST'])
def multiple_url():
    if request.method == 'POST':
        data = request.get_json()
        urls = data.get('urls', [])
        
        # Process or print the list of URLs
        print(f"Received URLs: {urls}")
        logger.info(f'Recived URLS : {urls}')
        logger.info(f'Articles saving session started')
        for url in urls:
            articles = parse_feed(url)
            print(articles)
            status = article_save(articles,logger)
            print(status)
        print("finished") 
        logger.info(f'Articles saving session ended')     
        return redirect('/data')
    else:
        return render_template('multiple_url.html')

@app.route('/data', methods=['GET'])
def data():
    data,columns,error = fetch_feeds_from_db()
    return render_template('data.html', data=data, columns=columns)

@app.route('/download', methods=['GET'])
def download():
    data,columns,error = fetch_feeds_from_db()
    output_file = './output.csv'
    with open(output_file, 'w+', newline='', encoding='utf-8') as f:
        writer = csv.writer(f)
        writer.writerow(columns)
        writer.writerows(data) 


    response = make_response(open(output_file, 'r', encoding='utf-8').read())
    response.headers['Content-Type'] = 'text/csv'
    response.headers['Content-Disposition'] = f'attachment; filename={output_file}'
    return response




if __name__ == '__main__':
    app.run(debug=True)
