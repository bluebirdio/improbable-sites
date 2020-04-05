import enum


class RepositoryTargetType(str, enum.Enum):
    branch = "branch"
    tag = "tag"
