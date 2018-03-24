from unittest import TestCase
import world_python

class TestWorld(TestCase):
    def test_is_string(self):
        s = world_python.world()
        self.assertTrue(isinstance(s, str))
