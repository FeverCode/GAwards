# By FeverCode

## GAwards

## Table of Content

+ [Description](#description)
+ [Requirements](#requirements)
+ [Installation](#installation)
+ [Running Project](#running-project)
+ [Running Tests](#running-tests)
+ [Api Endpoints](#api-endpoints)
+ [Project Objectives](#project-objectives)
+ [Features](#features)
+ [BDD](#bdd)
+ [Technologies Used](#technologies-used)
+ [Licence](#licence)
+ [Authors Info](#authors-info)

## Description

 An application that allows a user to post a project he/she has created and get it reviewed by his/her peers.

Live link to the project
[GAwards](https://gawards.up.railway.app)

## Requirements

+ A computer running on either Windows, MacOS or Ubuntu operating system installed with the following:

```-Python version 3.8
    -Django
    -Pip
    -virtualenv
```

## Installation

+ Open Terminal {Ctrl+Alt+T} on ubuntu
+ git clone `https://github.com/FeverCode/GAwards`
+ cd GAwards
+ code . or atom . based on prefered text editor

## Running Project

+ On terminal where you have opened the cloned project
  + `sudo pip3 install virtualenv` - To install virtual enviroment
  + `virtualenv venv` - To create virtual enviroment
  + `source venv/bin/activate` - To activate virtual enviroment
  + `pip install -r requirements.txt` - To install requirements
  + Setup your database User, Password, Host, Port and Database Name.
  + `make makemigrations` - To create migrations
  + `make migrate` - To migrate database  
  + `make` - to start the server

## Running Tests

+ To run test for the project
  + `$ make test`

## Api Endpoints

+ <https://g-awards.herokuapp.com/api/posts/>
+ <https://g-awards.herokuapp.com/api/profile/>
+ <https://g-awards.herokuapp.com/api/users/>

## Project Objectives

+ View posted projects and their details
+ Post a project to be rated/reviewed
+ Rate/ review other users' projects
+ Search for projects
+ View projects overall score
+ View my profile page

## Features

+ Users can register and get welcome emails
+ Users can update their profiles
+ Users can post projects and get rated
+ Users can rate other users' projects
+ Users can search for projects
+ Users can view projects overall score
+ Users can view their profile page
+ Users can view their projects and their ratings
+ Users can view other users' profiles
+ Users can view other users' projects and their ratings
+ Users can view other users' overall score

## BDD

+ Landing page with various projects from different users. A navigation bar as well with home, login and register routes.
+ Create an account with a unique username,an email and password.
+ User can also create and update their profile.
+ Profile view displays users projects, click on the image to view more details of the project and get access to a live link.
+ Click on the upload submit your site button to add a project for others to view.


## Technologies Used

+ python3.8
+ django 3.2
+ Cloudninary (for hosting images)
+ Heroku (for hosting the project)
+ Rest framework (for API)

## Licence

MIT License

Copyright (c) [2022] [FeverCode]

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.

## Authors Info

LinkedIn - [https://www.linkedin.com/in/gedion-onsongo-112543210/]

Reddit - [https://www.reddit.com/user/stainscode]
