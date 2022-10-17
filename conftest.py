import os
import pytest
from selenium import webdriver
from fake_useragent import UserAgent
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager

@pytest.fixture(scope="session", autouse=True)
def ses_class():

    # Run container
    port = 4487

    # for run docker local on M1
    # os.system(f"docker run -d --name mgm_seleniarm_chrome -p {port}:4444 -p 5900:5900 seleniarm/standalone-chromium")

    # for run docker local on Jenkins on other process
    os.system(f"docker run -d --name popravka -p {port}:4444 selenium/standalone-chrome-debug")
    time.sleep(3)

    # Chrome options
    options = webdriver.ChromeOptions()
    options.add_argument('--ignore-ssl-errors=yes')
    options.add_argument('--ignore-certificate-errors')

    # Run Chrome with options
    pytest.driver = webdriver.Remote(
        command_executor=f'http://localhost:{port}/wd/hub',
        options=options
    )
    
    yield pytest.driver
    pytest.driver.quit()
    # Post-conditions
    time.sleep(3)
    pytest.driver.close()
    os.system("docker rm --force popravka")


# options = webdriver.ChromeOptions()
# options.add_argument('--ignore-ssl-errors=yes')
# options.add_argument('--ignore-certificate-errors')


# @pytest.fixture(scope='session', autouse=True)
# def driver():
#     driver = webdriver.Remote(
#         command_executor='http://localhost:4440/wd/hub',
#         options=options
#     )
#     driver.maximize_window()
#     yield driver
#     driver.quit()


""" Код для запуска с ПК  """
# @pytest.fixture(scope='session', autouse=True)
# def driver():
#     driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
#     driver.maximize_window()
#     yield driver
#     driver.quit()


"""
Перед запуском docker pull selenium/standalone-chrome-debug:3.141
docker run -d --name selenium_hillel -p 4444:4444 -p 5900:5900 selenium/standalone-chrome-debug
docker rm selenium_chrome
docker stop selenium_chrome
docker rm --force selenium_chrome
"""
