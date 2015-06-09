# -*- coding: utf-8 -*-
from patterns_helper import ngrams
from WordsDb import words_db_api
import re

class pattern(object):
    def __init__(self, templates, use_synonyms=True):
        """
        Initiate pattern object
        :param templates: list of templates to match
        :param use_synonyms: use synonyms to create more templates
        :return: None
        """
        self.templates = templates
        if not use_synonyms:
            return
        words_api = words_db_api.words_db_api()
        for template in templates:
            sub_templates = (''.join(w.strip()) for w in template.split(u'*'))
            for sub_template in sub_templates:
                for i in list(reversed(range(1, 3))):
                    grams = ngrams(template, i)
                    for ngram in grams:
                        trans = words_api.get_translation(ngram)
                        for translation in trans:
                            if len(translation.split()) <= 2 and translation != "":
                                self.templates += template.replace(ngram, translation)


    def is_match(self, msg):
        """
        check if msg is match to pattern
        :param msg: string, required
        :return: true\ false
        """
        for template in self.templates:
            if re.match(template, msg):
                return True
        return False


# h = u'מבחן'
# print(h)
p = pattern([u'מה המצב אחי'])
print(p.is_match(u'איך המצב אחי'))