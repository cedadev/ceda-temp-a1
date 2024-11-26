"""
Unit tests for the main package
"""

import unittest

from ceda_temp_a1.main import main


class TestMain(unittest.TestCase):
    """
    Test the functionality of the main package.
    """

    def test_main(self) -> None:
        """
        Test the functionality of the :py:func:`ceda_temp_a1.main` function
        """

        main()
