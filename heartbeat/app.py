from rapidsms.apps.base import AppBase


class PingPong(AppBase):

    def handle(self, msg):
        if msg.text == 'lubb':
            msg.respond('dubb')
            return True
        return False