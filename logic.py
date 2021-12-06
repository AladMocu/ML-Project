import random
from datetime import date
from joblib import load

log = "SYSTEM STARTED\n"
clf = load("ids_iot.joblib")


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
    log += "\n=======BLOCKED TRACE=======\n" + str(date.today()) + str(trace) + "\n========================\n"


def __do_classify(trace):
    res = clf.predict([str(trace)])
    if res == 1:
        return "atk"
    return "GOOD"


if __name__ == '__main__':
    __do_classify("27000  >  50000 Len=4")

