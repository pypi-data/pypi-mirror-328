
from yta_general_utils.programming.validator import PythonValidator
from yta_general_utils.programming.validator.number import NumberValidator
from yta_general_utils.programming.validator.error_message import ErrorMessage
from typing import Union


class ParameterValidator:
    """
    Class to wrap and simplify the method parameters
    validation, so you are able to validate if a
    parameter is a mandatory string, if it is a 
    positive value, and normalize the exception
    messages.

    The type of the parameters passed to each method
    validation is not validated, so pay attention to
    what you pass there.

    Each method will raise an Exception with a custom
    message if failing.
    """

    @staticmethod
    def validate_mandatory(
        name: str,
        value: any
    ) -> None:
        """
        Validate if the provided 'value' is not None.
        """
        if value is None:
            raise Exception(ErrorMessage.parameter_not_provided(name))

    @staticmethod
    def validate_string(
        name: str,
        value: str,
    ) -> None:
        """
        Validate if the provided 'value' is of string type.
        """
        if not PythonValidator.is_string(value):
            raise Exception(ErrorMessage.parameter_is_not_string(name))
        
    @staticmethod
    def validate_mandatory_string(
        name: str,
        value: str,
        do_accept_empty: bool = True
    ) -> None:
        """
        Validate if the provided 'value' is a non-empty
        string.
        """
        ParameterValidator.validate_string(name, value)

        if (
            not do_accept_empty and
            value == ''
        ):
            raise Exception(ErrorMessage.parameter_not_provided(value))
    
    @staticmethod
    def validate_bool(
        name: str,
        value: bool
    ) -> None:
        """
        Validate if the provided 'value' is bool value or not.
        """
        if not PythonValidator.is_boolean(value):
            raise Exception(ErrorMessage.parameter_is_not_boolean(name))
        
    @staticmethod
    def validate_mandatory_bool(
        name: str,
        value: bool
    ) -> None:
        """
        Validate if the provided 'value' is not None and is
        a boolean value.
        """
        ParameterValidator.validate_mandatory(name, value)
        ParameterValidator.validate_bool(name, value)
        
    @staticmethod
    def validate_positive_number(
        name: str,
        value: Union[float, int],
        do_include_zero: bool = True
    ) -> None:
        """
        Validate if the provided 'value' is a positive number
        or not.
        """
        if not NumberValidator.is_positive_number(value, do_include_zero = do_include_zero):
            raise Exception(ErrorMessage.parameter_is_not_positive_number(name))
        
    @staticmethod
    def validate_mandatory_positive_number(
        name: str,
        value: Union[float, int],
        do_include_zero: bool = True
    ) -> None:
        """
        Validate if the provided 'value' is not None and is a
        positive number or not.
        """
        ParameterValidator.validate_mandatory(name, value)
        ParameterValidator.validate_positive_number(name, value, do_include_zero = do_include_zero)
        
    @staticmethod
    def validate_instance_of(
        name: str,
        value: object,
        cls: list[Union[object, str]]
    ) -> None:
        """
        Validate if the provided 'value' is an instance of the
        given 'cls' classes.
        """
        if not PythonValidator.is_instance(value, cls):
            raise Exception(ErrorMessage.parameter_is_not_instance_of(name, cls))

    @staticmethod
    def validate_mandatory_instance_of(
        name: str,
        value: object,
        cls: list[Union[object, str]]
    ) -> None:
        """
        Validate if the provided 'value' is not None and is an
        instance of the given 'cls' classes.
        """
        ParameterValidator.validate_mandatory(name, value)
        ParameterValidator.validate_instance_of(name, value, cls)

    @staticmethod
    def validate_class_of(
        name: str,
        value: type,
        cls: list[Union[type, str]]
    ) -> None:
        """
        Validate if the provided 'value' is one of the given
        'cls' classes.
        """
        if not PythonValidator.is_class(value, cls):
            raise Exception(ErrorMessage.parameter_is_not_class_of(name, cls))
        
    @staticmethod
    def validate_mandatory_class_of(
        name: str,
        value: type,
        cls: list[Union[type, str]]
    ) -> None:
        """
        Validate if the provided 'value' is not None and is 
        one of the given 'cls' classes.
        """
        ParameterValidator.validate_mandatory(name, value)
        ParameterValidator.validate_class_of(name, value, cls)

    @staticmethod
    def validate_list_of_string(
        name: str,
        value: list[str]
    ) -> None:
        """
        Validate if the provided 'value' is a list of string
        values.
        """
        if not PythonValidator.is_list_of_string(value):
            raise Exception(ErrorMessage.parameter_is_not_list_of_string(name))
        
    @staticmethod
    def validate_mandatory_list_of_string(
        name: str,
        value: list[str]
    ) -> None:
        """
        Validate if the provided 'value' is not None and is
        a list of string values.
        """
        ParameterValidator.validate_mandatory(name, value)
        ParameterValidator.validate_list_of_string(name, value)

    @staticmethod
    def validate_list_of_instances(
        name: str,
        value: list[object]
    ) -> None:
        """
        Validate if the provided 'value' is a list of 
        instances.
        """
        if not PythonValidator.is_list_of_instances(value):
            raise Exception(ErrorMessage.parameter_is_not_list_of_instances(name))
        
    @staticmethod
    def validate_mandatory_list_of_instances(
        name: str,
        value: list[object]
    ) -> None:
        """
        Validate if the provided 'value' is not None and
        is a list of instances.
        """
        ParameterValidator.validate_mandatory(name, value)
        ParameterValidator.validate_list_of_instances(name, value)
        
    @staticmethod
    def validate_list_of_these_instances(
        name: str,
        value: list[object],
        cls: Union[list[Union[type, str]], str, type]
    ) -> None:
        """
        Validate if the provided 'value' is a list of 
        instances of the given 'cls' class or classes.
        """
        if not PythonValidator.is_list_of_these_instances(value, cls):
            raise Exception(ErrorMessage.parameter_is_not_list_of_these_instances(name, cls))
        
    @staticmethod
    def validate_mandatory_list_of_these_instances(
        name: str,
        value: list[object],
        cls: Union[list[Union[type, str]], str, type]
    ) -> None:
        """
        Validate if the provided 'value' is not None
        and is a list of instances of the given 'cls'
        class or classes.
        """
        ParameterValidator.validate_mandatory(name, value)
        ParameterValidator.validate_list_of_these_instances(name, value, cls)

    @staticmethod
    def validate_list_of_classes(
        name: str,
        value: list[type]
    ) -> None:
        """
        Validate if the provided 'value' is a list of
        classes.
        """
        if not PythonValidator.is_list_of_classes(value):
            raise Exception(ErrorMessage.parameter_is_not_list_of_classes(name))
        
    @staticmethod
    def validate_mandatory_list_of_classes(
        name: str,
        value: list[type]
    ) -> None:
        """
        Validate if the provided 'value' is not None
        and is a list of classes.
        """
        ParameterValidator.validate_mandatory(name, value)
        ParameterValidator.validate_list_of_classes(name, value)

    @staticmethod
    def validate_list_of_these_classes(
        name: str,
        value: list[type],
        cls: Union[list[Union[type, str]], str, type]
    ) -> None:
        """
        Validate if the provided 'value' is a list
        of the given 'cls' class or classes.
        """
        if not PythonValidator.is_list_of_these_classes(value, cls):
            raise Exception(ErrorMessage.parameter_is_not_list_of_these_classes(name, cls))

    @staticmethod
    def validate_mandatory_list_of_these_classes(
        name: str,
        value: list[type],
        cls: Union[list[Union[type, str]], str, type]
    ) -> None:
        """
        Validate if the provided 'value' is not None
        and is a list of the given 'cls' class or
        classes.
        """
        ParameterValidator.validate_mandatory(name, value)
        ParameterValidator.validate_list_of_these_classes(name, value, cls)