class category(object):
    def __init__(self, topic, pattern, answer_template):
        """
        Initiate category object.
        :param topic: parent topic
        :param pattern: pattern to match the category
        :param answer_template: answer template the will be used to answer when the pattern is match
        :return: None
        """
        self.topic = topic
        self.pattern = None
        self.answer_template = None

