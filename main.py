import sqlite3


def Database(): # start database/sqlite
    conn = sqlite3.connect('activities.db') # set up to database
    c = conn.cursor() # create cursor
    # create table for the activities
    c.execute("""CREATE TABLE IF NOT EXISTS activities (
              id INT PRIMARY KEY AUTO_INCREMENT,
              Title TEXT,
              Hours INT              
              )""")


