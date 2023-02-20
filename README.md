# **The Craft Café**

The Craft Café is a regular café where people can go to enjoy a cup of coffee and a piece of cake. However, it's unique selling point is that in the afternoons, Monday to Friday, and on Saturday mornings, it also runs Craft workshops where people can learn crafty skills and make beautiful craft items to take away. Through the Craft Cafe website, users can check the craft workshop schedule, and reserve their places in advance. 

This fictional site was created for Portfolio Project #4 (Full-Stack Toolkit) - Diploma in Full Stack Software Development Diploma at the [Code Institute](https://www.codeinstitute.net).

[View live website here](https://craft-cafe.herokuapp.com/)

![Responsive design](static/images/readme/devicemockup.PNG)

# Table of Content

* [**Project**](<#project>)
    * [Objective](<#objective>)
    * [Site Users Goal](<#site-users-goal>)
    * [Site Owners Goal](<#site-owners-goal>)
    * [Project Management](<#project-management>)

* [**User Experience (UX)**](<#user-experience-ux>)
    * [Wireframes](<#wireframes>)
    * [User Stories](<#user-stories>)
    * [Site Structure](<#site-structure>)
    * [Design Choices](<#design-choices>)

* [**Existing Features**](<#existing-features>)
    * [Navigation](<#navigation>)
    * [About](<#about>)
    * [All](<#all>)
    * [Albums](<#albums>)
    * [Concerts](<#concerts>)
    * [Review Detail View](<#review-detail-view>)
    * [Update / Delete Comment](<#update-and-delete-comment>)
    * [Member Reviews](<#member-reviews>)
    * [Create Review](<#create-review>)
    * [Update Review](<#update-review>)
    * [Profile Page](<#profile-page>)
    * [Admin Area](<#admin-area>)
    * [Sign Up](<#sign-up>)
    * [Sign In](<#sign-in>)
    * [Sign Out](<#sign-out>)
    * [Footer](<#footer>)
    * [Flash Messages](<#flash-messages-and-confirmation-pages-to-the-user>)

* [**Features Left To Implement**](<#features-left-to-implement>)

* [**Technologies Used**](<#technologies-used>)
    * [Languages](<#languages>)
    * [Frameworks & Software](<#frameworks--software>)
    * [Libraries](<#libraries>)

* [**Testing**](<#testing>)
    * [Testing User Stories](<#testing-user-stories>)
    * [Code Validation](<#code-validation>)
    * [Additional Testing](<#additional-testing>)
    * [Known Bugs](<#known-bugs>)
* [Deployment](<#deployment>)
* [Credits](<#credits>)
* [Acknowledgements](<#acknowledgements>)

# **Project**

## Objective
I absolutely love crafting, both with my children, and as a personal hobby. I make patchwork quilts to relax and disconnect from work. It would be dream of mine to set up a craft café, where people could go to socialise through craft activities, and gain valuable crafting expertise at the same time. Based on the project 4 scope requirements, I was given the opportunity to build a site for this dream café.

## Site Users Goal
This café gives other like-minded craft enthusiasts the opportunity to meet each other and interact through a common shared hobby.

## Site Owners Goal
The goal of the site owner is to deliver a site where the users who share a passion for craft and creating can meet eachother through the craft workshops, and also share their creations with eachother by posting photos and comments.

## Project Management

### Github Project Board
I've been using the project board in GitHub to keep my project together. In the initial design phase, it was really helpful to plan the project as a whole, and create the user stories based on my wireframe designs. I created an Epic for each main html page with bullet points for the main desired features. Then, I created a linked User Story for each feature and gave it a level of prioritization using the MoSCoW method and a number of User Story points to indicate the level of difficulty for that feature. 

Later on, during the build, I also used the Project Board to log and track bugs found in my code which could not be fixed immmediately. 

![GitHub Project Board](static/images/readme/project-board.PNG)

[Back to top](<#table-of-content>)

### Database Schema
I have used a modelling tool called [Graph Models](https://django-extensions.readthedocs.io/en/latest/graph_models.html) to create the database schema. In short it shows the relationships between the different models in the database connected to the application. Graph Models exports a *.dot file which easily can be converted to a more 'easy to read' design with the help of the application [dreampuf](https://dreampuf.github.io/GraphvizOnline/).

Models used (besides standard user model) in this project are:

* **Category** - Handles categories. I made a specific model to be able to add more dynamics (create / remove categories going forward in the admin backend instead of 'hard code' it in the code).
* **Genre** - Handles genres. I made a specific model to be able to add more dynamics (create / remove genres going forward in the admin backend instead of 'hard code' it in the code).
* **Post** - Handles all the reviews
* **Comment** - Handles all the comments
* **UserProfile** - Handles the user profile information (first name, last name, presentation and featured image for the specific user/reviewer). There is a one-to-one relation to the user model to connect it to the standard user model.

<details><summary><b>Database Schema</b></summary>

![Database Schema](readme/assets/images/database_schema.png)
</details><br/>

# **User Experience (UX)**

## Wireframes
The wireframes for the site were created in the software [Balsamiq](https://balsamiq.com). The wireframes have been created for desktop, tablet and mobile devices. The text content wasn't finalized during the wireframe process. It's worth mentioning that there are visual differences compared to the wireframes, the reason being design choices that was made during the creation process.

<details><summary><b>Wireframes</b></summary>

![Wireframes](readme/assets/images/balsamiq.png)
</details><br/>

## User Stories
Below the user stories for the project are listed to clarify why particular feature matters. These will then be tested and confirmed in the [Testing](<#testing>) section.

### Site User
|  | | |
|:-------:|:--------|:--------|
| As a Site User | I can view a list of the music reviews so that I can select one to read | &check; |
| As a Site User | I can view a list of the concert reviews so that I can select one to read | &check; |
| As a Site User | I can click on a specific review so that I can read it in detail | &check; |
| As a Site User | I can like and unlike a review so that it is possible for me to interact with the review | &check; |
| As a Site User | I can view the number of likes on each review so that I can see how popular a specific review is | &check; |
| As a Site User | I can contact Review Alliance in an easy way so that I can interact with them if I have a need for it | &check; |
| As a Site User | I can navigate easy on the site through paginated list of posts so that I feel comfortable using the site | &check; |
| As a Site User | I can view comments on a specific review so that I can read the conversations between different users on the site | &check; |
| As a Site User | I can sign up an account so that I can like and comment on reviews, create a profile page, create own reviews and edit / remove my reviews | &check; |
| As a Site User | I can create a profile page so that other reviewers can read about who I am | &check; |
| As a Site User | I can comment on a review so that I can be involved in the conversation | &check; |
| As a Site User | I can edit my comment so that I can change the content if needed | &check; |
| As a Site User | I can remove my review so that I have full control of my reviews | &check; |
| As a Site User | I can choose to see my own reviews so that I can find them easily | &check; |
| As a Site User | I can create a new review so that I can contribute to with new content to Review Alliance | &check; |
| As a Site User | I can log out from the site so that I can feel safe that nobody can access my information | &check; |
| As a Site User | I can create draft reviews so that I can finish writing the content later | &check; |
| As a Site User | I can get visual feedback when interacting with the content so that I can be sure how I have interacted with the page | &check; |

### Site Admin

|  | | |
|:-------:|:--------|:--------|
| As a Site Admin | I can log out from the site so that I can feel safe that nobody can access my information | &check; |
| As a Site Admin | I can create, read, update and delete reviews so that I can manage my review content | &check; |
| As a Site Admin | I can approve reviews so that I can secure high quality of the content | &check; |
| As a Site Admin | I can approve and disapprove comments so that I can secure a safe environment for the Site Users | &check; |
| As a Site Admin | I can create draft reviews so that I can finish writing the content later | &check; |
| As a Site Admin | I can access an admin area so that I can get a general understanding of logged in users, number of likes and number of posts | &check; |
| As a Site Admin | I can get visual feedback when interacting with the content so that I can be sure how I have interacted with the page | &check; |

[Back to top](<#table-of-content>)

## Site Structure

The Review | Alliance site is split up in two parts: **when the user is logged out** and **when the user is logged in**. Depending on login status different pages is available for the user. When the user is logged out the pages: *about*, *all*, *albums*, *concerts* are avaliable. When the user is logged in *about*, *all*, *albums*, *concerts*, *create review*, *view my reviews* and *show profile page* are available. If you are logged in as an administrator an *admin area* is available. The site has an minimalistic, clean and intuitive design that makes the site easy to navigate for the user.

Read more about the different choices in the [Features](<#features>) section.

[Back to top](<#table-of-content>)

## Design Choices

* ### Color Scheme

The color scheme chosen for the 'Review | Alliance' site was based on the Bootstrap dark background. The colors are Black (used on some text elements), Raisin Black (top navigation and footer), Rocket Metallic (used on some of the text elements), Cultured (used very rarely in this project) and White (used i.e. as background and card background). All colors are very clean and they create a professional look together and offers a good readability and contrast as well. I used the online service [Coolors](https://coolors.co/) to choose the color scheme.

![Color Palette image](readme/assets/images/coolors_palette.png)

* ### Typography
The fonts used for the site are 'Roboto' and 'Tinos'. Fallback font for both of them is sans-serif.

* 'Roboto' is used on all headlines including the brand logo. It's a very clean font that works really well for headlines and logos. It's easy to read and matches the minimalistic style that I wanted the site to 'breath'.

* 'Tinos' was chosen for the review excerpt and the review full text. It has a nice serif design and works really well for longer paragraphs of text.

![Google Fonts Impact](readme/assets/images/google_fonts_roboto.png)

![Google Fonts Tinos](readme/assets/images/google_fonts_tinos.png)

[Back to top](<#table-of-content>)