# from django.http.response import HttpResponse
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.utils import timezone
from .models import Blog, Comment, Hashtag, Eat_C, Look_C, Play_C, Big_Region, Small_Region, Profile, Bucket, Post
from .forms import CreateForm, CommentForm, Eat_CForm, Look_CForm, Play_CForm, Big_RegionForm, Small_RegionForm, PostForm, ProfileForm, BucketForm, PostForm
#from datetime import date, datetime, timedelta

# Create your views here.


def layout1(request):
    return render(request, 'layout1.html')


def layout2(request):
    return render(request, 'layout2.html')


def login(request):
    return render(request, 'login.html')


def main(request):
    return render(request, 'main.html')
# ------frontend 개발-------

#임시 메인페이지
def layout(request):
    blogs = Blog.objects
    hashtag = Hashtag.objects
    return render(request, 'layout.html', {'blogs':blogs, 'hashtag':hashtag})

#커뮤니티 첫 페이지
def community(request, hashtag_id):
    hashtag = get_object_or_404(Hashtag, pk=hashtag_id)
    blogs = Blog.objects
    return render(request, 'community/community.html', {'blogs':blogs, 'hashtag':hashtag})

#커뮤니티 Write
@login_required
def commu_write(request):
    return render(request, 'community/commu_write.html')

#커뮤니티 C
@login_required
def commu_create(request, blog=None):
    hashtag = Hashtag.objects
    if request.method == "POST":
        form = CreateForm(request.POST, request.FILES, instance=blog)
        if form.is_valid():
            blog = form.save(commit=False)
            blog.Write_day = timezone.datetime.now()
            blog.save()
            form.save_m2m()
            return redirect('layout')
    else:
        form = CreateForm(instance=blog)
        return render(request, 'community/commu_write.html', {'form':form, 'hashtag':hashtag})

#커뮤니티 게시글 자세히 보기 페이지 + 댓글
@login_required
def commu_detail(request, id):
    blog = get_object_or_404(Blog, id = id)
    default_view_count = blog.view_count
    blog.view_count = default_view_count + 1
    blog.save()
    #여기서부터 댓글
    if request.method == 'POST':
        form = CommentForm(request.POST)
        if form.is_valid():
           comment = form.save(commit=False)
           comment.post_id = blog
           comment.text = form.cleaned_data['text']
           comment.save()
        return redirect('commu_detail', id)
    else:
        form=CommentForm()
    return render(request, 'community/commu_detail.html', {'blog':blog, 'form':form})

#커뮤니티 U
@login_required
def commu_edit(request, id):
   blog = get_object_or_404(Blog, id = id)
   if request.method == "POST":
       form = CreateForm(request.POST, instance=blog)
       if form.is_valid():
           form.save(commit=False)
           form.save()
           return redirect('commu_detail', id)
   else:
       form = CreateForm(instance=blog)
   return render(request, 'community/commu_edit.html', {'form':form})

#@login_required
#def commu_edit(request, pk):
#    notice = Blog.objects.get(id=pk)
#    
#    if request.method == "POST":
#        if(notice.Writer == request.user):
#            form = CreateForm(request.POST, instance=notice)
#            if form.is_valid():
#                notice = form.save(commit = False)
#                notice.save()
#                messages.success(request, "수정되었습니다.")
#                return redirect('/detail/'+str(pk))
#    else:
#        notice = Blog.objects.get(id=pk)
#        if notice.Writer == request.user:
#            form = CreateForm(instance=notice)
#            context = {
#                'form': form,
#                'edit': '수정하기',
#            }
#            return render(request, "community/commu_edit.html", context)
#        else:
#            messages.error(request, "본인 게시글이 아닙니다.")
#            return redirect('/detail/'+str(pk))

#게시글 삭제
@login_required
def commu_delete(request, id):
    delete_blog = get_object_or_404(Blog, id = id)
    delete_blog.delete()
    return redirect ('layout')

#댓글 삭제
@login_required
def commu_delete_comment(request, com_id, post_id):
    mycom = Comment.objects.get(id=com_id)
    mycom.delete()
    return redirect ('commu_detail', post_id)

