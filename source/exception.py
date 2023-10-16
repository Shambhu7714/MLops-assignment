import sys
from source.logger import logging
import os
def error_message_detail (error, error_detail:sys):
    __,__,exc_tb=error_detail.exc_info()
    file_name=exc_tb.tb_frame.f_code.co_filename
    error_message="Error occured in python script name [{0}] line number [{1}] error message[{2}]".format()

    file_name, exc_tb.tb_lineno, str(error)
    return error_message
    
    
class CustumException(Exception):
    def _init_(self, error_message, error_detail:sys):
        self.error_message=error_message_detail (error_message, error_detail=error_detail)
        super.init(error_message)

        return self.error_message

    def __str_(self):
        return self.error_message