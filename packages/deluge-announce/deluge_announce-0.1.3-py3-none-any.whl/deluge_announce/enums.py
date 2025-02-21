from enum import Enum


class LogLevel(Enum):
    """Enum class for pythons built in logging class debug types"""

    DEBUG = 10
    INFO = 20
    WARNING = 30
    ERROR = 40
    CRITICAL = 50

    def __str__(self) -> str:
        level_map = {
            LogLevel.DEBUG: "Debug",
            LogLevel.INFO: "Info",
            LogLevel.WARNING: "Warning",
            LogLevel.ERROR: "Error",
            LogLevel.CRITICAL: "Critical",
        }
        return level_map[self]

    @classmethod
    def _missing_(cls, value):
        """Override this method to ignore case sensitivity"""
        if value:
            value = str(value).lower()
            for member in cls:
                member_lowered = member.name.lower()
                if (member_lowered == value) or (
                    member_lowered.replace("_", " ") == value
                ):
                    return member
        raise ValueError(f"No {cls.__name__} member with value '{value}'")
