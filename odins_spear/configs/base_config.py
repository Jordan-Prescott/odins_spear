import copy


class BaseConfig:
    def __init__(self, default_config: dict):
        """Base class for all config classes. This class is used to store the default

        Args:
            default_config (dict): Default configuration for the config class.
        """
        self._default_config = default_config
        self.data = default_config.copy()

    def get_config(self):
        """Returns the current configuration.

        Returns:
            dict: Current configuration.
        """
        return self.data

    def get_section(self, key_path: str):
        """
        Retrieves a copy of a specific section of the configuration using dot notation.

        Args:
            key_path (str): Dot-separated path to the section (e.g., 'serviceInstanceProfile.name').

        Returns:
            A copy of the specified section, or None if the path doesn't exist.
        """
        import copy

        keys = key_path.split(".")
        data = self.data  # Start with the root configuration dictionary

        for key in keys:
            if isinstance(data, list) and key.isdigit():
                key = int(key)
                if key < len(data):
                    data = data[key]
                else:
                    return None
            elif isinstance(data, dict) and key in data:
                data = data[key]
            else:
                return None

        # Return a deep copy to ensure the original data remains unmodified
        return copy.deepcopy(data)

    def update_config(self, new_config: dict):
        """
        Updates the entire configuration with a custom one.

        Args:
            new_config (dict): A dictionary containing the new configuration.
        """
        if not isinstance(new_config, dict):
            raise TypeError("The new configuration must be a dictionary.")
        self.data = copy.deepcopy(new_config)

    def reset_config(self):
        """Resets the configuration to the default configuration."""
        self.data = self._default_config.copy()
