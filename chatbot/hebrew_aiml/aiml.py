# -*- coding: utf-8 -*-
import exceptions
import wikipedia
import random
import os
from .answer_template_wiki import answer_template_wiki
from .wiki_helper import *
import codecs


class aiml(object):
    def __init__(self, default_topic, topics):
        """
        initiate the hebrew_aiml object
        :param default_topic: default topic to answer by.
        :param topics: list of known topics the chat bot can use to answer the user
        :return: None
        """
        self.current_topic = default_topic
        self.default_topic = default_topic
        self.topics = topics
        self.avoiding_msg = self.get_avoiding_message()

    def get_avoiding_message(self):
        try:
            path = os.path.join(os.path.dirname(os.path.realpath(__file__)),"Templates","avoiding_templates")
            f = codecs.open(path,'r',encoding='utf8')
            templates = f.readlines()
            return answer_template_wiki(True,templates)
        except Exception as inst:
            print(inst)

    def find_topic(self,msg):
        """
        finds the conversation topic based on the current msg the user sent.
        :param msg:string, required
        :return: no return value. the function updates the current_topic field.
        """
        return self.default_topic

    def respond(self,msg):
        """
        implements the respond logic of the chat bot
        :param msg:string, required
        :return: return the chat bot response to the given msg
        """
        topic = self.find_topic(msg)
        if not (topic is None):
            self.current_topic = topic
        else:
            self.current_topic = self.default_topic

        for msg_handler in self.current_topic.message_handlers:
            if msg_handler.pattern.is_match(msg):
                return msg_handler.answer_template.get(msg)
        return self.avoiding_msg.get([msg,get_category])








