# Importing the required modules
import sys
import traceback
import time


def get_exception_info():
    """
    This function is used to get the exception information.
    :return: The exception information as a string.
    """

    try:
        exception_type, exception_value, exception_traceback = sys.exc_info()
        file_name, line_number, procedure_name, line_code = traceback.extract_tb(
            exception_traceback)[-1]
        exception_info = "".join(
            f"[Time Stamp]: {str(time.strftime('%d-%m-%Y %I:%M:%S %p'))}\n"
            f"[File Name]: {str(file_name)}\n"
            f"[Procedure Name]: {str(procedure_name)}\n"
            f"[Error Message]: {str(exception_value)}\n"
            f"[Error Type]: {str(exception_type)}\n"
            f"[Line Number]: {str(line_number)}\n"
            f"[Line Code]: {str(line_code)}"
        )
    except Exception as exception:
        exception_info = f"Exception occurred while getting the exception information: {str(exception)}"

    return exception_info


class ExceptionHandler(Exception):
    """
    This class is used to handle the exceptions
    > param Exception: This is the base class for all the exceptions
    """

    def __init__(self, *args):
        """
        This function is used to initialize the class
        > param args: This is used to get the arguments
        > param kwargs: This is used to get the keyword arguments
        """
        super().__init__(self, *args)
