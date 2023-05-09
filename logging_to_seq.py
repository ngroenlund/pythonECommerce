import seqlog
import logging

# DEBUG: Detailed information, typically of interest only when diagnosing problems.

# INFO: Confirmation that things are working as expected.

# WARNING: An indication that something unexpected happened, or indicative of some problem in the near future (e.g.
# ‘disk space low’). The software is still working as expected.

# ERROR: Due to a more serious problem, the software has not been able to perform some function.

# CRITICAL: A serious error, indicating that the program itself may be unable to continue running.

seqlog.log_to_seq(
    server_url="http://localhost:5341/",
    level=logging.INFO,
    batch_size=1,
    auto_flush_timeout=1,  # seconds
    override_root_logger=True
)

# Creating logger name specific to this script. Unsure how to add format conditions when handler is not used.
logger = logging.getLogger(__name__)

logging.debug('This should not be printed')


# examples of info and error logs

def add(x, y):
    result = x + y
    logger.info(f'Add: {x} + {y} = {result}')
    return result


def divide(x, y):
    try:
        result = x / y
    except ZeroDivisionError:
        logger.error('Tried to divide by zero')
    else:
        return result


a = 10
b = 0

add_result = add(a, b)
divide_result = divide(a, b)

input()
