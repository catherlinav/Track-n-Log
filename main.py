import sqlite3
from activity import Activity


conn = sqlite3.connect('activities.db') # set up to database
c = conn.cursor() # create cursor


# create table for the activities
c.execute("""CREATE TABLE IF NOT EXISTS activities_log 
          (
          id INTEGER PRIMARY KEY,
          Title TEXT,
          Hours INT              
          )""")

def display_log(): # show the activities log
    c.execute("SELECT * FROM activities_log")
    return c.fetchall()

def add_activity(act): # add an activity ('hours' set to 0)
    with conn:
        c.execute("INSERT INTO activities_log (Title, Hours) VALUES (:title, :hours)",
                  {'title': act.title, 'hours': act.hours})

def remove_activity(act): # remove an activity
    with conn:
        c.execute("DELETE FROM activities_log WHERE Title = :title",
                  {'title': act.title})

def add_hours(act, hours): # add hours to existing activity
    with conn:
        c.execute("""UPDATE activities_log SET Hours = Hours + :hours
                  WHERE Title = :title""",
                  {'hours': hours, 'title': act.title})

act1 = Activity('Coding')
add_hours(act1, 123)
add_hours(act1, 123)


conn.close() # close connection