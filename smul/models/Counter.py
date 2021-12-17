from django.db import models

# Create your models here.
import string

BASE = 62
CHARSET = string.ascii_uppercase + string.ascii_lowercase + string.digits

#from smul.models.Counter import Counter
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
