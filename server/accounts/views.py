import requests
from django.shortcuts import redirect
from app.settings import SOCIAL_OAUTH_CONFIG
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import AllowAny
from rest_framework.response import Response


@api_view(['GET'])
@permission_classes((AllowAny,))
def kakaoGetLogin(request):
    CLIENT_ID = SOCIAL_OAUTH_CONFIG['KAKAO_REST_API_KEY']
    REDIRECT_URL = SOCIAL_OAUTH_CONFIG['KAKAO_REDIRECT_URI']
    url = f"https://kauth.kakao.com/oauth/authorize?client_id={CLIENT_ID}&redirect_uri={REDIRECT_URL}&response_type=code"
    res = redirect(url)
    return res

@api_view(['GET'])
@permission_classes((AllowAny,))
def getUserInfo(request):
    CODE = request.query_params['code']

    url = "https://kauth.kakao.com/oauth/token"
    res = {
        "grant_type": "authorization_code",
        "client_id": SOCIAL_OAUTH_CONFIG['KAKAO_REST_API_KEY'],
        "redirect_uri": SOCIAL_OAUTH_CONFIG['KAKAO_REDIRECT_URI'],
        "client_secret": SOCIAL_OAUTH_CONFIG['KAKAO_SECRET_KEY'],
        "code": CODE
    }
    headers = {
        "Content-Type": "application/x-www-form-urlencoded;charset=utf-8"
    }

    response = requests.post(url, data=res, headers=headers)

    token_json = response.json()
    user_url = "https://kapi.kakao.com/v2/user/me"
    auth = f"Bearer {token_json['access_token']}"
    HEADER = {
        "Authorization": auth,
        "Content-type": "application/x-www-form-urlencoded;charset=utf-8"
    }

    res = requests.get(user_url, headers=HEADER)
    return Response(res.text)