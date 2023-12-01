*** Settings ***
Library     testworkspaces.py        WITH NAME     web

Test Teardown   Run Keyword If Test Failed   clean_up

*** Variables ***
${username}        nqlong@tma.com.vn
${password}        Lahai@123
${namespace}       Testspaces
${postname}        DemoCreatePost
${link}            https://spaces.avayacloud.com/
${description}     This is DemoCreatePost
*** Test Cases ***
TC_07 - Verify that User create Posts 
    Log To Console    Open Browser
    web.open_browser_spaces         ${link}
    Log To Console    1. Login with Account TMA
    web.login_spaces                ${username}        ${password}
    Log To Console    2. Create Group Space
    web.create_spaces               ${namespace}
    Log To Console    3. Create A Post 
    web.create_post                 ${postname}    ${description}
    Log To Console    4. Verify created create post
    web.verify_create_post         ${postname}
    Log To Console    5. Delete Space
    web.delete_space

** Keywords **
clean_up
    web.delete_space

