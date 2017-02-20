# -*- coding: utf-8 -*-
import math
import sys
#yahoo!形態素解析
import morphological

def getwords(doc):
    words = [s.lower() for s in morphological.split(doc)]
    return tuple(w for w in words)

class NaiveBayes:
  def __init__(self):
    self.vocabularies = set() # 単語の集合
    self.wordcount = {}       # {category : { words : n, ...}}
    self.catcount = {}        # {category : n}

  def wordcountup(self, word, cat):
    self.wordcount.setdefault(cat, {})
    self.wordcount[cat].setdefault(word, 0)
    self.wordcount[cat][word] += 1
    self.vocabularies.add(word)

  def catcountup(self, cat):
    self.catcount.setdefault(cat, 0)
    self.catcount[cat] += 1

  def train(self, doc, cat):
    word = getwords(doc)
    for w in word:
      self.wordcountup(w, cat)
    self.catcountup(cat)

  def priorprob(self, cat):
    return float(self.catcount[cat]) / sum(self.catcount.values())
