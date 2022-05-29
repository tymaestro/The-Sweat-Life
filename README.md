# The Sweat Life

The Sweat Life is a web application that allows users to post activities and interact with other users by commenting on their posts.

## User Stories
<br>

### Logged-Out User
<br>

As a standard (not logged-in) user, I would like to:
<br>

1. View the landing page and know that I'm on a social site for exercise enthusiasts

2. View posts by users

3. Have a unique sign-up option with username and password
<br>
<br>

### Logged-In User
<br>

As a registered (logged-in) user, I would like to:
<br>

1. Have a login option to log in to my previously registered account

2. Create and post my own activities

3. Rate how I felt after my activity

4. View the uploads of other users

5. Like and comment on users' posts

6. Choose a date and time for group activities

7. View the other users who have chosen these time slots

8. Edit my activity

9. Delete my activity
<br>
<br>

## Project Goals

- Create a platform for exercise enthusiasts to come together and share their activities and passion for exercise and the outdoors. This will be achieved through CRUD functionality to create activities (with the ability to both edit and delete the chosen activity) that allow for other users to comment and interact with fellow users of the site.

## Flowchart

![The Sweat Life Flowchart](/media/readme/flowchart/sweatlife-flowchart.png)

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

The agile development of this project used issues in the project environment on [Github](https://github.com/tymaestro/PP4/projects/1)

## Features

### Navbar

The navigation bar gives you access to the activities page as well as an opportunity to either login with a previously created account or create an account via the sign up option.

![Navbar Logged-Out](/media/readme/features/navbar-logged-out.png)

The navigation bar once you are logged in gives you the opportunity to add your own activities as well as log out of your account.

![Navbar Logged-In](/media/readme/features/navbar-logged-in.png)

### Sign Up Page

The sign up page allows you to create an account by providing a username and password for authentication. Creating an account gives you access to extra functionality such as the ability to create, edit, and delete your own activities and comment on the activities of others.

![Sign-Up Page](/media/readme/features/signup-page.png)

### Login Page

As with the sign up page, the login page allows previously registered users to access the extra functionality that having an account provides.

![Login Page](/media/readme/features/login-page.png)

### Logout Page

The logout page allows you to confirm if you are sure you would like to logout

![Logout Page](/media/readme/features/sign-out-page.png)

### Home Page

The home page welcomes users to the site and gives information on the concept behind the site and encourages you to sign-up to gain access to cool features where you can post your own activities and comment on the posts of other users.

![Home Page]()

### Activities Page

This page presents an ordered and paginated list of activities posted by users. Visible is the title and excerpt of the activity. These activities are public but an account must be created to leave a comment or create your own activities. You can also search for a specific activity using the search bar at the top right of the page.

![Activities Page (logged-out)](/media/readme/features/activities-logged-out.png)

### Activities Page (logged-in)

Note that the extra functionality such as edit and delete are user-specific so the buttons only display on the posts the user has created themselves and not the posts of others.

![Activities Page (logged-in)](/media/readme/features/activities-logged-in.png)

### Activity Detail Page

The activity detail page presents the selected activtiy in detail including its title, excerpt, content and comments left by users.

![Activity Detail Page](/media/readme/features/activity-detail.png)

### Create Activity Page

The create activity page displays a form where you can enter a title, excerpt and the content of your activity.

![Create Activity Page](/media/readme/features/create-activity-page.png)

### Create Comment Page

The create comment page is shown as a form where you can leave a comment on the selected post.

![Create Comment Page](/media/readme/features/create-comment-page.png)

### Edit Activity Page

The edit activity page displays your activity as a form, pre-populated with the details and content previously provided so that you can edit your post.

![Edit Activity Page](/media/readme/features/update-activity-page.png)

### Delete Activity Page

The delete activity page displays a warning (defensive programming) to ensure that you are certain of your choice to delete the chosen activity and are aware of the consequences.

![Delete Activity Page](/media/readme/features/delete-activity-page.png)

### 400 Error Page

The 400 error page displays a UX-friendly error message and the option to "return to safety".

### 403 Error Page

The 403 error page displays a UX-friendly error message and the option to "return to safety".

![403 Error Page](/media/readme/features/403-error-page.png)

### 404 Error Page

The 404 error page displays a UX-friendly error message and the option to "return to safety".

### 500 Error Page

The 500 error page displays a UX-friendly error message and the option to "return to safety".

## Features Left To Implement

- Add a calendar so that users can organise meet ups to exercise or explore nature in a group setting. This adds to the social aspect of this web application and encourages users to engage with others during their activities.

- Add functionality to delete comments

## Languages Used

Python 3.0

CSS

HTML

## Libraries, Frameworks, and Programs Used

Django.

Github was used for version control to store commit history.

Heroku was used to deploy our final project.

Balsamiq was used for wireframes.

FontAwesome for social media icons in footer.

## Testing

### Validator Testing

Python: Several "line too long" errors were returned when passing through the official [Pep8](http://pep8online.com/) linter.

These refer to:

- In settings.py there are 5 "line too long" errors related to Django's AUTH_PASSWORD_VALIDATORS and Cloudinary storage.

- In views.py there are 2 "line too long" errors related to Django MixIn imports.

HTML: No errors were returned when passing through the official [W3C](https://validator.w3.org/) validator.

CSS: No errors were returned when passing through the official [Jigsaw](https://jigsaw.w3.org/css-validator/) validator.

<hr>

### HTML Validation

[Index Page](/media/readme/htmlvalidation/index-valid.png)

[400 Error Page](/media/readme/htmlvalidation/400-error-valid.png)

[403 Error Page](/media/readme/htmlvalidation/403-error-valid.png)

[404 Error Page](/media/readme/htmlvalidation/404-error-valid.png)

[500 Error Page](/media/readme/htmlvalidation/500-error-valid.png)

[Activities Page](/media/readme/htmlvalidation/activities-valid.png)

[Activity Detail Page](/media/readme/htmlvalidation/activity-detail-valid.png)

[Create Activity Page](/media/readme/htmlvalidation/create-activity-valid.png)

[Create Comment Page](/media/readme/htmlvalidation/create-comment-valid.png)

[Delete Activity Page](/media/readme/htmlvalidation/delete-activity-valid.png)

[Login Page](/media/readme/htmlvalidation/login-valid.png)

[Logout Page](/media/readme/htmlvalidation/logout-valid.png)

[Sign-In Page](/media/readme/htmlvalidation/sign-in-valid.png)

[Update Activity Page](/media/readme/htmlvalidation/update-activity-valid.png)

<hr>

### CSS Validation

[CSS Page](/media/readme/cssvalidation/css-valid.png)

<hr>

### Python Validation

#### Activities Project

[Activities URLS Page](/media/readme/pythonvalidation/activities-urls-valid.png)

[Activities ASGI Page](/media/readme/pythonvalidation/asgi-valid.png)

[Activities Settings Page](/media/readme/pythonvalidation/settings-valid.png)

[Activities WSGI Page](/media/readme/pythonvalidation/wsgi-valid.png)

<hr>

#### Posts App

[Posts Admin Page](/media/readme/pythonvalidation/admin-valid.png)

[Posts Apps Page](/media/readme/pythonvalidation/apps-valid.png)

[Posts Forms Page](/media/readme/pythonvalidation/forms-valid.png)

[Posts Models Page](/media/readme/pythonvalidation/models-valid.png)

[Posts URLS Page](/media/readme/pythonvalidation/posts-urls-valid.png)

[Posts Views Page](/media/readme/pythonvalidation/views-valid.png)

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

[Cloudinary](https://cloudinary.com/) for cloud storage of images.

[Pexels](https://www.pexels.com/) to find and download images.

[Codemy](https://www.youtube.com/c/Codemycom) for a better understanding of a simplified views structure.

[Bootstrap](https://getbootstrap.com/) for some layout and styling features.

## Acknowledgements

A very big thank you to my mentor Daisy McGirr who gave me very helpful feedback and was very encouraging during our mentor sessions.

Also, a big thank you to the Slack community over the course of this entire module.

Stack Overflow for any troubleshooting over the course of this project.

Django documentation for setup, use of allauth and insight into class-based views and forms.