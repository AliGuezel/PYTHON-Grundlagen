# zu den Unterschieden der get-encodings:
# https://www.javaer101.com/en/article/15924505.html

import sys
import locale
import encodings.aliases

for a in encodings.aliases.aliases:
    print(a)

print()

print (sys.stdout.encoding)
print (locale.getpreferredencoding())
print (sys.getdefaultencoding())
