import requests
import json


API_ENDPOINT = "http://127.0.0.1:5000/health_check"

USER = "http://127.0.0.1:5000/user"

LOGIN = "http://127.0.0.1:5000/login"

COURSES = "http://127.0.0.1:5000/courses"

TOKEN_API = "https://dev-courses-api.herokuapp.com/get_token"

auth={ "client_id": "0oa2hl2inow5Uqc6c357", "client_secret": "25Dytivbm1tIBq37YujEsp5A3d486I08NDzdJZw94xe828DNR9TktHvJA3JTtvDA" }

data = {"email":"m@gmail.com","password":"123a","company_name":"Masterhub"}

create_account = True
retreieve_token = False

if create_account:
	create_user = requests.post(url=USER, json = data)
	print(create_user.text)



if retreieve_token:
	token = requests.post(url = "https://dev-courses-api.herokuapp.com/get_token", json = auth).json()
	access_token = token["access_token"]
	AUTHORIZATION = {"Authorization":access_token}


def course_download(url = "https://dev-courses-api.herokuapp.com/courses", to_csv=False):

	courses = requests.get(url="https://dev-courses-api.herokuapp.com/courses",headers=AUTHORIZATION).json()
	if to_csv:
		df = pd.read_json(courses)
		df.to_csv("courses.csv")
	return courses


with requests.Session() as s:
    p = s.post(url=LOGIN, json={"email":"m@gmail.com","password":"123a"})
    # print the html returned or something more intelligent to see if it's a successful login page.
    print(p.text)

    # An authorised request.
    r = s.get(url=USER)
    print(r.text)

    c = s.get(url=COURSES)
    print(c.text)
