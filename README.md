# FAI Football Academy Ireland

FAI is an online ecommerce shop that allows users to purchase football gear and accesories and sign up for a yearly payed subscription to the academy where the user will have access to all the training sessions and opt in to going to training and see other academy players profiles.

you can find the live site HERE

# Contents

1. Summary
2. UX
    * Strategy
    * Scope
    * Structure
    * Skeleton
    * Surface
3. Features
    * Existing Features
    * Features left to implement
4. Bugs
5. Technologies used
6. Testing
7. Deployment
   * Github Pages
   * heroku
8. Credits
   * Content
   * Acknowledgements

# Summary

FAI is an online ecommerce shop that allows users to purchase football gear and accesories and sign up for a yearly payed subscription to the academy where the user will have access to all the training sessions and opt in to going to training and see other academy players profiles.

# UX

## App Goals

## Strategy

### New site user's goals:

1. As a new visitor to the website I want to navigate the site with ease and no confusion.

2. As a new site user, I want to be able to browse and search for products

3. As a new site user, I want to be able to view the details of individual products

4. As a new site user, I want to be able to understand the intent of the page

5. As a new site user, I want to understand easily how to navigate the page and access the facilities provided

6. As a new site user, I want to be able to make a purchase without needing to create a profile

7. As a new site user, I want to be able to easily create an academy profile

8. As a new site user, I want to be able to view training sessions and have the option to attend or unattend.

9. As a new site user, I want to be able to view trials and see if i have been selected for a trial or not.

10. As a new site user, I want to be able to sort products on a page

11. As a new site user, I want to be able to sort by specific categories

12. As a new site user, I want to be able to amend the items in my bag including quantities and removing them entirely

 
### player site user's goals:

1. As a returning site user, I want to be able to log in and out.

2. As a returning site user, I want to be able to recover a forgotten password.

3. As a returning site user, I want to be able to view my trials. 

4. As a returning site user, I want to be able to view my training.

### Admin user's goals

1. As a site owner, I want to be able to create, edit and delete products.

2. As a site owner, I want to be able to create training sessions and see who is attending.
 
3. As a site owner, I want to be able to create delete and edit training sessions.

4. As a site owner, I want to be able to create delete and edit trials.
 
5. As a site owner, I want to be able to create trials and pick which players will attend.

## Scope

### Functional requirements:

#### For ease of use:

* Navigation bar which is simple and easy to navigate
* Search button and dropdown serach bar nav
* Button for academy profile
* Small navbar sm for phone size 

### Content requirements:

### To ensure the site is visually appealing and to draw the user's eye:
* clear colours 
* images of products
* Clear and constructive colours used for the page to be easy for the user to instinctively navigate.

### Foe usability 

* For links to be clear and for the page to be constructed in a way which is instructive enabling the user to instinctively navigate the page

## Structure

### Interaction design:

* User friendly interface to ensure usability and to encourage the user to return
* Ability to exit all popups with an x to exit and close the popup.
* Responsive and visible buttons which change on hover to provide user feedback as they navigate the site

### Information Architecture:

* Navigation bar at the top of the page
* Responsive navigation bar - adjusting for mobile for ease of use
* Responsive forms to ensure they fit within the designated spaces, no matter what device is being used or the size of the screen
* Mainly all features appropriate size and responsive for mobile and desktop viewing
* Products page is fully responsive and all pics are the same size


## Skeleton

### wireframe
Please click the below link to view the wireframe
* - [Wireframes]()

## Surface

### The intention of the website is to be clean, crisp and clear

* The font family choosen was a mixture of Ubuntu Roboto and open sans 
* The colour scheme chosen was a mix of white and black with hints of red and green in the images, Which makes the site look sports related and brings a professional look to the website, Ive also derkend all my images to allow any text infront to be seen clearly with no confucion or lack of clarity.
* The cover image was chosen as I felt it represented Football really well and also looked well with the rest of the website and due to the blur it allows it not to stck out to much and take over from the text and other features of the website.  


# Plan

## initial plan

* Initialy i had chosen to create a player profile and allow users to create a profile ontop of thier register but later decided not to go down this route as it was too much too late and I had to get allot of other things to do in the project 

## Changes to plan

* I changed to a less intricate plan where a user would sign in and browse training and trials and create comments instaed of creating a personal profile where this can be done.

# Features

## Database model / app structure

- [Database model]()

## Existing Features

| Feature        | Detailes           | 
| ------------- |:-------------:| 
| login     |     The user can register and log into their own account with personalised features   |      
| logout     |    There is a log out functionality on the page - this is especially important for users of a shared device   |  
| register  |   There is a register functionality on the page |
| add product     |     Superusers can sign in and add new products|
| edit product     |      Superusers can sign in and edit existing products|
| delete product     |    Superusers can sign in and delete a product|
| add training session  |   Superusers can sign in and add new training session  |
| edit training session    |   Superusers can sign in and edit existing training session|
| delete training session |   Superusers can sign in and add new training session  |                    
| add trial |  Superusers can sign in and add new trials            |     
| edit trial |   Superusers can sign in and edit existing trials    |
| delete trial |   Superusers can sign in and delete a trial      |     
| create comment|   Users can create a commment in training sessions|
| view comments |   Users can view all comments and see when they were created|
| select player for trial |  superusers can select players for trials|
| view trial if selected |  users can view a trial if they have been selected for that trial|
| search product |  users can search for a product|
| add product to bag|  users can add products to thier bags|
| checkout | Users can checkout and pay for thier product|
| unattend training | Users can Unattend a training session|
| attend training | Users can attend a training session |
        


## Features left to implement

| Feature        | Detailes           | 
| ------------- |:------------:| 
| create profile|  A player could sign in then view a profile which they could edit |
|view my training| A player could view all of the training sessions he has chosen to go to in a profile |
| view my trials | A player could view all of the trails they have been selected for in a profile |

