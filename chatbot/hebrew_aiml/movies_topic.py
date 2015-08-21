# -*- coding: utf-8 -*-
import codecs
import os
from hebrew_aiml.answer_template import answer_template
from hebrew_aiml.avoiding_msg_wiki import avoiding_msg_wiki
from hebrew_aiml.message_handler import message_handler
from hebrew_aiml.pattern import pattern
from .topic import topic
from .wiki_helper import *
from .xml_helper import parse_patterns_xml
from topic_classifier.topic_classifier import classifier


class movies_topic(topic):
    def __init__(self):
        super(movies_topic, self).__init__(classifier.movies_topic)
        super(movies_topic, self).init_from_xml(classifier.movies_topic + ".xml")

    def get_avoiding_message(self, msg):
        pass

