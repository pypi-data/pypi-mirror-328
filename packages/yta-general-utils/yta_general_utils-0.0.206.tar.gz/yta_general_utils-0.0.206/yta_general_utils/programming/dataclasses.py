from yta_general_utils.programming.validator import PythonValidator
from typing import Union
from dataclasses import dataclass

import inspect


@dataclass
class MethodParameters:
    """
    Dataclass to hold the parameters of a method,
    classified in mandatory or optional according
    to its declaration.

    Those parameters are obtained from the method
    signature, where any parameter with a default
    None value is considered optional.
    """

    mandatory_parameters: list[str]
    """
    The names of those parameters that have been
    considered mandatory according to the method
    signature.
    """
    optional_parameters: list[str]
    """
    The names of those parameters that have been
    considered optional according to the method
    signature.
    """

    def __init__(
        self,
        mandatory_parameters: list[str],
        optional_parameters: list[str]
    ):
        self.mandatory_parameters = mandatory_parameters
        self.optional_parameters = optional_parameters

@dataclass
class Parameter:
    """
    The representation of a parameter found in a
    method signature, indicating if it was what 
    we consider an optional parameter or a 
    mandatory one based on its default value.
    """

    name: str
    """
    The name of the parameter.
    """
    type: any
    """
    The type of the parameter.
    """
    default_value: any
    """
    The default value of the parameter.
    """

    def __init__(
        self,
        name: str,
        type: any,
        default_value: any
    ):
        self.name = name
        # TODO: The type, that comes from '.annotation' has
        # to be reconsidered as it is quite special
        self.type = type
        self.default_value = default_value

    @property
    def is_default_value_empty(
        self
    ) -> bool:
        """
        Check if the default value is empty (no value
        associated) or  not.
        """
        return self.default_value is inspect._empty
    
    @property
    def is_optional(
        self
    ) -> bool:
        """
        Check if the parameter is optional (its default
        value is None).
        """
        return self.default_value is None
    
    @property
    def is_mandatory(
        self
    ) -> bool:
        """
        Check if the parameter is mandatory (its default
        value is not None).
        """
        return not self.is_optional
    
    @property
    def as_dict(
        self
    ) -> dict:
        """
        Get the parameter as a dict with its 'name' as
        the key and the instance as the value.

        'name' : self
        """
        return {
            self.name: self
        }
    
@dataclass
class Parameters:
    """
    List of parameters that exist in a function
    or method signature, to be able to handle
    them easy and detect which ones are mandatory
    or optional and more stuff.
    """

    parameters: list[Parameter]
    """
    The parameters found in the method signature.
    """

    def __init__(
        self,
        parameters: list[Parameter]
    ):
        if (
            not PythonValidator.is_list(parameters) or
            any(not PythonValidator.is_instance(item, Parameter) for item in parameters)
        ):
            raise Exception('The provided "parameters" parameter is not a list of Parameter instances or at least one of the elements is not a Parameter instance.')

        self.parameters = parameters
        
    @property
    def mandatory(
        self
    ) -> 'Parameters':
        """
        Get the parameters that are mandatory as a new
        instance of a Parameters class containing only
        those ones.

        This is a new instance that doesn't modify the
        original one.
        """
        return Parameters(self.mandatory_as_list)
    
    @property
    def optional(
        self
    ) -> 'Parameters':
        """
        Get the parameters that are optional as a new
        instance of a Parameters class containing only
        those ones.

        This is a new instance that doesn't modify the
        original one.
        """
        return Parameters(self.optional_as_list)

    @property
    def mandatory_as_list(
        self
    ) -> list[Parameter]:
        """
        Get the parameters that are mandatory as a list
        of Parameter instances.
        """
        return [
            parameter
            for parameter in self.parameters
            if parameter.is_mandatory
        ]
    
    @property
    def optional_as_list(
        self
    ) -> list[Parameter]:
        """
        Get the parameters that are optional as a list
        of Parameter instances.
        """
        return [
            parameter
            for parameter in self.parameters
            if parameter.is_optional
        ]
    
    @property
    def as_dict(
        self
    ) -> dict[str, Parameter]:
        """
        Get the parameters as a dictionary in which the
        parameter names are the keys and the values are
        Parameter instances.
        """
        if (
            not hasattr(self, '_as_dict') or
            self._as_dict is None
        ):
            self._as_dict = {
                parameter.name: parameter
                for parameter in self.parameters
            }

        return self._as_dict
    
    def get(
        self,
        name: str
    ) -> Union[Parameter, None]:
        """
        Get the parameter with the given 'name' if
        existing, or None if not.
        """
        return self.as_dict.get(name, None)
    
    def has(
        self,
        name: str
    ) -> bool:
        """
        Check if the parameter with the given 'name' 
        exist or not.
        """
        return name in self.as_dict
    
    def remove(
        self,
        name: str
    ) -> 'Parameters':
        """
        Remove the parameter with the provided 'name' if
        existing.
        """
        self.parameters = [
            parameter
            for parameter in self.parameters
            if parameter.name != name
        ]

        # We force it to be recalculated
        self._as_dict = None

        return self
