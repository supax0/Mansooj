

"""
Mansooj Runtime Context
-------------------------------
Centralized configuration and environment hub for Arabic text processing.
Flexible, modular, and user-friendly with fine-grained control over core engines.
"""



from .config import auto_config
from .type import ConfigDict

class Runtime:
    """Basic runtime configuration setup for Mansooj modules."""

    def __init__(self, user_config: ConfigDict | None = None) -> None:
        """Initialize the runtime context with user-defined configurations."""
        self.config: ConfigDict = auto_config(user_config=user_config)

    def summary(self) -> dict:
        """Return a simple summary of the current configuration."""
        return {
            "language": self.config.get("language", "ar"),
            "direction": self.config.get("direction", "rtl")
        }

# Global instance (can be extended later)
__Mansooj__: Runtime = Runtime()

def get_runtime() -> Runtime:
    """Get the global Mansooj runtime instance."""
    return __Mansooj__
