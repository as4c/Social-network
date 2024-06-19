from django.contrib import admin
from .models import User, Friendship


admin.site.register([User, Friendship])
