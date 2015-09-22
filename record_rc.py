import json
import random
import sys
from math import log

import socketIO_client
import stopit


class WikiNamespace(socketIO_client.BaseNamespace):
        def on_change(self, change):
            if change['type'] in ('new', 'edit'):
                wait = random.lognormvariate(log(1), 1)
                change['wait'] = min(max(wait, 0.01), 10)
                json.dump(change, sys.stdout)
                sys.stdout.write("\n")

        def on_connect(self):
            self.emit('subscribe', 'en.wikipedia.org')  # Subscribes to enwiki

socketIO = socketIO_client.SocketIO("stream.wikimedia.org", 80)
socketIO.define(WikiNamespace, '/rc')

with stopit.ThreadingTimeout(5 * 60) as to_ctx_mgr:
    try:
        socketIO.wait(10000)
    except KeyboardInterrupt:
        sys.stderr.write("Keyboard interrupt detected.  Shutting down.\n")


sys.stderr.write("All done.\n")
