# -*- coding: utf-8 -*-

import vim
import subprocess
from ncm2 import Ncm2Source, getLogger
import re
from copy import deepcopy

logger = getLogger(__name__)


class Source(Ncm2Source):

    def on_warmup(self, ctx):
        shell_command = 'khard email --parsable | cut -f 1,2'
        self.dictionary = subprocess.run(shell_command, shell = True, capture_output = True).stdout.decode('utf8').split('\n')

    def on_complete(self, ctx):
        base = ctx['base']
        # matcher = self.matcher_get(ctx)
        # matches = []


        self.complete(ctx, ctx['startccol'], self.dictionary)


source = Source(vim)

on_complete = source.on_complete
