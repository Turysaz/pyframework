
import queue

class Room():

    def __init__(self, event_aggregator, object_factory):

        self.event_aggregator = event_aggregator
        self.object_container = object_factory

        self.width = 100
        self.height = 100
        self.size = property(lambda _: (self.width, self.height))
        self.scroll_vertical = False
        self.scroll_horizontal = False

        self.background_color = (0,0,0)
        self.background_image = None

        self.objects = []
        self.add_queue = queue.Queue()
        self.del_queue = queue.Queue()

    def step(self, delta):
        for obj in self.objects:
            obj.update_position(delta)
            obj.step(delta)

        while not self.del_queue.empty():
            obj = self.del_queue.get()
            self.objects.remove(obj)

        while not self.add_queue.empty():
            obj = self.add_queue.get()
            self.objects.add(obj)

    def pre_step(self):
        pass

    def post_step(self):
        pass

    def add_object(self, obj_name, x, y):
        obj = self.object_container.create_object(obj_name, x, y)

    def add_object(self, obj):
        self.add_queue.put(obj)

    def remove_object(self, obj):
        self.del_queue.put(obj)
