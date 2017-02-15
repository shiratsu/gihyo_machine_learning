# -*- coding: utf-8 -*-
import urllib
import urllib2
from BeautifulSoup import BeautifulSoup

appid = 'dj0zaiZpPVpXUE9yNG1QODN6aCZzPWNvbnN1bWVyc2VjcmV0Jng9OGQ-'
pageurl = "http://jlp.yahooapis.jp/MAService/V1/parse";

# Yahoo!形態素解析の結果をリストで返します。
def split(sentence, appid=appid, results="ma", filter="1|2|3|4|5|9|10"):
  sentence = sentence.encode("utf-8")
  params = urllib.urlencode({'appid':appid, 'results':results, 'filter':filter,'sentence':sentence})
  results = urllib2.urlopen(pageurl, params)
  soup = BeautifulSoup(results.read())

  return [w.surface.string for w in soup.ma_result.word_list]
