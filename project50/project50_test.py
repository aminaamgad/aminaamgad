import unittest.mock
import project

class TestProject(unittest.TestCase):
    def test_get_weather(self):
        with unittest.mock.patch('builtins.input', return_value='New York'):
            result = project.get_weather()
        self.assertIsNone(result)

    def test_create_file(self):
        with unittest.mock.patch('builtins.input', return_value='test_file.txt'):
            result = project.create_file()
        self.assertIsNone(result)

    def test_add_text_to_file(self):
        with unittest.mock.patch('builtins.input', return_value='test_file.txt'):
            with unittest.mock.patch('builtins.open', unittest.mock.mock_open()):
                result = project.add_text_to_file()
        self.assertIsNone(result)

    def test_add_event_to_planner(self):
        with unittest.mock.patch('builtins.input', side_effect=['2023-07-01', '12:00', 'Meeting', 'Team meeting']):
            with unittest.mock.patch('builtins.open', unittest.mock.mock_open()):
                result = project.add_event_to_planner()
        self.assertIsNone(result)

    def test_search_web(self):
        with unittest.mock.patch('builtins.input', return_value='Python'):
            with unittest.mock.patch('webbrowser.open') as mock_open:
                result = project.search_web()
        mock_open.assert_called_once_with('https://www.google.com/search?q=Python')
        self.assertIsNone(result)

if __name__ == '__main__':
    unittest.main()
