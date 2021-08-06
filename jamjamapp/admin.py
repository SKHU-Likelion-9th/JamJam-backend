from django.contrib import admin
from .models import Post, Profile, Bucket, Blog, Comment, Hashtag, Big_Region, Small_Region

admin.site.register(Blog)
admin.site.register(Hashtag)
admin.site.register(Comment)
admin.site.register(Big_Region)
admin.site.register(Small_Region)
# ----민정이 개발 부분------

admin.site.register(Post)
admin.site.register(Profile)
admin.site.register(Bucket)

# ----예찬이 개발 부분------
