"""
Unittesting for Chess
"""

__authors__ = "Bryleigh Koci, Walker Edwards, Elena Schmitt"
__date__ = "26 April 2024"
__license__ = "MIT"

import sys
import unittest
from unittest.mock import patch
from typing import List
from hypothesis import given
from hypothesis import strategies as st
from hypothesis import settings, Verbosity


class TestChess(unittest.TestCase):
    """
    test cases must start with test and must be a method
    """
    def setUp(self) -> None:
        """Set up"""

    def tearDown(self) -> None:
        """Tear down"""

    def test1_method(self) -> None:
