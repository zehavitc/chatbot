# -*- coding: utf-8 -*-
from threading import Thread
from .models import Message
import wikipedia
import hebrew_aiml
from hebrew_aiml.topic import topic
from hebrew_aiml.pattern import pattern
from hebrew_aiml.answer_template import answer_template
from hebrew_aiml.message_handler import message_handler
from hebrew_aiml.answer_template_wiki import answer_template_wiki
from hebrew_aiml.aiml import aiml
from hebrew_aiml.default_topic import default_topic

import time

class bot(object):
    def __init__(self):
        self.name = "bot user"
        self.aiml = aiml(default_topic(),[])

    def get_response(self, msg):
        r = self.aiml.respond(msg)
        return r





