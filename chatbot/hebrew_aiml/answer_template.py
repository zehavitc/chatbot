import exceptions
class answer_template(object):
    def __init__(self, is_random, li):
        """
        Initiate the answer_template object
        :param is_random: indicate if the chosen template is random or the first template in the list
        :param li: list of templates for response
        :return:None
        """
        self.is_random = is_random
        self.li = None



    def get(self):
        """
        gets the answer from the answer template
        :return:
        returns the first template if is_random is false, otherwise returns random template
        """
        raise NotImplementedError