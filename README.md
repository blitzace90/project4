# Premium Furnishing
## Full Stack Frameworks with Django Milestone Project 
### **Introduction**
This site is an e-commerce website for retail sale of furnitures, an online store called Premium Furnishing. Interested buyers can browse through the site to look for suitable furnitures for their home, offices or any spaces. Any users are free to browse the site, though should they want to checkout, an account must be created for the owner to capture the necessary data and information for tracking purposes. 
<br>
The site can be found from the link: [Premium_Furnishing](https://ojhj-project4.herokuapp.com/home/)
***

### **User Experience (UX)**
**User stories** 

For someone who is on the lookout for furnitures without signing in, I want to:
- Be able to navigate freely and easily
- Able to search for what i want easily
- Be able to know who to contact should i need more information
- Being able to have the important information of the furnitures (price, size, weight, etc)

For someone who is a member, I want to be able to:
- Add my interested to cart, as well as make amendments
- Make payments for my purchase
- View my purchase history
- A feedback page should there are anything wrong with my purchase

For the admin user, I want to be able to:
- Add furnitures
- Update furnitures
- Delete furnitures

**Some UX considerations**
- The navbar at the top is found on every page, for easy navigation. 
- Adding and upload of image is made simple with clear instructions.
- Images are fixed into equal sized cards to make the page looks neat
- Hovering above the selected image will show a prominent pop-up for user
- Alert messages are prompted should users want to delete
- Flash messages are added after an action is executed
- Easy search filter by categories or name search provided

### **UI**
- Navbar is presented on every page, with the website logo. 
#### Home page
- Jumbotron with a button to easily navigate to list of furnitures
- Image with links to bring customers easily to the furnitures they are looking for
#### About us page
- Some description and image 
#### Shop page
- Name filter and category filter is found and can be used
- Cards are arranged neatly in 3 columns and images are made same sized for neatness
- Pagination to prevent long list of a single page, limited to 6 items page
- Only admin user is able to see "add furniture" button
#### Furniture details page
- Title on top to indicate the furniture selected
- A larger image of the liquor is displayed on the left with its details on the right
- Information here are all read only
- Option to select quantity and add to cart
- Only admin user is able to see "edit" and "delete" button
#### Contact us page
- Any user is able to fill in the form and submit 
- Contact information and images available here
#### Members page
- Only has the register/login Option
- Once logged in, the username will be displayed replacing the word members' page
- More options are available after logging in, able to view purchase history, change password, logout or provide feedback/review
#### Carting page
- Able to view shopping cart, as well as update quantity or remove items
- Able to do checkout from here
***
### **Technologies used**
- HTML
- CSS
- Javascript
- Bootstrap to create a mobile responsive and stylish webpage
- JQuery to simplify DOM manipulation
- Python3 
- Django 2.2.6 as it's main framework
- Cloudinary to upload images 
- Django Crispy forms to present the Django forms in bootstrap format
- Gunicorn to deploy the project to Heroku
- Stripe API to process the payment
- Heroku as a host for the project
- Postgres as the database
***
### **Testing**
The test site is tested to be responsive for:
- iphone 4
- galaxy s5
- iphone 5/se
- iphone 6/7/8
- iphone 6/7/8 plus
- iphone X
- ipad
- ipad pro
- google chrome
- microsoft edge
- safari
- internet explorer

Basic checks include:
- Testing that the C(Create), R(Read), U(Update), D(Delete) functions for furnitures, carting are working
- Different view screen for non-signed in users, signed in users, as well as admin
- Checking that the filter for both name search and category search are working
- Testing that the navbar link categories are working
- Testing that all information are being processed correctly into the database
- Newly registered users received an email to verify, and once verified, able to sign in.
- Wrong username or password will not allow sign in to go through.

Known errors:
- For updates, will need to update image twice for it to go through, first time will indicate field is empty
- Time saved at checkout is in UTC (Coordinated Universal Time)

Features left to implement:
- Review using 5 star models
- Displaying the average reviews in home page
- Purchase history to contain quantity and amount
- Chatbot
***
### **Deployment**
The code is written using gitpod and pushed to github. Deployment is using Heroku and as sqlite database cannot be used, will switch to Postgres as mySQL database before deploying to Heroku.
***
### **Credits**
- Site images are taken from [unsplash.com](https://unsplash.com/)
- Furniture images and details are taken from [Hipvan](https://www.hipvan.com/?gclid=Cj0KCQjwp4j6BRCRARIsAGq4yMGlnAMi_nxJ7CLLDS-2Aav2b2r_c0gF-QQa60iwtya3oCIQFSBmO6AaAvpkEALw_wcB)
- Icons are taken from [fontawesome](https://fontawesome.com/)
- Logo is made using [hatchful](https://hatchful.shopify.com/)
- Mock up is obtained from [mockup_generator](https://techsini.com/multi-mockup/index.php)

*Site is strictly for educational purposes
