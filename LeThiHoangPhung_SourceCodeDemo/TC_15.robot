*** Settings ***
Library     testworkspaces.py        WITH NAME     web

Test Teardown   Run Keyword If Test Failed   clean_up

*** Variables ***
${username}           nqlong@tma.com.vn
${password}           Lahai@123
${namespace}          Testspaces
${namemember}         ndde@tma.com.vn
${passwordmember}     Nguyendinhde24@
${link}               https://spaces.avayacloud.com/  
${postname}           DemoCreatePost
${yourcomment}        Hello Everyone
${role}               Admin
${description}        Blackpink
*** Test Cases ***
TC_15 - Verify that User 2 login Avaya Space and create Posts 
    Log To Console     Open Browser
    web.open_browser_spaces          ${link} 
    Log To Console    1. Login with Account TMA
    web.login_spaces                 ${username}        ${password}
    Log To Console    2. Create A Group Space Invite Member
    web.create_spaces                ${namespace}    ${namemember}    ${role}
    ${invite_link}=        web.get_link_invited     
    Log To Console    3. Logout Space
    web.logout_space
    Log To Console    4. Login With Account Invited Member
    Sleep    7s
    web.open_browser_spaces          ${invite_link}
    web.login_spaces                 ${namemember}        ${passwordmember}
    Log To Console    5. User 2 Create Post
    web.create_post                  ${postname}       ${description} 
    Log To Console    6. Verify Post created by User 2
    web.verify_create_post           ${postname}  
    Log To Console    7. Delete Space 
    web.delete_space

 
** Keywords **
clean_up
    web.delete_space