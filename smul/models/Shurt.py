# Create your models here.
from django.db import models, transaction
from django.shortcuts import get_object_or_404
from .Counter import Counter

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