from orionis.luminate.bootstrap.config.parser import Parser
from orionis.luminate.config.sections import SECTIONS
from orionis.luminate.container.container import Container
from orionis.luminate.contracts.bootstrap.register_interface import IRegister
from orionis.luminate.contracts.config.config_interface import IConfig
from orionis.luminate.tools.reflection import Reflection

class Register(IRegister):
    """
    Handles the registration of configuration classes within the application.

    This class ensures that only valid configuration classes are registered
    while enforcing structure and type safety.

    Attributes
    ----------
    cache_config : CacheConfig
        An instance of `CacheConfig` used to store registered configurations.

    Methods
    -------
    config(config_class: type) -> type
        Registers a configuration class and ensures it meets the necessary criteria.
    """

    def __init__(self, container: Container) -> None:
        """
        Initializes the Register instance with a cache configuration.

        Parameters
        ----------
        cache : CacheConfig, optional
            The cache configuration instance to be used (default is a new instance of `CacheConfig`).
        """
        self.container = container

    def config(self, config_class: type) -> type:
        """
        Registers a configuration class and ensures it meets the required structure.

        This method performs multiple validation steps, including checking if the input
        is a class, verifying the existence of a `config` attribute, and confirming
        inheritance from `IConfig`.

        Parameters
        ----------
        config_class : type
            The class to be registered as a configuration.

        Returns
        -------
        type
            The same class passed as an argument, if registration is successful.

        Raises
        ------
        TypeError
            If `config_class` is not a class or does not inherit from `IConfig`.
        ValueError
            If `config_class` does not have a `config` attribute or is already registered.
        """

        if not isinstance(config_class, type):
            raise TypeError(f"Expected a class, but got {type(config_class).__name__}.")

        if not hasattr(config_class, 'config'):
            raise ValueError(f"Class {config_class.__name__} must have a 'config' attribute.")

        # Extract module name
        section = Reflection(config_class).getFileName(remove_extension=True)

        # Validate section
        if section not in SECTIONS:
            raise ValueError(
                f"Invalid configuration section '{section}'. Allowed sections: {SECTIONS}"
            )

        # Validate inheritance
        if not issubclass(config_class, IConfig):
            raise TypeError(f"Class {config_class.__name__} must inherit from 'IConfig'.")

        # Register configuration
        self.container.config(
            section=section,
            data=Parser.toDict(config_class)
        )