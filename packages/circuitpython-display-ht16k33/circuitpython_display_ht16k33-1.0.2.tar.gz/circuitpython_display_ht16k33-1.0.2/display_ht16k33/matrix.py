# SPDX-FileCopyrightText: Copyright (c) 2023 Jose D. Montoya
#
# SPDX-License-Identifier: MIT
"""
`display_ht16k33.matrix`
================================================================================

On Display Simulation for an HT16K33 driver. Works with 16x8 and 8x8 matrices.

Based on some code from https://github.com/adafruit/Adafruit_CircuitPython_HT16K33.git
Authors: Radomir Dopieralski and Tony DiCola License: MIT

* Author(s): Jose D. Montoya


"""

from display_ht16k33.ht16k33 import HT16K33

try:
    from typing import Optional, Tuple
except ImportError:
    pass


__version__ = "1.0.2"
__repo__ = "https://github.com/jposada202020/CircuitPython_DISPLAY_HT16K33.git"


class Matrix8x8(HT16K33):
    """A single matrix.
    :param int x: x coordinates in pixels for the matrix to start. This is the top
    left corner of the first digit. Default is 0
    :param int y: y coordinates in pixels for the matrix to start. This is the top
    left corner of the first digit. Default is 0

    :param int radius: led radius in pixels. Default is 5

    :param bool text: define if the matrix will be used to display text. For reasons
     that are beyond my understanding :). The text and pixels examples work differently.
     displaying text will use framebuffer, and it will show in a different direction. will be
     good to review a PR if you found this situation a little too much for your OCD ;).
     Default is False
    """

    def __init__(self, x: int = 0, y: int = 0, radius: int = 5, text: bool = False):
        self._x = x
        self._y = y

        super().__init__(
            x=x,
            y=y,
            radius=radius,
            text=text,
            num_led_x=8,
            num_led_y=8,
            register_width=1,
        )

    def __getitem__(self, key: Tuple[int, int]) -> Optional[bool]:
        x, y = key
        return self.pixel(x, y)

    def __setitem__(
        self, key: Tuple[int, int], color: Optional[bool], shown: bool = True
    ) -> None:
        x, y = key
        self._pixel_buffer = color
        self.pixel(x, y, shown)


class Matrix16x8(HT16K33):
    """A single matrix.
    :param int x: x coordinates in pixels for the matrix to start. This is the top
    left corner of the first digit. Default is 0
    :param int y: y coordinates in pixels for the matrix to start. This is the top
    left corner of the first digit. Default is 0
    :param int radius: led radius in pixels. Default is 5

    :param bool text: define if the matrix will be used to display text. For reasons
     that are beyond my understanding :). The text and pixels examples work differently.
     displaying text will use framebuffer, and it will show in a different direction. will be
     good to review a PR if you found this situation a little too much for your OCD ;).
     Default is False
    """

    def __init__(self, x: int = 0, y: int = 0, radius: int = 5, text: bool = False):

        super().__init__(
            x=x,
            y=y,
            radius=radius,
            text=text,
            num_led_x=16,
            num_led_y=8,
            register_width=2,
        )

    def __getitem__(self, key: Tuple[int, int]) -> Optional[bool]:
        x, y = key
        return self.pixel(x, y)

    def __setitem__(
        self, key: Tuple[int, int], color: Optional[bool], shown: bool = True
    ) -> None:
        x, y = key
        self._pixel_buffer = color
        self.pixel(x, y, shown)
