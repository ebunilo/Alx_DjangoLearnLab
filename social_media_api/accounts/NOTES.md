# Notes on the Social Media Project

### signals
After setting up signals, complete the following steps to make it take effect:
- In the __init__.py file of the app, add the line:
default_app_config = 'accounts.apps.AccountsConfig'

- In the apps.py file, inside the AccountsConfig(AppConfig) class, add the method:

def ready(self):
    import account.signals

### Media files (handle where pictures are stored)
- Install Pillow:
pip install Pillow

- In the settings.py file, 

import os
MEDIA_URL = '/media/'
MEDIA_ROOT = os.path.join(BASE_DIR, 'media')

### Register CustomUser and Profile 
In admin.py, create
ProfileAdmin(admin.ModelAdmin) and 
CustomUserAdmin(admin.ModelAdmin) classes
and register them.

### Define REST_FRAMEWORK
In settings.py define configurations for Authentication and Permission classes

REST_FRAMEWORK = {
    'DEFAULT_AUTHENTICATION_CLASSES': [
        'rest_framework.authentication.TokenAuthentication',
    ],
    'DEFAULT_PERMISSION_CLASSES': [
        'rest_framework.permissions.IsAuthenticated',
    ]
}

### Token Authentication
While communicating via API, in the header include:
key: Authorisation value: Token token_value

- For PUT or PATCH
Make sure to include all the "id" in the url. Example:
PUT: /api/users/{id}/
PATCH: /api/users/{id}/



