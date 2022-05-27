# The Sweat Life

The Sweat Life is a web application that allows users to post activities and interact with other users by commenting on their posts.

## User Stories

As a standard (not logged-in) user, I would like to:
<br>
<br>

1. View the landing page and know that I'm on a social site for exercise enthusiasts
<br>
<br>

2. View posts by users
<br>
<br>

3. Have a unique sign-up option with username and password
<br>
<br>

As a registered (logged-in) user, I would like to:
<br>
<br>

1. Have a login option to log in to my previously registered account
<br>
<br>

2. Create and post my own activities
<br>
<br>

3. Rate how I felt after my activity
<br>
<br>

4. View the uploads of other users
<br>
<br>

5. Like and comment on users' posts
<br>
<br>

6. Choose a date and time for group activities
<br>
<br>

7. View the other users who have chosen these time slots
<br>
<br>

8. Edit my activity
<br>
<br>

9. Delete my activity
<br>
<br>

## Project Goals

## Flowchart

![The Sweat Life Flowchart](/media/readme/sweatlife-flowchart.png)

## Wireframes

[Activity List Web](/media/readme/wireframes/activity-list-web.png)

[Activity List iPad](/media/readme/wireframes/activity-list-ipad.png)

[Activity List Phone](/media/readme/wireframes/activity-list-phone.png)

[Activity Detail Web](/media/readme/wireframes/activity-detail-web.png)

[Comment Web](/media/readme/wireframes/comment-web.png)

[Comment iPad](/media/readme/wireframes/comment-ipad.png)

[Comment Phone](/media/readme/wireframes/comment-phone.png)

[Create Activity Web](/media/readme/wireframes/create-activity-web.png)

[Create Activity iPad](/media/readme/wireframes/create-activity-ipad.png)

[Create Activity Phone](/media/readme/wireframes/create-activity-phone.png)

[Sign-Up Web](/media/readme/wireframes/signup-web.png)

[Sign-Up iPad](/media/readme/wireframes/signup-ipad.png)

[Sign-Up Phone](/media/readme/wireframes/signup-phone.png)

## Agile Methodology

## Features

### Navbar

The navigation bar gives you access to the activities page as well as an opportunity to either login with a previously created account or create an account via the sign up option.

![Navbar Logged-Out](/media/readme/navbar-logged-out.png)

The navigation bar once you are logged in gives you the opportunity to add your own activities as well as log out of your account.

![Navbar Logged-In](/media/readme/navbar-logged-in.png)

### Sign Up Page

The sign up page allows you to create an account by providing a username and password for authentication. Creating an account gives you access to extra functionality such as the ability to create, edit, and delete your own activities and comment on the activities of others.

![Sign-Up Page](/media/readme/signup-page.png)

### Login Page

As with the sign up page, the login page allows previously registered users to access the extra functionality that having an account provides.

![Login Page](/media/readme/login-page.png)

### Logout Page

The logout page allows you to confirm if you are sure you would like to logout

![Logout Page](/media/readme/sign-out-page.png)

### Activities Page

This page presents an ordered and paginated list of activities posted by users. Visible is the title and excerpt of the activity. These activities are public but an account must be created to leave a comment or create your own activities.

![Activities Page (logged-out)](/media/readme/activities-logged-out.png)

### Activities Page (logged-in)

![Activities Page (logged-in)](/media/readme/activities-logged-in.png)

### Activity Detail Page

The activity detail page presents the selected activtiy in detail including its title, excerpt, content and comments left by users.

![Activity Detail Page](/media/readme/activity-detail.png)

### Create Activity Page

The create activity page displays a form where you can enter a title, excerpt and the content of your activity.

![Create Activity Page](/media/readme/create-activity-page.png)

### Create Comment Page

The create comment page is shown as a form where you can leave a comment on the selected post.

![Create Comment Page](/media/readme/create-comment-page.png)

### Edit Activity Page

The edit activity page displays your activity as a form, pre-populated with the details and content previously provided so that you can edit your post.

![Edit Activity Page](/media/readme/update-activity-page.png)

### Delete Activity Page

The delete activity page displays a warning (defensive programming) to ensure that you are certain of your choice to delete the chosen activity and are aware of the consequences.

![Delete Activity Page](/media/readme/delete-activity-page.png)

### Edit Comment Page

The edit comment page displays your comment as a form, pre-populated with the content previously provided so that you can edit you comment.

### Delete Comment Page

The delete comment page displays a warning (defensive programming) to ensure that you are certain of your choice to delete the chosen comment and are aware of the consequences.

### 400 Error Page

The 400 error page displays a UX-friendly error message and the option to "return to safety".

### 403 Error Page

The 403 error page displays a UX-friendly error message and the option to "return to safety".

![403 Error Page](/media/readme/403-error-page.png)

### 404 Error Page

The 404 error page displays a UX-friendly error message and the option to "return to safety".

### 500 Error Page

The 500 error page displays a UX-friendly error message and the option to "return to safety".

## Features Left To Implement

Add a calendar so that users can organise meet ups to exercise or explore nature in a group setting. This adds to the social aspect of this web application and encourages users to engage with others during their activities.

## Languages Used

Python 3.0

CSS

## Libraries, Frameworks, and Programs Used

Django

Github was used for version control to store commit history

Heroku was used to deploy our final project

## Testing

### Validator Testing

Python: No errors were returned when passing through the official Pep8 linter.



<hr>

### Testing and debugging code

I have used Docstrings throughout my code to identify each function and its purpose.

## Bug Fixes

## Deployment

### Heroku Deployment

1. Create a new app in the Heroku dashboard. Choose a name and location for your app.

2. Click the resources tab to add the Heroku Postgres database.

3. Click on the settings tab and reveal config vars. Copy the DATABASE_URL and paste it into the env.py file in your project. Mkae sure that the env.py file is in the .gitignore file.

4. Add a SECRET_KEY both to the env.py file and in the config vars on Heroku.

5. In the Gitpod settings.py file, remove the insecure SECRET_KEY and replace it with the environment variable (SECRET_KEY) that was created.

6. Replace existing DATABASES section in settings.py file with the DATABASE_URL environment variable that is located in the env.py file.

7. Ensure that all static and files have been added to the settings.py file in Gitpod.

8. Add the TEMPLATES_DIR to settings.py file in Gitpod and link it in the TEMPLATES section.

9. Make sure that the project name for the Heroku app has been added as an allowed host in Gitpod.

10. Ensure to create a Procfile and add web: gunicorn activities.wsgi to this file

11. Make sure that the DEBUG flag is set to False in settings.py file in Gitpod

12. Add X_FRAME OPTIONS = 'SAMEORIGIN' to the settings.py file to ensure that the Summernote editor works once the project is deployed.

13. Make sure that all dependencies have been added to the requirements.txt file using the command pip3 freeze > requirements.txt

WARNING: Heroku has halted automatic deployments from Github so the steps to build your Heroku app are as follows...

Using the CLI, enter the following commands to deploy to Heroku

1. Login to Heroku using the command heroku login -i

2. Enter your email address and password

3. Find the relevant app using the command heroku apps

4. Set the Heroku remote using the command heroku git:remote -a <app_name>

5. Add, commit and push to Github using the command git add . && git commit -m "Deploy to Heroku via CLI"

6. Push to both Github and Heroku using the command git push origin main (for Github) and the command git push heroku main (for Heroku)

## Credits

Images etc.

## Acknowledgements

Daisy/Slack/Stack Overflow etc.