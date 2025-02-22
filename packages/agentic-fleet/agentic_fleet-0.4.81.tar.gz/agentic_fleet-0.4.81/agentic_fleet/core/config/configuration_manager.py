"""
Configuration Manager for AgenticFleet

Handles project configuration including project root detection.
"""

import os
from pathlib import Path


class ConfigurationManager:
    """
    Manages configuration settings for the AgenticFleet project.
    """

    def get_project_root(self) -> Path:
        """
        Get the root directory of the project.

        Returns:
            Path: The project root directory
        """
        return Path(__file__).parent.parent.parent.parent
