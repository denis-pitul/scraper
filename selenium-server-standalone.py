#!/usr/bin/env python3

import os
import time
from selenium import webdriver

script_path = os.path.abspath(__file__)\
    .replace('/%s' % (os.path.basename(__file__),), '')
email_file = script_path + '/emails/selenium.mail'
################################################################################
##########################   GET SELENIUM SERVER VER   #########################
################################################################################
driver = webdriver.PhantomJS()
driver.get('http://docs.seleniumhq.org/download')
downloadLnk = \
    driver.find_element_by_xpath("//p[contains(., 'Download version')][1]/a")
version = downloadLnk.text
url = downloadLnk.get_attribute('href')
################################################################################
##########################   GET SELENIUM MAVEN VER   ##########################
################################################################################
driver.get('https://search.maven.org/#search%7Cga%7C1%7Cselenium-java')
mvnVersion = \
    driver.find_element_by_xpath("//a[contains(@onclick, 'org.seleniumhq') " +
                                 "and contains(@onclick, 'selenium-java')]"
                                 ).text
driver.quit()
################################################################################
##########################   CREATE THE EMAIL FILE   ###########################
################################################################################
email_file = open(email_file, 'w')
email_file.write('Subject: Selenium versions\n')
email_file.write('\n')
email_file.write('selenium-server-standalone.jar:\n')
email_file.write('\tver: %s\n' % (version,))
email_file.write('\tlink: %s\n' % (url,))
email_file.write('\n')
email_file.write('Maven selenium-java:\n')
email_file.write('\tver: %s\n' % (mvnVersion,))
email_file.write('\n')
email_file.write('\nGenerated on: ' + time.strftime("%c %Z"))
email_file.close()
################################################################################
##########################          CLEANUP          ###########################
################################################################################
os.remove('ghostdriver.log')
