from contextlib import contextmanager
from dynaconf.utils import DynaconfDict

from cattle_grid.dependencies.globals import global_container


@contextmanager
def mocked_config(config):
    if isinstance(config, dict):
        config = DynaconfDict(config)
    old_config = global_container.config

    global_container.config = config

    yield

    global_container.config = old_config
