import random
from datetime import date

log = "SYSTEM STARTED\n"


def classify(trace):
    global log
    lbl = __do_classify(trace)
    if lbl == "atk":
        __do_atk(trace)
    else:
        log += "\n" + str(date.today()) + " " + str(trace) + "\n"
    return log


def __do_atk(trace, response={}):
    global log
    log += "\n=======BLOCKED TRACE=======\n" + str(date.today()) + str(trace) + "\n=======================\n"


def __do_classify(trace):
    # TODO place the classifier here
    return trace
