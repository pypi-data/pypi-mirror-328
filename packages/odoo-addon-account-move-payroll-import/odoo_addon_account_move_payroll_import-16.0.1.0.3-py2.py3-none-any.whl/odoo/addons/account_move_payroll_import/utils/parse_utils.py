# -*- coding: utf-8 -*-
from odoo.exceptions import UserError


def parse_float(value, thousands_sep=",", decimal_sep=".", context={}):
    """
    Parse a float value.
    :param thousands_sep: the thousands separator.
    :param decimal_sep: the decimal separator.
    :param value: the value to parse.
    :param context: the context.
    :return: the parsed float value.
    """
    if type(value) in (int, float, bool):
        return float(value)

    value = str(value).strip()
    if not value:
        return 0.0

    value = value.replace(thousands_sep, "", 1).replace(decimal_sep, ".", 1)
    try:
        return float(value)
    except ValueError:
        if context.get("raise_exception", True):
            msg = context.get("exception_msg", "Invalid float value: %s" % value)
            raise UserError(msg)
        return 0.0


def abs_float(value, thousands_sep=",", decimal_sep=".", context={}):
    """
    Parse a float value and return its absolute value.
    :param thousands_sep: the thousands separator.
    :param decimal_sep: the decimal separator.
    :param value: the value to parse.
    :param context: the context.
    :return: the absolute value of the parsed float value.
    """
    try:
        return abs(parse_float(value, thousands_sep, decimal_sep))
    except ValueError:
        if context.get("raise_exception", True):
            msg = context.get("exception_msg", "Invalid float value: %s" % value)
            raise UserError(msg)
        return 0.0