#좋아요
@login_required
def commu_like(request, pk):
    if not request.user.is_active:
        return HttpResponse('First SignIn please')

    blog = get_object_or_404(Blog, pk=pk)
    user = request.user

    if blog.Blog_likes.filter(id=user.id).exists():
        blog.Blog_likes.remove(user)
    else:
        blog.Blog_likes.add(user)
    
    return redirect('commu_detail', pk)

#course_eat 전체 목록
def course_eat(request):
    eat_Cs = Eat_C.objects
    return render(request, 'course/course_eat.html', {'eat_Cs':eat_Cs})

#course_eat_write
@login_required
def course_eat_write(request):
    return render(request, 'course/course_eat_C.html')

#course_eat_C
@login_required
def course_eat_C(request, eat_C=None):
    big_region = Big_Region.objects
    small_region = Small_Region.objects
    if request.method == "POST":
        form = Eat_CForm(request.POST, request.FILES, instance=eat_C)
        if form.is_valid():
            eat_C = form.save(commit=False)
            eat_C.Write_day = timezone.datetime.now()
            eat_C.save()
            form.save_m2m()
            return redirect('course_eat')
    else:
        form = Eat_CForm(instance=eat_C)
        return render(request, 'course/course_eat_C.html', {'form':form, 'big_region':big_region, 'small_region':small_region})

#course_look 전체 목록
def course_look(request):
    look_Cs = Look_C.objects
    return render(request, 'course/course_look.html', {'look_Cs':look_Cs})

#course_look_write
@login_required
def course_look_write(request):
    return render(request, 'course/course_eat_C.html')

#course_look_C
@login_required
def course_look_C(request, look_C=None):
    big_region = Big_Region.objects
    small_region = Small_Region.objects
    if request.method == "POST":
        form = Look_CForm(request.POST, request.FILES, instance=look_C)
        if form.is_valid():
            look_C = form.save(commit=False)
            look_C.Write_day = timezone.datetime.now()
            look_C.save()
            look_C.save_m2m()
            return redirect('course/course_look')
    else:
        form = Look_CForm(instance=look_C)
        return render(request, 'course/course_look_C.html', {'form':form, 'big_region':big_region, 'small_region':small_region})

#course_play 전체 목록
def course_play(request):
    play_Cs = Play_C.objects
    return render(request, 'course/course_play.html', {'play_Cs':play_Cs})

#course_play_write
@login_required
def course_play_write(request):
    return render(request, 'course/course_play_C.html')

#course_play_C
@login_required
def course_play_C(request, play_C=None):
    big_region = Big_Region.objects
    small_region = Small_Region.objects
    if request.method == "POST":
        form = Play_CForm(request.POST, request.FILES, instance=play_C)
        if form.is_valid():
            play_C = form.save(commit=False)
            play_C.Write_day = timezone.datetime.now()
            play_C.save()
            play_C.save_m2m()
            return redirect('course/course_play')
    else:
        form = Play_CForm(instance=play_C)
        return render(request, 'course/course_play_C.html', {'form':form, 'big_region':big_region, 'small_region':small_region})

#course_eat 게시글 자세히 보기 페이지 + 댓글
@login_required
def course_eat_detail(request, id):
    eat_C = get_object_or_404(Eat_C, id = id)
    default_view_count = eat_C.view_count
    eat_C.view_count = default_view_count + 1
    eat_C.save()
    if request.method == 'POST':
        form = CommentForm(request.POST)
        if form.is_valid():
           comment = form.save(commit=False)
           comment.post_id = eat_C
           comment.text = form.cleaned_data['text']
           comment.save()
        return redirect('course_eat_detail', id)
    else:
        form=CommentForm()
        return render(request, 'course/course_eat_detail.html', {'eat_C':eat_C, 'form':form})

#댓글 삭제
@login_required
def course_eat_delete_comment(request, com_id, post_id):
    mycom = Comment.objects.get(id=com_id)
    mycom.delete()
    return redirect ('course_eat_detail', post_id)

