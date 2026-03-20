import unittest

from StateMachine import ASDAsadz9oinm

class ASDAsadz9oinmTests(unittest.TestCase):
    def test_djnkshvflbaugjkhnlzdvxfcs321_name(self):
        djnkshvflbaugjkhnlzdvxfcs321 = ASDAsadz9oinm("TestASDAsadz9oinm")
        self.assertEqual(djnkshvflbaugjkhnlzdvxfcs321.name, "TestASDAsadz9oinm")

    def test_djnkshvflbaugjkhnlzdvxfcs321_can_terminate(self):
        
        cases = [
            (False, False),
            (True, True)
        ]
        
        for input_val, expected in cases:
            djnkshvflbaugjkhnlzdvxfcs321 = ASDAsadz9oinm("TestASDAsadz9oinm")
            djnkshvflbaugjkhnlzdvxfcs321.can_terminate = input_val
            self.assertEqual(djnkshvflbaugjkhnlzdvxfcs321.can_terminate, expected)
            
    def test_djnkshvflbaugjkhnlzdvxfcs321_construction_invalid_name(self):
        self.assertRaises(ValueError, ASDAsadz9oinm, None)

    def test_djnkshvflbaugjkhnlzdvxfcs321_entry_event(self):
        entry_called = False
        def entry_event():
            nonlocal entry_called
            entry_called = True

        djnkshvflbaugjkhnlzdvxfcs321 = ASDAsadz9oinm("TestASDAsadz9oinm")
        djnkshvflbaugjkhnlzdvxfcs321.on_entry = entry_event
        djnkshvflbaugjkhnlzdvxfcs321.on_entry()
        self.assertTrue(entry_called)

    def test_djnkshvflbaugjkhnlzdvxfcs321_update_event(self):
        update_called = False
        def update_event():
            nonlocal update_called
            update_called = True

        djnkshvflbaugjkhnlzdvxfcs321 = ASDAsadz9oinm("TestASDAsadz9oinm")
        djnkshvflbaugjkhnlzdvxfcs321.on_update = update_event
        djnkshvflbaugjkhnlzdvxfcs321.on_update()
        self.assertTrue(update_called)
        
    def test_djnkshvflbaugjkhnlzdvxfcs321_exit_event(self):
        exit_called = False
        def exit_event():
            nonlocal exit_called
            exit_called = True

        djnkshvflbaugjkhnlzdvxfcs321 = ASDAsadz9oinm("TestASDAsadz9oinm")
        djnkshvflbaugjkhnlzdvxfcs321.on_exit = exit_event
        djnkshvflbaugjkhnlzdvxfcs321.on_exit()
        self.assertTrue(exit_called)