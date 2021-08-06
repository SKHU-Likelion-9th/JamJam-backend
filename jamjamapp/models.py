from django.db import models
from django.conf import settings
from functools import update_wrapper

#게시글
class Blog(models.Model):
    Title = models.CharField(max_length=200)
    Writer = models.CharField(max_length=100)
    Write_day = models.DateTimeField('date published')
    Content = models.TextField()
    Image = models.ImageField(upload_to='images/', blank=True)
    hashtags = models.ManyToManyField('Hashtag', blank=True)
    Blog_likes = models.ManyToManyField(settings.AUTH_USER_MODEL, related_name="Blog_likes")
    view_count = models.IntegerField(default=0)

    def __str__(self):
        return self.Title

#댓글
class Comment(models.Model):
    def __str__(self):
        return self.text

    post_id = models.ForeignKey(Blog, on_delete=models.CASCADE, related_name='comments')
    text = models.CharField(max_length=50)

#커뮤니티 카테고리를 해시태그라고 편의상 해둠
class Hashtag(models.Model):
    name = models.CharField(max_length=50)
    
    def __str__(self):
        return self.name

#course_eat_C
class Eat_C(models.Model):
    Title = models.CharField(max_length=200)
    Writer = models.CharField(max_length=100)
    Write_day = models.DateTimeField('date published')
    Content = models.TextField()
    Image = models.ImageField(upload_to='images/', blank=True)
    big_region = models.ManyToManyField('big_region', blank=True)
    small_region = models.ManyToManyField('small_region', blank=True)
    Eat_likes = models.ManyToManyField(settings.AUTH_USER_MODEL, related_name="Eat_likes")
    view_count = models.IntegerField(default=0)

    def __str__(self):
        return self.Title

#course_look_C
class Look_C(models.Model):
    Title = models.CharField(max_length=200)
    Writer = models.CharField(max_length=100)
    Write_day = models.DateTimeField('date published')
    Content = models.TextField()
    Image = models.ImageField(upload_to='images/', blank=True)
    big_region = models.ManyToManyField('big_region', blank=True)
    small_region = models.ManyToManyField('small_region', blank=True)
    Look_likes = models.ManyToManyField(settings.AUTH_USER_MODEL, related_name="Look_likes")
    view_count = models.IntegerField(default=0)
    
    def __str__(self):
        return self.Title

#course_play_C
class Play_C(models.Model):
    Title = models.CharField(max_length=200)
    Writer = models.CharField(max_length=100)
    Write_day = models.DateTimeField('date published')
    Content = models.TextField()
    Image = models.ImageField(upload_to='images/', blank=True)
    big_region = models.ManyToManyField('big_region', blank=True)
    small_region = models.ManyToManyField('small_region', blank=True)
    play_likes = models.ManyToManyField(settings.AUTH_USER_MODEL, related_name="Play_likes")
    view_count = models.IntegerField(default=0)
    
    def __str__(self):
        return self.Title

class Big_Region(models.Model):
    name = models.CharField(max_length=50)
    
    def __str__(self):
        return self.name

class Small_Region(models.Model):
    name = models.CharField(max_length=50)
    
    def __str__(self):
        return self.name

# ----민정이 개발 부분------

class Post(models.Model):
    diary_title = models.CharField(max_length=100)#제목
    diary_date = models.CharField(null = False, max_length=15, default='oooo년 oo월 oo일')#기록하고 싶은 날짜( ex) 여행 다녀온 날 등 )
    diary_body = models.TextField()#내용

    def __str__(self):
        return self.diary_title

#버킷리스트 모델
class Bucket(models.Model):
    bucket_title = models.CharField(max_length=100)#제목
    bucket_date = models.CharField(null = False, max_length=15, default='oooo년 oo월 oo일')#하고 싶은 날짜( ex) ~날 ~하기 등 )
    bucket_body = models.TextField()#내용

    def __str__(self):
        return self.bucket_title

#프로필 모델
class Profile(models.Model):
    nickname = models.CharField(max_length=20)

    def __str__(self):
        return self.nickname

#스크랩
class Bookmark(models.Model):
    book_site_name = models.CharField(max_length=30)
    book_url = models.URLField()
    book_contents = models.TextField(blank=True)
    book_created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return "Site name : " + self.book_site_name + ", URL : " + self.book_url

    class Meta:
        ordering = ["-book_created"]


# ----예찬이 개발 부분------
