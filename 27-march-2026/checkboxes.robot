*** Settings ***
Documentation  handling checkboxes
Library  SeleniumLibrary

*** Variables ***
${url}  https://the-internet.herokuapp.com/
${url2}  https://testautomationpractice.blogspot.com/

*** Test Cases ***
Handling checkboxes
    [Documentation]  herokuapp checkboxes
    Open Browser  ${url}  chrome
    Maximize Browser Window
    Sleep    2s

    Click Element    xpath=//a[text()="Checkboxes"]
    
    Page Should Contain Checkbox    xpath=(//input[@type="checkbox"])[1]
    Select Checkbox    xpath=(//input[@type="checkbox"])[1]
    Sleep    2s
    Unselect Checkbox    xpath=(//input[@type="checkbox"])[2]
    Sleep    2s
    Close Browser

handling checbox in automation site

    [Documentation]  automation testing checkbox
    Open Browser  ${url2}  chrome
    Maximize Browser Window
    Sleep    2s


    Page Should Contain Checkbox    id=sunday
    Select Checkbox   id=sunday
    Sleep    2s

    Close Browser