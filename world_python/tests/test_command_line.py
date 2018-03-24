from unittest import TestCase
from world_python import command_line

class TestConsole(TestCase):
    def test_basic(self):
        command_line.main()
