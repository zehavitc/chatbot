from threading import Thread
from .models import Message
import wikipedia

import time


class bot(object):
    def __init__(self):
        self.name = "bot user"

    def get_response(self, msg):
        # return 'Hi, I\'m a human'
        first_word = msg.split(' ')
        wikipedia.set_lang('He')
        value = wikipedia.search(first_word)
        if len(value) != 0:
            catagories = wikipedia.WikipediaPage(value[0]).categories
            if len(catagories) != 0:
                return catagories[0]
            return wikipedia.summary(value)
        return "No result"




