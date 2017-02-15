# -*- coding: utf-8 -*-
import math
import sys
#yahoo!形態素解析
import morphological

def getwords(doc):
    words = [s.lower() for s in morphological.split(doc)]
    return tuple(w for w in words)
