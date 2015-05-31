import  exceptions

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

    def find_topic(self,msg):
        """
        finds the conversation topic based on the current msg the user sent.
        :param msg:string, required
        :return: no return value. the function updates the current_topic field.
        """
        raise NotImplementedError

    def respond(self,msg):
        """
        implements the respond logic of the chat bot
        :param msg:string, required
        :return: return the chat bot response to the given msg
        """
        topic = self.find_topic(msg);
        if not (topic is None):
            self.current_topic = topic
        else:
            self.current_topic = self.default_topic

        for category in self.current_topic.categories:
            if category.pattern.is_match(msg):
                return category.answer_template.get();






