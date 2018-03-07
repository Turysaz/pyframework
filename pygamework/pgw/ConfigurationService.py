
from configparser import ConfigParser

def create_configuration_parser():
    configuration = ConfigParser()
    configuration.read("configuration.txt")
    return configuration
