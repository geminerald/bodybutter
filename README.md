# Bodybutter

[![Build Status](https://travis-ci.org/geminerald/bodybutter.svg?branch=master)](https://travis-ci.org/geminerald/bodybutter)

<p>Welcome to Bodybutter - an ecommerce website for the sale of handmade body butter products online.

This project is aimed at people who are interested in purchasing handmade skincare products and wish to have them tailored to their needs.

This project was submitted as the final milestone project for the Code Institute Full Stack web developer course.

For more info on the developer or my other projects you can check out my [website](https://geminerald.github.io/geminerald/)
</p>

## Contents:

- [UX](#user-experience)
    - [Project Goals](#project-goals)
    - [User Goals](#user-goals)
    - [Site Owner Goals](#site-owner-goals)
    - [User Stories](#user-stories)
    - [User Requirements and Expectations](#user-requirements-and-expectations)

- [Design](#design)
    - [Fonts](#fonts)
    - [Icons](#icons)
    - [Colours](#colours)
    - [Styling](#styling)
    - [Images](#images)
    - [Backgrounds](#backgrounds)

- [Planning](#planning)
    - [Wireframes](#wireframes)
    - [Site Map](#site-map)
    - [Flowcharts](#flowcharts)
    - [Databse Schema](#database-schema)

- [Features](#features)
    - [Implemented](#implemented-features)
    - [In Development](#features-in-development)
    - [To be Developed](#features-to-be-developed)


## User Experience

### Project Goals

The goal of this project is to allow consumers to buy handmade bodybutter products. Users can set up an account, add various items to a basket, place orders, review and update their information, track their order status and review or re-order previous orders.

Users will eventually be able to customise the products and have bespoke body butter products manufactured to their specifications.

### User Goals

* Get information about various body butter products.
* Order products.
* Create an account.
* Place Orders. 
* Track and update their orders.
* Access website from any device.
* Visually appealling and intuitive website.
* Contact site owners with any issues or questions.

### Site Owner Goals

* Generate revenue from product sales.
* Encourage user sales with promotions or offers.
* Collect user and order data to better serve user needs.

### User Stories

* "Any online platform needs to work just the same on my phone as on my laptop - if you have to use two different sites to do the same thing on two devices that's a bad user experience" - Mark Smyth
* "I would never buy anything from a site where you don't know who is running it or at least how to contact them" - Alan Yeates
* "It's a basic rule of any business: Make it easy for your customer to give you money" - Mary Conneely

### User Requirements and Expectations

Online shopping is more popular now than ever before - this was true before the current world health crisis and has only become more true since then. 
As both supply and demand have grown the nature of what an online shop needs to be and needs to supply has changed.
Any online e-commerce platform needs to be easy to use an navigate or users will find another one that is easier. 
Similarly it will need to be secure - useing safe authentication and payment methods are now necessary for an e-commerce platform.

### Requirements

* Easily act with the website at all stages.
* All elements are visually appealling without being distraccting.
* Learn about how the site works and the various products offered at a glance or skim.
* Add items to a cart and update it as needed.
* Securely place orders to purchase items.
* View previous and current orders.
* FAQ section to answer frequently asked questions.
* Contat the business as required.

### Expectations

* Website will work quickly, efficiently and intuitively across all devices.
* User information is stored securely.
* User payment information is not stored in the store database.
* All navigation is simple, intuitive and necessary - no clutter. 

## Design

<p> The overall design ethos of this website was to be in keeping with what a user would expect with a skincare brand. Colours and elements are soft, the colours particularly are chosen to evoke the feeling or memory of a trip to a spa or similar. </p>

### Fonts

Key qualities needed for the font of an online web shop are simplicity, in order to not distract or slow the user down, and clarity - so that they can quickly absorb anything they see.
With these criteria in mind the Oswald font was chosen.

### Icons

The icons for this project came from [Font Awesome](https://fontawesome.com/6?next=%2F) as they are universally highly regarded as having a great selection of icons for development.

### Colours

The colour palate was taken from [coolers](https://coolors.co/)

An image was uploaded which encapsulated the tone of the website and a colour scheme generated from this.

The individual colours are as outlined below:

- ![#fdb793](https://placehold.it/15/fdb793/000000?text=+) **"Macaroni and Cheese"** #FDB793 : This is used as a backgrould colour as it is a soft colour which goes well with most skin tones and doesn't pull focus.
- ![#0fa3b1](https://placehold.it/15/0fa3b1/000000?text=+) **"Viridian Green"** #0FA3B1 : This was chosen as a good contrast to the base colour - it shows up well against the softer peach colour and is reminiscent of colours seen in health spas.
- ![#b5e2fa](https://placehold.it/15/b5e2fa/000000?text=+) **"Uranian Blue"** #B5E2FA : This colour was chosen for the "Information" alerts - as a soft blue it will fulfil the standards and expectations of a blue message notification but it is softer than most blues used in this context - again reminiscent of a trip to the spa.
- ![#f9f7f3](https://placehold.it/15/f9f7f3/000000?text=+) **"Baby Powder"** #F9F7F3 : This colour was chosed as the "white" colour for the website - as a slightly gray off-white colour it avoids the harsher contrast which the pure white would create and helps to keep the contrast high but not too high.
- ![#eddea4](https://placehold.it/15/eddea4/000000?text=+) **"Medium Champagne"** #EDDEA4 : 

### Styling

#706563

```scss
$primary-color: #FDB793; // primary
$secondary-color: #0FA3B1; // secondary
$tertiary-color: #EDDEA4; // tertiary 
$white-color: #F9F7F3; // white
$off-white-color: #f2f2f2; // off-white
$black-color: #0f0a0a; // black
$required-color: #b8336a; // required-red
$error-color: #461220; // error-red
$success-color: #1b998b; // success-green
```

Layout Colours:

```scss
$text-on-white-color: #017735;
$main-nav-color: $secondary-color;
$main-footer-color: $secondary-color;
$main-background-color: $white-color;
$main-panel-color: darken($off-white-color, 5%);
```

Shadows:

```scss
$panel-shadow: 1px 1px 2px rgba(0, 0, 0, 0.4);
$text-shadow: 0.5px 0.5px 1px rgba(0, 0, 0, 0.3);
```

Transitions: 
```scss
$fast-transition: 0.25s all ease-in-out;
$slow-transition: 0.5s all ease-in-out;
```

Borders: 

```scss
$default-border-radius: 6px;
```

### Images

The images for this website were taken from [Pexels](https://www.pexels.com/) and [Unsplash](https://unsplash.com/)

Image editing was done via [Affinity](https://affinity.serif.com/en-us/)

### Backgrounds

## Planning

### Wireframes

The wireframes for this project were developed useing Balsamiq and exported as PDF files for ease of viewing.

<p>The wireframes for this project can be seen <a href="https://github.com/geminerald/bodybutter/tree/master/wireframes">here</a></p>

### Site Map

### Flowcharts

### Database Schema

## Features

### Implemented Features

### Features In Development

### Features to be Developed

* Home, About, FAQ pages
* Account and authentication system.
* Account detail updates.
* Product page with all products.
* Product Filters
* Contact Us Page and form
* Cart page and system
* Ability to update cart
* Checkout page with stripe itegration
* Create your own bespoke bodybutter.
* Automated email system for order lifecycle.
* Loyalty system.
