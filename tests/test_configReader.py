import os
from unittest import TestCase
from pathlib import Path
from modules import config_reader


class TestConfigReader(TestCase):
    def test_reade(self):
        reader = config_reader.ConfigReader()
        reader.read('./tests')
        config_file = Path('./tests/' + reader.FILENAME)
        self.assertTrue(config_file.is_file())
        self.assertEqual(10, reader.width)
        self.assertEqual(10, reader.height)
        self.assertEqual(50, reader.numofseed)
        os.remove(str(config_file))

