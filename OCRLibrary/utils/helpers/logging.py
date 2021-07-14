"""
logging module.
"""
from os.path import dirname
from robot.api import logger
from robot.libraries.BuiltIn import BuiltIn

def get_log_dir():
    """
    Function gets the directory where the log.html file is stored.
    """
    variables_dict = BuiltIn().get_variables()
    log_file = variables_dict['${LOG_FILE}']
    output_dir = variables_dict['${OUTPUTDIR}']
    if log_file == 'NONE':
        return output_dir
    return dirname(log_file)

def log_info(message, html):
    """
    Function logs the provided message at the info level
    """
    logger.info(message, html)
