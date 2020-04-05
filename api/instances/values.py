import enum


class ProductionLevel(str, enum.Enum):
    PRODUCTION = "PRODUCTION"
    STAGING = "STAGING"
    TEST = "TEST"
    DEVELOPMENT = "DEVELOPMENT"
