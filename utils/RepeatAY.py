import logging
from JoycontrolPlugin import JoycontrolPlugin

logger = logging.getLogger(__name__)

class RepeatAY(JoycontrolPlugin):
    async def run(self):
        logger.info('Repeat AY Plugin')
        while True:
            await self.button_push('a','y')
            await self.wait(0.3)
