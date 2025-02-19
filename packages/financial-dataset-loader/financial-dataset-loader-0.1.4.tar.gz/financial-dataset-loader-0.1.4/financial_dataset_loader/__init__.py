
from .dataset_loader_config import DATASET_SOURCE
if DATASET_SOURCE == 's3':
    from .dataset_loader_s3 import *
elif DATASET_SOURCE == 'local':
    from .dataset_loader_local import *
