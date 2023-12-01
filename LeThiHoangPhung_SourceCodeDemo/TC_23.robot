*** Settings ***
Library     testworkspaces        WITH NAME     web

Test Teardown   Run Keyword If Test Failed   clean_up

*** Variables ***
${username}    nqlong@tma.com.vn
${password}    Lahai@123
${namespace}    Testspaces
${postname}    DemoCreatePost
${link}         https://spaces.avayacloud.com/
*** Test Cases ***
TC_03 Verify that the User who created the Group Space without inviting members
    Log To Console    Open Browser
    web.open_browser_spaces     ${link}
    Log To Console    1. Login with Account TMA
    web.login_spaces            ${username}        ${password}
    Log To Console    2. Logout Space
    web.logout_space 
    Log To Console    3. Close Browser
    web.close_browser 

** Keywords **
clean_up
    web.close_browser   
   