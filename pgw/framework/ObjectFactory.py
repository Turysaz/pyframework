from .UserfriendlyInjectionPackage import UserfriendlyInjectionPackage


class ObjectFactory():

    def __init__(self, event_aggregator, sound_provider):
        self.registered_classes = {}
        self.event_aggregator = event_aggregator

    def register_class(self, class_name_str, class_name):
        self.registered_classes.update({class_name_str : class_name})

    def create_object(self, room, obj_name_string):
        pack = UserfriendlyInjectionPackage(
            self.event_aggregator,
            self.sound_provider,
            room)
        return self.registered_classes[obj_name](pack)
