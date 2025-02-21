"""
Tests for Config Code

"""

#-----------------------------------------------------------------------------
# Copyright (c) 2016, Trident Development Team.
#
# Distributed under the terms of the Modified BSD License.
#
# The full license is in the file LICENSE, distributed with this software.
#-----------------------------------------------------------------------------

from trident.config import \
    trident, \
    trident_path

def test_banner():
    """
    Tests running the banner display
    """
    trident()

def test_path():
    """
    Tests that the trident path is working ok.
    """
    trident_path()
