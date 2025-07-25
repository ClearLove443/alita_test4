
import unittest
from ai_agent import AICodingAgent

class TestAICodingAgent(unittest.TestCase):
    def setUp(self):
        self.agent = AICodingAgent()
        
    def test_analyze_code(self):
        test_code = "x = 5\ny = 10\nif x == y:\n    print('equal')"
        analysis = self.agent.analyze_code(test_code)
        
        self.assertIsInstance(analysis, dict)
        self.assertIn('complexity', analysis)
        self.assertIn('style_issues', analysis)
        self.assertIn('potential_bugs', analysis)
        
    def test_generate_code(self):
        requirements = "Create a function that adds two numbers"
        generated_code = self.agent.generate_code(requirements)
        
        self.assertIsInstance(generated_code, str)
        self.assertTrue(requirements in generated_code)
        
    def test_complexity_calculation(self):
        simple_code = "x = 1"
        complex_code = "x = 1\ny = 2\nz = x + y\nprint(z)"
        
        self.assertEqual(self.agent._calculate_complexity(simple_code), 1)
        self.assertEqual(self.agent._calculate_complexity(complex_code), 3)

if __name__ == '__main__':
    unittest.main()
