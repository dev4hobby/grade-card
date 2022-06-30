from django.urls import path
from accounts.views import getUserInfo, kakaoGetLogin

urlpatterns = [
    path("kakao", kakaoGetLogin),
    path('kakao/callback', getUserInfo),
]
