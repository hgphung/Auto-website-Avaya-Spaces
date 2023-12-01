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
${role}               Member
*** Test Cases ***
TC_04 - Verify that Users invite members when they have successfully created Group Space with role "Member"
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
    Log To Console    5. Verify User 2 has been invited successfully
    web.verify_user2_invited         ${namespace}
 
** Keywords **
clean_up
    web.delete_space

    