#course_eat_U
@login_required
def course_eat_U(request, id):
   eat_C = get_object_or_404(Eat_C, id = id)
   if request.method == "POST":
       form = Eat_CForm(request.POST, instance=eat_C)
       if form.is_valid():
           form.save(commit=False)
           form.save()
           return redirect('course_eat_detail', id)
   else:
       form = Eat_CForm(instance=eat_C)
   return render(request, 'course/course_eat_U.html', {'form':form})

#course_eat 삭제
@login_required
def course_eat_delete(request, id):
    delete_eat_C = get_object_or_404(Eat_C, id = id)
    delete_eat_C.delete()
    return redirect ('course_eat')

#course_eat 좋아요
@login_required
def course_eat_like(request, pk):
    if not request.user.is_active:
        return HttpResponse('First SignIn please')

    eat_C = get_object_or_404(Eat_C, pk=pk)
    user = request.user

    if eat_C.Eat_likes.filter(id=user.id).exists():
        eat_C.Eat_likes.remove(user)
    else:
        eat_C.Eat_likes.add(user)
    
    return redirect('course_eat_detail', pk)

#course_look 게시글 자세히 보기 페이지
@login_required
def course_look_detail(request, id):
    look_C = get_object_or_404(Look_C, id = id)
    default_view_count = look_C.view_count
    look_C.view_count = default_view_count + 1
    look_C.save()
    return render(request, 'course/course_look_detail', {'look_C':look_C})

#course_look_U
@login_required
def course_look_U(request, id):
   look_C = get_object_or_404(Look_C, id = id)
   if request.method == "POST":
       form = Look_CForm(request.POST, instance=look_C)
       if form.is_valid():
           form.save(commit=False)
           form.save()
           return redirect('course_look_detail', id)
   else:
       form = Look_CForm(instance=look_C)
   return render(request, 'course/course_look_U.html', {'form':form})

#course_look 삭제
@login_required
def course_look_delete(request, id):
    delete_look_C = get_object_or_404(Look_C, id = id)
    delete_look_C.delete()
    return redirect ('course/course_look_R')

#course_look 좋아요
@login_required
def course_look_like(request, pk):
    if not request.user.is_active:
        return HttpResponse('First SignIn please')

    look_C = get_object_or_404(Look_C, pk=pk)
    user = request.user

    if look_C.Look_likes.filter(id=user.id).exists():
        look_C.Look_likes.remove(user)
    else:
        look_C.Look_likes.add(user)
    
    return redirect('course_look_detail', pk)

#course_play 게시글 자세히 보기 페이지
@login_required
def course_play_detail(request, id):
    play_C = get_object_or_404(Play_C, id = id)
    default_view_count = play_C.view_count
    play_C.view_count = default_view_count + 1
    play_C.save()
    return render(request, 'course/course_play', {'play_C':play_C})

#course_play_U
@login_required
def course_play_U(request, id):
   play_C = get_object_or_404(Play_C, id = id)
   if request.method == "POST":
       form = Play_CForm(request.POST, instance=play_C)
       if form.is_valid():
           form.save(commit=False)
           form.save()
           return redirect('course_play_detail', id)
   else:
       form = Play_CForm(instance=play_C)
   return render(request, 'course/course_play_U.html', {'form':form})

#course_play 삭제
@login_required
def course_play_delete(request, id):
    delete_play_C = get_object_or_404(Play_C, id = id)
    delete_play_C.delete()
    return redirect ('course/course_play_R')

#course_play 좋아요
@login_required
def course_play_like(request, pk):
    if not request.user.is_active:
        return HttpResponse('First SignIn please')

    play_C = get_object_or_404(Play_C, pk=pk)
    user = request.user

    if play_C.play_likes.filter(id=user.id).exists():
        play_C.play_likes.remove(user)
    else:
        play_C.play_likes.add(user)
    
    return redirect('course_play_detail', pk)


#course_eat 첫 페이지
def course_eat_R(request, small_region_id):
    small_region = get_object_or_404(Small_Region, pk=small_region_id)
    eat_Cs = Eat_C.objects
    return render(request, 'course/course_eat_R.html', {'eat_Cs':eat_Cs, 'small_region':small_region})

