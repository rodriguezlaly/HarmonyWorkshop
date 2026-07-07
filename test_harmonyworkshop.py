# test_harmonyworkshop.py
"""
Tests for HarmonyWorkshop module.
"""

import unittest
from harmonyworkshop import HarmonyWorkshop

class TestHarmonyWorkshop(unittest.TestCase):
    """Test cases for HarmonyWorkshop class."""
    
    def test_initialization(self):
        """Test class initialization."""
        instance = HarmonyWorkshop()
        self.assertIsInstance(instance, HarmonyWorkshop)
        
    def test_run_method(self):
        """Test the run method."""
        instance = HarmonyWorkshop()
        self.assertTrue(instance.run())

if __name__ == "__main__":
    unittest.main()
