#!/usr/bin/python

"""Gerrithubio  keep alive.

Usage:
    keep_alive.py -u <username> -p <password> -t <timeout> login

Options:
    -h --help       Show this screen.
    --username   Username for gerrithubio
    --password    Password for gerrithubio
    --timeout  If required add a timeout between clicks

"""

from docopt import docopt
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
import time

def main( arguments ):
    driver = webdriver.Firefox()
    #driver = webdriver.PhantomJS('phantomjs')
    #driver.get("https://github.com/login")
    driver.get("http://gerrithub.io")


    if arguments['login']:
        driver.get("http://gerrithub.io/")
        time.sleep(float(arguments['<timeout>']))
        open_gerrit = driver.find_element_by_xpath("//*[@id='menu-main-nav']/li[2]/a/span")
        open_gerrit.click()
        time.sleep(float(arguments['<timeout>']))
        github_signin = driver.find_element_by_xpath("//*[@id='gerrit_topmenu']/table/tbody/tr/td[3]/div/div[2]/a")
        github_signin.click()
        time.sleep(float(arguments['<timeout>']))

        username_element = driver.find_element_by_id('login_field')
        password_element = driver.find_element_by_id('password')
        login_element = driver.find_element_by_xpath("//*[@id='login']/form/div[3]/input[3]")

        username_element.send_keys(arguments['<username>'])
        password_element.send_keys(arguments['<password>'])
        login_element.submit()
        time.sleep(float(arguments['<timeout>']))



    result = driver.page_source

    if arguments['<username>'] in result:
        print "hooray"
    else:
        print  "failed"

    driver.close()

if __name__ == '__main__':
    arguments = docopt(__doc__, version='.1')
    print(arguments)

    main(arguments)

