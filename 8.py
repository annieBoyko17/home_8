import logging
def function_1():
    def function_2(x=5):
        return x * 2
    result = function_2()
    print(result)
logging.basicConfig(level=logging.DEBUG, filename="time.func.work", filemode="w",
                        format="Message about time of function work:%(relativeCreated)d")
logging.debug("work")