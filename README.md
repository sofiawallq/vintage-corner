# Vintage Corner

Vintage Corner is an online store with a carefully selected assortment of vintage items for the home. Every piece is unique and in general there is only one copy of every item, but you might find multiple items in the same category. On the webpage the user can view all products avaliable at the moment, sort them into categories, or filter them in a preferred order. The user can also register for a personal account where they can view and update their personal information such as delivery address, view their order history and save their details for future orders. The user have full CRUD functionality to update their profile or manage their shopping cart before making a purchase. 

Vintage Corner is a Full Stack e-commerce store build with the help of the Django framework, and in addition the users CRUD functionality the site admin also have the option to add, edit or delete items directly in the browser interface. 

The live website can be seen [here](https://vintage-corner-9f26bce1e332.herokuapp.com/)

![printscreen responsive website](static/images/printscreens/responsive_page.jpg)


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

I wanted the website to have a sort of vintage feel, but at the same time a modern touchg in the styling to be a good representation of me. The colour scheme is mild and the main purpose is to enhance the product images and the UX. As usual I set out with a high amibiton to design something beautiful with a really good user interface, responsive modals and nice-looking forms to fill out - all with the help of a perfect Bootstrap grid system. Some of the things I set out to do I absolutely achieved, while some visual effects just didn't fit into the projects timeframe. As always it came down to focusing on the functionality within the different apps, and since there are quite a lot of them for this project, the layout was forced to take a step back. I had to make sure the authentication process worked, that the user profiles was connected to checkout view, that the orders went through and that the emails were sent - along with a thousand other details that need to be in place when building an e-commerce store. I do believe I have a good foundation to stand on with both the UX and the user interface, but there are absolutely room for improvement. 


### Colour scheme

The colour scheme and inspiration for the webpage actually came from a somewhat unexpected place - namely my shower curtain. Everytime I look at it I fall in love with the combination of colours, so I thought "why not" and used it as my inspiration for the colours of the page.

![printscreen inspiration image](static/images/printscreens/inspo_image.png)

Below you can get a feel for the colour schema it inspired, and even though I didn't really have the time to follow it all the way through and had to lighten up some elements on the page due to readability, I think it's a really beautiful colour palett that works well with the vintage vibe. I will definitely come back to it when it's time to give some more love to the page and add on more of the colours to give the page some depth.

![printscreen colour palett](static/images/printscreens/colour_palett.png)


## User Stories

An agile approach was used to initialize the project - Epics to set the main structure for the user stories that needed to be written, and to make the project a little bit more approachable by bitesizing it. After the epics were set I wrote all the user stories and gave them labels to identify the must-haves, the should-haves, the could-haves and the wont-have - all in line with the MoSCoW prioritazion method. Every user story that I would work with then got some Acceptance Criterias and Tasks to make their purpose and what needed to be done even more clear. The final step of of the agile process was to give each user story a milestone label to help focus the work process even further. 

![printscreen user story](static/images/printscreens/example_user_story.jpg)

When it came down to the milestones I decided to divide them into 4 Iterations. User Stories concerning vital parts such as adding and viewing products, payment etc were part of the first iteration - and if I didn't finish them in the active iteration they would move into the next iteration, and something else had to be dropped or moved to another iteration. In real life I really see the value of working with iterations and I would have put a lot less "big" User Stories into each iteration for it to actually be realistic to manage. I would definitely not put so many vital parts in the first iteration ever again, but spread them out over the entire timeframe. In this scenario each iteration only lasted for two weeks and the timeframe continues on after my projects deadline - in a real worl project I would have split up each iteration into a 4 week period and as mentioned I would have made sure the vital functions was evenly distributed over all 4 iterations. But since we're working towards a hard deadline and with a short timeframe in this project, the Milestones are mainly there to show a more full circle approach to the agile way of working - but for the Vintage Corner project I don't really feel that they are applicable for the short amount of development time at my disposal.

![printscreen milestones](static/images/printscreens/milestones.jpg)

I ended up with a total of 25 User Stories to work with in the end, the majority o them made it into Done section of my Kanban Board. Two of the User Stories containt criterias about the ability to choose size and quantity on an item, which I think are vital in general to an online store. But in this case they are not current since the store sells one of a kind pieces that don't come in different sizes, so those two User Stories won't make it out of the Todo-section. Another User Story that will remain in the Todo-section is the one about identifying deals and offers, since it's a Vintage store with handpicked items the sale-vibe doesnt't really fit i nline with the business model and the store customer. They are not on this site to make a bargain but to find something unique for their home. 

![printscreen user stories](static/images/printscreens/stories_status.jpg)


Below are the epics and the User Stories I ended up with. 


__EPIC:__ View products and navigation

- As a Site User I can view a list of all products on the site so that I can find items I might like to purchase.

- As a Site User I can view detailed information on a specific product so that I can read more about it and make an informed decision before purchasing it.



__EPIC:__ Search, sort and filter products

- As a Site User I can search for products by name or category so that I can easily find what I am looking for without having to look through all products on the site.

- As a Site User I can sort the products into given categories so that I can easily find the products I am interested in, without having to go through all products on the page.

- As a Site User I can add a filter to the list of all available products so that I can view products according to filters such as name, price, rating, news etc.

- As a Site User I can add a filter to the list of products in a specific category so that I can view products according to filters such as name, price, rating, news etc. in the specific category of my choice.

- As a Site User I can select the quantity of a product I would like to purchase so that I have the option to buy more than one of that specific item if I want to.

- As a Site User I can easily select the size of a product when required so that I don't purchase a product that doesn't fit.

- As a Site User I can easily identify deals and special offers on products so that I can buy products at the best possible price.



__EPIC:__ Registration and personal profile

- As a Site User I can register for an account so that I can login and view my order history, update my personal information etc.

- As a Site User I can login to my registered account and edit my user profile so that I can save my payment details, view my order history and easily update my delivery adress.



__EPIC:__ Administrate products on site

- As a Site Admin I can easily add new items to my online store so that the site is always up to date with available products for purchase.

- As a Site Admin I can edit and update the product details so that the price, description, image etc. are always correct and up to date.

- As a Site Admin I can delete a product from the site if they are no longer available so that the customers don't accidentally buy products that are not available.



__EPIC:__ Shopping cart

- As a Site User I can easily add products to my shopping cart so that I can purchase the products I am interested in.

- As a Site User I can easily access my shopping cart at any point so that I can view what products I've added so far and the total amount spent.

- As a Site User I can update the items in my shopping cart when viewing it so that I can update the quantity, size or remove the product before checkout.



__EPIC:__ Purchase and checkout

- As a new Site User I can easily enter my payment information so that I can check out quickly and smoothly.

- As a Site User I can sign in to my account to get my saved payment information so that i don't have to fill it out every time I make a purchase.

- As a Site User I can view an order confirmation after chechout so that I can verify that my order is correct.

- As a Site User I can receive an email order confirmation to my chosen email address after chechout so that I can control my order later without having to sign in to an account.



__EPIC:__ Reviews and newsletter

- As a Site User I can read ratings and reviews on products so that I can make an informed purchase decision.

- As a Site User I can rate and write a review about a product, or the website in general so that I can share my experience and help other customers make informed decisions.

- As a Site User I can subscribe to a newsletter so that I don't miss out on deals and offers, new products I might like etc.

- As a Site Admin I can send a newsletter to registered email adresses so that the customers know about new products, specila offers etc.



## Wireframes

Wireframes for both the mobile design and larger devices such as tablets and computers were made using [Balsamique](https://balsamiq.com/).

I really love the process of creating wireframes since you don't really take in limitations such as time and coding experience into the process - you just create what you like and end up with a couple of inspiring frames that you really strive to make a reality. Soem changes were made along the way due to issues with responsivness and some features not looking so great when coming to life - but mainly I stuck to the wireframes. 

As some might notice there are no wireframes for the reviews page, since this feature came about later in the project when I felt the need for more custom models and more interactive features on the site. I also missed to create a wireframe for the shopping cart, and went straight for the checkout view. Luckily there is a shopping cart view on the actual webpage.

Below are some examples of my wireframes:

The first wirefram shows the landing page with all its features such as header, navigation menu with drop-down options, the searchbar, the account icon with its drop-down options and the little shoppingcart. You can also see selected products below a large jumbotron featuring an image, and the footers content at the bottom. 

![printscreen](static/images/wireframes/landing_page.png)

The wireframe for a detailed product page shows all the features I think are vital for the user - such as a product image, product name, a description of the product, the price and of course the option to actually put it into the shopping cart. 

![printscreen](static/images/wireframes/detailed_product_page.png)

I wanted the checkout view to containt two elements - a form to fill out all the delivery and pyament information, and a summary of the order so that the user can take one last look at it before they commit to the purchase. 

![printscreen](static/images/wireframes/checkout_view.png)

As mentioned all pages also got some mobile wireframes, for example the landing page is simply a responsive version of the one for larger screens, but here the products stack on top of each other and the navigation bar is an icon with drop-down functionality instead. 

Here is also the wireframe for the personal profile page where the user can update their personal information and view previous orders. 

![printscreen](static/images/wireframes/mobile_laning_page.png)![printscreen](static/images/wireframes/mobile_personal_profile.png)

There were 18 wireframes made in total, which can all be found [here](static/images/wireframes).


## Project planning

I started out with setting up pretty much the same file structure as the Boutique Ado project - since there are alot of apps and additional features when creating an e-commece store it's really easy to get lost somewhere in the many maaany folders and files. I did decide to go in a different direction with the static folders for CSS and JavaScript than what was made in the code along project - the Boutique Ado project had multiple folders with CSS-styling and js-files belonging to each app, but after a while I just felt that it made the structure more messy since I am the only one working on the project. I see the value when multiple people are involved, but in this project it just felt redundant.

Next part of the process was to tackle the User Stories so that I had something to achieve with each feature that was added to the page, more on that process below. After that the wireframes were created, and lastly the Entity Relationship Diagrams to plan the custom models that were needed were made.

After that I started building the actual e-commerce store, while at the same time I was figuring out how the Facebook page would look and drawing out some form of marketing strategy.


### Agile methodologies

- Kanban board - I used the Project Board in GitHub for the main planning of the Project. Issues were created as User Stories, with Acceptance Criterias belonging to each User Story. The User Stories were also assigned with tasks, to clarify for myself what each User Story demanded of me. As I love working on the design of a web page it's easy to put way to much time on that part, so the User Stories really help me to focus on the functionality of the project first and foremost.

- Epics - I really understand the value of Epics for large projects, to give the team a better overview of the projects User Stories and further prioritize the work process. I would have loved to work with even more Epics to break up the User Stories since I feel like some Epics are a little "heavy" with Stories (such as the Search, sort and filter products), but I had to move on to the next part of the planning so at that point I went with the Epics I had. 

- Milestones - Milestones were used as iterations and split the work into 4 iterations with its own Stories. I tried to evenly distribute the Stories so that each iteration would have pretty much the same amout of Stories - but if I would have added Story Points into the Agile mix I would have realized early on that some Stories in the first iterations would have demanded fewer Stories to accompany them in that specific iteration - there were simply to many demanding Storiews in the same iterations, as I talked about in the User Stories section above.

- MoSCoW Prioritization - The User Stories are labeled with one of the following four categories, all according to the MoSCow prioritization methodology:

  - Must Have: Features and requirements that are absolutely neccessary for the product to function and for the website to fulfill its purpose. These User Stories have the highest priority. 

  - Should Have: Important features that should be included if possible, but they are not critical for the website to function.

  - Could Have: Desirable features that can be added if there is enough time and resources.

  - Won’t Have: Features that will not be included in the project at this point, but might be a desirable feature in future development. 

![printscreen moscow open issues](static/images/printscreens/open_issues_moscow.jpg) 
![printscreen moscow closed issues](static/images/printscreens/closed_issues_moscow.jpg)



### Database Design

The database design consists of a main project directory called vintage_corner, and then separate apps for pretty much every feature on the page. The About page is the only page on the site one that lives in the same app as a different template - due to the fact that it doesn't need any models, views etc of its own.

![printscreen root directory](static/images/printscreens/root_directory.jpg)


__Entity Relationship Diagrams(ERD)__

Tree custom models were made for this project - one for managing all Products in the store, one to handle the Contact form in the contact app, and one to manage Reviews. Many more models exist within the project but they all come from the Boutique Ado code along project, and are somewhat or not altered at all - many of them have gotten an extra field or two but don't feel altered enough to be called custom.

Below are the ERD's that were drawn out for the project. The User model is handled by the Django Framwork, but it plays an importanty role in my Review model since it has a one-to-many relationship - making sure signed in users can write many reviews connected to their one profile. The Review model also has a ForeignKey in the form of a product-field that is connected to the Product model, so that a user is able to write a review about a specific product that they have bought if they wish to.


![printscreen entity relationship diagram](static/images/printscreens/erd_data_models.jpeg)

I actually had a model for a response-function as well where users could write a response to a review that somebody else had written, but to many aspects weren't working at the time so I decided to skip it for now and save it for future development.


## Features

### Existing features

### Header

The header has quite a few elements in it, even though it looks pretty clean. It has the name of the store, a search bar to search for products, a navigation menu, a section for management of the users personal profile (plus product management for superusers) and a shopping cart that takes the user to a shopping cart view when clicked. The shopping cart is also always updated with the total amount spent so far during the user session, if the user has added items to their cart that is. At the moment the search bar only filters throught product-realed querys, but I would love to add functionality so that it searches through the entire page in the future. 

![printscreen header](static/images/printscreens/header.jpg)

The mobile version containts pretty much the same features but presented in a responsive way, fitting into different screen sizes, which you can see in the navigation-section below. 



### Navigation menu

The navigation menu consists of a built-in drop-down menu if the user wishes to look at a specific product category or simply view all products on the page. It also contains links to the About page, a Contact page and a Reviews page - if the user wishes to read what other users think about the webshop and the products.  

![printscreen web page navigation menu](static/images/printscreens/nav_bar_large_screens.jpg)

With the help of Bootstrap and some custom CSS styling the navigation menu becomes a drop down feature on smaller devices. Features such as My Account, Search and the Shopping cart icon are not part of the drop-down menu but are always visible as separate icons for good UX. As you can see all the icons have a drop-down functions, such as the search bar in the image below.

![printscreen mobile drop down navigation menu](static/images/printscreens/mobile_dropdown_menu.jpg) ![printscreen mobile drop down navigation menu](static/images/printscreens/mobile_dopdown_search.jpg)



### Home page & Footer

The home page consist of only three sections apart from the header - a large jumbotron image to set the feeling for the user when they first land on the page, along with a big tagline that clarifies what the store is all about. Below that is a portion sized section of the all products view, where the user can get a quick look at the newest additions to the store - along and a button to redirect the user to a page where they can view all products in the store. 

![printscreen home page](static/images/printscreens/landing_page.jpg)

![printscreen home page product section](static/images/printscreens/landing_page_products.jpg)

Below those sections is the footer, which contains links to the stores social media and a newsletter sign-up form for users who wish to opt-in on that. It lacks a little bit on the layout but works as it should. The sign-up form is embedded via Mailchimp and when a user opts in for a newsletter they are added to Vintage Stores Contact list. 

![printscreen footer](static/images/printscreens/footer.jpg)



### Product list page

When navigation to the Products page the user has the option to either view all products on the site, or choose a specific category to filter out products. The categories can be found in the navigation bar at the moment. 

![printscreen all products page](static/images/printscreens/all_products_view.jpg)

Active category is shown to the user below the page headline.

![printscreen products filtered into category](static/images/printscreens/active_category.jpg)

They also have the option to Sort the products by either price, name or news. 

![printscreen products sorted by](static/images/printscreens/sort_by_filter_price.jpg)

The product page is ressponsive and sorting products works well in this view also.

![printscreen mobile products page](static/images/printscreens/mobile_all_products_view.jpg) ![printscreen mobile products sorted by](static/images/printscreens/mobile_sort_by_filter_price.jpg)



### About page

The about page containts some general info about the company behind the store. It also provides the user with important links to Terms & Conditions, Privacy Policy and Shipping information. I would have liked to put all of those important documents under its own headline in the navigation menu, but since time is of the esseence I had to settle with putting it all in here right now since I didn't really have the time to figure out the layout for that section in the navigation menu. 

![printscreen about page](static/images/printscreens/about_page.jpg)

By clicking one of the links the user is taken to a page with the entire Privacy Policy, generated by a Pricay Policy generator. The layout lacks some finess at the moment, but I felt the most improtant thing was to actually have a policy like this present on the page. The are responsive with the help of some simple Bootstrap styling. 

![printscreen privacy policy](static/images/printscreens/privacy_policy.jpg)



### Contact page

On the Contact page the user has the option to fill out a handy Contact Form if they want to get in touch with the store. The contact form is connencted to the Django admin panel so that the administrator can view incoming questions and inquiries from site users and reply to them. In line with a user friendly interface the site user gets an immediate respons validating that the message has been sent successfully, or if there are any errors in the field input when filling out the form. The respons is in the form a Success-message generated with Bootstrap Toasts-messages, which are used throughout the site for information and validation. 

![printscreen contact form](static/images/printscreens/contact_form.jpg)

The contact form is responsive and user friendly on all screen sizes and devices. Error handling works as it should on both small and large screens. You get to practice some swedish while viewing the images as well :)

![printscreen mobile contact form](static/images/printscreens/mobile_contact_form.jpg) ![printscreen field input error contact form](static/images/printscreens/mobile_contact_form_error_input.jpg)



### Review page

On the review page a site user can read reviews that have been written about the site in general, or read a product-review that the author have previously bought. There is also the option to click a button and get redirected to a page where they can write a review of their own. In order to write a review the user must be registered and logged in to their account, so that the view can fetch information about the users previously bought products and display them in a list to the user. 

![printscreen review page](static/images/printscreens/reviews_page.jpg)

As you can see SofWal has been very active on the review page, but that is just to show that when the number of reviews posted is more that six the user can browse multiple pages with the help of a "Next" and a "Previous" button for a better UI. The page is of course responsive, as you can see below. 

![printscreen mobile review pages](static/images/printscreens/mobile_review_page.jpg)

When signed in the user can choose to write a review about a previously bought product from a drop-down menu, or simply write a general review about the store. 

![printscreen add a review form](static/images/printscreens/add_a_review.jpg)

There is a lot of potential future features and developments that can be done to this page - I would love to have options for the user to edit or delete their reviews, write a response to somebody elses review and add images or videos to go along with their review - a user interaction like that would be gold for any site! But focus for now had to be on the functions that need to be in place for an online store, so additional content like this will have to wait. I am also not thrilled abot the design of the page, but again - function before style at this point. 



### Register for an account/sign in 

The user has the option to register for an account on the page, to be able to access their own personal profile page in the future. Or they can sign in to an existing account if they have already registered for one. Either way there's a possibility to do both in separate forms on the site - forms that got some styling with the help of Django Crispy Forms and they both contain password validation. Both options are accessible to the user through the "My account" icon in the page header, which the user can find on all pages of the site. 

![printscreen sign up form](static/images/printscreens/sign_up.jpg)

Both forms are responsive and works well on mobile screens. 

![printscreen sign in form](static/images/printscreens/sign_in.jpg)

Before a user is signed out they need to validate that they want to sign out from their account.

![printscreen sign out](static/images/printscreens/signout.jpg)



### Personal profile page

On the personal profile page the user can view their saved delivery information, update that information if they want to, and view a list of previous orders - if they have any. The user also ahs the option to delete their account if they wish to, due to restrictions from policys such as GDPR.

![printscreen personal profile page](static/images/printscreens/personal_profile.jpg)

They also have the option to update their personal information on this page, which is then saved instantly in the database and the user gets a success-message for confirmation. 

![printscreen update personal profile](static/images/printscreens/mobile_update_personal_profile.jpg)



### Product management

Under the "My account" icon in the header a superuser gets access to a view called Product Management, where they can add products to the site directly in the browser or edit/delete existing products. The database is updated in real-time with the superuser interaction and the whole function provides easy management and an interface with full CRUD-functionality for the store owner, without having to manage the page via the Django Admin panel.

![printscreen add product](static/images/printscreens/add_product.jpg)

The add and edit functions works well on small screens as well and the interface is easy to use. 

![printscreen edit product](static/images/printscreens/edit_product.jpg)

When a superuser is signed in to their account the Edit/Delte functionality is accessible via the product pages as well thanks to the links that are present in connection to the products. 

![printscreen edit_delete links](static/images/printscreens/edit_delete_links.jpg)



### Shopping cart view

In the shopping cart the user has the ability to view the entire content of their shopping cart. They also have the option to remove items from the cart if they wish to. The total amount of the order in the shopping cart is updated in real-time with user interactions such as adding or removing a product, and so is the database. 

![printscreen shopping cart view](static/images/printscreens/shopping_cart.jpg)

The shopping cart has pretty much the same layout on smaller screens, only responsive. I'm not thrilled about the look of the order summary on small screens since the images are to compressed, but that is an issue for the future.

![printscreen mobile shopping cart](static/images/printscreens/mobile_shopping_cart.jpg)

When a user adds an item to their cart a success-message shows up on the scrren showing the entire content of their cart so far, and the total amount spent. 

![printscreen add to cart](static/images/printscreens/success_add_to_cart.jpg)

If a user tries to add an item to the shopping cart that is already in there, they get an error message since there is only one of each item in the store.

![printscreen error add to cart](static/images/printscreens/error_add_to_cart.jpg)



### Checkout view

In the checkout view the user gets a last look at their order in the form of an order summary, so that they have the option to go back and change it if they wish to. In the checkout view the user can also fill out a form with delivery information and provide the store with credit card information to finalize the purchase. Here the user can opt in to save their personal information to their account if they are signed in, and if not signed in they are given the option to do so. The card payment is connected to Stripe.  

![printscreen checkout view](static/images/printscreens/checkout_view.jpg)

![printscreen checkout mobile view](static/images/printscreens/mobile_checkout.jpg) ![printscreen checkout mobile view two](static/images/printscreens/mobile_checkout_view-2.jpg)

Every field has error handling to inform the user of what went wrong - again we get the opportunity to learn a little swedish here, but for those of you who aren't fluid in the language, the error message tells us that the cards expiration date has passed.

![printscreen card validation](static/images/printscreens/card_validation_2.jpg)

Upon successful checkout the user is redirencted to an order confirmation page, along with a successmessage containing the order number. The user will also recieve an order confirmation to their registered email address. 

![printscreen order confirmation](static/images/printscreens/order_confirmation.jpg)

When the order is completed the products that have been bought are removed from the site, but they remain in the database so that the store admin can still view the products in the customers order on the admin panel. 



### Potential future features

I see alot of potential features in the future - I would love to implement a rating system and the ability to read reviews on products on the detailed product page, but that would mean that there would have to be a number of the same item in stock, and that seems unlikely in a Vintage Store. 

As mentioned before a more interactive reviews page would be nice. Where users can interact with each other in more than just a plain review - share their favourite vintage items at home and edit their own reviews if they want to - to create almost like a interactive forum on the site would be really cool!

Another really important feature to implement is the ability to search the entire site with the help of the search bar. At this point it only searches for product related items, but as a user I want the option to write shipping in the search bar and be redirected to the page contaning information about shipping. But that would be to massive to deal with at the moment. 

Some updates on the navigation menu on smaller screens is much needed from a UX/UI point of view because I am not thrilled about how some features overlap at the moment. 

I would also like for all headlines on the page to be linked to an actual page, since clickable headlines feels like a must on most websites now for a really good user exeperience.

I would also like to implement a Category selector on the actual product page, maybe above the "Sort by" box, and not only in the navbar for a better user interface. 



## SEO optimization, Meta and Marketing

When it was time to start sorting out the meta for the e-commerce store I started thinking about who the customer might be - who buys old and slightly quirky products for their home? To summarise them I think the majority of the customers are really enthustiatic collectors who love the thrill of finding just the right vintage product. I think they have a steady income since the store sells vintage items in the higher price range, and I think they like to have few but unique products in their home that you don't find everywhere. I also think they are really conscious consumers who likes to know the history behind the product they are purchasing and love the thrill of a good vintage find.

I absolutely think they use social media platforms, mainly Instagram and Facebook to get tips on good vintage stores and inspiration on what items to search for. I think they are active on platforms such as X as well, but these types of products doesn't really fit that type of content. In Sweden where I'm from this would be the perfect store for the typical swedish hipster nowadays - environmentally aware and likes to buy used items, striving to be unique in every way possible and therefor might end up with the exact same vintage items as every other hipster. But they are an easy market to target through social media. 

I would have liked to added a few external pages with rel-attributes to optimize the SEO, for example other vintage stores or maybe to a site that tells the story behind vintage products, but there wasn't really time to do the research. So at this point I think only my social media link has a rel-attribute - so the potential for improved SEO is big!


### Marketing Strategy 

Since it's a curated Vintage assortment it doesn't fit the aura of the page to market it through sales, deals and big adverts on multiple platforms - that's not the core of the store and its products. Vintage is all about slowing down and taking its time, so the marketing strategy would be to build longterm relationships with our customers - spread the word via satisfied customers, get them to discuss their purchase in social media and different vintage forums, get them engaged when we go out on shopping travels to curate new products for the store - simply go for an organic growth and a slow strategy in line with the items we sell. 

Another good way to go for a store like this would be newsletters via email - the content would be focused on building a relationship with the customer rather than screaming about a sale, so images from the latest bying trip, people we meet along the way and colaborations with other vintage stores would be great content! Along with a few of the items in stock at the moment. 



### Meta tags and keys

When it was time to set some meta tags and keys I started searching for different types of Vintage Stores online to see what type of meta content they use, which wasn't as easy as I thought due to the fact that many stores load in meta services from companies like Google into their head, so the actual keys and tags are stored elsewhere and can't be viewed with DevTools. But on the other hand I learned about special social media tags that way, so I tried implementing that on my page as well. 

The plan would be to update some of the meta keys according to what items are in the shop at the moment, since the assortment varies quite alot. I tried to think about both short tail and long tail keywords but ended up with mostly long tail at the moment. I would love to add some more short tail to reach a broader audience and appear in more search results, so that is absolutely something that can be worked on. 

![printscreen meta content](static/images/printscreens/meta_tags.jpg)



### Business model 

I like the idea of a proper business model for my store, but since I didn't really have the time to write one I asked ChatGPT for one and I think it looks alright so I'll paste it in for the sake of having one. I think the AI nailed the customer segments since they are pretty much the same as what I discussed a little earlier. 

__Value Proposition__
Unique and High-Quality Vintage Items: Vintage Corner offers carefully selected items that cannot be found in mainstream stores.
Sustainability: Promotes reuse and reduces environmental impact.
Nostalgia and Style: Vintage designs provide customers with the opportunity to create a personalized home with character.

__Customer Segments__
Home Decor Enthusiasts: Individuals looking for unique and distinctive home decor items.
Eco-Conscious Shoppers: Customers who value sustainability and reuse.
Collectors: People who are interested in specific, period-authentic pieces.

__Channels__
Website: A user-friendly and visually appealing e-commerce platform.
Social Media: Platforms like Instagram and Pinterest to showcase products, inspire potential customers, and expand the reach.
Email Newsletters: Regular updates with promotions and decorating tips for subscribers.

__Customer Relationships__
Personal Interaction: Direct communication via chat, email, and social media.
Post-Purchase Support: Guidance on the care and maintenance of vintage items.

__Revenue Streams__
Product Sales: Primary revenue comes from selling vintage items.
Memberships: Special subscriptions for exclusive previews of new products.
Collaborations: Partnerships with interior design bloggers and stylists, offering commissions.

__Key Resources__
Inventory: A diverse range of vintage items.
Staff: Buyers, customer service representatives, and e-commerce developers.
Technology Platform: An e-commerce solution to enable smooth and efficient shopping.

__Key Activities__
Sourcing and Procurement: Identifying and purchasing high-quality vintage items.
Marketing: Actively promoting products through digital channels.
Order Fulfillment: Efficiently packing and shipping orders.

__Key Partnerships__
Vintage Suppliers: Collaborations with auction houses and antique dealers.
Logistics Partners: Ensuring reliable and timely delivery.
Influencers and Bloggers: To reach a wider audience and build credibility.

__Cost Structure__
Purchasing Costs: Expenses for acquiring products.
Marketing Expenses: Costs for digital campaigns and advertising.
E-commerce Platform Maintenance: Technical upkeep and design enhancements.
Logistics: Shipping and packaging costs.



### Facebook page

The Facebook page is pretty simple and straight forward, and hopefully it can still be viewed on the link below. Since there is no user iteractivity on the page right now there might be a risk that the link isn't working du to Facebooks business page protocol. I think the most important part of the stores Facebook page is to continuolsy upload new items so that the customers don't miss out on anything. To tell the stories behind the products would be a nice touch, and maybe how and where the store found them. To sell through story building is extremly important for this type of store where you don't push products through sales and large marketing campaigns. 

![facebook cover](static/images/printscreens/facebook_cover.jpg)

Hopefully the posts will spark interactivity with the users. 

![facebook posts](static/images/printscreens/facebook_second_view.jpg)

Images seems like a vital part of a Facebook page to catch the eye of a user when they scroll through the massive amount of posts in their Facebook feed. 

![facebook pohotos](static/images/printscreens/facebook_photos_and_post_view.jpg)


You can view the page at: [Vintage Corner Facebook page](https://www.facebook.com/vintage.corner.eshop/)



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
- AWS S3 - used to store all product images/media files for deployed site
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

The manual testing consisted of not only the things listed below, but the testing also meant asking everybody I know to test the website and all its functions - such as filling out the Contact form, adding products to the cart, make purchases with the Stripe test-card number, sign up for an account, log in to their account, deleting their account, edit their profile information, viewing previous orders, writing a review and every other possible interaction there is. All while I checked the admin panel for real-time action. 

I also asked them to check that the email verification and confirmation was working the way that it should. 

### Responsivness 

Mainly thanks to Bootstrap the page is responsive on all devices - from mobile phones to tablets, laptops and larger screens. It reaches a max-width on larger devices as to not look to stretched out and looks alright on even the smallest mobile screens. I've asked friends and family to try it out on different devices to get as many opinions in as possible. 

### Browser compability

The project has been tested on different browsers such as: Google Chrome, Safari, Microsoft Edge and Mozilla Firefox. It looks and functions pretty much the same on all browsers. 

### Validator testing

- HTML - through the official W3C validator. Some issues regarding links and list objects came back from the HTML-validator, but they are all fixed now. 

![printscreen html validator](static/images/printscreens/html_validator.jpg)

- CSS - through the official Jigsaw validator. No issues came back when i ran the code through the CSS validator. 

![printscreen css validator](static/images/printscreens/css_validator.jpg)

- JavaScript - the JavaScript check in JSHint came back with no issues except for a few warnings regarding syntaxissues with specific browsers, but I chose to igonre that. 

![printscreen javascript validator](static/images/printscreens/jshint_validator.jpg)

- Python - PEP8 Python Validator

There were quite a few files to run throught the PEP8 validator, somewhere around 70 since there are a lot of apps ... If there is an easier way to test all the files at once I do not want to know about it until long after this course has ended due to the frustration it would provoke. There were alot of blank spaces to remove and many too long lines that needed fix, but no other major issues with the python files.

![printscreen python validator](static/images/printscreens/pep8_validator.jpg)

When testing the page using Lighthouse for Chrome, 

![printscreen lighthouse]()



### User Story testing

The User Story testing has been performed throughout the development. When building the site I moved the Stories I was working on into the "In Progress" column on my Kanban-board, and then checked that every acceptance criteria and task was fulfilled before moving it into the "Done" column. As you can see there are still Stories left in the "In progress" column, due to the fact that some criterias have been met, but not all of them. The project is still functional but I don't want to move them into the Done column until the criterias are fully met. 

For example the Acceptance Criterias in the User Stories regarding Reviews haven't all been met, and will not be fulfilled at this point in the project. Some of the criterias concern the ability to add images and videos to a review, and to be able edit a review and leave a response to somebody elses review - so they will both remain in the "In Progress" column for now. 

At the moment a users card information isn't saved to their personal profile, so the criterias in "Pay for products - returning customer" User Story hasnt been fully met at therefore it is not Done at this point either. 

And lastly the story regarding Signing up for a newsletter contains criterias about the ability to sign up for a newsletter at checkout, and criterias about being able to opt out from the mailing list via a link in the newsletter which I can't deliver at this point. 

![printscreen kanban board](static/images/printscreens/kanban_board.jpg)

Some User Stories haven't made it out of the "Todo" column due the fact that they a Stories that I do believe apply to e-commerce stores in general and therefor is valuable to include, but they do not apply to this particualr store due to the fact that you can not choose size or quantity on any of the products on the page, and we don't work with deals and offers so they will remain in the Todo part of the board for this project. 


### Bugs

- There are still some issues with storing the content of the shopping cart when you log in/log out during a shopping session, the cart gets emptied and I know the issue is regarding how the data is stored in the session, but I have to save that issue for the future. 

- For some reason my Toast message for when an item in the shopping cart is removed doesn't work and even though I've tried time and time again to fix it, I haven't been able to solve it. 

- I've also had some BIG issues with adding checkboxes to different parts of the site. I had one required checkbox in the checkout view that the user had to fill in to ensure that they accept the Terms and Conditions on the site, but no matter how many times I changed the code it didn't quite work with the POST-methods so instead it caused issues with fulfilling the payment process. So at the moment it's no longer present in the checkout view, but I am determined to get it back in there and get the whole process working. 

I also planned on having checkboxed for accepting the Privacy Policy on both the Sign up page and in the footer included in the newsletter sign-up form, but once again trouble emerged and I felt I didn't have the time to fix it. So again i really want them present because I know how important they are. 

- There is an issue with the CSS rules on some Samsung phones that use the Android Internet Browser, some of the colours get inverted som the colour scheme is alot darker in those browsers. It still works but it doesn't look like I intended, so I will have to dig deeper into that. 

- For some reason blue colour remain on some links when clicked in the deployed version, but since that's just an aesthetic issue I'll leave it for now.


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


5. Deployment with media files
- Install S3 Storage and Boto with the command pip3 install boto3
- Add ... to to your requirements.txt file with the command: pip3 freeze --local > requirements.txt
- Add 'storages' to your list of INSTALLED_APPS in settings.py.
- In setting.py add a these parameters to manage external storage in AWS and replace with correct paths were needed:
    AWS_STORAGE_BUCKET_NAME = 'bucket-name'
    AWS_S3_REGION_NAME = 'eu-north-1'
    AWS_ACCESS_KEY_ID = os.environ.get('AWS_ACCESS_KEY_ID')
    AWS_SECRET_ACCESS_KEY = os.environ.get('AWS_SECRET_ACCESS_KEY')
    AWS_S3_CUSTOM_DOMAIN = f'{AWS_STORAGE_BUCKET_NAME}.s3.amazonaws.com'
    DEFAULT_FILE_STORAGE = 'custom_storages.MediaStorage'
    MEDIAFILES_LOCATION = 'media/product_images'
    MEDIA_URL = f'https://{AWS_S3_CUSTOM_DOMAIN}/{MEDIAFILES_LOCATION}/'
- 


6. Deploy on Heroku
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

As always [Stack Overflow](https://stackoverflow.com/) has been my go to place everytime I've googled a piece of code for troubleshooting. 

Product info mainly from Wikipedia

I also chose to ask ChatGPT for a good example of a docstring, which I then altered for the different parts of Python code in the progress. But thanks to AI i got a good structure to work with.


### Media

[Pexels.com](https://www.pexels.com/)
[Unsplash.com](https://unsplash.com/)
[Favicon](https://favicon.io/emoji-favicons/)
https://imagecolorpicker.com/