# Mission-to-Mars

## Project Overview
The goal is to create a web application using flask, as a custom interface to share and format scraped data in the form of a web page. This project specifically focusing on mars data and creating a personal webpage to display mars and earth information in a table, recent news article, images of mars hemispheres.

## Resources
-   Python 3.7.6, Flask 1.1.2, JupyterLab 2.26, VS Code 1.51.1
-   MongoDB 4.4.2
-   HTML5, Bootstrap 3

## Website Application 

-   Web Scraping
    Perfomed with a python script. Set parameters and code perform specified web scraping to collect and format data.

-   MongoDB
    The database simply stores the scraped data within a BSON format. This is necessary since there is no specific or orderly structure to the data.

-   Flask App
    A separate python script is used to define the framework. This bridges the communication between the scraping script and the database, as well as the html components needed to display the webpage. This app runs it without individually running the code.

-   HTML
    This file tidies the data in a desired format with html. The code contains parameters that allow the flask app to extrtact data.

## Website
The two added features are a colored scrape button and the hemispheres are diplayed with white backgrounds and no logo.

New Red Button
![New_Button](https://github.com/nfujikad/Mission-to-Mars/blob/main/Resources/button_bootstrap.png)

Default Hemisphere Images
![Default_Images](https://github.com/nfujikad/Mission-to-Mars/blob/main/Resources/hemisphere_original.png)

New Hemisphere Images
![New_Images](https://github.com/nfujikad/Mission-to-Mars/blob/main/Resources/hemisphere_bootstrap.png)
