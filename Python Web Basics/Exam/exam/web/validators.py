from django.core import exceptions
from django.core.exceptions import ValidationError


def validate_string_min_2_symbols(value):
    MIN_SYMBOLS = 2
    if len(value) < MIN_SYMBOLS:
        raise exceptions.ValidationError("The username must be a minimum of 2 chars")


def validate_year_between_1980_and_2049(value):
    MIN_YEAR = 1980
    MAX_YEAR = 2049
    if value < MIN_YEAR or value > MAX_YEAR:
        raise exceptions.ValidationError("Year must be between 1980 and 2049")