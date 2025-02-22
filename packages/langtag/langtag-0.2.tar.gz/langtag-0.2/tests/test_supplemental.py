#!/usr/bin/python
# -*- encoding: utf-8

import unittest, os, re, json
from xml.etree import ElementTree as et
from itertools import product
import sldr         # for the path

langtagjson = os.path.join(os.path.dirname(__file__), '..', 'pub', 'langtags.json')

exceptions = set(["aii-Cyrl", 
    "en-Latn-CQ"        # CQ crashes old FLex
])

class Supplemental(unittest.TestCase):
    ''' Tests alltags.txt for discrepencies against likelySubtags.xml '''
    def setUp(self):
        with open(langtagjson, "r") as inf:
            self.data = json.load(inf)
        self.ltags = {}
        for j in self.data:
            if j['tag'].startswith("_"):
                continue
            self.ltags.setdefault(j['tag'], []).append(j)
            if j['tag'] != j['full']:
                self.ltags.setdefault(j['full'], []).append(j)
            if 'tags' in j:
                for t in j['tags']:
                    self.ltags.setdefault(t, []).append(j)
        thisdir = os.path.dirname(sldr.__file__)
        self.doc = et.parse(os.path.join(thisdir, "supplementalData.xml"))

    def test_languageData(self):
        failures = []
        for e in self.doc.findall('./languageData/language'):
            lang = e.get('type')
            if lang == "und":
                continue
            scripts = e.get('scripts', '').split(' ')
            regions = e.get('territories', '').split(' ')
            for s in scripts:
                tag = lang + ("-" + s if len(s) else "")
                if str(tag) in exceptions:
                    continue
                if tag not in self.ltags:
                    failures.append(tag)
                    continue
                for r in regions:
                    if not len(r):
                        continue
                    t = tag + "-" + r
                    if t in self.ltags or str(t) in exceptions:
                        continue
                    if r not in self.ltags[tag][0].get('regions', []):
                        failures.append(t)
        if len(failures):
            self.fail("Missing tags from supplemental Data" + str(failures))

    def test_names(self):
        for r in self.data:
            if r['tag'].startswith("_"):
                continue
            if 'names' in r:
                if any(x == u'↑↑↑' for x in r['names']):
                    self.fail("Inherited names item in " + str(r['tag']))
            if 'name' in r:
                if r['name'] == u'↑↑↑':
                    self.fail("Inherited name in " + str(['tag']))

    def test_duplicates(self):
        failures = []
        for k, v in self.ltags.items():
            if len(v) > 1:
                failures.append("{}: " + ", ".join(r['full'] for r in v))
        if len(failures):
            self.fail("Duplicated tags: " + str(failures))
