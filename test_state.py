import unittest

from StateMachine import State

class StateTests(unittest.TestCase):
    def test_state_name(self):
        state = State("TestState")
        self.assertEqual(state.name, "TestState")

    def test_state_can_terminate(self):
        
        cases = [
            (False, False),
            (True, True)
        ]
        
        for input_val, expected in cases:
            state = State("TestState")
            state.can_terminate = input_val
            self.assertEqual(state.can_terminate, expected)
            
    def test_state_construction_invalid_name(self):
        self.assertRaises(ValueError, State, None)

    def test_state_entry_event(self):
        entry_called = False
        def entry_event():
            nonlocal entry_called
            entry_called = True

        state = State("TestState")
        state.on_entry = entry_event
        state.on_entry()
        self.assertTrue(entry_called)

    def test_state_update_event(self):
        update_called = False
        def update_event():
            nonlocal update_called
            update_called = True

        state = State("TestState")
        state.on_update = update_event
        state.on_update()
        self.assertTrue(update_called)
        
    def test_state_exit_event(self):
        exit_called = False
        def exit_event():
            nonlocal exit_called
            exit_called = True

        state = State("TestState")
        state.on_exit = exit_event
        state.on_exit()
        self.assertTrue(exit_called)