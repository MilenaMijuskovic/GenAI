import logging
import sys
logging.basicConfig(level=logging.DEBUG, format='%(asctime)s :: %(levelname)s %(name)s :: %(message)s', stream=sys.stdout)
applogger = logging.getLogger(__name__)
applogger.setLevel(logging.DEBUG)
