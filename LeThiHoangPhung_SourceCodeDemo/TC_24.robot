*** Settings ***
Library     testworkspaces        WITH NAME     web

Test Teardown   Run Keyword If Test Failed   clean_up

*** Variables ***
${username}    ndde@tma.com.vn
${password}    Nguyendinhde24@
${namespace}    Testspaces
${postname}    DemoCreatePost
${link}         https://spaces.avayacloud.com/
*** Test Cases ***
TC_24 Verify that User can start meeting and end meeting
    Log To Console    Open Browser
    web.open_browser_spaces     ${link}
    Log To Console    1. Login with Account TMA
    web.login_spaces            ${username}        ${password}
    Log To Console    2. Create Group Space
    web.create_spaces           ${namespace}
    Log To Console    3. Start Meeting
    web.start_meeting
    Log To Console    4. End Meeting
    web.end_meeting
    Log To Console    5. Delete Space
    web.delete_space 

** Keywords **
clean_up
    web.delete_space  