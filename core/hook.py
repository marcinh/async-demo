class EventHook(object):

    def __init__(self):
        self.__handlers = []

    def __iadd__(self, handler):
        self.__handlers.append(handler)
        return self

    def __isub__(self, handler):
        self.__handlers.remove(handler)
        return self

    def fire(self, *args, **kwargs):
        for handler in self.__handlers:
            handler(*args, **kwargs)

    def clear_handlers(self, handler):
        for theHandler in self.__handlers:
            if theHandler.im_self == handler:
                self -= theHandler
