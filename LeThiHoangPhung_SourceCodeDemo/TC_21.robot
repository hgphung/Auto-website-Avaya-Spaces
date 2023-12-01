*** Settings ***
Library     testworkspaces.py        WITH NAME     web

Test Teardown   Run Keyword If Test Failed   clean_up

*** Variables ***
${username}        nqlong@tma.com.vn
${password}        Lahai@123
${namespace}       Testspaces
${postname}        DemoCreatePost
${link}            https://spaces.avayacloud.com/
${yourcomment}     Blackpink in your area!!!
${description}     This is DemoCreatePost
${new_comment}     Kill this love
*** Test Cases ***
TC_21 - Verify that User can delete comment Post
    Log To Console    Open Browser
    web.open_browser_spaces         ${link}
    Log To Console    1. Login with Account TMA
    web.login_spaces                ${username}        ${password}
    Log To Console    2. Create Group Space
    web.create_spaces               ${namespace}
    Log To Console    3. Create A Post 
    web.create_post                 ${postname}        ${description}
    Log To Console    4. Comment Posts
    web.comment_posts               ${postname}      ${yourcomment}       
    Log To Console    5. Verify Comment Post 
    web.verify_comment_posts        ${yourcomment}
    Log To Console    6. Delete commnent Post
    web.delete_comment              ${postname}
    Log To Console    7. Delete Space
    web.delete_space
     
** Keywords **
clean_up
    web.delete_space
