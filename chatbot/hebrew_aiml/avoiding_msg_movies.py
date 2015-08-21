# -*- coding: utf-8 -*-
from answer_template import answer_template
import sys
import os
import site
from BeautifulSoup import BeautifulSoup
for site in site.getsitepackages():
    p = os.path.join(site,'xgoogle-master')
    if p not in sys.path:
        sys.path.append(p)
from xgoogle.search import GoogleSearch, SearchError
from xgoogle.browser import *
import wikipedia
# from browser import Browser, BrowserError

# from pygoogle import google
class avoiding_msg_movies(answer_template):
    def get(self, params=None):
        """
        gets the answer from the answer template
        :param params: msg = params[0], func = params[1]
        :return:
        returns the first template if is_random is false, otherwise returns random template
        """
        msg = params[0] + u"סרט ויקיפדיה"
        try:
            b = Browser()
            gs = GoogleSearch(msg)
            gs.results_per_page = 50
            results = gs.get_results()
            for res in results:
                # print res.title.replace('ynet','')
                try:
                    if (res.url is not None):
                        page = b.get_page(res.url)
                        soup = BeautifulSoup(page)
                        title = soup.find("title")
                        if (title is not None):
                            res = title.text.split('-')[0]
                            wikipedia.set_lang('He')
                            wiki_summary = wikipedia.summary(res.text)
                            print(wiki_summary)
                            break
                except:
                    continue
                print res
        except SearchError, e:
            print "Search failed: %s" % e




#a = avoiding_msg_ynet(None,None)
# a.get(["ynet.co.il:האם טביב ימכור את הקבוצה?"])
# res = a.get(["ynet.co.il:האם ביבי ימכור את המדינה?"])
#a.get(["ynet.co.il:מה יהיה עם הגז?"])
#a.get(["seret.co.il:המרגלת"])
