from django.db import models

# Create your models here.
class Party(models.Model):

    # put characteristics of party here
    name = models.CharField(max_length = 100, unique=True)
    address = models.CharField(max_length = 1000,null=True)
    #status = models.BooleanField(null=True)
    distance = models.DecimalField(decimal_places = 2, max_digits = 4,null=True)
    #entryFee = models.IntegerField(null=True)
    #dateTime = models.DateTimeField(auto_now_add=True, null=True, blank=True)
    #guysAllowed = models.BooleanField(null=True)
    #photo = models.ImageField(upload_to="party/", null=True, blank=True)

    def __str__(self):
        return self.name
#2020-03-01 23:22
