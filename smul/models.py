from django.db import models

# Create your models here.
import string

from django.db import models, transaction
from django.shortcuts import get_object_or_404

BASE = 62
CHARSET = string.ascii_uppercase + string.ascii_lowercase + string.digits

#from smul.models import Counter
#>>> c = Counter()
#>>> c.save()
#commands used on the shell to initialize Counter on database
#otherwise counter = get_object_or_404(Counter, pk=1) throws an error
#because of not existing a Counter object in the database

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

    @classmethod
    def get_or_create_shurt(cls, url):
        shurt = cls.objects.filter(url=url).first()
        if shurt:
            return shurt
        counter = get_object_or_404(Counter, pk=1)
        code = counter.encode()
        counter.value += 1
        shurt = cls(url=url, code=code)
        with transaction.atomic():
            shurt.save()
            counter.save()
        return shurt