# RobotFramework-Python3-SeleniumLibrary-WebTestSuite

![alt text](https://raw.githubusercontent.com/ozgurkayaist/RobotFramework-Python3-SeleniumLibrary-WebTestSuite/master/images/banner.png)

Tested on:
------------------
Robot Framework 3.1.2 (Python 3.8.1 on win32)

Python 3.8.1

SeleniumLibrary 4.1.0

Required installations:
--------------------
Python 3  -> https://www.python.org/downloads/

pip install robotframework

pip install --upgrade robotframework-pageobjectlibrary

pip install --upgrade robotframework-seleniumlibrary

pip install webdrivermanager

webdrivermanager firefox chrome --linkpath /usr/local/bin

pip install -r requirements.txt

Running Tests Commands:
----------------------
robot tests\HepsiburadaTest.robot

robot --variable BROWSER:Chrome tests\HepsiburadaTest.robot

robot --variable BROWSER:Firefox tests\HepsiburadaTest.robot

![alt text](https://raw.githubusercontent.com/ozgurkayaist/RobotFramework-Python3-SeleniumLibrary-WebTestSuite/master/images/cmd.png)

![alt text](https://raw.githubusercontent.com/ozgurkayaist/RobotFramework-Python3-SeleniumLibrary-WebTestSuite/master/images/report.png)

IntelliJ settings:
----------------------

Open  (File-> project Structure -> Project Settings -> Project)

Select (Project SDK-> New -> Python SDK)

Select (Add Python Interpreter->System Interpreter-> OK/Apply)

OS System Environment Variables (for Windows):
-------------------------------

Add the following lines to your PATH env. variable. You need to edit the username and version fields. Otherwise you should get the following errors.

  WebDriverException: Message: 'geckodriver' executable needs to be in PATH.
  
  WebDriverException: Message: 'chromedriver' executable needs to be in PATH.


C:\Users\YOUR_USER_NAME\AppData\Local\Programs\Python\Python38
C:\Users\YOUR_USER_NAME\AppData\Local\Programs\Python\Python38\Scripts
C:\Users\YOUR_USER_NAME\AppData\Local\salabs_\WebDriverManager\gecko\v0.26.0\geckodriver-v0.26.0-win64\
C:\Users\YOUR_USER_NAME\AppData\Local\salabs_\WebDriverManager\chrome\79.0.3945.36\chromedriver_win32\


Extra Information/Libraries/Updates/Documentations/Tools:
-------------------------------------------------------

https://robotframework.org/

