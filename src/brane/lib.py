# LIB.py
#   by Lut99
#
# Created:
#   19 Sep 2023, 14:10:07
# Last edited:
#   28 Sep 2023, 12:05:09
# Auto updated?
#   Yes
#
# Description:
#   Defines the entrypoint for the library file.
#

import functools
import inspect
import typing


##### LIBRARY DECORATORS #####
def function(env_map: typing.Dict[str, str] = {}) -> typing.Callable[[typing.Callable], typing.Callable]:
    """
        Wraps the decorated function in code that reads Brane arguments from the appropriate environment variables and exports the results as YAML.

        # Arguments
        - `env_map`: Maps arguments of the child function to environment variable names. Any argument not mentioned will default to the same name but CAPITALIZED.
    """

    # Build the actual decorator function
    def decorator(func: typing.Callable) -> typing.Callable:
        """
            Decorator function for the `brane.function()` decorator.

            # Arguments
            - `func`: Some function to wrap.

            # Returns
            The wrapped function but now really wrapped.
        """

        # Find the function's argument names
        args = inspect.signature(func)
        print(args)

        # This is the function that transforms inputs first
        @functools.wraps(func)
        def brane_func(*args, **kwargs) -> typing.Callable:
            """
                Does the heavy lifting.
            """

            return func


        return brane_func

    # Return that
    return decorator
