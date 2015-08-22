from rapidsms.contrib.handlers import KeywordHandler

help_text = {
    'cause': 'Content not yet available for CAUSE.',
    'subscribe': 'Content not yet available for SUBSCRIBE.',
    'unsubscribe': 'Content not yet available for UNSUBSCRIBE.',
}


class HelpHandler(KeywordHandler):
    keyword = "help"

    def help(self):
        """Invoked if someone just sends `HELP`.  We also call this
        from `handle` if we don't recognize the arguments to HELP.
        """
        self.respond("Allowed commands are CAUSE, SUBSCRIBE, and UNSUBSCRIBE. \
                    Send HELP <command> for more help on a specific command.")

    def handle(self, text):
        """Invoked if someone sends `HELP <any text>`"""
        text = text.strip().lower()
        if text == 'cause':
            self.respond(help_text['cause'])
        elif text == 'subscribee':
            self.respond(help_text['subscribe'])
        elif text == 'unsubscribe':
            self.respond(help_text['unsubscribe'])
        else:
            self.help()