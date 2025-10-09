import unittest
from pathlib import Path

import src.mindblow as mindblow

EXAMPLES_PATH = Path("src") / Path("example")


class TestCompiler(unittest.TestCase):
    def test_compile(self):
        with open(EXAMPLES_PATH / Path("mind.🤯")) as source_code_file:
            source_code = source_code_file.read()
        attempt_object_bytes = mindblow.compile(source_code, 0)

        with open(EXAMPLES_PATH / Path("mind.🤯.o"), "rb") as object_file:
            correct_object_bytes = object_file.read()

        self.assertEqual(attempt_object_bytes, correct_object_bytes, "BAD")

    def test_decompile(self):
        with open(EXAMPLES_PATH / Path("mind.🤯.o"), "rb") as object_file:
            correct_object_bytes = object_file.read()

        source_code = mindblow.decompile(correct_object_bytes)

        attempt_object_bytes = mindblow.compile(source_code, 0)

        self.assertEqual(attempt_object_bytes, correct_object_bytes, "BAD")
