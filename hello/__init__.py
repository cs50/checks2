import check50
import check50.c

import re

@check50.check()
def exists():
    """hello.c exists."""
    check50.exists("hello.c")

@check50.check(exists)
def compiles():
    """hello.c compiles."""
    check50.c.compile("hello.c", lcs50=True)

@check50.check(compiles)
def prints_hello():
    """prints "hello, world\\n" """
    expected = "[Hh]ello, world!?\n"
    actual = check50.run("./hello").stdout()
    if not re.match(expected, actual):
        help = None
        if re.match(expected[:-1], actual):
            help = r"Did you forget a newline ('\n') at the end of your printf string?"
        raise check50.Mismatch(expected, actual, help=help)