#course_look 첫 페이지
def course_look_R(request, small_region_id):
    small_region = get_object_or_404(Small_Region, pk=small_region_id)
    look_Cs = Look_C.objects
    return render(request, 'course/course_look_R.html', {'look_Cs':look_Cs, 'small_region':small_region})

#course_play 첫 페이지
def course_play_R(request, small_region_id):
    small_region = get_object_or_404(Small_Region, pk=small_region_id)
    play_Cs = Play_C.objects
    return render(request, 'course/course_play_R.html', {'play_Cs':play_Cs, 'small_region':small_region})



# ------민정이 개발-------

# day_detail
def day_detail(request):
    posts = Post.objects
    return render(request, 'day_detail.html', {'posts':posts})

# 프로필
def profile(request):
    profiles = Profile.objects
    return render(request, 'mypage/profile.html', {'profiles':profiles})

# 버킷리스트
def bucketlist(request):
    buckets = Bucket.objects
    return render(request, 'bucketlist.html', {'buckets':buckets})

#다이어리 작성
def diary_create(request):
    if request.method == "POST":
        form = PostForm(request.POST)
        if form.is_valid():
            form = form.save(commit=False)
            form.save()
            return redirect('day_detail')
    else:
        form = PostForm
        return render(request, 'diary.html', {'form':form})

#버킷리스트 작성
def bucket_create(request):
    if request.method == "POST":
        form = BucketForm(request.POST)
        if form.is_valid():
            bucket = form.save(commit=False)
            bucket.save()
            return redirect('bucketlist')
    else:
        form = BucketForm
        return render(request, 'bucketlist_write.html', {'form':form})

#다이어리 디테일
def diary_detail(request, id):
    post = get_object_or_404(Post, id = id)
    if request.method == 'POST':
        form = PostForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.post_id = post
            post.text = form.cleaned_data['text']
            post.save()
            return redirect('day_detail', id)
    else:
        form=PostForm()
        return render(request, 'day_detail_detail.html', {'post':post, 'form':form})

#버킷리스트 디테일
def bucket_detail(request, id):
    bucket = get_object_or_404(Bucket, id = id)
    if request.method == 'POST':
        form = BucketForm(request.POST)
        if form.is_valid():
            bucket = form.save(commit=False)
            bucket.post_id = bucket
            bucket.text = form.cleaned_data['text']
            bucket.save()
            return redirect('bucketlist', id)
    else:
        form=BucketForm()
        return render(request, 'bucketlist_detail.html', {'bucket':bucket, 'form':form})

#데이디테일 수정
def diary_edit(request, id):
    post = get_object_or_404(Post, id = id)
    if request.method == "POST":
        form = PostForm(request.POST, instance=post)
        if form.is_valid():
            form.save(commit=False)
            form.save()
            return redirect('day_detail')
    else:
        form = PostForm(instance=post)
        return render(request, 'diary_edit.html', {'form':form})

#버킷리스트 수정
def bucket_edit(request, id):
    bucket = get_object_or_404(Bucket, id = id)
    if request.method == "POST":
        form = BucketForm(request.POST, instance=bucket)
        if form.is_valid():
            form.save(commit=False)
            form.save()
            return redirect('bucketlist')
    else:
        form = BucketForm(instance=bucket)
        return render(request, 'bucketlist_edit.html', {'form':form})

#프로필 (비번)수정
def p_edit(request, id):
    post = get_object_or_404(Post, id = id)
    if request.method == "POST":
        form = ProfileForm(request.POST, instance=post)
        if form.is_valid():
            form.save(commit=False)
            form.save()
            return redirect('layout')
    else:
        form = ProfileForm(instance=post)
        return render(request, 'profile_edit.html', {'form':form})

#다이어리 삭제
def diary_delete(request, id):
    post = get_object_or_404(Post, id = id)
    post.delete()
    return redirect('day_detail')

#버킷리스트 삭제
def bucket_delete(request, id):
    delete_bucket = get_object_or_404(Bucket, id = id)
    delete_bucket.delete()
    return redirect('bucketlist')

#젬 결제
def pay(request):
    return render(request, 'shop/pay.html')

# ------예찬이 개발-------
