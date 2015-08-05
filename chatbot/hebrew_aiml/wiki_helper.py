# -*- coding: utf-8 -*-
import wikipedia
import random


def get_category(word):
    wikipedia.set_lang('He')
    value = wikipedia.search(word,10,True)
    if len(value) != 0:
        catagories = wikipedia.WikipediaPage(value[0]).categories
        if len(catagories) != 0:
            catagories = filter(lambda a: a != u'ערכים בלי תמונה', catagories)
            # lens = []
            # for category in catagories:
            #     res = wikipedia.page(category)
            #     lens = [len(res.links)]
            # max_len = max(lens)
            # idx = [i for i, x in enumerate(lens) if x == max(max_len)]
            # max_category = catagories[random.choice(idx)]
            if (len(catagories)!= 0):
                return random.choice(catagories).replace(u'קטגוריה',u'').replace(u':',u'')
    return "זה"



