

class ObjectFactory():

    def __init__(self, event_aggregator):
        self.registered_classes = {}
        self.event_aggregator = event_aggregator

    def register_class(self, class_name_str, class_name):
        self.registered_classes.update({class_name_str : class_name})

    def create_object(self, room, obj_name):
        o = self.registered_classes[obj_name](room, self.event_aggregator)
