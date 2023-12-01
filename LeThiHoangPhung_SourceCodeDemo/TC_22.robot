*** Settings ***
Library     testworkspaces.py        WITH NAME     web
Test Teardown   Run Keyword If Test Failed   clean_up

*** Variables ***
${username}            nqlong@tma.com.vn
${password}            Lahai@123
${namespace}           Testspaces
${postname}            DemoCreatePost
${link}                https://spaces.avayacloud.com/
${yourcomment}         Blackpink in your area!!!
${description}         This is DemoCreatePost
${new_comment}         Kill this love
${namemember}          ndde@tma.com.vn
${passwordmember}      Nguyendinhde24@
${role}                Admin
*** Test Cases ***
TC_22 - Verify that User can delete comment Post
    Log To Console    Open Browser
    web.open_browser_spaces         ${link}
    Log To Console    1. Login with Account TMA
    web.login_spaces                ${username}        ${password}
    Log To Console    2. Create A Group Space Invite Member
    web.create_spaces                ${namespace}    ${namemember}    ${role}
    ${invite_link}=        web.get_link_invited 
    Log To Console    3. Create A Post 
    web.create_post                 ${postname}        ${description}
    Log To Console    4. Comment Posts
    web.comment_posts               ${postname}      ${yourcomment}       
    Log To Console    5. Verify Comment Post 
    web.verify_comment_posts        ${yourcomment}
    Log To Console    6. Logout Space
    web.logout_space
    Log To Console    7. Login With Account Invited Member
    Sleep    7s
    web.open_browser_spaces          ${invite_link}
    web.login_spaces                 ${namemember}        ${passwordmember}
    Log To Console    8. User 2 verify Post has been existed 
    web.verify_create_post           ${postname}
    Log To Console    9. Delete commnent Post
    web.delete_comment              ${postname}
    Log To Console    10. Delete Space
    web.delete_space
     
** Keywords **
clean_up
    web.delete_space
