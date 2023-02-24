# **The Craft Café**

# Testing

## Code Validation

The Craft Café site has been passed through the [W3C html Validator](https://validator.w3.org/), the [W3C CSS Validator](https://jigsaw.w3.org/css-validator/) and the [JS Hint Validator](https://jshint.com/).

The Craft Café site has also been passed through the internal PEP8 validation tests which I installed into GitPod. The method I used to do this was as per the Slack Article written by kevin_ci on the 28th September 2022 in #announcements, since the PEP8online website no longer works:

1. Run the command 'pip3 install pycodestyle'
2. Press Ctrl+Shift+P
3. Type 'linter' into the search field
4. Select 'Python: Select Linter
5. Select 'pycodestyle' from the list
6. Select the 3 lines menu in the top left hand corner. Select 'View' and then 'Problems'. 
6. PEP8 errors are now displayed in a list as well as being underlined in red in the central editor window. 

## W3C html Validation Results

* base.html - 1 error and 1 warning found. Details can be found in the [Bugs](<#known-bugs>) section. The issues were easily fixed and after a retest, no more errors were returned.

![W3C html home page validation results](static/images/testing/w3c-html-pass.png)

## W3C CSS Validation Results

* Style.css – No errors were found.

![CSS validation test pass results](static/images/testing/css-test.png)

## JS Hint Validation Results

* Script.js - 2 undefined variables found.  Details can be found in the [Bugs](<#known-bugs>) section. The issues were fixed and after further testing, no more errors were returned.

![JSHint validation test pass results](static/images/testing/js-testing-passed.png)

## PEP8 Validation Results

### Booking App py files

* admin.py - No problems or warnings found
* apps.py - No problems or warnings found
* forms.py - No problems or warnings found
* models.py - No problems or warnings found
* urls.py - No problems or warnings found
* views.py - No problems or warnings found

### Community App py files

* admin.py - No problems or warnings found
* apps.py - No problems or warnings found
* forms.py - No problems or warnings found
* models.py - No problems or warnings found
* urls.py - No problems or warnings found
* views.py - No problems or warnings found


## Manual Testing

In addition to the code validation tests stated above I have performed a series of manual tests. 

| Status | **Homepage - User Logged Out**
|:-------:|:--------|
| &check; | Clicking the navbar brand logo loads the home page
| &check; | Clicking the Home button on the nav bar re-loads the home page
| &check; | Clicking the Food button on the nav bar scrolls down to the Craft Cafe Menu section of the homepage
| &check; | Clicking the Craft Workshops button on the nav bar takes you to the top of the contact.html page
| &check; | Clicking the Contact Us button on the nav bar takes you to the booking form section on the contact.html page but the user can't see the booking form
| &check; | Clicking the Craft Cafe Community button on the nav bar takes you to the craft-community.html page with a message saying you must be logged in to view community posts. No posts can be seen.
| &check; | Clicking the Sign Up button on the nav bar loads the sign up page
| &check; | Clicking the Login button on the nav bar loads the sign in page
| &check; | The user can not see the personal profile icon in the navigation bar
| &check; | The user can not see the admin menu option in the navigation bar
| &check; | Clicking on the 'Book into a craft workshop here' button on the hero image takes you to the top of the contact.html page
| &check; | Clicking the 'Wool' button on the Craft Cafe Workshop category cards takes the user to the Mondays: All things Wool section of the Contact Page
| &check; | Clicking the 'Quilting' button on the Craft Cafe Workshop category cards takes the user to the Wednesdays: Quilting section of the Contact Page
| &check; | Clicking the 'Clothing' button on the Craft Cafe Workshop category cards takes the user to the Tuesdays: Clothing section of the Contact Page
| &check; | Clicking the 'Home Crafts' button on the Craft Cafe Workshop category cards takes the user to the Thursdays: Home Crafts section of the Contact Page
| &check; | Clicking the 'Needlepoint' button on the Craft Cafe Workshop category cards takes the user to the Fridays: Needlepoint section of the Contact Page
| &check; | Clicking the 'Kids Crafts' button on the Craft Cafe Workshop category cards takes the user to the Saturdays: Kids Crafts section of the Contact Page
| &check; | Clicking on the 'Click here to find out more and book' button takes the user to the top of the contact.html page
| &check; | Desktop users can see three reviews
| &check; | Tablet and Mobile users can see two reviews
| &check; | Google map is visible with a marker pin showing the exact location of the Craft Cafe
| &check; | Clicking the KH Designs link in the footer area opens my GitHub profile in a new window
| &check; | Clicking the Craft Cafe brand logo in the footer area takes the user back to the top of the homepage
| &check; | Clicking the Facebook link in the footer area opens Facebook in a new window
| &check; | Clicking the Twitter link in the footer area opens Twitter in a new window
| &check; | Clicking the Instagram link in the footer area opens Instagram in a new window

| Status | **Contact Page - User Logged Out**
|:-------:|:--------|
| &check; | The user can view the workshop schedule for Mondays, including pricing, example activites, and session times. 
| &check; | The user can view the workshop schedule for Tuesdays, including pricing, example activites, and session times.
| &check; | The user can view the workshop schedule for Wednesdays, including pricing, example activites, and session times.
| &check; | The user can view the workshop schedule for Thursdays, including pricing, example activites, and session times.
| &check; | The user can view the workshop schedule for Fridays, including pricing, example activites, and session times. 
| &check; | The user can view the workshop schedule for Saturdays, including pricing, example activites, and session times.
| &check; | Clicking the 'Book your places here' button for any day takes the user down to the contact form section
| &check; | In the booking form section, the user can't see the booking form
| &check; | In the booking form section, the user can see a message saying 'You must be logged in to make a booking'.
| &check; | Clicking on the 'Log in Here' link takes the user to the sign in page.

| Status | **Craft Community Page - User Logged Out**
|:-------:|:--------|
| &check; | The user can't view community posts  
| &check; | The user can see a message informing them that 'You must be logged in to view community posts'.. 
| &check; | Clicking on the 'Join the Craft Cafe Community Here' link takes the user to the sign in page.

These testing scenarios fulfil the objectives set out in the initial user stories for a logged out user. 

| Status | **Homepage - User Logged In**
|:-------:|:--------|
| &check; | Clicking the navbar brand logo loads the home page
| &check; | Clicking the Home button on the nav bar re-loads the home page
| &check; | Clicking the Food button on the nav bar scrolls down to the Craft Cafe Menu section of the homepage
| &check; | Clicking the Craft Workshops button on the nav bar takes you to the top of the contact.html page
| &check; | Clicking the Contact Us button on the nav bar takes you to the booking form section on the contact.html page 
| &check; | Clicking the Craft Cafe Community button on the nav bar takes you to the craft-community.html page
| &check; | The user can't see the Log In button in the navigation bar
| &check; | The user can't see the Sign Up button in the navigation bar
| &check; | The user can see the Log Out button in the navigation bar
| &check; | Clicking the Logout button on the nav bar loads the sign out page
| &check; | The user can see the personal profile icon in the navigation bar
| &check; | The user can not see the admin menu option in the navigation bar
| &check; | Clicking the personal profile icon on the nav bar loads the user's profile page
| &check; | Clicking on the 'Book into a craft workshop here' button on the hero image takes you to the top of the contact.html page
| &check; | Clicking the 'Wool' button on the Craft Cafe Workshop category cards takes the user to the Mondays: All things Wool section of the Contact Page
| &check; | Clicking the 'Quilting' button on the Craft Cafe Workshop category cards takes the user to the Wednesdays: Quilting section of the Contact Page
| &check; | Clicking the 'Clothing' button on the Craft Cafe Workshop category cards takes the user to the Tuesdays: Clothing section of the Contact Page
| &check; | Clicking the 'Home Crafts' button on the Craft Cafe Workshop category cards takes the user to the Thursdays: Home Crafts section of the Contact Page
| &check; | Clicking the 'Needlepoint' button on the Craft Cafe Workshop category cards takes the user to the Fridays: Needlepoint section of the Contact Page
| &check; | Clicking the 'Kids Crafts' button on the Craft Cafe Workshop category cards takes the user to the Saturdays: Kids Crafts section of the Contact Page
| &check; | Clicking on the 'Click here to find out more and book' button takes the user to the top of the contact.html page
| &check; | Desktop users can see three reviews
| &check; | Tablet and Mobile users can see two reviews
| &check; | Google map is visible with a marker pin showing the exact location of the Craft Cafe
| &check; | Clicking the KH Designs link in the footer area opens my GitHub profile in a new window
| &check; | Clicking the Craft Cafe brand logo in the footer area takes the user back to the top of the homepage
| &check; | Clicking the Facebook link in the footer area opens Facebook in a new window
| &check; | Clicking the Twitter link in the footer area opens Twitter in a new window
| &check; | Clicking the Instagram link in the footer area opens Instagram in a new window

| Status | **Contact Page - User Logged In**
|:-------:|:--------|
| &check; | The user can view the workshop schedule for Mondays, including pricing, example activites, and session times. 
| &check; | The user can view the workshop schedule for Tuesdays, including pricing, example activites, and session times.
| &check; | The user can view the workshop schedule for Wednesdays, including pricing, example activites, and session times.
| &check; | The user can view the workshop schedule for Thursdays, including pricing, example activites, and session times.
| &check; | The user can view the workshop schedule for Fridays, including pricing, example activites, and session times. 
| &check; | The user can view the workshop schedule for Saturdays, including pricing, example activites, and session times.
| &check; | Clicking the 'Book your places here' button for any day takes the user down to the contact form section
| &check; | In the booking form section, the user can see the booking form
| &check; | The user's username is automatically populated in the 'booking as' field
| &check; | The user can't open the 'Day' field calendar if the 'Workshop' field has not been selected first. 
| &check; | The user can view a list of the six workshop categories on clicking the 'Workshop' field dropdown selection
| &check; | The user can open the 'Day' field calendar after having selected a workshop.
| &check; | The user can't select any dates in the past
| &check; | The user can only select dates up to 5 months in the future, from today's date.
| &check; | The user can't manually type anything into the 'Day' field
| &check; | On selecting the 'All Things Wool' workshop, the user can only select Mondays from the calendar
| &check; | On selecting the 'Quilting' workshop, the user can only select Wednesdays from the calendar
| &check; | On selecting the 'Clothing' workshop, the user can only select Tuesdays from the calendar
| &check; | On selecting the 'Home Crafts' workshop, the user can only select Thursdays from the calendar
| &check; | On selecting the 'Needlepoint' workshop, the user can only select Fridays from the calendar
| &check; | On selecting the 'Kids Crafts' workshop, the user can only select Saturdays from the calendar
| &check; | On selecting the 'All Things Wool', 'Quilting', 'Clothing', 'Home Crafts' or 'Needlepoint workshop, the user can only select the afternoon options of 4 - 6pm or 6 - 8pm from the 'Time' field dropdown menu.
| &check; | On selecting the 'Kids Crafts' workshop, the user can only select the morning options of 10 - 11.30 or 11.30 till 1 from the 'Time' field dropdown menu.
| &check; | The user can view a list of the number of places they wish to book from 1 to 10 in the 'Places' field dropdown selection
| &cross; | On changing the 'Workshop' field selection, the date field is reset to blank.
| &check; | On changing the 'Workshop' field selection, the Time field is reset to correspond with the selected workshop.
| &check; | On changing the 'Workshop' field selection, the Places field is reset to 1.
| &check; | Clicking 'Submit booking request', the user will see an error message alert above the contact form saying 'The selected date is full. Please try a different session', if there are already more than 10 places reserved on the same workshop session requested.
| &check; | On submitting a booking request on a session where there are not enough places available, the user is redirected back to the booking form and the fields have been reset
| &check; | Clicking 'Submit booking request', if there are enough places available, the user is redirected to the profile page so that they can see the details of the booking.
| &check; | Clicking 'Submit booking request', if there are enough places available, the user can see an alert message saying 'Booking request successful, awaiting approval'.
| &check; | On submitting a booking request with no Workshop selected, a message pops up telling the user to select a workshop
| &cross; | On submitting a booking request with no date selected, a message pops up telling the user to select a date



## Responsiveness Test

The responsive design tests were carried out manually throughout the build using Google Chrome Dev Tools. I used a mobile first approach basing my initial design around the iPhone 6,7,8 (375 x 667px) which became my first media query break point. I then selected another break point at 768px for tablet devices 992px and above for larger devices, following the bootstrap standard breakpoints. 

During the testing process I also used the [Responsive Design Checker](https://www.responsivedesignchecker.com/) website to simulate the website on several other devices. Here are my findings:

### Mobile Devices

||<p>iPhone 6/7 plus</p><p>414 x 736</p>|<p>Samsung Galaxy S5/6/7</p><p>360 x 640</p>|<p>Google Pixel/Nexus 5/6</p><p>411 x 731</p>|
| :- | :-: | :-: | :-: |
|Render|Pass |Pass|Pass|
|Images|Pass|Pass|Pass|
|Links|Pass|Pass|Pass|

I chose not to test the iPhone models 3, 4, or 5 as these have a smaller screen (320 x 480) and were only supported officially by Apple until March 2021. 

On devices with a height of 640 pixels, such as the Samsung mobile devices, once the quiz has begun, you have to scroll down after choosing an answer to see the bottom of the question container in some cases where the question is longer. The next button sometimes is slightly hidden, but I find this scrolling acceptable in the case of certain longer questions for shorter devices. 

### Tablet Devices

||<p>Amazon Kindle Fire</p><p>768 x 1024</p>|<p>Samsung Galaxy Tab 10</p><p>800 x 1280</p>|<p>Apple iPad Pro</p><p>1366 x 1024</p><p></p>|
| :- | :-: | :-: | :-: |
|Render|Pass|Pass(2nd time)|Pass |
|Images|Pass|Pass|Pass|
|Links|Pass|Pass|Pass|

When I tested the form page on the Samsung Galaxy Tab 10, the background image was not reaching the bottom of the screen, so it was leaving a blank area across the bottom of the device. I changed the CSS styling of the background size from 'Auto' to '200rem' and I have re-tested. The image now seems to cover the full screen, on taller devices. I don't like it however that the image is moving on each click of the buttons, so I have adjusted the CSS styling of the background image to set the background attachment to fixed. 

![tablet device view of quiz](assets/readmeimages/samsung-tablet-testing.PNG)

On the larger Apple iPad Pro, the rules text appears very small in comparison with the relative screen size. I have therefore decided to create a third media query break point at 1200px to make the font bigger for wider screens.

### Desktop Devices

||<p>24 “ Desktop</p><p>1920 x 1200</p>|<p>19” Desktop</p><p>1440 x 900</p>|<p>10” Notebook</p><p>1024 x 600</p>|
| :- | :-: | :-: | :-: |
|Render|Pass|Pass|Pass|
|Images|Pass|Pass|Pass|
|Links|Pass|Pass|Pass|

Playing the quiz on the 10inch Notebook, the display appears odd because the dimensions are very wide but very short; shorter in fact than most mobile devices. Therefore, when this device is in use, more scrolling is required. You have to scroll down slightly in the 'Rules' screen to reach the 'Start Quiz' button which is only half visible, and then once the quiz has begun, you have to scroll down to see all the answer options at once which means you lose sight of the header whilst playing. I find this acceptable as once the quiz has begun and you have scrolled down to the game area, you don't have to scroll anymore whilst playing the game.

![Notebook view of quiz pre-scroll](assets/readmeimages/beforescroll-notebook.PNG)

![Notebook view of quiz post-scroll](assets/readmeimages/afterscroll-notebook.PNG)

## Browser Compatibility 

The Craft Café was tested on the following browsers:

- Google Chrome
- Microsoft Edge
- Mozilla Firefox

I do not have any Apple devices available to carry out testing on a Safari browser. Appearance and functionality appear to be consistent throughout all browsers.
  

## Known Bugs

### Resolved 

1. As a result of the W3C html validation test, the base.html page had 1 error and 1 warning. 

![Index.html validation error](static/images/testing/w3c-html-errors.png)

This error suggested that the Meta charset line was too far down my head section so I moved it to the top so that it would load faster. The warning suggested that the type attribute that I had on my javascript file link was unnecessary so I removed it. 

2. As a result of the JS Hint validation test, 2 undefined variables were found.

![JSHint validation test results](static/images/testing/js-testing.png)

Initially, I had a lot of missing semi-colons which were easy to add back in. Then I was left with 2 undefined variables; 
* $
* bootstrap

I created a global variable at the top of the file for each of these, and I no longer saw the error messages.


### Unresolved

1. In the console log, I can see that when the End Page is loaded

## Additional Testing

### Lighthouse
Google Lighthouse in Chrome Developer Tools was used to test the application within the areas of *Performance*, *Accessibility*, *Best Practices* and *SEO*. I tested the *index page*, *craft workshops page*, *craft cafe community page* and *profile page*. The testing showed the following:

* Index Page - Performance: 51, Accessibility: 93, Best Practises: 67, SEO: 90
* Craft Workshops Page - Performance: 86, Accessibility: 93, Best Practises: 75, SEO: 90
* Craft Cafe Community Page - Performance: 70, Accessibility: 74, Best Practises: 67, SEO: 80
* Profile Page - Performance: 96, Accessibility: 95, Best Practises: 75, SEO: 80

In general this is OK results. The performance is affected in a negative way by external scripts (connected to i.e. Bootstrap) and the lower result on the Index page I think due to a large hero image. The site images also seem to be affecting my best practice scores throughout so this is something I may need to address in future projects and in projects in general where users upload photos.

<details><summary><b>Lighthouse Index Result</b></summary>

![Lighthouse Index Result](static/images/testing/lighthouse-home.png)
</details><br/>

<details><summary><b>Lighthouse Workshops/Contact Page</b></summary>

![Lighthouse Workshops/Contact Page](static/images/testing/lighthouse-workshops.png)
</details><br/>

<details><summary><b>Lighthouse Community Posts Page</b></summary>


![Lighthouse Community Posts Page](static/images/testing/lighthouse-posts.png)
</details><br/>

<details><summary><b>Lighthouse Profile Page</b></summary>

![Lighthouse Profile Page](static/images/testing/lighthouse-profile.png)
</details><br/>

## Peer Review

In addition to the above tests, I asked my peers to create a profile and interact with the site and their overall response was very positive. 
 

Please click [**_here_**](README.md) to return to the Craft Cafe README file.