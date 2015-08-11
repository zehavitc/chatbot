class topic(object):
    def __init__(self, id):
        """
        Initiate topic object
        :param id: int (unique)
        :return:None
        """
        self.message_handlers = []
        self.id = id

