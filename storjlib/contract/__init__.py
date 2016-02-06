import jsonschema
from . schema import CONTRACT_SCHEMA  # NOQA


def validate(contract):
    try:
        jsonschema.validate(contract, CONTRACT_SCHEMA)
        return True
    except jsonschema.exceptions.ValidationError:
        return False