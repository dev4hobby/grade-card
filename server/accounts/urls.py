from django.urls import path, include
from .oauth.kakao import kakao_login, kakao_callback, KakaoLogin
from rest_framework_simplejwt.views import TokenBlacklistView

urlpatterns = [
    path("token/blacklist/", TokenBlacklistView.as_view(), name="token_blacklist"),
    path("kakao/login/", kakao_login, name="kakao_login"),
    path('kakao/callback/', kakao_callback, name='kakao_callback'),
    path('kakao/login/finish/', KakaoLogin.as_view(), name='kakao_login_finish'),
]
