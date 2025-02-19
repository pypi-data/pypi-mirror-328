from yta_general_utils.programming.dataclasses import MethodParameters
from yta_general_utils.programming.dataclasses import Parameter, Parameters
from yta_general_utils.programming.validator import PythonValidator

import inspect


class ParameterObtainer:
    """
    Class to interact with python methods and classes to obtain
    the parameters those method have. This is usefull for dynamic
    functionality that need to fill or check if the required
    parameters are passed or not.
    """

    PARAMETER_EMPTY = inspect._empty
    """
    Class that represents an empty parameter default value
    """
    
    @staticmethod
    def get_parameters_from_method(
        method,
        params_to_ignore: list[str] = ['self', 'cls', 'args', 'kwargs']
    ) -> MethodParameters:
        """
        This methods returns the existing parameters in the provided
        'method' that are not in the 'params_to_ignore' list. These
        parameters will be categorized in 'mandatory' and 'optional'.
        The 'optional' values are those that have None as default 
        value.

        The 'method' parameter must be a real python method to be able
        to inspect it.
        """
        parameters = {
            'mandatory': [],
            'optional': []
        }

        params_to_ignore = [] if params_to_ignore is None else params_to_ignore

        # TODO: What about parameters that accept a None
        # as possible value but its not the default value (?)

        params = inspect.signature(method).parameters.values()
        for parameter in params:
            if parameter.name in params_to_ignore:
                continue
            
            # If parameter is set as None, it is optional
            if parameter.default is parameter.empty:
                parameters['mandatory'].append(parameter.name)
            else:
                parameters['optional'].append(parameter.name)

        return MethodParameters(
            parameters['mandatory'],
            parameters['optional']
        )
    
    # TODO: This method will replace the one above
    @staticmethod
    def get_parameters_from_methodX(
        method: callable
    ) -> Parameters:
        """
        Obtain the parameters of the given 'method' as
        a list of our custom dataclass Parameter, easy
        to handle and to get information from.
        """
        if not PythonValidator.is_callable(method):
            raise Exception('The provided "method" is not actually a valid method.')
        
        return Parameters([
            Parameter(
                method_parameter.name,
                method_parameter.annotation,
                method_parameter.default
            ) for method_parameter in inspect.signature(method).parameters.values()
        ])

"""
This code below is nice for testing:
from typing import Union
import inspect

def test_method(text: str, output_filename: Union[str, int, None] = None):
    pass

for parameter in inspect.signature(test_method).parameters:
    print(parameter)

for parameter_value in inspect.signature(test_method).parameters.values():
    print('Este es uno:')
    print(parameter_value.name)
    #print(parameter_value.kind)
    print(parameter_value.annotation)
    print(parameter_value.default)
"""