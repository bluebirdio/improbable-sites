import enum


class RepositoryTargetType(str, enum.Enum):
    branch = "Branch"
    tag = "Tag"
