import datetime as dt
import requests
from datetime import timezone
import canvasbotdb
from flask import Blueprint

cb_controller = Blueprint('cb_controller',__name__,static_folder="static",template_folder="templates")



#@app.route("/register_user", methods=["POST", "GET"])
@cb_controller.route("/register_user")
def register_user(user_login_info):
    result = canvasbotdb.create_user(user_login_info.get("username"),user_login_info.get("password"))
    if result == True:
        return gather_info(user_login_info.get("api"))
    else:
        return "Returned False"#False
    
#@app.route("/login_user",methods=["POST", "GET"])
def login_user(user_login_info):
    if canvasbotdb.verify_credentials(user_login_info.get("username"),user_login_info.get("password")):
        result = canvasbotdb.get_user_assignments((user_login_info.get("username"))
        course_list = []
        id = 1
        for course_assignment in result:
    
            course = course_assignment[0]
            assignment = course_assignment[1]
            due = course_assignment[2]
            if len(course_list) == 0:
             course_list.append({"id":id,"name":course,"children":[{"name": assignment,"due":due}]})
             continue
            if not any(d['name'] == course for d in course_list):
                id = id + 1
                course_list.append({"id":id,"name":course,"children":[{"name": assignment,"due":due}]})
            else:
                for d in course_list:
                    if d['name'] == course:
                        child_item_list = d.get("children")
                        child_item_list.append({"name": assignment,"due":due})
        return {"success":"true","courses":course_list}
    else:
        return {success: false, courses: []}
    

def update_preferences(user_info):
    if canvasbotdb.verify_credentials(user_info.get("username"),user_info.get("password")):
        return canvasbotdb.create_preferences(user_info.get("username"),user_info.get("preferences"))
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
#app.run(debug=True)