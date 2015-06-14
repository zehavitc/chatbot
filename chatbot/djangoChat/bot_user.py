# -*- coding: utf-8 -*-
from threading import Thread
from .models import Message
import wikipedia
import hebrew_aiml
from hebrew_aiml.topic import topic
from hebrew_aiml.pattern import pattern
from hebrew_aiml.answer_template import answer_template
from hebrew_aiml.message_handler import message_handler
from hebrew_aiml.aiml import aiml

import time


class bot(object):
    def __init__(self):
        self.name = "bot user"
        default_topic = topic("default")
        default_topic.message_handlers.append(message_handler(default_topic,pattern(["מה המצב *"],False),answer_template(True,["סבבה מה איתך?","הכל טוב ואצלך?", "מעולה, מה איתך?","בסדר, הכל רגיל, מה אצלך?"])))
        self.aiml = aiml(default_topic,[])

    def get_response(self, msg):
        return self.aiml.respond(msg)




