import datetime as dt
import requests
from datetime import timezone
from .canvasbotdb import *

init()

def register_user(user_login_info):
    result = create_user(user_login_info.get("username"),user_login_info.get("password"),user_login_info.get("email"))
    if result == True:
        print("User created sucessfully! Gathering Canvas Information...")
        return gather_info(user_login_info.get("username"),user_login_info.get("api"))
    else:
        return False
    

def login_user(user_login_info):
    if verify_credentials(user_login_info.get("username"),user_login_info.get("password")):
        print("Verified!")
        result = get_user_assignments((user_login_info.get("username")))
        #print(result)
        course_list = []
        id = 1
        print("Getting courses")
        for course_assignment in result:
            course = course_assignment[0]
            assignment = course_assignment[1]
            due = course_assignment[2]
            if len(course_list) == 0:
             course_list.append({"id":id,"name":course,"children":[{"name": assignment,"due":due}]})
             continue
            if not any(d['name'] == course for d in course_list):
                id = id + 1
                course_list.append({"id":id,"name":course,"children":[{"name: ":assignment, " - due:":due}]})
            else:
                for d in course_list:
                    if d['name'] == course:
                        child_item_list = d.get("children")
                        child_item_list.append({"name": assignment,"due":due})
        #print({"success":"true","courses":course_list})
        return {"success":True,"courses":course_list}
    else:
        return {"success": False, "courses": []}
    

def update_preferences(user_info):
    username = user_info.get("username")
    password = user_info.get("password")
    preferences = user_info.get("preferences")
    
    result = create_preferences(username,preferences)
     #   print(result)
    if result:
        return {"success": True }
    else:
        return {"success": False }

def gather_info(username, API_TOKEN):
    info_result = None
    course_list = []
    #Will attempt to parse the response to json, should print out an error if it fails
    try:
        print("Grabbing Canvas Information...")
        courses = requests.get(url="https://rowan.instructure.com/api/v1/courses?access_token={}".format(API_TOKEN))
        print("Converting Info to Json...")
        json_courses = courses.json()

        #print(json_courses)

        for jcourse in json_courses:
            course_id = jcourse.get("id")
            course_name = jcourse.get("name")
            print(course_id)
            print(course_name)
            #Appears to grab other courses that are not visible anymore and are set as None.
            #Not adding the None courses because there is nothing to grab.
            if course_name == None:
                continue
            course_dict = {"id":course_id,"name":course_name}
            course_list.append(course_dict)

        #Loop through list of courses
        for course in course_list:
            print("Grabbing data for {}...".format(course))
            result = requests.get(url="https://rowan.instructure.com/api/v1/courses/{id}/assignments?access_token={api}".format(id=course['id'], api=API_TOKEN))

            json_results = result.json()
            #Create a course
            create_course(username,course["name"])
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
                create_assignment(username,course["name"],assignment_name,formatted_due_date)
                assignment_list.append({"name":assignment_name,"due":formatted_due_date})
            course.update({"children":assignment_list})
        #    info_result = course_list
        return True
    except:
        print("An error occured: {}".format(courses))
        return False
#app.run(debug=True)