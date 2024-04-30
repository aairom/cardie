from django.contrib import admin
from authentication.models import User
from main.models import Server, Card

admin.site.register(User)
admin.site.register(Server)
admin.site.register(Card)