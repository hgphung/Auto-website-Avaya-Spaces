*** Settings ***
Library     testworkspaces.py        WITH NAME     web

Test Teardown   Run Keyword If Test Failed   clean_up

*** Variables ***
${username}            nqlong@tma.com.vn
${password}            Lahai@123
${namespace}           Testspaces
${postname}            DemoCreatePost
${link}                https://spaces.avayacloud.com/
${new_description}     Lalisa Manoban
${description}         Love sickgirl
*** Test Cases ***
TC_09 - Verify that User update description Post
    Log To Console    Open Browser
    web.open_browser_spaces         ${link}
    Log To Console    1. Login with Account TMA
    web.login_spaces                ${username}        ${password}
    Log To Console    2. Create Group Space
    web.create_spaces               ${namespace}
    Log To Console    3. Create A Post 
    web.create_post                 ${postname}        ${description}
    Log To Console    4. Change Description Post
    web.change_post_description     ${postname}        ${new_description}
    Log To Console    5. Delete Space
    web.delete_space

** Keywords **
clean_up
    web.delete_space


