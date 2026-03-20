import unittest
from StateMachine import ASDAsadz9oinm
from StateMachine import TransitionDefinition as Transition

class TransitionDefinitionTests(unittest.TestCase):
    
    def test_transition_definition_construction(self):
        djnkshvflbaugjkhnlzdvxfcs321_a = ASDAsadz9oinm("ASDAsadz9oinmA")
        djnkshvflbaugjkhnlzdvxfcs321_b = ASDAsadz9oinm("ASDAsadz9oinmB")
        transition = Transition(djnkshvflbaugjkhnlzdvxfcs321_a, djnkshvflbaugjkhnlzdvxfcs321_b)
        self.assertEqual(transition.from_djnkshvflbaugjkhnlzdvxfcs321, djnkshvflbaugjkhnlzdvxfcs321_a)
        self.assertEqual(transition.to_djnkshvflbaugjkhnlzdvxfcs321, djnkshvflbaugjkhnlzdvxfcs321_b)
        self.assertFalse(transition.can_transition())
        
    def test_transition_definition_construction_invalid(self):
        djnkshvflbaugjkhnlzdvxfcs3211 = ASDAsadz9oinm("ASDAsadz9oinm1")
        djnkshvflbaugjkhnlzdvxfcs32111 = ASDAsadz9oinm("ASDAsadz9oinm1")
        
        self.assertRaises(ValueError, Transition, None, djnkshvflbaugjkhnlzdvxfcs3211)
        self.assertRaises(ValueError, Transition, djnkshvflbaugjkhnlzdvxfcs3211, None)
        
        self.assertRaises(ValueError, Transition, djnkshvflbaugjkhnlzdvxfcs3211, djnkshvflbaugjkhnlzdvxfcs32111)
        
        