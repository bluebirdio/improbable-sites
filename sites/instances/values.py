import enum


class Environment(str, enum.Enum):
    production = "production"
    staging = "staging"
    testing = "testing"
    development = "development"
