import logging
from datetime import datetime
from string import Template

logging.basicConfig(
    filename = Template('logs/$name.log').substitute(name=str(datetime.now().strftime('%Y-%m-%d-%H-%M-%S'))),
    level=logging.DEBUG,
    format='[%(asctime)s] [%(levelname)s] [%(funcName)s]: %(message)s'
)
consoleHandler = logging.StreamHandler()
consoleHandler.setFormatter(logging.Formatter('[%(asctime)s] [%(levelname)s] [%(funcName)s]: %(message)s'))
consoleHandler.setLevel(logging.INFO)
logger = logging.getLogger()
logger.addHandler(consoleHandler)
logger.info('Intellyricist App launched')