import exceptions
class pattern(object):
    def __init__(self):
        pass

    def is_match(self,msg):
        """
        check if msg is match to pattern
        :param msg: string, required
        :return: true\ false
        """
        raise NotImplementedError