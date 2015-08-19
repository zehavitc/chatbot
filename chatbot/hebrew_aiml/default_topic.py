# -*- coding: utf-8 -*-
import codecs
import os
from hebrew_aiml.answer_template import answer_template
from hebrew_aiml.answer_template_wiki import answer_template_wiki
from hebrew_aiml.message_handler import message_handler
from hebrew_aiml.pattern import pattern
from .topic import topic
from .wiki_helper import *
from .xml_helper import parse_patterns_xml


class default_topic(topic):
    def __init__(self):
        super(default_topic, self).__init__("DefaultTopic")
        # self.message_handlers.append(message_handler(default_topic,
        #      pattern(["מה המצב *"],False),
        #      answer_template(True,
        #      ["סבבה מה איתך?","הכל טוב ואצלך?", "מעולה, מה איתך?","בסדר, הכל רגיל, מה אצלך
        # ?"])))
        path = os.path.join(os.path.dirname(os.path.realpath(__file__)), "Templates", "DefaultTopic.xml")
        patterns = parse_patterns_xml(path)
        for pattern_xml in patterns:
            self.message_handlers.append(
                message_handler(self, pattern(pattern_xml[0], False)
                                , answer_template(pattern_xml[1], pattern_xml[2])))

    def get_avoiding_message(self, params):
        try:
            path = os.path.join(os.path.dirname(os.path.realpath(__file__)), "Templates", "avoiding_templates")
            f = codecs.open(path, 'r', encoding='utf8')
            templates = f.readlines()
            return answer_template_wiki(True, templates).get([params[0], get_category])
        except Exception as inst:
            print(inst)
