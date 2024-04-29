from enum import Enum


class Env(Enum):
    PROD = 'prod'
    PREPROD = 'preprod'
    STAGE = 'stage'


class Domain(Enum):
    CANARY = 'canary'
    REGULAR = 'regular'
