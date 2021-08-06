from django import forms
from .models import Blog, Comment, Hashtag, Post, Eat_C, Look_C, Play_C, Big_Region, Small_Region  # 민정


class CreateForm(forms.ModelForm):
    class Meta:
        model = Blog
        fields = ['Title', 'Content', 'Image', 'hashtags']#카톡완료 후 작성자 추가하기

class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['text']

class HashtagForm(forms.ModelForm):
    class Meta:
        model = Hashtag
        fields = ['name']

class Eat_CForm(forms.ModelForm):
    class Meta:
        model = Eat_C
        fields = ['Title', 'Content', 'Image', 'big_region', 'small_region']

class Look_CForm(forms.ModelForm):
    class Meta:
        model = Look_C
        fields = ['Title', 'Content', 'big_region', 'small_region']

class Play_CForm(forms.ModelForm):
    class Meta:
        model = Play_C
        fields = ['Title', 'Content', 'big_region', 'small_region']

class Big_RegionForm(forms.ModelForm):
    class Meta:
        model = Big_Region
        fields = ['name']

class Small_RegionForm(forms.ModelForm):
    class Meta:
        model = Small_Region
        fields = ['name']

# ----민정이 개발 부분------


class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ['title', 'date', 'body']  # 제목, 날짜, 내용

# ----예찬이 개발 부분------
