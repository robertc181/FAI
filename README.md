# FAI Football Academy Ireland

FAI is an online ecommerce shop that allows users to purchase football gear and accesories and sign up for the FAI academy where the user will have access to all the training sessions and attend or unattend training and hopefully get selected for a trial in the trials sections of the site. A player can alse speak with all the other players which are attending and unnatending a training session in the comments section.

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

# UX

## App Goals

## Strategy

### New site user's goals:

* As a new visitor to the website I want to navigate the site with ease and no confusion.

* As a new site user, I want to be able to browse and search for products

* As a new site user, I want to be able to view the details of individual products

* As a new site user, I want to be able to understand the intent of the page

* As a new site user, I want to understand easily how to navigate the page and access the facilities provided

* As a new site user, I want to be able to make a purchase without needing to create a profile

* As a new site user, I want to be able to easily create an academy profile

* As a new site user, I want to be able to view training sessions and have the option to attend or unattend.

* As a new site user, I want to be able to view trials and see if i have been selected for a trial or not.

* As a new site user, I want to be able to sort products on a page

* As a new site user, I want to be able to sort by specific categories

* As a new site user, I want to be able to amend the items in my bag including quantities and removing them entirely

 
### player site user's goals:

* As a returning site user, I want to be able to log in and out.

* As a returning site user, I want to be able to recover a forgotten password.

* As a returning site user, I want to be able to view my trials. 

* As a returning site user, I want to be able to view my training.

### Admin user's goals

* As a site owner, I want to be able to create, edit and delete products.

* As a site owner, I want to be able to create training sessions and see who is attending.
 
* As a site owner, I want to be able to create delete and edit training sessions.

* As a site owner, I want to be able to create delete and edit trials.
 
