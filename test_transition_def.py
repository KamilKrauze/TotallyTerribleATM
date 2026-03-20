import unittest
from StateMachine import State
from StateMachine import TransitionDefinition as Transition

class TransitionDefinitionTests(unittest.TestCase):
    
    def test_transition_definition_construction(self):
        state_a = State("StateA")
        state_b = State("StateB")
        transition = Transition(state_a, state_b)
        self.assertEqual(transition.from_state, state_a)
        self.assertEqual(transition.to_state, state_b)
        self.assertFalse(transition.can_transition())
        
    def test_transition_definition_construction_invalid(self):
        state1 = State("State1")
        state11 = State("State1")
        
        self.assertRaises(ValueError, Transition, None, state1)
        self.assertRaises(ValueError, Transition, state1, None)
        
        self.assertRaises(ValueError, Transition, state1, state11)
        
        