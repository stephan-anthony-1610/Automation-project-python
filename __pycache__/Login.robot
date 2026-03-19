*** settings ***
Library SeleniumLibrary

*** Test Cases ***
Valid Login Test
    Open Browser https://qa.maayaa.ai/login chrome
    Input Text id='email' stephan.anthony1610@gmail.chrome
    Input Text id='password' St3ph4n*xd1610
    Click Button type='submit'
    Page Shoule Contain Dashboard
    Close Browser