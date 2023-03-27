from enum import Enum
from django.db import models
from django.core import validators

from exam_30_10_22.web.validators import validate_string_min_2_symbols, validate_year_between_1980_and_2049


# Create your models here.

# Profile model
class Profile(models.Model):
    MAX_LEN_USERNAME = 10
    MIN_AGE = 18
    MAX_LEN_NAME = 30
    MAX_LEN_PASSWORD = 30

    username = models.CharField(
        max_length=MAX_LEN_USERNAME,
        null=False,
        blank=False,
        validators=(
            validate_string_min_2_symbols,
        ),
    )

    email = models.EmailField(
        null=False,
        blank=False,
    )

    age = models.PositiveIntegerField(
        null=False,
        blank=False,
        validators=(
            validators.MinValueValidator(MIN_AGE),
        ),
    )

    password = models.CharField(
        max_length=MAX_LEN_PASSWORD,
        null=False,
        blank=False,
    )

    first_name = models.CharField(
        max_length=MAX_LEN_NAME,
        null=True,
        blank=True,
    )

    last_name = models.CharField(
        max_length=MAX_LEN_NAME,
        null=True,
        blank=True,
    )

    profile_picture = models.URLField(
        null=True,
        blank=True,
    )

# Car model

class ChoicesEnum(Enum):
    @classmethod
    def choices(cls):
        return [(x.name, x.value) for x in cls]


class CarTypes(ChoicesEnum):
    SPORTS = 'Sports Car'
    PICKUP = "Pickup"
    CROSSOVER = "Crossover"
    MINIBUS = "Minibus"
    OTHER = "Other"


class Car(models.Model):
    MAX_LEN_TYPE = 10
    MAX_LEN_MODEL = 20
    MIN_PRICE = 1

    type = models.CharField(
        max_length=MAX_LEN_TYPE,
        choices=CarTypes.choices(),
        null=False,
        blank=False,
    )

    model = models.CharField(
        max_length=MAX_LEN_MODEL,
        null=False,
        blank=False,
        validators=(
            validate_string_min_2_symbols,
        ),
    )

    year = models.PositiveIntegerField(
        null=False,
        blank=False,
        validators=(
            validate_year_between_1980_and_2049,
        ),
    )

    image_url = models.URLField(
        null=False,
        blank=False,
        verbose_name='Image URL',
    )

    price = models.FloatField(
        null=False,
        blank=False,
        validators=(
            validators.MinValueValidator(MIN_PRICE),
        ),
    )

    class Meta:
        ordering = ('pk',)

    # def __str__(self):
    #     return self.model