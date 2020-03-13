

# Graphic-Designer-Art
[![Build Status](https://www.travis-ci.org/Sreniok/graphic_design.svg?branch=master)](https://www.travis-ci.org/Sreniok/graphic_design)

Graphic Design-Art is a Django project where the owner can create a project, and they will be displayed on the main page where visitors can add to the cart. The user needs to register to make a purchase. After registration user will be able to fil with all details, including project description and payment.

## UX
 
The main page is showing all projects available for purchase with description and price. User can register to the website using a register tab in the navbar. If the user already has an account, he can log in using a login tab where can reset the password. In card, user can change the quantity of project and checkout where need to fill the form with all details and project information.

## Features

### Existing Features
- Simple website where user can make a purchase a graphic project.

### Potential future features
- The password reset will need to be fixed 
- upvote for the project  may be implemented 
- user can specify the size of the project when adding to cart 

## Technologies Used

* [HTML 5](https://html.spec.whatwg.org/) - basic templating language
* [CSS](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference) - site styling
* [Bootstrap](https://getbootstrap.com/) - HTML structure for mobile first navigation
* [JQuery](https://code.jquery.com/) - front end site functionality
* [JavaScript](https://www.keycdn.com/support/javascript-cdn-resources) - required code to action Stripe API
* [Django](https://www.djangoproject.com/) - python platform for project
* [Python](https://www.python.org/) - backend functionality
* [Stripe API](https://stripe.com/en-se) - API to process online payments
* [AWS](https://aws.amazon.com/) - devlopment platform 
* [Travis](https://travis-ci.org/) - test integration for site
* [Heroku](https://dashboard.heroku.com/) - site hosisting platform
- [JQuery](https://jquery.com)


## Testing
The website was tested using a debugger and was deployed to Travis for checking errors.

- Main page: add quantity work, and the amount is displayed right to the card 
- Registering: user can register, and information is displayed when is success
- Login/Logout: user can log in, or Logout with confirmation message also can reset the password if forgot (currently not working)
- Cart: the user can see his cart and make changes to quantity or checkout.
- Checkout: user needs to fill the form correctly if not error message shows up. user can leave post-code and project description empty

## Deployment
- The project is deployed to Heroku.
- Created Procfile and requirements.txt for dependencies.
- Linked my Github and environment with Heroku
- Static file and Media are stored on AWS
- Pushed to Heroku.
- Pushed to Github.
- A website can be found on Heroku (https://graphic-designe-art.herokuapp.com).
- The repository can be found on Github (https://github.com/Sreniok/graphic_design)


## Credits

### Content
- The text for section banner was copied from the [unahealydesign](https://www.unahealydesign.com)
- The project contains code from code institute Full-Stack Frameworks with Django

### Media
 The photos used in this site were obtained from google search.

