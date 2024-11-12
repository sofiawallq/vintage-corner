# Vintage Corner



The live website can be seen [here]()

![printscreen responsive website]()


## Table of content
- [UX/UI Design](#uxui-design)
  - [User Stories](#user-stories)
  - [Wireframes](#wireframes)
  - [Colour scheme](#colour-scheme)
  - [Project Planning](#project-planning)
    - [Agile methodologies](#agile-methodologies)
    - [Database design](#database-design)
- [Features](#features)
  - [Existing features](#existing-features)
  - [Header](#header)
  - [Navigation menu](#navigation-menu)
  - [Landing page](#landing-page)
  - [Contact page](#contact-page)
  - [Register account/login page](#register-accountlogin-page)
  - [Footer](#footer)
  - [Potential future features](#potential-future-features)
- [Technologies used](#technologies-used)
  - [Languages](#languages)
  - [Database](#database)
  - [Frameworks](#frameworks)
  - [Libraries & Additional Programs/Software/Tools](#libraries--additional-programssoftwaretools)
- [Manual Testing](#manual-testing)
  - [Responsivness](#responsivness)
  - [Browser compability](#browser-compability)
  - [Validator testing](#validator-testing)
  - [User Story testing](#user-story-testing)
  - [Bugs](#bugs)
- [Deployment](#deployment)
  - [Forking](#forking)
  - [Cloning](#cloning)
  - [Deployment to Heroku](#deployment-to-heroku)
- [References/credit](#referencescredit)
  - [Content](#content)
  - [Media](#media)


## UX/UI Design



### User Stories

An agile approach was used to initialize the project - Epics to set the main structure for the user stories that needed to be written, and to give me the bigger picture of the project. After the epics were set I wrote all the user stories and gave them labels to identify the must-haves, the should-haves, the could-haves and the wont-have - all in line with the MoSCoW prioritazion method. Every user story that I would work with then got some Acceptance Criterias and Tasks make their purpose even clearer.


I ended up with a total of 25 User Stories to work with in the end, the majority o them made it into

some of them contain acceptance criterias about size and quantity, which I think are vital to a general online store but in this case that criteria isn't aktuell since very item only exist in one exemplar och the store doesn't sell clothes at this point.

![printscreen user story]()


Below are the epics and the Stories I ended up with. If they made it all the way to the end or need more work I will discuss further down in the [User Story testing](#user-story-testing) section. 


__EPIC:__


__EPIC:__
 

__EPIC:__


__EPIC:__


__EPIC:__


__EPIC:__


### Wireframes

Wireframes for both the mobile design and larger devices such as tablets and computers were made using [Balsamique](https://balsamiq.com/). The apporach was as mentioned a simple but straight forward design and almost every view got its own wireframe to make the code process as simple and effective as possible, since the design was already drawn out. I really loved the process and even though I made some changes to some pages along the way, due to it not looking as I imagined when for example responsivness came into the picture - I kept all of the wireframes in its original state as a reference.

Below are some examples:



There were 18 wireframes made in total, which can all be found [here]().

As some might notice there are no wireframes for the reviews page, since this came about later in the project when I felt the need for more custom models and more interactive features on the site. 


### Colour scheme



### Project planning

At first I set up pretty much the same structure as the Boutique Ado project, with multiple static folders for CSS beloning to different apps, but after a while I just felt that it made the structure more messy since I am the only one working on the project. I see the value when multiple people are involved, but in this project it just felt redundant.




### Agile methodologies

- Kanban board - I used the Project Board in GitHub for the planning of the Project. Issues were created as User Stories with Acceptance Criterias belonging to each User Story. The User Stories were also assigned with some tasks, to clarify for myself what each User Story demanded of me. As discussed above I had to come back to my Project board and redo plus add some stories, but this just meant that I learned the value of a good Agile approach even more. 

As I love working on the design of a web page it's easy to put way to much time on that part, so the User Stories really helped me to focus on the functionality of the project first and foremost.

- Epics - I really understand the value of Epics for larger projects, to give a better overview of the projects user stories and further prioritize the work process. But they seem a little over-ambitious for a project of this size, although they work well with my brain.

- MoSCoW Prioritization - The User Stories are labeled with one of the following four categories, all according to the MoSCow prioritization methodology:

  - Must Have: Features and requirements that are absolutely neccessary for the product to function and for the website to fulfill its purpose. These User Stories have the highest priority. 

  - Should Have: Important features that should be included if possible, but they are not critical for the website to function.

  - Could Have: Desirable features that can be added if there is enough time and resources.

  - Won’t Have: Features that will not be included in the project at this point, but might be a desirable feature in future development. 

![printscreen moscow open issues]() ![printscreen moscow closed issues]()



### Database Design


![printscreen root directory]()


__Entity Relationship Diagrams(ERD)__


![printscreen entity relationship diagram]()


## Features

### Existing features


### Header


![printscreen header]()

The mobile version containts pretty much the same features but presented in a responsive way, fitting into different screen sizes. 

![printscreen header mobile version]()


### Navigation menu


![printscreen web page navigation menu]()

With the help of Bootstrap and some custom CSS styling the navigation menu becomes a drop down feature on smaller devices. On smaller screens the social media icons aren't visible to the visitor in the navigation menu - so that the menu doesn't take up to much space. Instead they are only visible in the footer area on smaller screens. 

![printscreen drop down navigation menu]()


### Home page & Footer


### Product list page

Sort by option by either price, name or news. at the moment the news doesn't really change much since 

### About page


### Contact page

On the Contact page the user can find all the information they can possibly need if the wan't to get in touch with 

Phone number, email adress and the restaurants adress is all there, in case somebody want's to send them a letter.

![printscreen contact information]()


![printscreen contact form]()


### Register account/sign in 


### Personal profile page


### Shopping cart view


### Checkout view


### Potential future features


## SEO/Meta optimization

Searched different vintage stores online to see what keywords they use, 

quite hard since many companies load in tags from companies so they cannot be viewed in the head when you use DevTools

also learned about the social media meta tags

meta keys will be updated according to what items are in the shop

## Facebook page

## Technologies used

### Languages
- HTML5
- CSS3
- JavaScript
- Python


### Database
- CI Database URL (Postgres) - used to store all data.


### Frameworks
Django - main framework for a secure and resuable development process.


### Libraries & Additional Programs/Software/Tools
- Bootstrap - used for some of the front-end design. Mainly to make the page responsive and make use of Bootstraps grid system. It was accompanied by some custom CSS since I'm not all that familiar with Bootstraps many fuctions and add ons just yet.
- Balsamique - used to create all wireframes for the project
- Django All Auth - used for user registration and authentication
- Django Crispy Forms - used for all forms on the page, mainly to control their behaviour and give them the same look for a good UX
- Django Summernote - used as the editor for the Admin panel
- dj-database-url - used to connect Django to database via URL
- Favicon - used for finding a tab icon, which also became part of the logo for the restaruant project
- Font Awesome - used for social media icons 
- GitHub - used to store all the code and the Projects Kanban board
- GitPod - used as the IDE during development
- Google Fonts - used for custom fonts on the entire page
- Gunicorn - used as the server to run Python code/Django on Heroku platform
- Heroku - used as the platform to deploy the project
- Lucidchart - used to create the Entity Relationship Diagrams, also known as ERD
- Pexels - used to find suiting images for all pages of the site
- Psycopg - PostgreSQL adapter for Python
- Whitenoice - used to handle the static files for deployment

Images are hosted in the projects static directory for this project, but in the future I want to work Cloudinary.


## Manual testing

The manual testing consisted of not only the things listed below, but the testing also meant asking everybody I know to test the website and all its functions - such as 

### Responsivness 

Mainly thanks to Bootstrap the page is responsive on all devices - from mobile phones to tablets, laptops and larger screens. It reaches a max-width on larger devices as to not look to stretched out and looks alright on even the smallest mobile screens. I've asked friends and family to try it out on different devices to get as many opinions in as possible. 

### Browser compability

The project has been tested on different browsers such as: Google Chrome, Safari, Microsoft Edge and Mozilla Firefox. It looks and functions pretty much the same on all browsers. 

### Validator testing

- HTML - through the official W3C validator. 

![printscreen html validator]()

- CSS - through the official Jigsaw validator. No issues came back when i ran the code through the CSS validator. 

![printscreen css validator]()

- JavaScript - the JavaScript check in JSHint came back with 

![printscreen javascript validator]()

- Python - PEP8 Python Validator

There were quite a few files to run throught the PEP8 validator,

![printscreen python validator]()

When testing the page using Lighthouse for Chrome, 

![printscreen lighthouse]()


### User Story testing

The User Story testing has been performed throughout the development. When building the site I moved the Stories I was working on into the "In Progress" column on my Kanban-board, and then checked that every acceptance criteria and task was fulfilled before moving it into the "Done" column. As you can see there are still Stories left in the "In progress" column, due to the fact that some criterias have been met, but not all of them. The project is still functional but I don't want to move them into the Done column until the criterias are fully met. 


Along with the User Stories regarding some admin features, there are stories about a review page that haven't made it out of the "Todo" column yet. These are really good Stories to work with in the future 


![printscreen kanban board]()


### Bugs



## Deployment

This project was deployed using Heroku.

### Forking

- Navigate to the GitHub repository.
- On the top right hand side, click the button named "Fork".
- A new page named "Create new Fork" will open up, where you can choose to edit hte name of the project.
- Click on "Create Fork" at the bottom of the page. 
- Now a copy of the project will appear in your list of repositories.


### Cloning

- Navigate to the GitHub repository.
- Click on the "Code" tab at the top of the repository and copy the URL for web that appears. 
- Open up the terminal in a code editor of your choice and change the current working directory to a new one you will use to clone the repository. 
- Type in "git clone" in the terminal, paste in the copied URL and press "Enter".


### Deployment to Heroku

1. Create and set up the Heroku app
- Login to your Heroku account and navigate to the dashboard.
- Click on the "New"-button to create a new app.
- Give the app a unique name.


2. Ready your code for deployment in your Code Editor.
- Install a production ready webserver for Heroku such as gunicorn by writing the following command in your terminal: pip3 install gunicorn~=20.1.0.
- Add gunicorn==20.1.0 to the requirements.txt file with the following command in your terminal: pip3 freeze --local > requirements.txt.
- Create a file called Procfile in the root directory of your project.
- Inside the Procfile declare that the web process followed by the command to execute your Django project: web: gunicorn yourprojectsname.wsgi
- Open the projects settings.py file an set DEBUG=False
- In settings.py add '.herokuapp.com' to the ALLOWED_HOSTS list.
- Git add, git commit and git push to GitHub so that all files are up to date in your repository.


3. Ready your database for deployment
- Create an env.py file and add the following:
import os
os.environ.setdefault( "DATABASE_URL", "")
os.environ.setdefault("SECRET_KEY", "your__secret_key")
- Check to se that your env.py file is added to the .gitignore file. 
- Make sure your settings.py has this code in it: SECRET_KEY = os.environ.get("SECRET_KEY").
- Click on the "Settings" tab and navigate to the "Reveal Config Vars" section. 
- Add a SECRET_KEY value to Herokus Config Vars.


4. Deployment with static files
- Install Python package for whitenoise with the command: pip3 install whitenoise==6.7.0
- Add whitenoise to your requirements.txt file with the command: pip3 freeze --local > requirements.txt
- Add 'whitenoise.middleware.WhiteNoiseMiddleware' to the list of MIDDLEWARE in settings.py below Django SecurityMiddleware.
- In settings.py add a path to staticfiles in this way: STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles')
- Run python3 manage.py collectstatic in the terminal to collect the static files and when asked to choose yes or no, type "yes" in the terminal.
- Check what Python version is used in your development environment and look up the supported runtime closest to your Python version. 
- Create a runtime.txt file in your apps root directory and add the Python version from the list of supported runtimes, in a format like this: python-3.12.5.


4. Deploy on Heroku
- Click on the "Deploy" tab on your Heroku Dashboard.
- Under the "Deploy method" section choose to Connect to GitHub, depending on earlier access you might be asked to authenticate using GitHub.
- Choose the projects repository in the list that apperas when you start to type in the search box. 
- Start a manual deployment of the main branch by scrolling to the bottom of the Deploy-page and click on "Deploy branch".
- Click "Open app" to view your deployed project. 
- Open the "Resources" tab and switch to Eco Dyno to keep the project up and running. 


## References/credit


### Content


The Code Institute code along project "Boutique Ado" has been extremly helpful when it comes to setting up the structure for the project and I have returned to it again and agian throughout the development to make sure i use the right commands, deploy in the right way and so on. 
The models we worked with in that project was of course inspiration for when designing my own 

As always [Stack Overflow](https://stackoverflow.co/) has been my go to place everytime I've googled a piece of code for troubleshooting. 

Product info mainly from Wikipedia


### Media

[Pexels.com](https://www.pexels.com/)
[Unsplash.com](https://unsplash.com/)
[Favicon](https://favicon.io/emoji-favicons/)