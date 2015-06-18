__author__ = 'zehavitc'

import exceptions
import random
from . import answer_template
from answer_template import answer_template
import wikipedia


class answer_template_wiki(answer_template):

    def get(self, params=None):
        """
        gets the answer from the answer template
        :param params: msg = params[0], func = params[1]
        :return:
        returns the first template if is_random is false, otherwise returns random template
        """
        msg = params[0]
        topic = self.get_topic_wiki(msg)
        if self.is_random:
            answer = random.choice(self.li)
        else:
            answer = self.li[0]
        func = params[1]
        replace_to = func(topic)
        return answer.replace(u'*',replace_to)




    def get_topic_wiki(self,msg):
        words = msg.split()
        lens = []
        wikipedia.set_lang('He')
        for word in words:
            value = wikipedia.search(word,10,True)
            if (len(value) == 0):
                lens.append(0)
            else:
                try:
                    lens.append(len(wikipedia.page(value[0]).content))
                except:
                    lens.append(0)

        max_len = max(lens)
        idx = [i for i, x in enumerate(lens) if x == max(max_len)]
        return words(random.choice(idx))