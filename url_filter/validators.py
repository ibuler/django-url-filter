# -*- coding: utf-8 -*-
from __future__ import absolute_import, print_function, unicode_literals

from django.core.validators import (
    MaxLengthValidator as _MaxLengthValidator,
    MinLengthValidator as _MinLengthValidator,
)
from django.utils.deconstruct import deconstructible
try:
    from django.utils.translation import gettext_lazy
except ImportError:
    from django.utils.translation import ungettext_lazy as gettext_lazy


@deconstructible
class MinLengthValidator(_MinLengthValidator):
    """
    Customer Django min length validator with better-suited error message
    """

    code = "min_length"
    message = gettext_lazy(
        "Ensure this value has at least %(limit_value)d items (it has %(show_value)d).",
        "Ensure this value has at least %(limit_value)d items (it has %(show_value)d).",
        "limit_value",
    )

    def compare(self, a, b):
        return a < b

    def clean(self, x):
        return len(x)


@deconstructible
class MaxLengthValidator(_MaxLengthValidator):
    """
    Customer Django max length validator with better-suited error message
    """

    code = "max_length"
    message = gettext_lazy(
        "Ensure this value has at most %(limit_value)d items (it has %(show_value)d).",
        "Ensure this value has at most %(limit_value)d items (it has %(show_value)d).",
        "limit_value",
    )

    def compare(self, a, b):
        return a > b

    def clean(self, x):
        return len(x)
