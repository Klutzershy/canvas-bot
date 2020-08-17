import os
import sqlite3
from sqlite3 import Error
import hashlib, uuid

db_file = r"./canvasbot.db"

def create_connection(db_file):
    conn = None
    try:
        conn = sqlite3.connect(db_file)
        return True
    except Error as e:
        print(e)
        return False

def create_table(create_table_sql):
    try:
        conn = sqlite3.connect(db_file)
        c = conn.cursor()
        c.execute(create_table_sql)
        return True
    except Error as e:
        print(e)
        return False

def create_user(username, password, email):
    password = password.encode('utf-8')
    salt = uuid.uuid4().hex
    salt = salt.encode('utf-8')
    password_hash = hashlib.sha256(password+ salt).hexdigest()
    user = (username, password_hash, salt, email)
    ret_val = insert_user(user)
    return ret_val

def create_preferences(username, reminder_time):
    row = select_user(username)
    if row is not None:
        preferences = (row[0], reminder_time)
        ret_val = insert_preferences(preferences) 
    else:
        ret_val = False
    return ret_val

def create_course(username, course_name) :
    row = select_user(username)
    if row is not None:
        course = (row[0], course_name)
        ret_val = insert_course(course)
    else:
        ret_val = False
    return ret_val

def create_assignment(username, course_name, assignment_title, due_date):
    user = select_user(username)
    if user is not None:
        course = select_course(user[0], course_name)
        if course is not None:
            assignment = (course[0], assignment_title, due_date)
            ret_val = insert_assignment(assignment)
        else:
            ret_val = False
    else:
        ret_val = False
    return ret_val

def insert_user(user):
    try:
        conn = sqlite3.connect(db_file)
        cur = conn.cursor()
        row = select_user(user[0])
        if row is None:
            sql = ''' INSERT INTO users(username, password_hash, password_salt, email_address)
                  VALUES(?,?,?,?) '''
            val = user
        else:
            sql = ''' UPDATE users SET password_hash = ?, password_salt = ?
                  WHERE username = ?'''
            val = (user[1], user[2], user[0])
        cur.execute(sql, val)          
        conn.commit()
        return True
    except Error as e:
        print(e)
        return False

def insert_preferences(preferences):
    try:
        conn = sqlite3.connect(db_file)
        cur = conn.cursor()
        cur.execute("SELECT * FROM preferences WHERE user_id = {id}".format(id = preferences[0]))
        row = cur.fetchone()
        if row is None:
            sql = ''' INSERT INTO preferences(user_id, reminder_time)
                  VALUES({id}, {rem_time}) '''.format(id = preferences[0], rem_time = preferences[1])
        else:
            sql = ''' UPDATE preferences SET reminder_time = {rem_time} 
                  WHERE user_id = {id}'''.format(rem_time = preferences[1], id = preferences[0])
        cur.execute(sql)
        conn.commit()
        return True
    except Error as e:
        print(e)
        return False

def insert_course(course):
    try:
        conn = sqlite3.connect(db_file)
        cur = conn.cursor()
        cur.execute("SELECT * FROM courses WHERE user_id = {id} AND name = \"{name}\"".format(id = course[0], name = course[1]))
        row = cur.fetchone()
        if row is None:
            sql = ''' INSERT INTO courses(user_id, name)
                  VALUES({id}, \"{course_name}\") '''.format(id = course[0], course_name = course[1])
            cur.execute(sql)
            conn.commit()
        return True
    except Error as e:
        print(e)
        return False

def insert_assignment(assignment):
    try:
        conn = sqlite3.connect(db_file)
        cur = conn.cursor()
        cur.execute("SELECT * FROM assignments WHERE course_id = {id} AND title = \"{name}\"".format(id = assignment[0], name = assignment[1]))
        row = cur.fetchone()
        if row is None:
            sql = ''' INSERT INTO assignments(course_id, title, due_date)
                  VALUES({id}, \"{title}\", \"{due_date}\") '''.format(id = assignment[0], title = assignment[1], due_date = assignment[2])
        else:
            sql = ''' UPDATE assignments SET due_date = \"{due_date}\" 
                  WHERE course_id = {id} AND title = \"{title}\"'''.format(due_date = assignment[2], id = assignment[0], title = assignment[1])
        cur.execute(sql)
        conn.commit()
        return True
    except Error as e:
        print(e)
        return False

def select_user(username):
    try:
        conn = sqlite3.connect(db_file)
        cur = conn.cursor()
        cur.execute("SELECT * FROM users WHERE username = \"{uname}\"".format(uname = username))
        row = cur.fetchone()
        return row
    except Error as e:
        print(e)
        return None

def select_course(user_id, course_name):
    try:
        conn = sqlite3.connect(db_file)
        cur = conn.cursor()
        cur.execute("SELECT * FROM courses WHERE name = \"{cname}\" AND user_id = {uid}".format(cname = course_name, uid = user_id))
        row = cur.fetchone()
        return row
    except Error as e:
        print(e)
        return None

def user_registered(username):
    user = select_user(username)
    if user is None:
        return False
    else:
        return True

def verify_credentials(username, password):
    user = select_user(username)
    print(user)
    if user is not None:
        password = password.encode('utf-8')
        db_salt = user[3]
        print(db_salt)
        password_hash = hashlib.sha256(password+ db_salt).hexdigest()
        print(password_hash)
        print(user[2])
        print(password_hash == user[2])
        return (password_hash == user[2])
    else:
        return False

def get_user_assignments(username):
    user = select_user(username)
    if user is not None:
        conn = sqlite3.connect(db_file)
        cur = conn.cursor()
        cur.execute('''SELECT courses.name, assignments.title, assignments.due_date FROM assignments 
                    INNER JOIN courses ON assignments.course_id = courses.id 
                    WHERE user_id = {id}'''.format(id = user[0]))
        courses = cur.fetchall()
        return courses
    else:
        return None

def get_user_preferences(username):
    user = select_user(username)
    if user is not None:
        conn = sqlite3.connect(db_file)
        cur = conn.cursor()
        cur.execute('''SELECT users.username, preferences.reminder_time FROM preferences 
                    INNER JOIN users ON preferences.user_id = users.id 
                    WHERE user_id = {id}'''.format(id = user[0]))
        preferences = cur.fetchone()
        return preferences
    else:
        return None

def clean():
    try:
        conn = sqlite3.connect(db_file)
        cur = conn.cursor()
        cur.execute("DELETE FROM users;")
        cur.execute("DELETE FROM preferences;")
        cur.execute("DELETE FROM courses;")
        cur.execute("DELETE FROM assignments;")
        cur.execute("DROP TABLE users;")
        cur.execute("DROP TABLE preferences;")
        cur.execute("DROP TABLE courses;")
        cur.execute("DROP TABLE assignments;")
        return True
    except Error as e:
        print(e)
        return False
    

def init():
    # create a database connection
    create_connection("./canvasbot.db")
    
    sql_create_users_table = """ CREATE TABLE IF NOT EXISTS users (
                                        id integer PRIMARY KEY,
                                        username text NOT NULL,
                                        password_hash text NOT NULL,
                                        password_salt text NOT NULL,
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


if __name__ == '__main__':
    init()