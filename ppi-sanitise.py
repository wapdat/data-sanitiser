from __future__ import print_function

import sys
import re

if len(sys.argv) < 2:
    print('Exit code 10: Please enter a string to sanitise')
    sys.exit(10)
    
dirtyStr = sys.argv[1]

print('%-30s "%s"' % ('Unsanitised', dirtyStr))

cleanStr = re.sub( r'[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+', 'NAME@EMAIL.COM', dirtyStr, re.I)
print('%-30s "%s"' % ('cleaned emails', cleanStr))

cleanStr = re.sub( r'(gir ?0aa|GIR ?0AA|[a-pr-uwyzA-PR-UWYZ]([0-9]{1,2}|([a-hk-yA-HK-Y][0-9]([0-9abehmnprv-yABEHMNPRV-Y])?)|[0-9][a-hjkps-uwA-HJKPS-UW]) ?[0-9][abd-hjlnp-uw-zABD-HJLNP-UW-Z]{2})', 'POSTCODE', cleanStr, re.IGNORECASE)
print('%-30s "%s"' % ('cleaned UK postcodes', cleanStr))

cleanStr = re.sub( r'(?!219-09-9999|078-05-1120)(?!666|000|9\d{2})\d{3}-(?!00)\d{2}-(?!0{4})\d{4}', 'SSN', cleanStr, re.IGNORECASE)
print('%-30s "%s"' % ('cleaned dashed SSN', cleanStr))

cleanStr = re.sub( r'(\s|^)(?!219099999|078051120)(?!666|000|9\d{2})\d{3}(?!00)\d{2}(?!0{4})\d{4}(\s|$)', 'SSN', cleanStr, re.IGNORECASE)
print('%-30s "%s"' % ('cleaned SSN', cleanStr))

cleanStr = re.sub( r'(?:(?:\(?(?:0(?:0|11)\)?[\s-]?\(?|\+)44\)?[\s-]?(?:\(?0\)?[\s-]?)?)|(?:\(?0))(?:(?:\d{5}\)?[\s-]?\d{4,5})|(?:\d{4}\)?[\s-]?(?:\d{5}|\d{3}[\s-]?\d{3}))|(?:\d{3}\)?[\s-]?\d{3}[\s-]?\d{3,4})|(?:\d{2}\)?[\s-]?\d{4}[\s-]?\d{4}))(?:[\s-]?(?:x|ext\.?|\#)\d{3,4})?', 'UKPHONE', cleanStr, re.IGNORECASE)
print('%-30s "%s"' % ('cleaned UK Phone', cleanStr))

# Problem with chomping leading and training space
cleanStr = re.sub( r'(1?\W*([2-9][0-8][0-9])\W*([2-9][0-9]{2})\W*([0-9]{4})(\se?x?t?(\d*))?)', ' USPHONE ', cleanStr, re.IGNORECASE)
print('%-30s "%s"' % ('cleaned US Phone', cleanStr))

cleanStr = re.sub( r'(\s|^)(?:(?:\+?1\s*(?:[.-]\s*)?)?(?:\(\s*([2-9]1[02-9]|[2-9][02-8]1|[2-9][02-8][02-9])\s*\)|([2-9]1[02-9]|[2-9][02-8]1|[2-9][02-8][02-9]))\s*(?:[.-]\s*)?)?([2-9]1[02-9]|[2-9][02-9]1|[2-9][02-9]{2})\s*(?:[.-]\s*)?([0-9]{4})(?:\s*(?:#|x\.?|ext\.?|extension)\s*(\d+))?(\s|$)', 'USPHONE', cleanStr, re.IGNORECASE)
print('%-30s "%s"' % ('cleaned US Phone', cleanStr))

