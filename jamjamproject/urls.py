"""jamjamproject URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path
import jamjamapp.views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', jamjamapp.views.layout, name='layout'),#임시메인
    path('commu_detail/<str:id>/', jamjamapp.views.commu_detail, name='commu_detail'),#커뮤니티 게시글 자세히 보기
    path('community/<int:hashtag_id>/', jamjamapp.views.community, name='community'),#게시글 각 카테고리 페이지(해시태그로 치면 search)
    path('commu_write/commu_create/', jamjamapp.views.commu_create, name='commu_create'),#게시글 C
    path('commu_edit/<str:id>/', jamjamapp.views.commu_edit, name='commu_edit'),#게시글 수정
    path('commu_delete/<str:id>/', jamjamapp.views.commu_delete, name='commu_delete'),#게시글 삭제
    path('commu_delete_comment/<int:post_id>/<int:com_id>/', jamjamapp.views.commu_delete_comment, name='commu_delete_comment'),#댓글 삭제
    path('commu_like/<int:pk>', jamjamapp.views.commu_like, name='commu_like'),
    path('course_eat/', jamjamapp.views.course_eat, name='course_eat'),#course_eat 전체글 보기
    path('course_eat_detail/<str:id>/', jamjamapp.views.course_eat_detail, name='course_eat_detail'),#eat 게시글 자세히 보기
    path('course_eat_R/<int:small_region_id>/', jamjamapp.views.course_eat_R, name='course_eat_R'),#eat search
    path('course_eat_write/course_eat_C/', jamjamapp.views.course_eat_C, name='course_eat_C'),#eat 게시글 C
    path('course_eat_U/<str:id>/', jamjamapp.views.course_eat_U, name='course_eat_U'),#eat 게시글 수정
    path('course_eat_delete/<str:id>/', jamjamapp.views.course_eat_delete, name='course_eat_delete'),#eat 게시글 삭제
    path('course_eat_like/<int:pk>', jamjamapp.views.course_eat_like, name='course_eat_like'),#eat 게시글 좋아요
    path('course_look/', jamjamapp.views.course_look, name='course_look'),#course_eat 전체글 보기
    path('course_look_detail/<str:id>/', jamjamapp.views.course_look_detail, name='course_look_detail'),#look 게시글 자세히 보기
    path('course_look_R/<int:small_region_id>/', jamjamapp.views.course_look_R, name='course_look_R'),#look search
    path('course_look_write/course_look_C/', jamjamapp.views.course_look_C, name='course_look_C'),#look 게시글 C
    path('course_look_U/<str:id>/', jamjamapp.views.course_look_U, name='course_look_U'),#look 게시글 수정
    path('course_look_delete/<str:id>/', jamjamapp.views.course_look_delete, name='course_look_delete'),#look 게시글 삭제
    path('course_look_like/<int:pk>', jamjamapp.views.course_look_like, name='course_look_like'),#look 게시글 좋아요
    path('course_play/', jamjamapp.views.course_play, name='course_play'),#course_eat 전체글 보기
    path('course_play_detail/<str:id>/', jamjamapp.views.course_play_detail, name='course_play_detail'),#play 커뮤니티 게시글 자세히 보기
    path('course_play_R/<int:small_region_id>/', jamjamapp.views.course_play_R, name='course_play_R'),#play search
    path('course_play_write/course_play_C/', jamjamapp.views.course_play_C, name='course_play_C'),#play 게시글 C
    path('course_play_U/<str:id>/', jamjamapp.views.course_play_U, name='course_play_U'),#play 게시글 수정
    path('course_play_delete/<str:id>/', jamjamapp.views.course_play_delete, name='course_play_delete'),#play 게시글 삭제
    path('course_play_like/<int:pk>', jamjamapp.views.course_play_like, name='course_play_like'),#play 게시글 좋아요
    
    
    # ------민정 개발-------

    path('pay/', jamjamapp.views.pay, name='pay'), #아직 수정중
    path('day_detail/', jamjamapp.views.day_detail, name='day_detail'), #데이디테일 페이지
    path('diary/diary_create', jamjamapp.views.diary_create, name='diary_create'), #데이디테일 작성
    path('bucketlist_write/bucket_create/', jamjamapp.views.bucket_create, name='bucket_create'), #버킷리스트 작성
    path('diary_detail/<str:id>/', jamjamapp.views.diary_detail, name='diary_detail'), #데이디테일 디테일 페이지
    path('diary_edit/<str:id>/', jamjamapp.views.diary_edit, name='diary_edit'), #데이디테일 수정
    path('p_edit/<str:id>/', jamjamapp.views.p_edit, name='p_edit'), #프로필 수정
    path('diary_delete/<str:id>/', jamjamapp.views.diary_delete, name='diary_delete'), #데이디테일 삭제
    path('profile/', jamjamapp.views.profile, name='profile'), #프로필 페이지
    path('bucketlist/', jamjamapp.views.bucketlist, name='bucketlist'), #버킷리스트 페이지
    path('bucket_edit/<str:id>', jamjamapp.views.bucket_edit, name='bucket_edit'), #버킷리스트 수정
    path('bucket_delete/<str:id>/', jamjamapp.views.bucket_delete, name='bucket_delete'), #버킷리스트 삭제
    path('bucket_detail/<str:id>/', jamjamapp.views.bucket_detail, name='bucket_detail'), #버킷리스트 디테일
    # ------예찬 개발-------


] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
