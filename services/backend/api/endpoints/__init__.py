from . import equipment
from . import fermentable
from . import hop
from . import mash
from . import misc
from . import recipe
from . import style
from . import user
from . import water
from . import yeast

__all__ = [
    "equipment",
    "fermentable",
    "hop",
    "mash",
    "misc",
    "recipe",
    "style",
    "user",
    "water",
    "yeast"
]

# This will make all the routers available when importing the package
# from services.backend.api.endpoints import *
# instead of importing each router separately
