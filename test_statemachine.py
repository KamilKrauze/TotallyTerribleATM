import unittest
from StateMachine import *

class StateMachineTests(unittest.TestCase):
    
    def test_state_machine_construction_default(self):
        state_a = State("StateA")
        sm = StateMachine(state_a)
        self.assertEqual(sm.current_state, state_a)
        self.assertEqual(sm.exec_state, ExecutionState.NotStarted)

    def test_state_machine_construction_invalid_initial_state(self):
        self.assertRaises(ValueError, StateMachine, None)

    def test_state_machine_construction_initial_state_terminating(self):
        state_a = State("StateA")
        state_a.can_terminate = True
        self.assertRaises(ValueError, StateMachine, state_a)
        
    def test_state_machine_add_state(self):
        state_a = State("StateA")
        state_b = State("StateB")
        sm = StateMachine(state_a)
        sm.add_state(state_b)
        
        self.assertIn(state_b.name, sm._states)
        self.assertEqual(sm._states[state_b.name], state_b)
        
        state_b2 = State("StateB")
        
        # adding same state again should raise error
        self.assertRaises(ValueError, sm.add_state, state_b2)
        
    def test_state_machine_transition_definition(self):
        state_a = State("StateA")
        state_b = State("StateB")
        sm = StateMachine(state_a)
        sm.add_state(state_b)
        
        transition = TransitionDefinition(state_a, state_b)
        sm.define_transition(transition)
        
        self.assertIn(transition, sm._transitions)
        
    def test_state_machine_transition_definition_invalid_states(self):
        state_a = State("StateA")
        state_b = State("StateB")
        sm = StateMachine(state_a)
        
        transition1 = TransitionDefinition(state_a, state_b)
        transition2 = TransitionDefinition(state_b, state_a)
        
        self.assertRaises(ValueError, sm.define_transition, transition1)
        self.assertRaises(ValueError, sm.define_transition, transition2)