#  * This file is part of me2u project.
#  * (c) Ochui Princewill Patrick <ochui.princewill@gmail.com>
#  * For the full copyright and license information, please view the "LICENSE.md"
#  * file that was distributed with this source 
import os
from django.utils.translation import gettext_lazy as _

#Heroku
import django_heroku
#Heroku

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/2.1/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = os.environ.get('SECRET_KEY')

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = os.environ.get('DEBUG')

ALLOWED_HOSTS = []


# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'django.contrib.sites',

    # 3rd party
    'allauth',
    'allauth.account',
    'allauth.socialaccount',
    #'allauth.socialaccount.providers.twitter',
    #'allauth.socialaccount.providers.facebook',
    #'allauth.socialaccount.providers.google',
    'django_countries',

    # local apps
    'accounts.apps.AccountsConfig',
    'exchange.apps.ExchangeConfig',
    'wallet.apps.WalletConfig',
    'contact.apps.ContactConfig'
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'whitenoise.middleware.WhiteNoiseMiddleware',
    'django.middleware.locale.LocaleMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'me2u.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(BASE_DIR, 'templates')],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

WSGI_APPLICATION = 'me2u.wsgi.application'


# Database
# https://docs.djangoproject.com/en/2.1/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': os.environ.get('DATABASE_NAME'),
        'USER': os.environ.get('DATABASE_USER'),
        'PASSWORD': os.environ.get('DATABASE_PASSWORD'),
        'HOST': os.environ.get('DATABASE_HOST'),
        'PORT': os.environ.get('DATABASE_PORT'),
    }
}


# Password validation
# https://docs.djangoproject.com/en/2.1/ref/settings/#auth-password-validators

AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
    },
]


# Internationalization
# https://docs.djangoproject.com/en/2.1/topics/i18n/

LANGUAGES = (
    ('af', _('Afrikaans')),
    ('ar', _('Arabic')),
    ('ast', _('Asturian')),
    ('az', _('Azerbaijani')),
    ('bg', _('Bulgarian')),
    ('be', _('Belarusian')),
    ('bn', _('Bengali')),
    ('br', _('Breton')),
    ('bs', _('Bosnian')),
    ('ca', _('Catalan')),
    ('cs', _('Czech')),
    ('cy', _('Welsh')),
    ('da', _('Danish')),
    ('de', _('German')),
    ('dsb', _('Lower Sorbian')),
    ('el', _('Greek')),
    ('en', _('English')),
    ('en-au', _('Australian English')),
    ('en-gb', _('British English')),
    ('eo', _('Esperanto')),
    ('es', _('Spanish')),
    ('es-ar', _('Argentinian Spanish')),
    ('es-co', _('Colombian Spanish')),
    ('es-mx', _('Mexican Spanish')),
    ('es-ni', _('Nicaraguan Spanish')),
    ('es-ve', _('Venezuelan Spanish')),
    ('et', _('Estonian')),
    ('eu', _('Basque')),
    ('fa', _('Persian')),
    ('fi', _('Finnish')),
    ('fr', _('French')),
    ('fy', _('Frisian')),
    ('ga', _('Irish')),
    ('gd', _('Scottish Gaelic')),
    ('gl', _('Galician')),
    ('he', _('Hebrew')),
    ('hi', _('Hindi')),
    ('hr', _('Croatian')),
    ('hsb', _('Upper Sorbian')),
    ('hu', _('Hungarian')),
    ('ia', _('Interlingua')),
    ('id', _('Indonesian')),
    ('io', _('Ido')),
    ('is', _('Icelandic')),
    ('it', _('Italian')),
    ('ja', _('Japanese')),
    ('ka', _('Georgian')),
    ('kab', _('Kabyle')),
    ('kk', _('Kazakh')),
    ('km', _('Khmer')),
    ('kn', _('Kannada')),
    ('ko', _('Korean')),
    ('lb', _('Luxembourgish')),
    ('lt', _('Lithuanian')),
    ('lv', _('Latvian')),
    ('mk', _('Macedonian')),
    ('ml', _('Malayalam')),
    ('mn', _('Mongolian')),
    ('mr', _('Marathi')),
    ('my', _('Burmese')),
    ('nb', _('Norwegian Bokmål')),
    ('ne', _('Nepali')),
    ('nl', _('Dutch')),
    ('nn', _('Norwegian Nynorsk')),
    ('os', _('Ossetic')),
    ('pa', _('Punjabi')),
    ('pl', _('Polish')),
    ('pt', _('Portuguese')),
    ('pt-br', _('Brazilian Portuguese')),
    ('ro', _('Romanian')),
    ('ru', _('Russian')),
    ('sk', _('Slovak')),
    ('sl', _('Slovenian')),
    ('sq', _('Albanian')),
    ('sr', _('Serbian')),
    ('sr-latn', _('Serbian Latin')),
    ('sv', _('Swedish')),
    ('sw', _('Swahili')),
    ('ta', _('Tamil')),
    ('te', _('Telugu')),
    ('th', _('Thai')),
    ('tr', _('Turkish')),
    ('tt', _('Tatar')),
    ('udm', _('Udmurt')),
    ('uk', _('Ukrainian')),
    ('ur', _('Urdu')),
    ('vi', _('Vietnamese')),
    ('zh-hans', _('Simplified Chinese')),
    ('zh-hant', _('Traditional Chinese'))
)


LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/2.1/howto/static-files/

STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles')
STATIC_URL = '/static/'
# Extra places for collectstatic to find static files.
STATICFILES_DIRS = (
    os.path.join(BASE_DIR, 'static'),
)

STATICFILES_STORAGE = 'whitenoise.storage.CompressedManifestStaticFilesStorage'

# Custom Settings

AUTH_USER_MODEL = 'accounts.CustomUser'

AUTHENTICATION_BACKENDS = (
    "django.contrib.auth.backends.ModelBackend",
    "allauth.account.auth_backends.AuthenticationBackend",
)

LOGIN_REDIRECT_URL = '/accounts/'

LOCALE_PATHS = (
    os.path.join(BASE_DIR, 'locale'),
)

SITE_ID = 1

ACCOUNT_EMAIL_REQUIRED = True
ACCOUNT_USERNAME_REQUIRED = False
ACCOUNT_AUTHENTICATION_METHOD = "username_email"
ACCOUNT_EMAIL_CONFIRMATION_EXPIRE_DAYS = 7

ACCOUNT_FORMS = {
'signup': 'accounts.forms.CustomSignupForm',
'login': 'accounts.forms.CustomLoginForm',
'reset_password': 'accounts.forms.CustomResetPasswordForm',
'add_email': 'accounts.forms.CustomAddEmailForm',
}

EMAIL_BACKEND = "sendgrid_backend.SendgridBackend"

SENDGRID_API_KEY = os.environ.get('SENDGRID_API_KEY')

#Heroku
django_heroku.settings(locals())
#Heroku
