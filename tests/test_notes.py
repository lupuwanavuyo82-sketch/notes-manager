import unittest
from src.notes import add_note, list_notes, notes


class TestNotesManager(unittest.TestCase):

    def setUp(self):
        # Clear notes before each test
        notes.clear()

    def test_add_note(self):
        add_note("Test note")
        self.assertIn("Test note", notes)

    def test_list_notes(self):
        add_note("Note 1")
        add_note("Note 2")
        self.assertEqual(list_notes(), ["Note 1", "Note 2"])


if __name__ == "__main__":
    unittest.main()
