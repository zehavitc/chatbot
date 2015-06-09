class topic(object):
    def __init__(self,aiml, id):
        """
        Initiate topic object
        :param aiml: aiml parent object
        :param id: int (unique)
        :return:None
        """
        self.message_handlers = []
        self.id = id

