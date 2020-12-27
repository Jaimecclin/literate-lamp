import datetime

class ValueError(Exception):
    pass

class SpecialError(Exception):
    pass

class Bias():
    
    @staticmethod
    def get_bias():
        return 5
        
class Demo:

    def __init__(self, num1, num2):
        self._num1 = num1
        self._num2 = num2

    @property
    def num1(self):
        return self._num1
    
    @property
    def num2(self):
        return self._num2

    def _special_number(self):
        ''' This might be a function using third-party methods '''
        return 1

    def sum(self):
        n = self._special_number()
        if n < 0:
            raise ValueError
        return self._num1 + self._num2 + n 
    
    def sum_bias(self):
        return self._num1 + self._num2 + Bias.get_bias()

    def append_datetime(self, string):
        return str(datetime.datetime.today()) + string