* As a site owner, I want to be able to create trials and pick which players will attend.

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
* A toasts system which allows users to be notifued as they construct and lay out tasks accross the site with a simple alert at the top right of the page.

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
* - [Wireframes](https://github.com/robertc181/FAI/tree/main/wireframes)

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

| syntax        | description           | 
| ------------- |:------------:| 
| create profile|  A player could sign in then view a profile which they could edit |
|view my training| A player could view all of the training sessions he has chosen to go to in a profile |
| view my trials | A player could view all of the trails they have been selected for in a profile |

# Bugs

| Feature        | Detailes     | 
| ------------- |:-------------:| 
| An error occured when attempting to deploy the site to heroku with Collect Static files | I had to set PutObject and DeleteObject in my AWS S3 bucket. |
| When a purchase is made a user is shown a confirmation toast which says that hey will recive a confirmation email | This email has to be manually sent by the stripe profile admin this is an example of the email sent, [email example sent to my email]()  |


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
    * A user can log in and out from the academy part of the site by clicking the profile button in the nav and chooseing weather to log out or log in.

2. As a returning site user, I want to be able to recover a forgotten password.
   * If a user has forgotten thier password they can click the forgot password button with will alert the user to enter in thier email address and a change password email will be sent to thier email where they can clik on the link to create a new password and create one.

3. As a returning site user, I want to be able to view my trials. 
   * As a user you can sign in click on trials and see all the trials that you have been selcetd for and not selected for and click into the trials you have been selected for.

4. As a returning site user, I want to be able to view my training.
   * As a user you can sign in click on training and see all the training sessions that are on and click to view the session and click to attend or unattend the session you can also see any comments that have been ceated or create your own comment.
### Admin user's goals

1. As a site owner, I want to be able to create, edit and delete products.
   * A site owner can click product management in the shopfront nav and then click add product where he is brought to the add product page where he can add a new product , when this is finished an dthe product has been created the site owner is brought to the products page where he can view his new product, the admin can go into the product and click to either edit the product or delete the product.

2. As a site owner, I want to be able to create training sessions and see who is attending.
   * A site owner can click training management in the academy nav where he is brought to the add training session page where he can add a new training session, The admin can also view which players are attending the training session.
 
3. As a site owner, I want to be able to create delete and edit training sessions.
   * A site owner can go into the product and click to either edit the product or delete the product.

4. As a site owner, I want to be able to create delete and edit trials.
   * A site owner can click trial management in the academy nav where he is brought to the add trial page where he can add a new trial , a site owner can also delete and edit a trial from the trials page.
 
5. As a site owner, I want to be able to create trials and pick which players will attend.
   *  The admin can also select which player will be attending the trail in the edit trail page or the add trial page, 

## Performance testing:

1. Tested website responsiveness using  Google Dev Tools by inspecting the page and setting the size to responsive mode
      - Results: The website is responsive to all device sizes without any unnecessary x-scroll
      
2. Tested the image size to ensure no image is to large and impacting the website loading times. I used the Google Dev Tools - Network
      * Results: The site loading time is appropriate. The total website loading time is 1.1s is acceptable
      
3. Tested the images on the all products page using Google Dev Tools - Lighthouse
      * Results: It was recommended that the images used were of a smaller size to improve download speed and cause less data consumption.
      * All HTML and CSS were tested using https://jigsaw.w3.org/css-validator/validator
      * All but the templates resulted in errors that the Lang Doctype and Title were missing. This was to be expected as the details were being extended from the base template to       did not need to be added
      * All HTML pages resulted in errors where the Jinja template language was used creating a parse error
      * None of these are actual errors within the code
      * Some CSS errors were observed. However, the items highlighted were added intentionally to the CSS files and did create the desired affect
      
4. Tested the website on the Google Chrome browser Version 89.0.4389.90 (Official Build) (64-bit)
      * Results: The website was responsive and the elements performed in the way they were intended to
      
5. Tested the website on the Microsoft Edge browser Version 89.0.774.63 (Official build) (64-bit)
      * Results: The website was responsive and the elements performed in the way they were intended to
      
6. Tested the website on the Firefox browser Version 82.0.3 (64-bit)
      * Results: The website was responsive and the elements performed in the way they were intended to
      
7. Tested adding items to the bag
      * Results: Successfully able to add an item to the bag
      
8. Tested increasing the quantity of items in the bag
      * Results: Successfully able to increase the quantity of an item in the bag
      
9. Tested removing items from the bag
      * Results:Successfully removed an item from the bag
      
10. Tested the stripe process using 4242 4242 4242 4242 which should be successful
      * Results: Order completed successfully and the confirmation page appears
      
11. Tested the stripe process using 4000 0027 6000 3184 which will request authorisation - completed authentication
      * Results: Authorisation screen appears then the order completed successfully and the confirmation page appears
      
12. Tested the stripe process using 4000 0027 6000 3184 which will request authorisation - selected declined
      * Results: The payment fails and the user is returned to the checkout page. The appropriate error message appears
      
13. Tested the profile page and that the orders placed above show correctly
      * Results: The two successful orders made during testing appeared on the right hand side of the screen


### To clone the repository for local deployment:

1. On the main page of the repository, click the down arrow Code button
2. Click the download icon under the relevant section to clone with either HTTPS, SSH or 3GitHub CLI
4. In Git Bash, change the current directory to the location you want the directory to be stored
5. Type git clone and then paste the URL you copied in step 2
6. An example for HTTPS: git clone ************
7. Press enter - that's it, your clone has been completed!

### Fork repo

1. Navigate to the main page of the repository you wish to fork
2. Click the Fork button on the top right hand side of the page

# Deployment


## Heroku

### How to deploy to Heroku

To deploy the app to Heroku from its GitHub repository, the following steps were taken:

1. From the GitPod terminal, create requirements.txt and Procfile using these commands:
      ```
     pip3 freeze --local > requirements.txt
     echo web: python app.py > Procfile
     ```
3. Push these files to GitHub
4. Log In to Heroku
5. Select Create new app from the dropdown in the Heroku dashboard
6. Choose a unique name ('recipe-nation') for the app and the location nearest to you
7. Go to the Deploy tab and under Deployment method choose GitHub
8. In Connect to GitHub enter your GitHub repository details and once found, click Connect
9. Go to the Settings tab and under Config Vars choose Reveal Config Vars
10. Enter the following keys and values, which must match those in the settings.py file:

| Key        | Value           | 
| ------------- |-------------| 
| AWS_ACCESS_KEY_ID   | AWS_ACCESS_KEY_ID | 
| AWS_SECRET_ACCESS_KEY     | AWS_SECRET_ACCESS_KEY | 
| DATABASE_URL     | DATABASE_URL  | 
| EMAIL_HOST_PASS     | EMAIL_HOST_PASS | 
| EMAIL_HOST_USER     | EMAIL_HOST_USER | 
| SECRET_KEY     | SECRET_KEY | 
| STRIPE_PUBLIC_KEY     | STRIPE_PUBLIC_KEY | 
| STRIPE_SECRET_KEY     | STRIPE_SECRET_KEY | 
| STRIPE_WH_SECRET     | STRIPE_WH_KEY | 
| USE_AWS     | True | 

10. Go back to the Deploy tab and under Automatic deploys choose Enable Automatic Deploys
11. Under Manual deploy, select master and click Deploy Branch
12. Once the app has finished building, click Open app from the header row of the dashboard

## Credits

| image       | Used For |
| ------------- |-------------|
| ![image (5)](https://user-images.githubusercontent.com/72562765/143719105-c44f2509-0872-43b3-a111-61dedc2669bf.png) | background image for trials and training |
|  ![image (1)](https://user-images.githubusercontent.com/72562765/143719129-4cd007fe-45ef-4157-aff8-143132ba8317.png)| academy home page header   |
| ![image (2)](https://user-images.githubusercontent.com/72562765/143719161-83dba724-63de-47b0-b9d2-e403e2f3c4c6.png) | Training session and trial background image |
| ![uniforia](https://user-images.githubusercontent.com/72562765/143719195-69ded3fa-3ef8-4b87-95b2-f816f990d21f.jpeg) | shopfront page header |



### Acknowledgements

* My mentor Antonio Rodriguez who has been great help with guidance and support throughout the project
