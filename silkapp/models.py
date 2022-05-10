

from django.db import models

# AUTH MODEL 
from django.contrib.auth.models import User
from django.forms import CharField
import datetime
from pytz import timezone

# Create your models here.

# Main catalog which contains categories related to this catalog only!!!

class Catalog(models.Model):
    title = models.CharField(max_length=100)

    def __str__(self):
        return self.title

class Category(models.Model):
    title = models.CharField(max_length=100)
    catalog = models.ForeignKey(Catalog, on_delete=models.CASCADE)
    slug = models.SlugField(unique=True)

    def __str__(self):
        return '%s %s %s' % (self.title, ' relates to catalog: ', self.catalog.title)

class SubCategory(models.Model):
    title = models.CharField(max_length=100)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    slug = models.SlugField(unique=True)

    def __str__(self):
        return '%s %s %s' % (self.title, ' relates to category: ', self.category.title)

class ProductImage(models.Model):
    img = models.ImageField(upload_to='photos/%Y/%m/%d')

class CommentNRate(models.Model):
    text = models.TextField()
    rate = models.DecimalField(max_digits=1, decimal_places=0, default=0)
    author = models.CharField(max_length=150)

class Product(models.Model):
    title = models.CharField(max_length=100)
    sub_category = models.ForeignKey(SubCategory, on_delete=models.CASCADE, blank=True)
    slug = models.SlugField(unique=True)

    price = models.DecimalField(max_digits=9 ,decimal_places=2)
    img = models.ManyToManyField(ProductImage)
    desc = models.TextField(max_length=600)
    # Rate system
    rate = models.DecimalField(max_digits=2, decimal_places=1, default=0.0)
    comment = models.ManyToManyField(CommentNRate, blank=True)
    # Owner of the product
    owner = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return '%s %s %s' % (self.title, ' relates to Subcategory: ', self.sub_category.title)

class ImageInstance(models.Model):
    img = CharField()

# Bid 
class Bid(models.Model):
    bidname = models.CharField(max_length=150)
    biddesc = models.TextField()
    bidtype = models.ForeignKey(Category, on_delete=models.CASCADE)
    owner = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return '%s' % (self.bidname)
        
# Notifications 
class Notification(models.Model):
    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=150)
    initiator = models.ForeignKey(User, on_delete=models.CASCADE, related_name="Initiator+")

from django.utils import timezone
# Chat. No web sockets
class ChatMessage(models.Model):
    sender = models.ForeignKey(User, on_delete=models.CASCADE, related_name="User who sends message+")
    receiver = models.ForeignKey(User, on_delete=models.CASCADE, related_name="User who receives message+")
    text = models.TextField()
    tstamp = models.DateField(default=datetime.date.today)
    time = models.TimeField(default=timezone.now)

class ChatFriends(models.Model):
    friend1 = models.ForeignKey(User, on_delete=models.CASCADE, related_name="Friend one+")
    friend2 = models.ForeignKey(User, on_delete=models.CASCADE, related_name="Friend two+")


