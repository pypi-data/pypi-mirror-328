from ._main import (
    main, fetch_parameters, add_main_arguments
)

import logging
from dotenv import load_dotenv

load_dotenv()

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s | %(pathname)s | %(name)s | func: %(funcName)s:%(lineno)s | %(levelname)s | %(message)s",
)