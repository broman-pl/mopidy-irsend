import pykka
import pylirc
import logging

from mopidy.core import PlaybackState
from mopidy.utils import process
from mopidy.core import CoreListener

logger = logging.getLogger('mopidy_IRSend')

class IRSendFrontend(pykka.ThreadingActor, CoreListener):
    def __init__(self, config, core):
        super(IRSendFrontend, self).__init__()
        self.core = core
        self.config = config

    def on_start(self):
        logger.debug('IRSend starting')

    def on_stop(self):
        logger.info('IRSend stopped')

    def on_failure(self):
        logger.warning('IRSend failing')

    def track_playback_started(self,tl_track):
        logger.info('IRSend: Track has changed')


