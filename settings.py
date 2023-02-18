from os import environ


SESSION_CONFIGS = [

dict(
        name='Studio_23_Lite',
        display_name="Studio_23_Lite",
        num_demo_participants=2,
        app_sequence=['Intro_Lite','Fase1_Lite', 'bret_Lite', 'Fase_Likert', 'Fase4', 'FinalPayment']
     ),
    dict(
        name='Studio_23',
        display_name="Studio_23",
        num_demo_participants=2,
        app_sequence=['Intro','Fase1NEW', 'bret', 'Fase_Likert', 'Fase4', 'FinalPayment']
     ),
    dict(
        name='Fase1NEW',
        display_name="Fase1NEW",
        num_demo_participants=1,
        app_sequence=['Fase1NEW', 'Fase2NEW', 'FinalPayment']
     ),
    dict(
        name='Fase1_SuperLite',
        display_name="Fase1_SuperLite",
        num_demo_participants=10,
        app_sequence=['Fase1_SuperLite', 'FinalPaymentSuperLite']
     ),
    dict(
        name='Fase1_Lite',
        display_name="Fase1_Lite",
        num_demo_participants=1,
        app_sequence=['Fase1_Lite', 'FinalPayment']
     ),
    dict(
        name='Intro_Lite',
        display_name="Intro_Lite",
        num_demo_participants=2,
        app_sequence=['Intro_Lite']
     ),
    dict(
        name='FinalPaymentSuperLite',
        display_name="FinalPaymentSuperLite",
        num_demo_participants=30,
        app_sequence=['FinalPaymentSuperLite']
     ),
    dict(
        name='Fase4',
        display_name="Fase4",
        num_demo_participants=1,
        app_sequence=['Fase4']
    ),
    dict(
        name='bret',
        display_name="bret",
        num_demo_participants=1,
        app_sequence=['bret','FinalPaymentSuperLite']
    ),
    dict(
        name='bret_Lite',
        display_name="bret_Lite",
        num_demo_participants=1,
        app_sequence=['bret_Lite','FinalPaymentSuperLite']
    ),
    dict(
        name='Fase_Likert',
        display_name="Questionario_finale",
        num_demo_participants=1,
        app_sequence=['Fase_Likert','Fase4']
    )
]

# if you set a property in SESSION_CONFIG_DEFAULTS, it will be inherited by all configs
# in SESSION_CONFIGS, except those that explicitly override it.
# the session config can be accessed from methods in your apps as self.session.config,
# e.g. self.session.config['participation_fee']

SESSION_CONFIG_DEFAULTS = dict(
    real_world_currency_per_point=1.00, participation_fee=0.00, doc=""
)

# ISO-639 code
# for example: de, fr, ja, ko, zh-hans
LANGUAGE_CODE = 'en'

# e.g. EUR, GBP, CNY, JPY
REAL_WORLD_CURRENCY_CODE = 'EUR'
USE_POINTS = False
TIME_ZONE = 'UTC'

ADMIN_USERNAME = 'admin'
# for security, best to set admin password in an environment variable
ADMIN_PASSWORD = environ.get('OTREE_ADMIN_PASSWORD')

DEMO_PAGE_INTRO_HTML = """ """

SECRET_KEY = 'd*234n^cxml5nkk09#r0%&%8$kt)pwi3qq)8jk36ts*y)nk)kf'

# if an app is included in SESSION_CONFIGS, you don't need to list it here
INSTALLED_APPS = ['otree']

PARTICIPANT_FIELDS = ['applearea']
STATICFILES_STORAGE = 'django.contrib.staticfiles.storage.StaticFilesStorage'

ROOMS = [
    dict(
        name='pilot_1',
        display_name = 'Studio Pilota 1',
        participant_label_file='rooms/pilot1label.txt',
        use_secure_urls=True
    ),
    dict(
        name='pilot_2',
        display_name = 'Studio Pilota 2',
        participant_label_file='rooms/pilot2label.txt',
        use_secure_urls=True
    ),
    dict(
        name='pilot_3',
        display_name = 'Studio Pilota 3',
        participant_label_file='rooms/pilot3label.txt',
        use_secure_urls=True
    ),
    dict(
        name='day_1',
        display_name = 'Studio Giorno 1',
        participant_label_file='rooms/day1_label.txt',
        use_secure_urls=True
    ),
    dict(
        name='day_2',
        display_name = 'Studio Giorno 2',
        participant_label_file='rooms/day2_label.txt',
        use_secure_urls=True
    ),
    dict(
        name='day_3',
        display_name = 'Studio Giorno 3',
        participant_label_file='rooms/day3_label.txt',
        use_secure_urls=True
    ),
    dict(
        name='day_4',
        display_name = 'Studio Giorno 4',
        participant_label_file='rooms/day4_label.txt',
        use_secure_urls=True
    ),
    dict(
        name='day_5',
        display_name = 'Studio Giorno 5',
        participant_label_file='rooms/day5_label.txt',
        use_secure_urls=True
    ),
    dict(
        name='day_6',
        display_name = 'Studio Giorno 6',
        participant_label_file='rooms/day6_label.txt',
        use_secure_urls=True
    ),
    dict(
        name='day_7',
        display_name = 'Studio Giorno 7',
        participant_label_file='rooms/day7_label.txt',
        use_secure_urls=True
    ),
    dict(
        name='day_8',
        display_name = 'Studio Giorno 8',
        participant_label_file='rooms/day8_label.txt',
        use_secure_urls=True
    ),
    dict(
        name='day_9',
        display_name = 'Studio Giorno 9',
        participant_label_file='rooms/day9_label.txt',
        use_secure_urls=True
    ),
    dict(
        name='day_10',
        display_name = 'Studio Giorno 10',
        participant_label_file='rooms/day10_label.txt',
        use_secure_urls=True
    )
]