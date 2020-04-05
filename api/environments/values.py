import enum


class ProductionLevel(str, enum.Enum):
    PRODUCTION = "PRODUCTION"
    STAGING = "STAGING"
    DEVELOPMENT = "DEVELOPMENT"


def default_environments():
    return [
        {
            "id": "dev",
            "name": "Development",
            "production_level": "DEVELOPMENT",
            "description": "Development environment",
        },
        {
            "id": "stage",
            "name": "Staging",
            "production_level": "STAGING",
            "description": "Staging environment",
        },
        {
            "id": "prod",
            "name": "Production",
            "production_level": "PRODUCTION",
            "description": "Production environment",
        },
    ]
