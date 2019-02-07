# -*- coding: utf-8 -*-

import vim
import subprocess
from ncm2 import Ncm2Source, getLogger

logger = getLogger(__name__)


class Source(Ncm2Source):

    def on_warmup(self, ctx):
        bufnr = ctx['bufnr']
        shell_cmd = "khard email --parsable | cut -f 1,2 | sed -r 's/(.*)\t(.*)/\\2 <\\1>/'"
        self.matches = subprocess.run(shell_cmd, shell = True, capture_output = True).stdout.decode('utf8').split('\n')

    def on_complete(self, ctx):
        self.complete(ctx, ctx['startccol'], self.matches)


source = Source(vim)

on_warmup = source.on_warmup
on_complete = source.on_complete
