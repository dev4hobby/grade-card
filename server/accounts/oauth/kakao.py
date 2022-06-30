from django.conf import settings
from django.shortcuts import redirect
from accounts.models import User
from allauth.socialaccount.models import SocialAccount
from dj_rest_auth.registration.views import SocialLoginView
from allauth.socialaccount.providers.kakao import views as kakao_view
from allauth.socialaccount.providers.oauth2.client import OAuth2Client
from django.http import JsonResponse
import requests
from rest_framework import status
from json.decoder import JSONDecodeError
from django.conf import settings
from rest_framework import serializers

state = getattr(settings, "STATE")
BASE_URL = settings.BASE_URL
SOCIAL_OAUTH_CONFIG = settings.SOCIAL_OAUTH_CONFIG
KAKAO_REDIRECT_URI = SOCIAL_OAUTH_CONFIG["KAKAO_REDIRECT_URI"]

def kakao_login(request):
    CLIENT_ID = SOCIAL_OAUTH_CONFIG['KAKAO_REST_API_KEY']
    REDIRECT_URL = SOCIAL_OAUTH_CONFIG['KAKAO_REDIRECT_URI']
    url = f"https://kauth.kakao.com/oauth/authorize?client_id={CLIENT_ID}&redirect_uri={REDIRECT_URL}&response_type=code"
    res = redirect(url)
    return res


def kakao_callback(request):
    code = request.GET['code']

    url = "https://kauth.kakao.com/oauth/token"
    res = {
        "grant_type": "authorization_code",
        "client_id": SOCIAL_OAUTH_CONFIG['KAKAO_REST_API_KEY'],
        "redirect_uri": SOCIAL_OAUTH_CONFIG['KAKAO_REDIRECT_URI'],
        "client_secret": SOCIAL_OAUTH_CONFIG['KAKAO_SECRET_KEY'],
        "code": code
    }
    headers = {
        "Content-Type": "application/x-www-form-urlencoded;charset=utf-8"
    }
    response = requests.post(url, data=res, headers=headers)

    token_json = response.json()
    error = token_json.get("error")
    if error is not None:
        raise JSONDecodeError(error)
    access_token = token_json.get("access_token")
    user_url = "https://kapi.kakao.com/v2/user/me"
    auth = f"Bearer {access_token}"
    HEADER = {
        "Authorization": auth,
        "Content-type": "application/x-www-form-urlencoded;charset=utf-8"
    }

    res = requests.get(user_url, headers=HEADER)
    profile_json = res.json()
    kakao_account = profile_json.get("kakao_account")
    email = kakao_account.get("email")

    """
    Signup or Signin Request
    """
    try:
        user = User.objects.get(email=email)
        # 기존에 가입된 유저의 Provider가 kakao가 아니면 에러 날리고 맞으면 로그인
        # 다른 SNS로 가입된 유저
        social_user = SocialAccount.objects.get(user=user)
        if social_user is None:
            return JsonResponse(
                {"err_msg": "email exists but not social usser"},
                status=status.HTTP_400_BAD_REQUEST,
            )

            # 기존에 Google로 가입된 유저
            data = {"access_token": access_token, "code": code}
            accept = requests.post(f"{BASE_URL}/accounts/kakao/login/finish/", data=data)
            accept_status = accept.status_code
            print()
            return JsonResponse(
                {"err_msg": "email exists but not social usser"},
                status=status.HTTP_400_BAD_REQUEST,
            )
            # if accept_status != 200:
            #     return JsonResponse(
            #         {"err_msg": "failed to signin"}, status=accept_status
            #     )
            accept_json = accept.json()
            accept_json.pop("user", None)
            return JsonResponse(accept_json)
    except User.DoesNotExist:
        # 기존에 가입된 유저가 없으면 새로 가입
        data = {"access_token": access_token, "code": code, "email": email}
        accept = requests.post(f"{BASE_URL}/accounts/kakao/login/finish/", data=data)
        accept_status = accept.status_code
        print(accept_status)
        if accept_status != 200:
            return JsonResponse({"err_msg": "failed to signup"}, status=accept_status)
        # user의 pk, email, first name, last name, Access Token, Refresh Token 받아옴
        accept_json = accept.json()
        print("accept_json >> ",accept_json)
        # accept_json.pop("user", None)
        return JsonResponse(accept_json)


class KakaoLogin(SocialLoginView):
    adapter_class = kakao_view.KakaoOAuth2Adapter
    client_class = OAuth2Client
    callback_url = KAKAO_REDIRECT_URI