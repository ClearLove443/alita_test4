

import unittest
from ai_agent import AICodingAgent

class IntegrationTests(unittest.TestCase):
    def setUp(self):
        self.agent = AICodingAgent("TestAgent")
        
    def test_full_workflow(self):
        # Test complete analyze-generate-analyze cycle
        requirements = "Create a function that multiplies two numbers"
        generated_code = self.agent.generate_code(requirements)
        
        # Verify generated code contains key elements
        self.assertIn("def", generated_code)
        self.assertIn("return", generated_code)
        
        # Analyze the generated code
        analysis = self.agent.analyze_code(generated_code)
        self.assertGreater(analysis['complexity'], 0)
        
    def test_knowledge_base_integration(self):
        # Test that knowledge base affects code generation
        test_knowledge = {"multiplication": "Use * operator"}
        self.agent.knowledge_base.update(test_knowledge)
        
        generated_code = self.agent.generate_code("multiplication function")
        self.assertIn("*", generated_code)

if __name__ == '__main__':
    unittest.main()

