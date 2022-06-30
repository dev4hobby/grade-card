import requests
from django.conf import settings
from django.http import JsonResponse
from rest_framework import status
from json.decoder import JSONDecodeError
from accounts.models import User