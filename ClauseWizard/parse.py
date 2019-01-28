# -*- coding: utf8 -*-

import pyparsing as pp
import re
from datetime import datetime


def _preprocess(txt):
    txt = txt.replace("EU4txt", "", 1)  # Remove first line
    # Hack for CK2 parsing because there's a trailing } at the end of the file
    txt = txt.replace("CK2txt", "CK2data={", 1)
    txt = txt.replace("HOI4txt", "", 1)  # Same for HOI4 games
    txt = re.sub(r"([A-Za-z0-9_.\-]+){",
                 r"\1={", txt)  # Solve phrases without equal sign
    txt = re.sub(r"\"([A-Za-z0-9_.\-]+)\"\s*=",
                 r"\1=", txt, 0, re.MULTILINE)  # Unquote keys in phrases
    txt = re.sub(r"=\s*{", r"={", txt, 0, re.MULTILINE)  # Fix spaces
    txt = re.sub(r"^\s*{\s*\}", r"", txt, 0, re.MULTILINE)  # Hack for random empty objects start of the line
    # If this breaks any further I'll break myself
    return txt


def parse_grammar(txt, debug=False):
    txt = _preprocess(txt)

    EQ, LBRACE, RBRACE = map(pp.Suppress, "={}")  # Do not output
    comment = pp.Suppress("#") + pp.Suppress(pp.restOfLine)
    real = pp.Regex(r"[+-]?\d+\.\d*").setParseAction(lambda x: float(x[0]))
    integer = pp.Regex(r"[+-]?\d+").setParseAction(lambda x: int(x[0]))
    yes = pp.CaselessKeyword("yes").setParseAction(pp.replaceWith(True))
    no = pp.CaselessKeyword("no").setParseAction(pp.replaceWith(False))

    # Convert strings to date
    def convert_to_date(s, loc, tokens):
        try:
            return str(datetime(int(tokens.year), int(tokens.month), int(tokens.day)).date())
        except Exception as ex:
            errmsg = "Error in convert_to_date " + str(ex)
            raise pp.ParseException(s, loc, errmsg)

    # Account for "negative dates" and things like "1.1.1"
    date_type = pp.Regex(r"\-?(?P<year>\d{1,4})\.(?P<month>\d\d?)\.(?P<day>\d\d?)")
    date_type.setParseAction(convert_to_date).setName('date_type')
    # TODO Check if dateu is needed

    pp.dblQuotedString.setParseAction(pp.removeQuotes)
    pp.dblQuotedString.setName('dblQuotedString')
    unQuotedString = pp.Word(pp.alphanums + pp.alphas8bit + "_-.:?")  # 8bit for parsing accented characters
    # I had to put : there just for Stellaris saves
    unQuotedString.setName('unQuotedString')

    data = (date_type | real | integer | yes | no | pp.dblQuotedString | unQuotedString)
    data.setName('data')
    str_types = (pp.dblQuotedString | unQuotedString)
    str_types.setName('str_types')
    obj = pp.Forward()
    phrase = (str_types + EQ + (pp.Group(obj | data)))
    phrase.setName('phrase')
    data_obj = (pp.OneOrMore(pp.Group(obj)) | pp.OneOrMore(pp.Group(phrase)) | pp.OneOrMore(pp.Group(data)))
    data_obj.setName('data_obj')

    # obj << nestedExpr(LBRACE, RBRACE, content=dataObj, ignoreExpr=dblQuotedString)
    # I think that slowed the code
    empty_obj = pp.Empty().setParseAction(pp.replaceWith(''))
    empty_obj.setName('empty_obj')

    obj << (LBRACE + (data_obj | empty_obj) + RBRACE)
    obj.setName('obj')

    file = pp.OneOrMore(pp.Group(phrase))
    file.ignore(comment)
    file.setName('file')

    if debug:
        date_type.setDebug()
        pp.dblQuotedString.setDebug()
        unQuotedString.setDebug()
        data.setDebug()
        str_types.setDebug()
        phrase.setDebug()
        empty_obj.setDebug()
        data_obj.setDebug()
        obj.setDebug()
        file.setDebug()

    file.parseWithTabs()  # Not sure if this does anything, thought it could improve performance

    try:
        res = file.parseString(txt, parseAll=True)  # Change to False if you don't mind your output truncated at errors
        return res.asList()
    except pp.ParseException as pe:
        # Prints the last lines to cause the error, sometimes not very useful
        print(pp.ParseException.explain(pe, depth=None))
        raise pe  # Should throw exception, not exit
