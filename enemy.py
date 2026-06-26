"""A wrappper for MySprite to allow additional.

functionality for the Enemy class later.
"""

from mysprite import MySprite


class Enemy(MySprite):
    """Used to get certain functions from the MySprite class."""

    def __init__(self, x, y, w, h, screen, images):
        """Initialise what is needed from MySprite."""
        super().__init__(x, y, w, h, images, screen)
