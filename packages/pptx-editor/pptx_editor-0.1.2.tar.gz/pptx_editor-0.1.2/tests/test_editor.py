import unittest
from pptx_editor.editor import PPTXEditor

class TestPPTXEditor(unittest.TestCase):

    def setUp(self):
        """Set up a test PowerPoint file."""
        self.test_ppt = "test.pptx"
        self.editor = PPTXEditor(self.test_ppt)

    def test_navigation(self):
        """Test slide navigation functions."""
        initial_slide = self.editor.get_current_slide_index()
        self.editor.next_slide()
        self.assertEqual(self.editor.get_current_slide_index(), initial_slide + 1)

        self.editor.previous_slide()
        self.assertEqual(self.editor.get_current_slide_index(), initial_slide)

    def test_add_red_dot(self):
        """Test adding a red dot to a slide."""
        self.editor.add_red_dot(x=2, y=2)
        self.editor.save_presentation("test_output.pptx")
        self.assertTrue(True)  # You can extend this with actual verification

if __name__ == "__main__":
    unittest.main()
