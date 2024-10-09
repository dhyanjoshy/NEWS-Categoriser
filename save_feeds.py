import mysql.connector
from mysql.connector import Error


def insert_feed_entry(title, content, published, url, media_url, category):
    status = None
    try:
        # Connect to the MySQL database
        connection = mysql.connector.connect(
            host='localhost',
            user='dhyan',
            password='1234',
            database='news_categoriser'
        )

        if connection.is_connected():
            cursor = connection.cursor()

            # Check if the title already exists
            check_query = "SELECT COUNT(*) FROM feed_entries WHERE title = %s"
            cursor.execute(check_query, (title,))
            count = cursor.fetchone()[0]

            if count == 0:
                # SQL query to insert a new entry
                sql_insert_query = """
                INSERT INTO feed_entries (title, content, published, url, media_url, category) 
                VALUES (%s, %s, %s, %s, %s, %s)
                """
                # Data to insert
                data_tuple = (title, content, published, url, media_url, category)

                # Execute the query
                cursor.execute(sql_insert_query, data_tuple)

                # Commit the transaction
                connection.commit()
                status = "Success"
                print("Record inserted successfully into feed_entries table.")
                return status
            else:
                status = f"Entry with title '{title}' already exists. No insertion made."
                print(f"Entry with title '{title}' already exists. No insertion made.")
                return status

    except Error as e:
        print(f"Error: {e}")
        status = e
    finally:
        # Close the database connection
        if connection.is_connected():
            cursor.close()
            connection.close()
            print("MySQL connection is closed.")
        return status


def article_save(articles,logger):
    logger.info(f'Articles saving session started')
    for article in articles:
        status = insert_feed_entry(
            title=article['title'],
            content=article['content'],
            published=article['published'],
            url=article['url'],
            media_url=article['media_url'],
            category=article['category']
        )
        logger.info(f'Article saving status : {status}')
    print("finished")
    return "Done"

if __name__=="__main__":
    pass
