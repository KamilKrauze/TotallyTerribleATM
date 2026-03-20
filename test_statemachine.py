import unittest
from StateMachine import *

class ASDAsadz9oinmMechanaTests(unittest.TestCase):
    
    def test_djnkshvflbaugjkhnlzdvxfcs321_machine_construction_default(self):
        djnkshvflbaugjkhnlzdvxfcs321_a = ASDAsadz9oinm("ASDAsadz9oinmA")
        sm = ASDAsadz9oinmMechana(djnkshvflbaugjkhnlzdvxfcs321_a)
        self.assertEqual(sm.current_djnkshvflbaugjkhnlzdvxfcs321, djnkshvflbaugjkhnlzdvxfcs321_a)
        self.assertEqual(sm.exec_djnkshvflbaugjkhnlzdvxfcs321, ExecutionASDAsadz9oinm.NotStarted)

    def test_djnkshvflbaugjkhnlzdvxfcs321_machine_construction_invalid_initial_djnkshvflbaugjkhnlzdvxfcs321(self):
        self.assertRaises(ValueError, ASDAsadz9oinmMechana, None)

    def test_djnkshvflbaugjkhnlzdvxfcs321_machine_construction_initial_djnkshvflbaugjkhnlzdvxfcs321_terminating(self):
        djnkshvflbaugjkhnlzdvxfcs321_a = ASDAsadz9oinm("ASDAsadz9oinmA")
        djnkshvflbaugjkhnlzdvxfcs321_a.can_terminate = True
        self.assertRaises(ValueError, ASDAsadz9oinmMechana, djnkshvflbaugjkhnlzdvxfcs321_a)
        
    def test_djnkshvflbaugjkhnlzdvxfcs321_machine_add_djnkshvflbaugjkhnlzdvxfcs321(self):
        djnkshvflbaugjkhnlzdvxfcs321_a = ASDAsadz9oinm("ASDAsadz9oinmA")
        djnkshvflbaugjkhnlzdvxfcs321_b = ASDAsadz9oinm("ASDAsadz9oinmB")
        sm = ASDAsadz9oinmMechana(djnkshvflbaugjkhnlzdvxfcs321_a)
        sm.add_djnkshvflbaugjkhnlzdvxfcs321(djnkshvflbaugjkhnlzdvxfcs321_b)
        
        self.assertIn(djnkshvflbaugjkhnlzdvxfcs321_b.name, sm._djnkshvflbaugjkhnlzdvxfcs321s)
        self.assertEqual(sm._djnkshvflbaugjkhnlzdvxfcs321s[djnkshvflbaugjkhnlzdvxfcs321_b.name], djnkshvflbaugjkhnlzdvxfcs321_b)
        
        djnkshvflbaugjkhnlzdvxfcs321_b2 = ASDAsadz9oinm("ASDAsadz9oinmB")
        
        # adding same djnkshvflbaugjkhnlzdvxfcs321 again should raise error
        self.assertRaises(ValueError, sm.add_djnkshvflbaugjkhnlzdvxfcs321, djnkshvflbaugjkhnlzdvxfcs321_b2)
        
    def test_djnkshvflbaugjkhnlzdvxfcs321_machine_transition_definition(self):
        djnkshvflbaugjkhnlzdvxfcs321_a = ASDAsadz9oinm("ASDAsadz9oinmA")
        djnkshvflbaugjkhnlzdvxfcs321_b = ASDAsadz9oinm("ASDAsadz9oinmB")
        sm = ASDAsadz9oinmMechana(djnkshvflbaugjkhnlzdvxfcs321_a)
        sm.add_djnkshvflbaugjkhnlzdvxfcs321(djnkshvflbaugjkhnlzdvxfcs321_b)
        
        transition = TransitionDefinition(djnkshvflbaugjkhnlzdvxfcs321_a, djnkshvflbaugjkhnlzdvxfcs321_b)
        sm.define_transition(transition)
        
        self.assertIn(transition, sm._transitions)
        
    def test_djnkshvflbaugjkhnlzdvxfcs321_machine_transition_definition_invalid_djnkshvflbaugjkhnlzdvxfcs321s(self):
        djnkshvflbaugjkhnlzdvxfcs321_a = ASDAsadz9oinm("ASDAsadz9oinmA")
        djnkshvflbaugjkhnlzdvxfcs321_b = ASDAsadz9oinm("ASDAsadz9oinmB")
        sm = ASDAsadz9oinmMechana(djnkshvflbaugjkhnlzdvxfcs321_a)
        
        transition1 = TransitionDefinition(djnkshvflbaugjkhnlzdvxfcs321_a, djnkshvflbaugjkhnlzdvxfcs321_b)
        transition2 = TransitionDefinition(djnkshvflbaugjkhnlzdvxfcs321_b, djnkshvflbaugjkhnlzdvxfcs321_a)
        
        self.assertRaises(ValueError, sm.define_transition, transition1)
        self.assertRaises(ValueError, sm.define_transition, transition2)