#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sys

hdr = sys.stdin.readline().strip().split("\t")
col = {}
for i, tok in enumerate(hdr):
    col[tok] = i

for l in sys.stdin:
    l = l.strip()
    toks = l.split("\t")
    descr = "{} {} ({} {})".format(
        toks[col["diameter"]], toks[col["type"]].split(" ")[0],
        toks[col["manufacturer"]], toks[col["product-id"]]
    )
    sys.stdout.write("T{} P{} D{} Z+50 ; {}\n".format(
        toks[col["number"]], toks[col["diameter-offset"]], toks[col["diameter"]], descr
    ))



