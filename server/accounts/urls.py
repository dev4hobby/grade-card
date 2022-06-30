from django.urls import path
from .oauth.kakao import kakao_login, kakao_callback, KakaoLogin

urlpatterns = [
    path("kakao/login", kakao_login, name="kakao_login"),
    path('kakao/callback', kakao_callback, name='kakao_callback'),
    path('kakao/login/finish', KakaoLogin.as_view(), name='kakao_login_finish'),
]
