# SPDX-FileCopyrightText: © 2024 University of Bristol
# SPDX-License-Identifier: MIT

import re

from pygments.lexers import BashLexer, BashSessionLexer

__all__ = ["IsambardBashSessionLexer"]

class IsambardBashSessionLexer(BashSessionLexer):
    """
    A duplicate of the built-in pygments bash-session parser but
    where it also treats `>` as a valid prompt character.
    """
    name = "Isambard Bash Session"
    aliases = ["isambard-session"]

    _innerLexerCls = BashLexer
    _ps1rgx = re.compile(
        r'^((?:(?:\[.*?\])|(?:\(\S+\))?(?:| |sh\S*?|\w+\S+[@:]\S+(?:\s+\S+)' \
        r'?|\[\S+[@:][^\n]+\].+))\s*[$#%>]\s*)(.*\n?)')
    _ps2 = '> '
