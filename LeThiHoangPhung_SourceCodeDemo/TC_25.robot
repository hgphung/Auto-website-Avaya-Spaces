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
TC_24 Verify that User can add favorite space
    Log To Console    Open Browser
    web.open_browser_spaces     ${link}    # robotcode: ignore
    Log To Console    1. Login with Account TMA
    web.login_spaces            ${username}        ${password}    # robotcode: ignore
    Log To Console    2. Create Group Space
    web.create_spaces           ${namespace}    # robotcode: ignore
    Log To Console    3. Add favorite space
    web.add_favorite    # robotcode: ignore
    Log To Console    4. Verify add favorite space 
    web.verify_add_favorite     ${namespace}     # robotcode: ignore
    Log To Console    4. Delete Space
    web.delete_space    # robotcode: ignore

** Keywords **
clean_up
    web.delete_space    # robotcode: ignore