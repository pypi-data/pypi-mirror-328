import os

BASE_DIR = 'data'

FILE_FOLDER = {
    'market': os.path.join(BASE_DIR, 'dataset-market'),
    '2160': os.path.join(BASE_DIR, 'dataset-menu2160'),
    '2160-snapshot': os.path.join(BASE_DIR, 'dataset-menu2160-snapshot'),
    '2205': os.path.join(BASE_DIR, 'dataset-menu2205'),
    '2205-snapshot': os.path.join(BASE_DIR, 'dataset-menu2205-snapshot'),
    '4165': os.path.join(BASE_DIR, 'dataset-menu4165'),
    '8186-snapshot': os.path.join(BASE_DIR, 'dataset-menu8186-snapshot'),
    'fund': os.path.join(BASE_DIR, 'dataset-fund'),
    'index': os.path.join(BASE_DIR, 'dataset-index'),
    'currency': os.path.join(BASE_DIR, 'dataset-currency'),
}

BUCKET_SYSTEM = 'dataset-system'
BUCKET_BBG = 'dataset-bbg'

BUCKET_PREFIX = {
    'market': 'dataset-market',
    '2160': 'dataset-menu2160',
    '2160-snapshot': 'dataset-menu2160-snapshot',
    '2205': 'dataset-menu2205',
    '2205-snapshot': 'dataset-menu2205-snapshot',
    '4165': 'dataset-menu4165',
    '8186-snapshot': 'dataset-menu8186-snapshot',
    'index': 'dataset-index',
    'currency': 'dataset-currency',
}