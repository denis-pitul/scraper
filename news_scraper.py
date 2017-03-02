#!/usr/bin/env python3

import os
import time
import requests
from lxml import etree

US_NEWS_URL='https://news.google.com/news/section?cf=all&ned=us&topic=n&' + \
            'siidp=e5342d1cb1634b0f6f1ed41a0783e7102d59&ict=ln&edchanged=1&' + \
            'authuser=0'
RO_NEWS_URL='https://news.google.com/news/section?cf=all&ned=ro_ro&topic=n&' + \
            'siidp=e5342d1cb1634b0f6f1ed41a0783e7102d59&ict=ln&ar=1488356866'
script_path = os.path.abspath(__file__)\
    .replace('/%s' % (os.path.basename(__file__),), '')
us_email_file = script_path + '/emails/us_news.mail'
ro_email_file = script_path + '/emails/ro_news.mail'
ro_out = open(ro_email_file, 'w')
us_out = open(us_email_file, 'w')

ro_out.write('Subject: Stiri Romania\n\n')
us_out.write('Subject: Stiri US\n\n')
ro_start = time.clock()
root = etree.HTML(requests.get(RO_NEWS_URL).text, etree.HTMLParser())
for article in root.xpath("//a[contains(@class, 'article') " +
                          "and ./span/@class='titletext']"):
    ro_out.write('%s\n%s\n\n' % (article.getchildren()[0].text,\
                                 article.get('href')))

ro_end = time.clock()
ro_out.write('Generated on: ' + time.strftime("%c %Z") + \
             ' in %.09f' % (ro_end - ro_start))
ro_out.close()

us_start = time.clock()
root = etree.HTML(requests.get(US_NEWS_URL).text, etree.HTMLParser())
for article in root.xpath("//a[contains(@class, 'article') " +
                          "and ./span/@class='titletext']"):
    us_out.write('%s\n%s\n\n' % (article.getchildren()[0].text,\
                                 article.get('href')))

us_end = time.clock()
us_out.write('Generated on: ' + time.strftime("%c %Z") + \
             ' in %.09f' % (us_end - us_start))
us_out.close()
