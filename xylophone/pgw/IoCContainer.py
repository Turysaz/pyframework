# Copyright (c) 2018 Turysaz <turysaz@posteo.org>

class IoCContainer():

    def __init__(self):

        self.__constructors = {}  # {"service_key" : service_ctor}
        self.__dependencies = {}  # {"service_key" : ["dep_key_1", "dep_key_2", ..]} constructor parameters
        self.__quantity = {}      # {"service_key" : "singleton" | "multiple"}

        self.__singletons = {}


    def register_on_demand(self,
                service_name_string,
                service,
                *dependencies):
        self.__register_internal(service_name_string, service, "multiple", dependencies)


    def register_singleton(self,
                service_name_string,
                service,
                *dependencies):
        self.__register_internal(service_name_string, service, "singleton", dependencies)


    def get_instance(self, service_name_string):
        if service_name_string not in self.__constructors:
            raise Exception()

        if self.__quantity[service_name_string] == "multiple":
            return __create_instance_recursive(service_name_string)

        elif self.__quantity[service_name_string] == "singleton":
            if service_name_string in self.__singletons:
                return self.__singletons[service_name_string]

            singleton = self.__create_instance_recursive(service_name_string)
            self.__singletons[service_name_string] = singleton
            return singleton


    def __register_internal(self,
                service_name_string,
                service,
                quantity,
                dependencies):
        if service_name_string in self.__constructors:
            raise Exception() # already registered

        self.__constructors[service_name_string] = service
        self.__dependencies[service_name_string] = dependencies
        self.__quantity[service_name_string] = quantity


    def __create_instance_recursive(self, service_name_string):
        deps = [self.get_instance(d)
                for d in self.__dependencies[service_name_string]]
        return self.__constructors[service_name_string](*deps)
