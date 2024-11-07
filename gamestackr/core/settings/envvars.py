"""
This takes env variables with a matching prefix, strips out the prefix, and add it to global() for easy reference

For example:
export GAMESTACKR_SETTING_IN_DOCKER=true (environment variable)

Cloud then be referenced as a global as:
IN_DOCKER (where the value would be True)
"""

from gamestackr.core.utils.collections import deep_update
from gamestackr.core.utils.settings import get_settings_from_environment

# globals() is a dictionary of global variables
deep_update(globals(), get_settings_from_environment(ENVVAR_SETTINGS_PREFIX))  # type: ignore # noqa: F821
