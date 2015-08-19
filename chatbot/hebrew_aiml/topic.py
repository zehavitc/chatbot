class topic(object):
    def __init__(self, id):
        """
        Initiate topic object
        :param id: int (unique)
        :return:None
        """
        self.message_handlers = []
        self.id = id

    def get_avoiding_message(self, msg):
        """
        Get avoiding message if the message does not match any of the patterns
        :param msg:  The message to response to
        :return: return avoiding msg based on msg
        """
        pass


