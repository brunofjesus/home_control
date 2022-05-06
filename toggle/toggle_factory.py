import toml

from toggle.press_release_toggle import PressReleaseToggle
from toggle.press_toggle import PressToggle


def create(id):
    toml_dict = toml.load("actions.toml")

    toggle = toml_dict['toggles'][id]
    if not toggle:
        raise AttributeError("{} not found".format(id))
    if toggle['type'] == 'press_release':
        return PressReleaseToggle(id, toggle['pin'], toggle['duration'])
    elif toggle['type'] == 'press':
        return PressToggle(id, toggle['pin'])
    else:
        raise AttributeError("type {} unknown".format(toggle['type']))
