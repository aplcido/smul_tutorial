from django.db import models

# Create your models here.
import string

from django.db import models, transaction
from django.shortcuts import get_object_or_404

BASE = 62
CHARSET = string.ascii_uppercase + string.ascii_lowercase + string.digits


class Counter(models.Model):
    value = models.IntegerField(null=False, default=1)

    def encode(self):
        number = self.value
        code = ""
        while number:
            number, remainder = divmod(number - 1, BASE)
            code = CHARSET[remainder] + code
        return code


class Shurt(models.Model):
    url = models.URLField(db_index=True, unique=True, null=False)
    code = models.CharField(max_length=10, db_index=True, unique=True, null=False)