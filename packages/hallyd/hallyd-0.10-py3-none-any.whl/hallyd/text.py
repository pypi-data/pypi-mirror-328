#  SPDX-FileCopyrightText: © 2023 Josef Hahn
#  SPDX-License-Identifier: AGPL-3.0-only
import re
import xml.etree.ElementTree


def match_format_string(pattern: str, string: str) -> dict[str, str]:
    def unescape_double_braces(s):
        return s.replace("{{", "{").replace("}}", "}")

    pattern_re = ""
    i = 0
    for expression_match in re.finditer(r"(?:[^{]|^)\{([^{}]+)\}(?:[^}]|$)", pattern):
        pattern_re += re.escape(unescape_double_braces(pattern[i:expression_match.start(1) - 1]))
        pattern_re += f"(?P<{expression_match.group(1)}>.*)"
        i = expression_match.end(1) + 1
    pattern_re += re.escape(unescape_double_braces(pattern[i:])) + "$"
    result_match = re.match(pattern_re, string)
    return result_match.groupdict() if result_match else None


def pretty_print_xml(input_xml: str) -> str:  # TODO broken
    xtree = xml.etree.ElementTree.fromstring(input_xml)
    ytree = xml.etree.ElementTree.ElementTree(xtree)
    xml.etree.ElementTree.indent(ytree, space=4*" ")
    result = ""
    for line in xml.etree.ElementTree.tostring(xtree, encoding="unicode").split("\n"):
        if line.strip():
            result += line + "\n"
    return result
