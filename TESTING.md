# **The Craft Café**

# Testing

## Code Validation

The Craft Café site has been passed through the [W3C html Validator](https://validator.w3.org/), the [W3C CSS Validator](https://jigsaw.w3.org/css-validator/) and the [JS Hint Validator](https://jshint.com/).

## W3C html Validation Results

* Index.html - 1 error. Details can be found in the [Bugs](<#known-bugs>) section. The issue was easily fixed and after a retest, no more errors were returned.

![W3C html home page validation results](assets/readmeimages/w3validator-pass.PNG)


## W3C CSS Validation Results

* Style.css – No errors were found.

![CSS validation test pass results](assets/readmeimages/w3c-css-validator-pass.PNG)

## JS Hint Validation Results

* Script.js - 2 undefined variables found.  Details can be found in the [Bugs](<#known-bugs>) section. The issues were fixed and after further testing, no more errors were returned.

![JSHint validation test pass results](static/images/testing/js-testing-passed.png)

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

1. The .hide class elements have a display setting of 'none' but the #answer-area id element has a display setting of 'grid'. 


10. As a result of the W3C html validation test, the index.html page had 1 error. 

![Index.html validation error]()

This error says that I have used an <a></a> tag within a button element for my link back to the home page from the end page, but according to the W3 Validator this is not allowed.  I therefore removed the button element and styled the anchor element to look the same as the other buttons, so from a user point of view there is no difference.

11. As a result of the JS Hint validation test, 2 undefined variables were found.

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