# BRANE FUNCTION.py
#   by Lut99
#
# Created:
#   19 Sep 2023, 14:25:00
# Last edited:
#   19 Sep 2023, 14:40:19
# Auto updated?
#   Yes
#
# Description:
#   Tests the `brane_function` decorator.
#

import brane
import typing


##### TESTS #####
def test_basic() -> typing.Tuple[bool, str]:
    # Define a BraneScript function that doesn't take anything
    @brane.function()
    def simple_func():
        pass

    # Assert it works
    assert simple_func() is None, "unimplemented"
