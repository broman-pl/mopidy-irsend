import pykka
import logging
import time
import os

from mopidy import core

logger = logging.getLogger('mopidy_IRSend')

class IRSendFrontend(pykka.ThreadingActor, core.CoreListener):
  def __init__(self, config, core):
    super(IRSendFrontend, self).__init__()
    self.core = core
    self.config = config
    self.lastWake = 0

  def on_start(self):
    logger.debug('IRSend starting')

  def on_stop(self):
    logger.info('IRSend stopped')

  def on_failure(self):
    logger.warning('IRSend failing')

  def playback_state_changed(self, old_state, new_state):
    logger.info('IRSend: state changed')
    if new_state == core.PlaybackState.PLAYING:
      logger.info('IRSend: start playing ')
      if self.checkLastWake():
        self.send_ir_command()

  def checkLastWake(self):
    logger.info ("last time: " + str(self.lastWake))

    if int(time.time()) - self.lastWake > 600:
      self.lastWake = int(time.time())
      return True
    else:
      return False

  def send_ir_command(self):
    logger.info ("sending command: AUX")
    os.system('irsend SEND_ONCE philips-htl1180b KEY_AUX')
