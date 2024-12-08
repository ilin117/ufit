from django.contrib import admin
from .models import Profile

# Register your models here.
from .models import Post, User, Message, Author

admin.site.register(Post)
admin.site.register(Profile)
admin.site.register(Author)
admin.site.register(Message)
