import os
import sqlite3
from sqlite3 import Error
import hashlib

db_file = r"./canvasbot.db"

def create_connection(db_file):
    conn = None
    try:
        conn = sqlite3.connect(db_file)
        return conn
    except Error as e:
        print(e)

def create_table(create_table_sql):
    try:
        conn = sqlite3.connect(db_file)
        c = conn.cursor()
        c.execute(create_table_sql)
    except Error as e:
        print(e)

def create_user(username, password):
    password = password.encode()
    salt = os.urandom(16)
    password_hash = hashlib.pbkdf2_hmac("sha256", password, salt, 100000)
    user = (username, password_hash, salt, "{short}@students.rowan.edu".format(short = username))
    insert_user(user)

def create_preferences(username, reminder_time):
    row = select_user(username)
    if row is not None:
        preferences = (row[0], reminder_time)
        insert_preferences(preferences) 

def create_course(username, course_name) :
    row = select_user(username)
    if row is not None:
        course = (row[0], course_name)
        insert_course(course)

def create_assignment(course_name, assignment_title, due_date):
    row = select_course(course_name)
    if row is not None:
        assignment = (row[0], assignment_title, due_date)
        insert_assignment(assignment)

def insert_user(user):
    conn = sqlite3.connect(db_file)
    cur = conn.cursor()
    row = select_user(user[0])
    if row is None:
        sql = ''' INSERT INTO users(username, password_hash, password_salt, email_address)
              VALUES(\"{uname}\",\" {pw_hash}\", {pw_salt}, \"{email}\") '''.format(uname = user[0], pw_hash = user[1], pw_salt = user[2], email = user[3])
        cur.execute(sql, user)
        conn.commit()

def insert_preferences(preferences):
    conn = sqlite3.connect(db_file)
    cur = conn.cursor()
    cur.execute("SELECT * FROM preferences WHERE user_id = {id}".format(id = preferences[0]))
    row = cur.fetchone()
    if row is None:
        print("Adding preferences for user_id {}".format(preferences[0]))
        sql = ''' INSERT INTO preferences(user_id, reminder_time)
              VALUES({id}, {rem_time}) '''.format(id = preferences[0], rem_time = preferences[1])
    else:
        print("Updating preferences for user_id {}".format(preferences[0]))
        sql = ''' UPDATE preferences SET reminder_time = {rem_time} 
              WHERE user_id = {id}'''.format(rem_time = preferences[1], id = preferences[0])
    cur.execute(sql)
    conn.commit()

def insert_course(course):
    conn = sqlite3.connect(db_file)
    cur = conn.cursor()
    cur.execute("SELECT * FROM courses WHERE user_id = {id} AND name = \"{name}\"".format(id = course[0], name = course[1]))
    row = cur.fetchone()
    if row is None:
        print("Adding new course for user_id {}".format(course[0]))
        sql = ''' INSERT INTO courses(user_id, name)
              VALUES({id}, \"{course_name}\") '''.format(id = course[0], course_name = course[1])
        cur.execute(sql)
        conn.commit()

def insert_assignment(assignment):
    conn = sqlite3.connect(db_file)
    cur = conn.cursor()
    cur.execute("SELECT * FROM assignments WHERE course_id = {id} AND title = \"{name}\"".format(id = assignment[0], name = assignment[1]))
    row = cur.fetchone()
    if row is None:
        print("Adding new assignment for course id {}".format(assignment[0]))
        sql = ''' INSERT INTO assignments(course_id, title, due_date)
              VALUES({id}, \"{title}\", \"{due_date}\") '''.format(id = assignment[0], title = assignment[1], due_date = assignment[2])
    else:
        print("Updating assignments for course_id {}".format(assignment[0]))
        sql = ''' UPDATE assignments SET due_date = \"{due_date}\" 
              WHERE course_id = {id} AND title = \"{title}\"'''.format(due_date = assignment[2], id = assignment[0], title = assignment[1])
    cur.execute(sql)
    conn.commit()

def select_user(username):
    conn = sqlite3.connect(db_file)
    cur = conn.cursor()
    cur.execute("SELECT * FROM users WHERE username = \"{uname}\"".format(uname = username))
    row = cur.fetchone()
    return row

