from rapidsms.contrib.handlers import KeywordHandler

from .models import Cause


class ResultsHandler(KeywordHandler):
    keyword = "results"

    def help(self):
        """help() gets invoked when we get the ``results`` message
        with no arguments"""
        # Build the response message, one part per choice
        results = []
        causes = Cause.objects.all()[:5]
        msg = ""
        if causes:
            for cause in causes:
                part = "%s: %s" % (cause.headline, cause.supporters)
                results.append(part)
            # Combine the results into the response, with a semicolon after each
            msg = "; ".join(results) + ". "
        msg += "For information on the progress of a specific cause, " \
           "send RESULTS <cause_name>. \n\n " \
           "Send HELP for a list of commands to use on this service."
        # Respond
        self.respond(msg)

    def handle(self, text):
        """This gets called if any arguments are given along with
        ``RESULTS``, but we don't care; just call help() as if they
        passed no arguments"""
        self.help()


class CauseHandler(KeywordHandler):
    keyword = "cause"

    def help(self):
        """help() gets invoked when we get the ``cause`` message
        with no arguments"""
        # Build the response message, one part per choice
        results = []
        msg = "For information on how to use CAUSE, send HELP CAUSE."
        # Respond
        self.respond(msg)

    def handle(self, text):
        """This gets called if any arguments are given along with
        ``CAUSE``, but we don't care; just call help() as if they
        passed no arguments"""
        self.help()