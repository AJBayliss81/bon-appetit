# [Bon Appetit](https://ba-cook.herokuapp.com/)

A website for sharing and commenting on recipes.

!["Example responsivity"](static/images/responsive.png "Example responsivity")

## Table of Contents
1. [**UX**](#ux)
    - [**Project Goals**](#project-goals)
    - [**Player Goals**](#player-goals)
    - [**Developer Goals**](#developer-goals)
    - [**User Stories**](#user-stories)
    - [**Design Choices**](#design-choices)

2. [**Features**](#features)
    - [**Existing Features**](#existing-features)
    - [**Features Left to Implement**](#features-left-to-implement)

3. [**Technologies Used**](#technologies-used)

4. [**Testing**](#testing)
    - [**Tested Devices**](#tested-devices)
    - [**Laptop Testing**](#laptop-testing)
    - [**Smartphone Testing**](#smartphone-testing)
    - [**Validation Services**](#validation-services)
    - [**Bugs Discovered**](#bugs-discovered)

6. [**Deployment**](#deployment)
    - [**How to run this project locally**](#how-to-run-this-project-locally)

7. [**Credits**](#credits)
    - [**Code**](#code)
    - [**Media**](#media)
    - [**Acknowledgments**](#acknowledgments)

8. [**Disclaimer**](#disclaimer)

## UX


### Project Goals  
  
The aim of the project was to create a website where users would be able to share recipes with one another and comment on the recipes that they enjoyed to build a community on the site.  
  
### User Goals  
  
User goals are:  
- Find new recipe ideas.  
- Share new recipe ideas with others.  
- Leave comments for others about which recipes they like, and why.  
- Have feedback from the community on recipes they have submitted.
- Be able to navigate the site intuitively.  
  
[Bon Appetit](https://ba-cook.herokuapp.com/) achieves this by:    
- Allowing user to have their own profile areas.  
- Having an intuitive design and layout whereby the user can quickly learn how to navigate the site and contribute by adding recipes and comments. 
- Having comments linked to recipes so they can see what other users have said about them.
- Having the management of their own submitted recipes and comments on their profile page to allow them to edit or delete them. 
  
### Developer Goals  
  
- To enable CRUD operations for a website, allowing users to register and update information to a database.  
- Design a useful, functional website to further implementation of CRUD functionality for a website. 
- Expand upon previous skills to add increased functionality to website design. 
- Expand portfolio to showcase new skills.
 
### User Stories  
  
Being a user that is interested in sharing recipes within a community:  
  
1. To be able to share recipes with other users quickly and easily.
2. To be able to edit and delete recipes whenever necessary.
3. To be able to add comments to recipes that I like to create a welcoming community experience.
4. To be able to edit and delete comments whenever necessary.
5. To be able to quickly see all the recipes and comments I have shared.
6. To have an intuitive site that is easy to follow.  
7. To have a site that is responsive and good to look at while using it.
  
### Design Choices  
  
1. **Fonts**  
Fonts were selected from [Google Fonts](https://fonts.google.com/). All were chosen as they paired well together. 
    - _Lato_: The font used for the body text and buttons was chosen as it was easy to read, pairs well with _dancing script_, and is a font that I am familiar with,,, having used it on previous projects. It provides a clean and easily legible font at all sizes.  
    - _Dancing script_: Was used for the site logo, as well as the header elements. I chose  this particular font due to looking more handwritten. I thought that this would provide users a more human, friendly aspect to the site. Perhaps to provide a more _"homely"_ feel to it. 
  
2. **Buttons**  
Buttons used the majority of [Materialize's](https://materializecss.com/) styling and functionality with a custom blue colour added for the mouseover functionality to improve the user experience. The text color of the buttons also used that of the rest of the fonts on the site to tie it in better with the colour scheme, and a custom text shadow effect was used to make this stand out better and make the buttons appear less flat.   
 
3. **Colors**  
I wanted the site to have a monochromatic feel to it to tie in with the chrome/silver/black that is often found with kitchen utensils and equipment. I elected to also use a bright blue to give a bit more contrast to certain elements to make them stand out more and be hightlighted better. The colour scheme I chose can be found [here](https://coolors.co/dcdcdd-c5c3c6-46494c-4c5c68-1985a1).
  
4. **Images**  
Images were chosen to fit with the theme of the website. 
    - _Food Images_: Stock photo images of dishes that I felt were representative of particular cuisines were chosen for the cuisine cards for the browse template to give users a visual representation of the type of cuisine. Both for those unfamiliar with it, and also to provide a nice image to engage the user to dig deeper. The images are generated dynamically onto the cards using _Jinja_.  
    - _Background Image_: Is that of a kitchen, to give the user an image associated with recipes and cooking. I selected the particular image as it was quite dark and tied in well with the monochromatic colour scheme I was using for the site.  
  
6. **Styling**  
The website style is inspired by kitchen equipment and utensils, with a monochromatic, functional aesthetic.
    - _Monochromatic Theme_: This theme was chosen to give the user the feeling of cookware and kitchens. As it is a scheme that I feel many people would be familiar with from the different products they have in their own homes.  
    - _Modals_: Modals were used to provide checks for cancellation messages, for ease of use and to force the user to confirm their intention to prevent accidental deletion of database entries.
 
## Features  
  
The website follows a one page design with accompanying modals to maintain a clutter free environment and guide the flow of the game.
  
### Existing Features  
  
1. **Flask**  
[Flask](https://flask.palletsprojects.com/en/1.1.x/) framework is used to allow the use of other functionality of the site, such as the _Jinja_ templating and _Werkzeug_ security features.

2. **Jinja Templates**  
Are used to allow ease of navigation throughout the site. Using inheiritance of the base template to eliminate the need for duplication of common features of the website, such as the navbars.
  
3. **User Verification**  
Users must sign up to the website to be able to use the features. Registration requires users to submit a username and password that conforms to the requirements of length and characters to make it more secure. This data is then stored on the [MongoDB](https://www.mongodb.com/) database using password hashing to provide security.

4. **CRUD functionality for recipes**  
To allow users to add, edit, view and delete recipes that they have added themselves, as well as view those shared by others.

5. **CRUD Functionality for Cuisines(admin only)**
To allow admins the ability to add new cuisines when required that will dynamically appear as options for users to select for their new added recipes.

6. **CRUD Functionality for Comments**
To allow users to add, edit, view and delete comments that they wish to share with the community about their favourite recipes. Other users are also able to view the comments for particular recipes on the recipes page itself.

### Features Left to Implement  
  
1. **Star Ratings**  
To allow users to submit a star rating alongside their comments that would then provide each recipe an average user based rating score so that people would be able to easily see which recipes are the most popular. This could also coincide with an additional search perameter for user to search for the highest rated recipes.

2. **Cookware**  
To provide each recipe with a list of required cookware for preparing it, with a pop-up image to show users what it is, and also a link to where it could be purchased from.

3. **More Intricate Scoring System**  
Redesigning the scoring system so that points are generating by each correct matching of an individual image rather than a complete sequence. This would allow for a more diverse score to be generated.

## Technologies Used  
  
- **Languages**  
    - [HTML5](https://devdocs.io/html/)
    - [CSS3](https://devdocs.io/css/) 
    - [JavaScript](https://devdocs.io/javascript/)
    - [Python](https://www.python.org/)
  
- **Libraries**  
    - [JQuery](https://jquery.com) - used to simplify DOM manipulation, and make the JavaScript easier to read. 
    - [Google Fonts](https://fonts.google.com/) - provided the fonts for the website to make the text more interesting.  
  
- **Frameworks**  
    - [Materialize](https://materializecss.com/) - used to create an easily responsive design for all screen sizes.  
  
- **Cookies**  
    - [Cookies](https://developer.mozilla.org/en-US/docs/Web/HTTP/Cookies) - were used to store the session user so they can remained logged in. This became key to much of the code to show users their own personalised profile area.  
    
- **Services**  
    - [GitPod](https://www.gitpod.io/) - the IDE used exclusively to create the website.  
    - [Git](https://git-scm.com/) - for version control.  
    - [GitHub](https://github.com/) - to store the repository online and host the finished website.
    - [Heroku](https://www.heroku.com/) - used to deploy the website.
    - [MongoDB](https://www.mongodb.com) - used to host the database necessary for the project to function.
    - [Chrome DevTools](https://developers.google.com/web/tools/chrome-devtools) - used mainly for checking responsiveness of the website throughout the development process and to address bugs and error messages with code.  
    - [HTML Validator](https://validator.w3.org/) - used to test the final HTML code and address improper syntax.  
    - [CSS Validator](https://jigsaw.w3.org/css-validator/) - used to test the final CSS code and address improper syntax.  
    - [JSHint](https://jshint.com/) - used to test the final JavaScript code and address improper syntax.  
    - [Am I Responsive?](http://ami.responsivedesign.is/) - used to provide a visual representation of the responsiveness of the game across all platforms. 
  
- **Software**  
    - [Paint.net](https://www.getpaint.net/) - used to crop and resize the original animal images to better fit the image display box. 
  
  
## Testing  
  
### Tested Devices  
The majority of the testing was conducted on the desktop PC via [Chrome DevTools](https://developers.google.com/web/tools/chrome-devtools).    
  
```  
| -----------|---------------------------- |------------------------------|  
| Type       | Device                      | Browsers                     |  
| -----------|---------------------------- |------------------------------|  
| Desktop    | Windows 10, 1080p display   | Chrome, Firefox, Edge, Opera |
| Laptop     | Asus X550C                  | Chrome, Firefox, Edge, Opera |  
| Smartphone | Samsung Note 9              | Chrome, Firefox              |  
| Smartphone | Huawei P30 Pro              | Chrome, Firefox              |  
| Smartphone | Samsung Tab E               | Chrome                       |    
| -----------|---------------------------- |------------------------------|  
```  
  
### Testing Process
The following process was conducted for all devices, with the desktop and laptop process repeated twice and higher and lower resolutions.  
  
1. **User Functionality**  
    - Open the website and ensure that the welcome page displays correctly.  
    - Ensure that navbars contain the correct links for an unregistered user.  
    - Ensure the registration page displays correctly.  
    - Ensure ensure registration functionality is working.  
    - Close browser window and open again to ensure the username still displays and the correct links are visible on the navbar.  
    - (Desktop and laptop only) Hovered the mouse over the buttons on the profile page to ensure the animation occured. 
    - Ensured the logout link worked and returned to the login page.
    - Ensured the login link worked and the login page displayed correctly.
    - Ensured login functionality worked correctly.
    - Ensured profile page displayed correct recipes and comments.
    - Ensured all profile page buttons were working..
    - Ensured confirmation delete modal was displaying for deletion of comments and recipes.  
  
2. **Recipe CRUD Functionality**  
    - Ensured the add and edit pages displayed correctly.
    - Ensured the add and edit page buttons worked correctly.
    - Ensured the add and edit functions added and updated the correct entries on the databse.
    - Ensured the delete button displayed the modal.
    - Ensured the delete function worked on the correct entry, and only after confirmation from clicking the modal button.
    - Ensured the recipes and comments added were displayed correctly on the appropriate pages.
    
2. **Cuisine CRUD Functionality**  
    - Ensured the add and edit pages displayed correctly.
    - Ensured the add and edit page buttons worked correctly.
    - Ensured the add and edit functions added and updated the correct entries on the databse.
    - Ensured the delete button displayed the modal.
    - Ensured the delete function worked on the correct entry, and only after confirmation from clicking the modal button.
    - Ensured the recipes and comments added were displayed correctly on the appropriate pages.
    - Ensured the functionality was only available to those with admin authority.

3. **Comment CRUD Functionality**  
    - Ensured the add and edit pages displayed correctly.
    - Ensured the add and edit page buttons worked correctly.
    - Ensured the add and edit functions added and updated the correct entries on the databse.
    - Ensured the delete button displayed the modal.
    - Ensured the delete function worked on the correct entry, and only after confirmation from clicking the modal button.
    - Ensured the recipes and comments added were displayed correctly on the appropriate pages.
    
### Validation services  
Upon completion of the project the code was checked using the following resources and the corresponding feedback acted upon where appropriate.  
- [HTML Validator](https://validator.w3.org/) - The only issue raised was a missing alt tag for the cuisine images, so one was added.
- [CSS Validator](https://jigsaw.w3.org/css-validator/) - many errors shown, but were relating to the various CDN sources.
- [JSHint](https://jshint.com/) - checked the javascript, no errors were shown.  
  
### Bugs Discovered  
- The bugs that were discovered through development have been fixed, so presently there are no known bugs in the deployed version.  
  
## Deployment  
  
[GitPod](https://www.gitpod.io/) was the sole IDE used to deveop this project due to the synergy with [Git](https://git-scm.com/) and [GitHub](https://github.com/) for the hosting of repositories and version control.  
  
Bon Appetit was deployed via [Heroku](http://ba-cook.herokuapp.com/) from its [GitHub repository](https://github.com/AJBayliss81/bon-appetit). This can be achieved by:  
1. Logging in to Github.  
2. Selecting the repository for deploying, eg. [Bon Appetit](https://github.com/AJBayliss81/bon-appetit).
3. Clicking the **Settings** option at the end of the menubar below the repository name.  
4. The penultimate section is for GitHub Pages.  
5. Within this section the first options are for the source, with a drop-down box. 
6. Select the _Master_ option from the branch box, the page will reload and a link for the deployed page will show.
  
### How to run this project locally  
  
Should you wish to pull the code to your own repository:  
1. Login to your own Github.  
2. Open the repository you wish to pull. eg. [Bon Appetit](https://github.com/AJBayliss81/bon-appetit).  
3. Just above the file list is a green button `Clone`, click this.  
4. Select from the options to clone via `HTTPS or SVN` using the link, open with `GitHub Destop` if the app is installed, or download as a `.zip` file.  
5. Open Git Bash.  
6. Change the current working directory to the location where you want the cloned directory to be made.  
7. Type `git clone`, and then paste the URL you copied in Step 3.  
8. Press `Enter`. Your local clone will be created.  

Though this will clone the repository to view the code, full functionality will not be possible unless linked to a database from [MongoDB](https://www.mongodb.com) or similar. 
  
## Credits  
  
### Code  
  
- [StackOverflow](https://stackoverflow.com/) was used extensively to research solutions to problems I was having with getting the desired result from the code when it wasn't behaving as I had intended.  
  
### Media  
  
- The images found for use on the site can be found and used royalty free from [Unsplash](https://unsplash.com/).

### Acknowledgments 
    
- [Code Institute](https://codeinstitute.net/) tutors and support for assisting with some issues during the creation of this project.
  
