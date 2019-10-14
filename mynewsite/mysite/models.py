from django.db import models

# Create your models here.
from django.utils import timezone


class Post(models.Model):
    title = models.CharField(max_length=200)
    slug = models.CharField(max_length=200)
    body = models.TextField()
    pub_date = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.title


class NewTable(models.Model):
    bigint_f = models.BigIntegerField()
    bool_f = models.BooleanField()
    date_f = models.DateField(auto_now=True)
    char_f = models.CharField(max_length=20, unique=True)
    datetime_f = models.DateTimeField(auto_now_add=True)
    decimal_f = models.DecimalField(max_digits=10, decimal_places=2)
    float_f = models.FloatField(null=True)
    int_f = models.IntegerField(default=2010)
    text_f = models.TextField()


class Product(models.Model):
    SIZES = (
        ('S', 'Small'),
        ('M', 'Medium'),
        ('L', 'Large'),
    )

    sku = models.CharField(max_length=5)
    name = models.CharField(max_length=20)
    price = models.PositiveIntegerField()
    size = models.CharField(max_length=1, choices=SIZES)
    qty = models.PositiveIntegerField(default=0)

    def __str__(self):
        return self.name



class PMOS_COVERATE_AUTOTEST(models.Model):

    DEPT = models.CharField(max_length=20,null=True)
    TEAM = models.CharField(max_length=20,null=True)
    VERSION = models.CharField(max_length=11,null=True)
    COVEREDPROG = models.CharField(max_length=6,null=True)
    ALLPROG = models.CharField(max_length=6,null=True)
    COVERATEPROG = models.CharField(max_length=7,null=True)
    COVERDBRANCH = models.CharField(max_length=6,null=True)
    ALLBRANCH = models.CharField(max_length=6,null=True)
    COVERATEBRANCH = models.CharField(max_length=7,null=True)
    FLAG = models.CharField(max_length=2,null=True)
    UPDATE_DATE = models.CharField(max_length=20,null=True)
    UPDATE_TIME = models.CharField(max_length=20,null=True)

    def __str__(self):
        return self.name