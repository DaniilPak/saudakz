from django.contrib import admin
from .models import *

# Register your models here.

admin.site.register(Catalog)
admin.site.register(Category)
# admin.site.register(SubCategory)
admin.site.register(Product)
admin.site.register(ProductImage)
admin.site.register(CommentNRate)
admin.site.register(ImageInstance)
admin.site.register(Bid)
admin.site.register(Notification)
admin.site.register(ChatFriends)
admin.site.register(ChatMessage)