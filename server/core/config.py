import os
from dotenv import load_dotenv

load_dotenv('./.env')

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

PORT = os.environ['PORT']
SECRET_KEY = os.environ['SECRET_KEY']

# database settings
DATABASE_URL = (
    f"mysql://{os.environ['MYSQL_USER']}:"
    f"{os.environ['MYSQL_PASSWORD']}@"
    f"{os.environ['MYSQL_HOST']}:"
    f"{os.environ['MYSQL_PORT']}/"
    f"{os.environ['MYSQL_DB']}"
)
APPS_MODELS = [
    "app.auth.models",
    "app.social_account.models",
    "app.user.models",
    "aerich.models",
]

TORTOISE_ORM = {
    "connections": {"default": DATABASE_URL},
    "apps": {
        "models": {
            "models": APPS_MODELS,
            "default_connection": "default",
        }
    },
}

# Multiple connections
# tortoise_orm = {
#     "connections": {
#         "default": expand_db_url(db_url, True),
#         "second": expand_db_url(db_url_second, True),
#     },
#     "apps": {
#         "models": {"models": ["tests.models", "aerich.models"], "default_connection": "default"},
#         "models_second": {"models": ["tests.models_second"], "default_connection": "second", },
#     },
# }

# settings for jwt authentication
TOKEN_TYPE = os.environ['TOKEN_TYPE']
ALGORITHM = os.environ['ALGORITHM']
ACCESS_TOKEN_JWT_SUBJECT = os.environ['ACCESS_TOKEN_JWT_SUBJECT']
# Token 60 minutes * 24 hours * 8 days = 8 days
ACCESS_TOKEN_EXPIRE_MINUTES = 60 * 24 * 8

# settings for smtp
EMAIL_HOST = os.environ['EMAIL_HOST']
EMAIL_HOST_USER = os.environ['EMAIL_HOST_USER']
EMAIL_PORT = os.environ['EMAIL_PORT']
EMAIL_USE_TLS = os.environ['EMAIL_USE_TLS']
EMAIL_USERNAME = os.environ['EMAIL_USERNAME']
EMAIL_PASSWORD = os.environ['EMAIL_PASSWORD']

# superuser settings
USERNAME_SUPERUSER = os.environ['SUPERUSER_NAME']
EMAIL_SUPERUSER = os.environ['SUPERUSER_EMAIL']
PASSWORD_SUPERUSER = os.environ['SUPERUSER_PASSWORD']
REPEAT_PASSWORD_SUPERUSER = os.environ['SUPERUSER_REPEAT_PASSWORD']

# github
CLIENT_ID = os.environ['GITHUB_CLIENT_ID']
CLIENT_SECRET = os.environ['GITHUB_CLIENT_SECRET']

# aws s3, cf
S3_BUCKET_NAME = "grade-card"
CF_URL = "https://grade.d3fau1t.net"

AWS_SECRET_KEY_ID = os.environ["AWS_SECRET_KEY_ID"]
AWS_SECRET_ACCESS_KEY = os.environ["AWS_SECRET_ACCESS_KEY"]
AWS_REGION_NAME = os.environ["AWS_REGION_NAME"]
