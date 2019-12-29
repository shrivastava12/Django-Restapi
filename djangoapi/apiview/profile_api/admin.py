from django.contrib import admin
from .models import UserProfile
from .models import ProfileFeedItem
# Register your models here.
admin.site.register(UserProfile)
admin.site.register(ProfileFeedItem)