# Bugs

| Feature        | Detailes     | 
| ------------- |:-------------:| 
| An error occured when attempting to deploy the site to heroku with Collect Static files | I had to set PutObject and DeleteObject in my AWS S3 bucket.


# Technologies Used

* HTML
* CSS
* Python
* Git
* github
* Google Chrome
* Heroku
* Jinja
* Bootstrap
* JavaScript
* Google fonts
* Gitpod
* Django
* Favicon
* Json
* AWS


# View

* It is reccomended to view this application at a resolution ??

## Testing


### New site user's goals:

1. As a new visitor to the website I want to navigate the site with ease and no confusion.
   * A navbar with links clearly labeled and working is present throughout the website and is shown in a clearer way in the phone size in bothe the academy and shop.

2. As a new site user, I want to be able to browse and search for products
   * A button is present on the shop home page wgere a user can click to view products, they can also click all products or products in the nav which will open a products page showing all products on the website, A user can also use the search bar to serach for any products on the website. 

3. As a new site user, I want to be able to view the details of individual products
   * In the products page you can click on any product this will dring you to that products details page where you can pick your size and add the product to your bag.

4. As a new site user, I want to be able to understand the intent of the page
   * there is a toasts system accross the full app where when a task is completed or underway the user is shown an error allert or info message which lets them know the intent of the page and what functions they are doing.

5. As a new site user, I want to be able to make a purchase without needing to create a profile
   * A user can add a product to thier bag and then checkout , fill in thier details and purchase a product without having to create an account with fai.

6. As a new site user, I want to be able to easily create an academy profile
   * There is an academy button in the shop page where a user can either sign in or register for the academy, this will bring the user to a register page in the academy part of the website where they can register with FAI.

7. As a new site user, I want to be able to view training sessions and have the option to attend or unattend.
   * When a user has successfully created an account and signed in they can view all the training sessions and view them. The user can also click the attend button to attend the sesssion or click the unattend button to unattend the session.

8. As a new site user, I want to be able to view trials and see if i have been selected for a trial or not.
   * A user has to be selected by an admin to have access to a trial, If so a user can then view that trial and see when it is.

9. As a new site user, I want to be able to sort products on a page
   * A user can click to sort products on the products page in many different orders 

10. As a new site user, I want to be able to sort by specific categories
   * A user can click to sort products on the products page by category

11. As a new site user, I want to be able to amend the items in my bag including quantities and removing them entirely
   * A user can remove a product from thier bag and add more quantity or less quantity if needed.

 
### player site user's goals:

1. As a returning site user, I want to be able to log in and out.

2. As a returning site user, I want to be able to recover a forgotten password.

3. As a returning site user, I want to be able to view my trials. 

4. As a returning site user, I want to be able to view my training.

### Admin user's goals

1. As a site owner, I want to be able to create, edit and delete products.

2. As a site owner, I want to be able to create training sessions and see who is attending.
 
3. As a site owner, I want to be able to create delete and edit training sessions.

4. As a site owner, I want to be able to create delete and edit trials.
 
5. As a site owner, I want to be able to create trials and pick which players will attend.

## Performance testing:

* 

# Git hub pages

1. Create a new repository or access an existing repository
2. Click the green Gitpod button to launch the project in Gitpod
3. Create an index.html file
4. Add the file to the staging area using the git add Functional
5. Commit the file using the git commit function, adding an appropriate commentary
6. Push the file to GitHub using the git commit and git push functions
7. Refresh your GitHub repository and click the 'Settings' tab
8. Scroll to the GitHub Pages section and select a publishing source
9. Click 'Save'
10. Click the URL created within the Settings - GitHub Pages section

### To clone the repository for local deployment:

1. On the main page of the repository, click the down arrow Code button
2. Click the download icon under the relevant section to clone with either HTTPS, SSH or 3GitHub CLI
4. In Git Bash, change the current directory to the location you want the directory to be stored
5. Type git clone and then paste the URL you copied in step 2
6. An example for HTTPS: git clone ******************************************** 
7. Press enter - that's it, your clone has been completed!

### Fork repo

1. Navigate to the main page of the repository you wish to fork
2. Click the Fork button on the top right hand side of the page

# Deployment


## Heroku

To deploy the app to Heroku from its GitHub repository, the following steps were taken:

1. From the GitPod terminal, create requirements.txt and Procfile using these commands:

     ```pip3 freeze --local > requirements.txt
     echo web: python app.py > Procfile
     ```

2. Push these files to GitHub
3. Log In to Heroku
4. 4.Select Create new app from the dropdown in the Heroku dashboard
5. Choose a unique name ('player_link') for the app and the location nearest to you
6. Go to the Deploy tab and under Deployment method choose GitHub
7. In Connect to GitHub enter your GitHub repository details and once found, click Connect
8. Go to the Settings tab and under Config Vars choose Reveal Config Vars
9. Enter the following keys and values, which must match those in the env.py file created earlier:

| Key        | Value           | 
| ------------- |-------------| 
| IP   | 0.0.0.0 | 
| PORT     | 5000 | 
| SECRET_KEY     | app secret key  | 
| MONGO_URI     | mongodb+srv://root:dsxigyzwsao0sozm@myfirstcluster.n0en1.mongodb.net/player_link?retryWrites=true&w=majority | 
| MONGO_DBNAME     | player_link | 

10. Go back to the Deploy tab and under Automatic deploys choose Enable Automatic Deploys
11. Under Manual deploy, select master and click Deploy Branch
12. Once the app has finished building, click Open app from the header row of the dashboard

## Credits

### Acknowledgements

* My mentor Antonio Rodriguez who has been great help with guidance and support throughout the project
