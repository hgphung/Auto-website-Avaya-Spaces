*** Settings ***
Library     testworkspaces        WITH NAME     web

Test Teardown   Run Keyword If Test Failed   clean_up

*** Variables ***
${username}    Lethihoangphung.tk1@gmail.com
${password}    Lahai@123
${namespace}    Testspaces
${postname}    DemoCreatePost
${link}         https://spaces.avayacloud.com/
*** Test Cases ***
TC_02 Verify that User logs in to Avaya Spaces with a invalid username and password
    Log To Console     Open Browser
    web.open_browser_spaces         ${link}
    Log To Console    1. Login with Account TMA
    web.login_spaces                ${username}       ${password}
    Log To Console    2. Close Browser
    web.close_browser 
    
** Keywords **
clean_up
    web.close_browser

