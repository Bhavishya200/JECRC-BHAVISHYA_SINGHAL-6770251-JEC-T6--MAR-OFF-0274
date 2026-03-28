*** Settings ***
Documentation  Opening of browsers
Library  SeleniumLibrary
*** Variables ***

${url}  https://www.cricbuzz.com/  #scaler variables
@{bikes}  ktm  kawasaki  honda  pulsar   #list variable
&{cars}  nissan=gtr  honada=civic  bmw=m5  #dict variable


*** Test Cases ***
Opening Chrome Browser
   [Documentation]  Chrome browser navigating to https://crickbuzz
   Open Browser   ${url}  chrome
   Maximize Browser Window
   Log  navigated to cricbuzz
   Log To Console    ${bikes}[1]  #when accessing only single value we use $
   Log To Console    ${cars.nissan}
   Sleep    3s

   Close Browser

#Opening firefox browser
#
#   [Documentation]  firefox browser navigating to https://crickbuzz
#   Open Browser   https://www.cricbuzz.com/  firefox
#   Maximize Browser Window
#   Log  navigated to cricbuzz
#   Log To Console    navigated to cricbuzz
#   Sleep    3s
#
#   Close Browser




Opening headless Chrome Browser
   [Documentation]  Chrome headless browser navigating to https://crickbuzz
   [Tags]  smoke
   Open Browser   ${url}  headlesschrome
   Maximize Browser Window
   Log  navigated to cricbuzz
   Log To Console    navigated to cricbuzz
   Sleep    3s

   Close Browser

Opening crickbuzz in edge browser

    Opening edge browser

*** Keywords ***

Opening edge browser

   [Documentation]  edge browser navigating to https://crickbuzz
   Open Browser   https://www.cricbuzz.com/  edge
   Maximize Browser Window
   Log  navigated to cricbuzz
   Log To Console    navigated to cricbuzz
   Sleep    3s

   Close Browser