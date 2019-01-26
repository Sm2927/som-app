import sqlite3

# create a new database if the database doesn't already exist
with sqlite3.connect('som.db') as connection:

    # get a cursor object used to execute SQL commands
    c = connection.cursor()

    # create the table
    c.execute('CREATE TABLE IF NOT EXISTS courses(subject TEXT, Lecturer TEXT)')

    # insert dummy data into the table
    c.execute('INSERT INTO courses VALUES("Machine Learning", "Andrew")')
    c.execute('INSERT INTO courses VALUES("Data Science", "Jose Portilla")')
    c.execute('INSERT INTO courses VALUES("Front End Dev", "Colt Steele")')
    c.execute('INSERT INTO courses VALUES("Flask API", "Michael Herman")')
    c.execute('SELECT * FROM courses')
