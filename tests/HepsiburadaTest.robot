*** Settings ***
Documentation     A test suite with a single Gherkin style test.
...
...               Hello world
...               Hello world
Resource    ../helpers/resource.robot

#Test Teardown     Close Browser
Variables   ../helpers/config.py

Library     PageObjectLibrary
Library     SeleniumLibrary
Library     Process
Library     ../pages/BasketPage.py
Library     ../pages/CheckoutPage.py
Library     ../pages/HomePage.py
Library     ../pages/LoginPage.py
Library     ../pages/ProductPage.py
Library     ../pages/SearchPage.py

Suite Setup       Browser is opened to welcome page
Suite Teardown    Stop webapp and close all browsers

*** Keywords ***
Stop webapp and close all browsers
    Terminate all processes
    Close all browsers

Browser is opened to login page
    Open browser to login page

Browser is opened to welcome page
    Open browser to welcome page

*** Test Cases ***
Logged in member adds a homepage product to basket and goes to credit card checkout page
     [Setup]  Go to page  LoginPage
     Given user logs in with credentials  ozgur.kaya@arutesolutions.com    1QAZ2wsx
     When adds a homepage product to basket
     And navigate to credit card checkout page
     Then The current page should be    CheckoutPage

Search and filter results and mark product comment as helpful
     [Setup]  Go to page  HomePage
     Given User searches for    bluetooth kulaklık
     When filter search results with brand  JBL
     And filter search results with price between   750     1000
     And filter search results with color   siyah
     And choose a product from filtered results and open comments TAB
     And mark a comment as helpful

