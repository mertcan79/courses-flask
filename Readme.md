# Junior/Mid Python Assignment

Following application provides backend **REST API** for on-line Courses.

### Instructions

1. Start with setting up your local and **Heroku** apps with guidelines from **Application setup** section below
2. Code as many **Requirements** as you're able to. **Requirement** completed partially is better then nothing
3. Push latest working app to **Heroku**
4. Replace Readme link to your **Heroku** app in section **Heroku app link**
5. Update application Readme with useful informations
6. Create your own branch and push final version back to repository
7. Create Pull Request to **master** from your branch (in review we will address lines of code in Github Pull Request)
8. Notify your recruiter about assignment completion
9. Good job! We're gonna reach back to you with feedback :)

#### Application setup

1. Make sure you have **GIT** installed
2. Clone repository with assigment and enter project directory
3. Make sure you have **venv** installed
4. Create local **venv** (Python version is defined in `runtime.txt`) for project and activate it
5. Install app dependencies and run app locally `flask run`
6. Local app health check should be accessible [http://127.0.0.1:5000/health_check](`http://127.0.0.1:5000/health_check`)
7. Install **Heroku** cli ([https://heroku.com/](https://heroku.com/))
8. Create **Heroku** free account
9. Login into **Heroku** with `heroku login`
10. Create **Heroku** app with `heroku create your-app-name`
11. Enable **Heroku** app metadata in runtime with `heroku labs:enable runtime-dyno-metadata --app your-app-name`
12. Add **Heroku** remote to GIT `git remote add heroku https://git.heroku.com/your-app-name.git`
13. Create **Heroku** database `heroku addons:create heroku-postgresql:hobby-dev --app your-app-name`
14. Display **Heroku** config for your app `heroku config --app your-app-name`
15. Update `.flaskenv` `SQLALCHEMY_DATABASE_URI` with your database url (mind protocol which should be `postgresql`)
16. Set the same env var for database in **Heroku** with `heroku config:set SQLALCHEMY_DATABASE_URI=...`
17. Commit your local changes and push to **Heroku** - `git push heroku master`
18. Your **Heroku** app health check should be accessible [https://your-app-name.herokuapp.com/health_check](`https://your-app-name.herokuapp.com/health_check`)
19. It's time to start coding!

#### Heroku app link

<< replace with your Heroku app link >>

#### Requirements

As a developer:
- I want to keep code clean, simple and organized
- I want to keep clean and descriptive repository history
- I want to have linter to verify my code on demand
- I want all repository code matching linter rules
- I want to be sure my code works by applying tests!

As student:
- I want to have my password stored in secure manner 
- I want to be able to persist information about my completed Courses with time of the completion event
- I want to be able to be able to get list of all completed and all available Courses (with author, category and publication date) sorted by Course name
- I want to have a way to get suggestion of one Course that I haven't completed yet based on my preferred category (preferred category should be allowed to set per user)

As content admin:
- I would like to have API endpoints restricted to content admins exclusively
- I would like to have API endpoint to get all globally available Courses with option that downloads results as CSV file
- I would like to have API endpoint to assign Courses to Companies so Students of Companies are able to see and complete them
- I would like to have API endpoint to get Company stats containing: number of users in Company; number of completed Courses by Company users within last 20 days
- I would like to have **Flask** cli command that whenever triggered will look for Courses from **Courses API** and persist them as application Courses not assigned to any Company initially
> ##### Courses API
> - Credentials:
>   - client_id: `0oa2hl2inow5Uqc6c357`
>   - client_secret: `25Dytivbm1tIBq37YujEsp5A3d486I08NDzdJZw94xe828DNR9TktHvJA3JTtvDA`
> - Get Token endpoint: `https://dev-courses-api.herokuapp.com/get_token` POST json with `client_id` and `client_secret` (example: `echo '{ "client_id": "0oa2hl2inow5Uqc6c357", "client_secret": "25Dytivbm1tIBq37YujEsp5A3d486I08NDzdJZw94xe828DNR9TktHvJA3JTtvDA" }' | http POST https://dev-courses-api.herokuapp.com/get_token`)
> - Get Courses endpoint: `https://dev-courses-api.herokuapp.com/courses` GET with `Authorization` header containing Token (example: `http https://dev-courses-api.herokuapp.com/courses Authorization:1cfc539a-ce16-41c4-9102-c4759dd72a2c`)

As data engineer:
- I would like to have a way to get number of median length of Courses completed during weekends per each User in system
