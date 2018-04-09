# Copyright (c) 2018 Turysaz <turysaz@posteo.org>

class ConfigOption():
    def __init__(self,
            section,
            option,
            value_prehandling,
            variable_name):
        self.section = section
        self.option = option
        self.value_prehandling = value_prehandling
        self.variable_name = variable_name

    def conditional_apply_to(self, conf_parser, target):
        if conf_parser.has_section(self.section):
            if conf_parser.has_option(self.section, self.option):
                val = conf_parser.get(self.section, self.option)
                target.__dict__[self.variable_name] = self.value_prehandling(val)


def __convert_to_tuple(string):
    s = [int(x) for x in string.strip()[1:-1].split(',')]
    return (s[0], s[1], s[2])

room_options = [
    ConfigOption(
        section="size",
        option="width",
        value_prehandling=lambda x: int(x),
        variable_name="width"),
    ConfigOption(
        section="size",
        option="height",
        value_prehandling=lambda x: int(x),
        variable_name="height"),
    ConfigOption(
        section="size",
        option="scrolling",
        value_prehandling=lambda x: x == "v" or x == "b",
        variable_name="scroll_vertical"),
    ConfigOption(
        section="size",
        option="scrolling",
        value_prehandling=lambda x: x == "h" or x == "b",
        variable_name="scroll_horizontal"),
    ConfigOption(
        section="background",
        option="picture",
        value_prehandling=lambda x: "project/assets/images" + x,
        variable_name="background_image"),
    ConfigOption(
        section="background",
        option="color",
        value_prehandling=__convert_to_tuple,
        variable_name="background_color")
    ]