def select_course(course_name):
    conn = sqlite3.connect(db_file)
    cur = conn.cursor()
    cur.execute("SELECT * FROM courses WHERE name = \"{cname}\"".format(cname = course_name))
    row = cur.fetchone()
    return row

def user_registered(username):
    user = select_user(username)
    if user is None:
        return False
    else:
        return True

def verify_credentials(username, password):
    user = select_user(username)
    if user is not None:
        password = password.encode()
        password_hash = hashlib.pbkdf2_hmac("sha256", password, user[3], 100000)
        return (password_hash == user[2])
    else:
        return False

def get_user_assignments(username):
    user = select_user(username)
    print(user)
    if user is not None:
        conn = sqlite3.connect(db_file)
        cur = conn.cursor()
        cur.execute("SELECT * FROM courses WHERE user_id = \"{uname}\"".format(uname = user[1]))
        courses = cur.fetchall()
        for course in courses:
            print(course)

    

def init():
    # create a database connection
    create_connection("./canvasbot.db")
    
    sql_create_users_table = """ CREATE TABLE IF NOT EXISTS users (
                                        id integer PRIMARY KEY,
                                        username text NOT NULL,
                                        password_hash text NOT NULL,
                                        password_salt integer NOT NULL,
                                        email_address text NOT NULL
                                    ); """

    sql_create_preferences_table = """CREATE TABLE IF NOT EXISTS preferences (
                                    id integer PRIMARY KEY,
                                    user_id integer,
                                    reminder_time integer,
                                    FOREIGN KEY (user_id) REFERENCES users (id)
                                );"""

    sql_create_courses_table = """CREATE TABLE IF NOT EXISTS courses (
                                    id integer PRIMARY KEY,
                                    user_id integer,
                                    name text,
                                    FOREIGN KEY (user_id) REFERENCES users (id)
                                );"""
    
    sql_create_assignments_table = """CREATE TABLE IF NOT EXISTS assignments (
                                    id integer PRIMARY KEY,
                                    course_id integer,
                                    title text,
                                    due_date text,
                                    FOREIGN KEY (course_id) REFERENCES courses (id)
                                );"""

    # create db tables
    create_table(sql_create_users_table)
    create_table(sql_create_preferences_table)
    create_table(sql_create_courses_table)
    create_table(sql_create_assignments_table)

    # insert sample data

    # insert sample users
    sample_username1 = "jeffersod2"
    sample_password1 = "Baseball1996!"
    create_user(sample_username1, sample_password1)
    sample_username2 = "randerson1"
    sample_password2 = "Football1965!"
    create_user(sample_username2, sample_password2)

    # set preferences
    reminder_time = 86400   # 1 day before due date
    create_preferences(sample_username2, reminder_time)
    reminder_time = 1209600   # 2 weeks before due date
    create_preferences(sample_username1, reminder_time)

    # insert sample courses
    sample_course_name1 = "Adv. Software Engineering"
    create_course(sample_username1, sample_course_name1)
    sample_course_name2 = "Concepts of Artificial Intelligence"
    create_course(sample_username1, sample_course_name2)
    sample_course_name3 = "History of Broadcast Media"
    create_course(sample_username2, sample_course_name3)
    
    # insert sample assignments
    sample_assignment_title1 = "Group Assignment 3 - Implementation&Testing"
    sample_assignment_due_date1 = "2020-08-25 03:59:00"
    create_assignment(sample_course_name1, sample_assignment_title1, sample_assignment_due_date1)
    sample_assignment_title2 = "Log 5"
    sample_assignment_due_date2 = "2020-08-12 03:59:00"
    create_assignment(sample_course_name1, sample_assignment_title2, sample_assignment_due_date2)
    sample_assignment_title3 = "Final Project"
    sample_assignment_due_date3 = "2020-08-21 11:59:00"
    create_assignment(sample_course_name3, sample_assignment_title3, sample_assignment_due_date3)

    # test
    incorrect_password = "Sloshfest02"
    correct_password = "Baseball1996!"
    print("false password checked: {}".format(verify_credentials(sample_username1, incorrect_password)))
    print("correct password checked: {}".format(verify_credentials(sample_username1, correct_password)))

    #print(get_user_assignments(sample_username1))
    #print(get_user_assignments(sample_username2))



if __name__ == '__main__':
    init()