# coding: utf-8

import re

matches = re.findall('c.+?s', 'it rains cats and dogs.', re.S)

print(matches)

matches2 = re.findall('it', 'it rains cats, it rain dogs.', re.S | re.I)

print(matches2)

matches3 = re.findall('\.\Z', 'it rains cats! it rain dogs.', re.I)

print(matches3)
