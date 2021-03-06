# Embedded file name: /Users/versonator/Jenkins/live/output/mac_64_static/Release/python-bundle/MIDI Remote Scripts/KeyFadr/KeyFadr.py
# Compiled at: 2018-04-23 20:27:04
from __future__ import absolute_import, print_function, unicode_literals
from KeyPad import KeyPad

class KeyFadr(KeyPad):
    u"""
    Reloop KeyFadr controller script.
    """
    _encoder_range = range(80, 72, -1)
    _product_model_id = 102

    def __init__(self, *a, **k):
        super(KeyFadr, self).__init__(*a, **k)
