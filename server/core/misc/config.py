from decouple import config
import os

# MODE
DEV_MODE = config("DEV_MODE", cast=bool)
LOCAL_MODE = config("LOCAL_MODE", cast=bool)

# PRIVATE KEY
PRIVATE_KEY = config("PRIVATE_KEY")

# MONGODB
MONGO_URI = config("MONGO_URI")

# GOOGLE CREDENTIALS
os.environ["GOOGLE_APPLICATION_CREDENTIALS"]="Google-Credentials.json"

# AWS
AWS_ACCESS_KEY_ID = config("AWS_ACCESS_KEY_ID")
AWS_SECRET_ACCESS_KEY = config("AWS_SECRET_ACCESS_KEY")

# STRIPE API
if DEV_MODE:
    STRIPE_API_KEY = config("STRIPE_DEV_API_KEY")
    STRIPE_WEBHOOK_KEY = config("STRIPE_DEV_WEBHOOK_KEY")
else:
    STRIPE_API_KEY = config("STRIPE_LIVE_API_KEY")
    STRIPE_WEBHOOK_KEY = config("STRIPE_LIVE_WEBHOOK_KEY")

# SENDGRID API
SENDGRID_API_KEY = config("SENDGRID_API_KEY")

# AI APIs
YOUTUBE_API_KEY = config("YOUTUBE_API_KEY")
BING_SEARCH_KEY = config("BING_SEARCH_KEY")
LOVO_API_KEY = config("LOVO_API_KEY")
GOOGLE_ANALYTICS_API_KEY = config("GOOGLE_ANALYTICS_API_KEY")
TEXT_GENERATION_KEY = config("TEXT_GENERATION_KEY")

# Stock Footage APIs
PIXA_BAY_API_KEY = config("PIXA_BAY_API_KEY")
STORYBLOCKS_PUBLIC_KEY = config("STORYBLOCKS_PUBLIC_KEY")
STORYBLOCKS_PRIVATE_KEY = config("STORYBLOCKS_PRIVATE_KEY")
SHUTTERSTOCK_API_KEY = config("SHUTTERSTOCK_API_KEY")
