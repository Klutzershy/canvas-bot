import datetime as dt
import requests
from datetime import timezone

course_list=[]

#This assumes you are working on Windows, change the \ to / if you are on Mac/Linux
token_file = "..\canvas_auth_token.txt"

with open(token_file,'r') as file: API_TOKEN = file.read()

courses = requests.get(url="https://rowan.instructure.com/api/v1/courses?access_token={}".format(API_TOKEN))

json_courses = courses.json()

def gather_info():
    info_result = None
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
        result = requests.get(url="https://rowan.instructure.com/api/v1/courses/{id}/assignments?access_token={api}".format(id=course['id'], api=API_TOKEN))

        json_results = result.json()
        print("Course: {}".format(course['name']))
        assignment_list=[]
        for i in json_results:
            assignment_name = i.get("name")
            due_date = i.get("due_at")
            #Time is currently UTC, haven't bothered with switching to EST yet
            formatted_due_date = dt.datetime.strptime(due_date,"%Y-%m-%dT%H:%M:%SZ")

            print("Name: {}".format(assignment_name))
            print("Due: {}".format(formatted_due_date))
            assignment_list.append({"name":assignment_name,"due_date":formatted_due_date})
        course.update({"assignments":assignment_list})
    info_result = course_list
    return info_result
