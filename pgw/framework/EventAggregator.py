

class EventAggregator():

    def __init__(self):
        # {eventtype : {(recipient, hander), (.., ..), ...}}
        self.subscriptions = {}


    def subscribe(self, eventtype, recipient, handler):

        if eventtype in self.subscriptions:
            self.subscriptions[eventtype].add((recipient, handler))
        else:
            self.subscriptions.update({eventtype : {(recipient, handler)}})


    def unsubscribe(self, eventtype, recipient, handler):

        if not eventtype in self.subscriptions:
            return

        if not (recipient, handler) in self.subscriptions[eventtype]:
            return

        self.subscriptions[eventtype].remove((recipient, handler))

        if len(self.subscriptions[eventtype]) == 0:
            self.subscriptions.pop(eventtype)


    def publish(self, eventtype, event):
        if not eventtype in self.subscriptions:
            return
        for (recipient, handler) in self.subscriptions[eventtype]:
            recipient.handler(event)
