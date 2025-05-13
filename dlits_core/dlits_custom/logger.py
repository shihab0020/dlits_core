import logging
from frappe.utils.logger import get_logger
logger = get_logger('shb1', max_size=1_000_000)
logger.setLevel(logging.INFO)