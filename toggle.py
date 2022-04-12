import toml


class Toggle(object):

    def __init__(self, id=None):
        if not id:
            raise AttributeError("id must not be None")

        self.toggle_data = self.__load(id)

    def press(self) -> str:
        return "" + str(self.toggle_data) + " pressed!"

    @staticmethod
    def __load(id):
        toml_dict = toml.load("actions.toml")

        toggle = list(filter(lambda toggle: toggle["id"] == id, toml_dict.get("toggles")))

        if not toggle or len(toggle) == 0:
            raise AttributeError("{} not found".format(id))

        return toggle[0]
