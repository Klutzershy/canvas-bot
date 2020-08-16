import datetime as dt
import requests
from datetime import timezone
import canvasbotdb
from flask import Flask,request
from flask import CORS

app = Flask(__name__)
CORS(app)

#@app.route("/")
#def index():


@app.route("/register_user", methods=["POST", "GET"])
def register_user():
    result = canvasbotdb.create_user(test_user_name,"Test2")
    if result == True:
        token="token_here"
        
        return "Returned True"#gather_info(token)
    else:
        return "Returned False"#False
    
@app.route("/login_user",methods=["POST", "GET"])
def login_user(user_login_info):
    if canvasbotdb.verify_credentials(user_login_info[0],user_login_info[1]):
        return canvasbotdb.get_user_assignments(user_login_info[0])
    else:
        return "{success: false, courses: []}"}
    

def update_preferences(user_login_info,preference):
    if canvasbotdb.verify_credentials(user_login_info[0],user_login_info[1]):
        canvasbotdb.create_preferences(user_login_info[0],preference)
    else:
        return False

def gather_info(API_TOKEN):
    info_result = None
    
    #Will attempt to parse the response to json, should print out an error if it fails
    try:
        courses = requests.get(url="https://rowan.instructure.com/api/v1/courses?access_token={}".format(API_TOKEN))
        json_courses = courses.json()
    


        for jcourse in json_courses:
            course_id = jcourse.get("id")
            course_name = jcourse.get("name")
        
            #Appears to grab other courses that are not visible anymore and are set as None.
            #Not adding the None courses because there is nothing to grab.
            if course_name == None:
                continue
            course_dict = {"id":course_id,"name":course_name}
            course_list.append(course_dict)

            #Loop through list of courses
            for course in course_list:
                try:
                    result = requests.get(url="https://rowan.instructure.com/api/v1/courses/{id}/assignments?access_token={api}".format(id=course['id'], api=API_TOKEN))

                    json_results = result.json()
                except:
                    print("An error occured accessing course: {} {}".format(course['name'],result))
                    return False
        
                #Create a course
                canvasbotdb.create_course(test_user_name,course["name"])
                print("Course: {}".format(course["name"]))
                assignment_list=[]
                for i in json_results:
                    #Get the assignment name and due date
                    assignment_name = i.get("name")
                    due_date = i.get("due_at")
                    #Time is converted from utc to local time
                    formatted_due_date = dt.datetime.strptime(due_date,"%Y-%m-%dT%H:%M:%SZ")
                    formatted_due_date = formatted_due_date.replace(tzinfo=timezone.utc).astimezone(tz=None)
                    print("Name: {}".format(assignment_name))
                    print("Due: {}".format(formatted_due_date))
                    #Insert Assignment into the 
                    canvasbotdb.create_assignment(course["name"],assignment_name,formatted_due_date)
                    assignment_list.append({"name":assignment_name,"due":formatted_due_date})
                course.update({"children":assignment_list})
            info_result = course_list
            return True
    except:
        print("An error occured: {}".format(courses))
        return False
app.run(debug=True)