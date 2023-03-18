from enum import Enum

from django.core import exceptions, validators
from django.db import models

def validate_string_alphanumeric(value):
    for char in value:
        if not char.isalnum() and char != '_':
            raise exceptions.ValidationError("Ensure this value contains only letters, numbers, and underscore.")

class Profile(models.Model):
    MIN_LEN_USERNAME = 2
    MAX_LEN_USERNAME = 15

    username = models.CharField(
        max_length=MAX_LEN_USERNAME,
        null=False,
        blank=False,
        validators=(
            validators.MinLengthValidator(MIN_LEN_USERNAME),
            validate_string_alphanumeric,
        ),
    )

    email = models.EmailField(
        null=False,
        blank=False,
    )

    age = models.PositiveIntegerField(
        null=True,
        blank=True,
    )


# With enums
class ChoicesEnum(Enum):
    @classmethod
    def choices(cls):
        return [(x.name, x.value) for x in cls]


class AlbumGenres(ChoicesEnum):
    POP = 'Pop Music'
    JAZZ = "Jazz Music"
    RNB = "R&B Music"
    ROCK = "Rock Music"
    COUNTRY = "Country Music"
    DANCE = "Dance Music"
    HIP_HOP = "Hip Hop Music"
    OTHER = "Other"


# print(AlbumGenres.choices())


class Album(models.Model):
    MAX_LEN_NAME = 30
    MAX_LEN_ARTIST = 30
    MAX_LEN_GENRE = 30

    album_name = models.CharField(
        max_length=MAX_LEN_NAME,
        unique=True,
        null=False,
        blank=False,
        verbose_name='Album Name',
    )

    artist = models.CharField(
        max_length=MAX_LEN_ARTIST,
        null=False,
        blank=False,
    )

    genre = models.CharField(
        max_length=MAX_LEN_GENRE,
        choices=AlbumGenres.choices(),
        null=False,
        blank=False,
    )

    description = models.TextField(
        null=True,
        blank=True,
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
            validators.MinValueValidator(0.0),
        ),
    )

    class Meta:
        ordering = ('pk',)

# # Without enums
# class Album(models.Model):
#     MAX_LEN_CHARS = 30
#     MIN_PRICE_VALUE = 0.0
#
#     POP = 'Pop Music'
#     JAZZ = "Jazz Music"
#     RNB = "R&B Music"
#     ROCK = "Rock Music"
#     COUNTRY = "Country Music"
#     DANCE = "Dance Music"
#     HIP_HOP = "Hip Hop Music"
#     OTHER = "Other"
#
#     MUSICS = (
#         (POP, POP),
#         (JAZZ, JAZZ),
#         (RNB, RNB),
#         (ROCK, ROCK),
#         (COUNTRY, COUNTRY),
#         (DANCE, DANCE),
#         (HIP_HOP, HIP_HOP),
#         (OTHER, OTHER),
#     )
#
#     album_name = models.CharField(
#         unique=True,
#         max_length=MAX_LEN_CHARS,
#         null=False,
#         blank=False,
#         verbose_name="Album Name",
#     )
#
#     artist = models.CharField(
#         max_length=MAX_LEN_CHARS,
#         null=False,
#         blank=False,
#     )
#
#     genre = models.CharField(
#         max_length=MAX_LEN_CHARS,
#         choices=MUSICS,
#         null=False,
#         blank=False,
#     )
#
#     description = models.TextField(
#         null=True,
#         blank=True,
#     )
#
#     image_url = models.URLField(
#         null=False,
#         blank=False,
#         verbose_name="Image URL",
#     )
#
#     price = models.FloatField(
#         null=False,
#         blank=False,
#         validators=(
#             validators.MinValueValidator(MIN_PRICE_VALUE),
#         ),
#     )
#
#     class Meta:
#         ordering = ('pk',)
