#from lxml import html
import re
from StringIO import StringIO

TEXT_TOKEN = 0
NAME_TOKEN = 1

single_pat = re.compile('''
{@(?:i18n|_)\stext="(.*)"/}
''', re.MULTILINE | re.VERBOSE)

multiopen_pat = re.compile('''
{@(?:i18n|_)}
''', re.MULTILINE | re.VERBOSE)

multiclose_pat = re.compile('''
{/(?:i18n|_)}
''', re.MULTILINE | re.VERBOSE)

def extractor(fileobj, keywords, comment_tags, options):
    """Extract messages from Dustjs Template source code.

    :param fileobj: the seekable, file-like object the messages should be
                    extracted from
    :param keywords: a list of keywords (i.e. function names) that should be
                     recognized as translation functions
    :param comment_tags: a list of translator tags to search for and include
                         in the results
    :param options: a dictionary of additional options (optional)
    :return: an iterator over ``(lineno, funcname, message, comments)`` tuples
    :rtype: ``iterator``
    """
    i = 0
    data = fileobj.readlines()
    for l in data:
        i += 1
        for match in single_pat.findall(l):
            yield (i, None, match, [])

    i = 0
    lineno = 0
    start = 0
    is_open = False

    for l in data:
        # examine a new line
        i += 1
        examined = 0

        while examined < len(l):
            # Create a new substring of the data which is i unexamined
            s = l[examined:]

            if not is_open:
                match = multiopen_pat.search(s)

                # If we cannot find an open tag, and we are not open, then
                # continue.
                if not match:
                    break

                # If we found a match start recording the meta-data
                lineno = i
                data = []
                is_open = True
                start = match.end()

            # Look for a closing match on this line
            match = multiclose_pat.search(s[start:])

            if match:
                # if we found a closing match, record how far in the string it
                # is, then yield the data for this block
                is_open = False
                end = start+match.start()
                examined += end
                data.append(s[start:end])
                yield (lineno, None, ''.join(data), [])
            else:
                # record all the data since the closing match is not on this line.
                examined = len(l)
                data.append(s[start:])

        start = 0
