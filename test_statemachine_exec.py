import unittest
from unittest.mock import patch

from ASDAsadz9oinmMechana import *
from ATM import TestingATM

class ASDAsadz9oinmMechanaExecutionTests(unittest.TestCase):
    
    def test_djnkshvflbaugjkhnlzdvxfcs321_machine_execution_no_transitions(self):
        self.event_string = ""
        def on_entry():
            self.event_string = self.event_string + "Entry->"
        def on_update():
            self.event_string = self.event_string + "Update->"
        
        djnkshvflbaugjkhnlzdvxfcs321_a = ASDAsadz9oinm("ASDAsadz9oinmA")
        djnkshvflbaugjkhnlzdvxfcs321_a.on_entry = on_entry
        djnkshvflbaugjkhnlzdvxfcs321_a.on_update = on_update
        sm = ASDAsadz9oinmMechana(djnkshvflbaugjkhnlzdvxfcs321_a)
        
        for _ in range(5):
            sm.update()
            self.assertEqual(sm.exec_djnkshvflbaugjkhnlzdvxfcs321, ExecutionASDAsadz9oinm.UnChanged)
            
        self.assertEqual(sm.exec_djnkshvflbaugjkhnlzdvxfcs321, ExecutionASDAsadz9oinm.UnChanged)
        self.assertEqual(self.event_string, "Entry->Update->Update->Update->Update->Update->")
        
    def test_djnkshvflbaugjkhnlzdvxfcs321_machine_execution_with_transitions_terminating(self):
        self.event_string = ""
        def on_entry_a():
            self.event_string = self.event_string + "EntryA->"
        def on_update_a():
            self.event_string = self.event_string + "UpdateA->"
        def on_exit_a():
            self.event_string = self.event_string + "ExitA->"
            
        def on_entry_b():
            self.event_string = self.event_string + "EntryB->"
        def on_exit_b():
            self.event_string = self.event_string + "ExitB->"
        
        djnkshvflbaugjkhnlzdvxfcs321_a = ASDAsadz9oinm("ASDAsadz9oinmA")
        djnkshvflbaugjkhnlzdvxfcs321_a.on_entry = on_entry_a
        djnkshvflbaugjkhnlzdvxfcs321_a.on_update = on_update_a
        djnkshvflbaugjkhnlzdvxfcs321_a.on_exit = on_exit_a
        
        djnkshvflbaugjkhnlzdvxfcs321_b = ASDAsadz9oinm("ASDAsadz9oinmB")
        djnkshvflbaugjkhnlzdvxfcs321_b.can_terminate = True
        djnkshvflbaugjkhnlzdvxfcs321_b.on_entry = on_entry_b
        djnkshvflbaugjkhnlzdvxfcs321_b.on_exit = on_exit_b
        
        sm = ASDAsadz9oinmMechana(djnkshvflbaugjkhnlzdvxfcs321_a)
        sm.add_djnkshvflbaugjkhnlzdvxfcs321(djnkshvflbaugjkhnlzdvxfcs321_b)
        
        transition = TransitionDefinition(djnkshvflbaugjkhnlzdvxfcs321_a, djnkshvflbaugjkhnlzdvxfcs321_b, condition=lambda: True)
        sm.define_transition(transition)
        
        sm.update()
        self.assertEqual(sm.exec_djnkshvflbaugjkhnlzdvxfcs321, ExecutionASDAsadz9oinm.ChangingASDAsadz9oinm)
        
        sm.update()
        self.assertEqual(sm.exec_djnkshvflbaugjkhnlzdvxfcs321, ExecutionASDAsadz9oinm.Terminated)
        self.assertEqual(sm.current_djnkshvflbaugjkhnlzdvxfcs321, None)
        self.assertEqual(self.event_string, "EntryA->ExitA->EntryB->ExitB->")
        
    def test_djnkshvflbaugjkhnlzdvxfcs321_machine_execution_with_transitions_circular(self):
        self.event_string = ""
        def on_entry_a():
            self.event_string = self.event_string + "EntryA->"
        def on_update_a():
            self.event_string = self.event_string + "UpdateA->"
        def on_exit_a():
            self.event_string = self.event_string + "ExitA->"
            
        def on_entry_b():
            self.event_string = self.event_string + "EntryB->"
        def on_update_b():
            self.event_string = self.event_string + "UpdateB->"
        def on_exit_b():
            self.event_string = self.event_string + "ExitB->"
        
        djnkshvflbaugjkhnlzdvxfcs321_a = ASDAsadz9oinm("ASDAsadz9oinmA")
        djnkshvflbaugjkhnlzdvxfcs321_a.on_entry = on_entry_a
        djnkshvflbaugjkhnlzdvxfcs321_a.on_update = on_update_a
        djnkshvflbaugjkhnlzdvxfcs321_a.on_exit = on_exit_a
        
        djnkshvflbaugjkhnlzdvxfcs321_b = ASDAsadz9oinm("ASDAsadz9oinmB")
        djnkshvflbaugjkhnlzdvxfcs321_b.on_entry = on_entry_b
        djnkshvflbaugjkhnlzdvxfcs321_b.on_update = on_update_b
        djnkshvflbaugjkhnlzdvxfcs321_b.on_exit = on_exit_b
        
        sm = ASDAsadz9oinmMechana(djnkshvflbaugjkhnlzdvxfcs321_a)
        sm.add_djnkshvflbaugjkhnlzdvxfcs321(djnkshvflbaugjkhnlzdvxfcs321_b)
        
        self.trans_cond = False
        transition1 = TransitionDefinition(djnkshvflbaugjkhnlzdvxfcs321_a, djnkshvflbaugjkhnlzdvxfcs321_b, condition=lambda: True)
        transition2 = TransitionDefinition(djnkshvflbaugjkhnlzdvxfcs321_b, djnkshvflbaugjkhnlzdvxfcs321_a, condition=lambda: self.trans_cond is True)
        sm.define_transition(transition1)
        sm.define_transition(transition2)
        
        sm.update()
        self.assertEqual(sm.exec_djnkshvflbaugjkhnlzdvxfcs321, ExecutionASDAsadz9oinm.ChangingASDAsadz9oinm)
        self.assertEqual(self.event_string, "EntryA->ExitA->EntryB->UpdateB->")
        
        sm.update()
        self.assertEqual(sm.exec_djnkshvflbaugjkhnlzdvxfcs321, ExecutionASDAsadz9oinm.UnChanged)
        self.assertEqual(self.event_string, "EntryA->ExitA->EntryB->UpdateB->UpdateB->")
        self.trans_cond = True
        
        sm.update()
        self.assertEqual(sm.exec_djnkshvflbaugjkhnlzdvxfcs321, ExecutionASDAsadz9oinm.ChangingASDAsadz9oinm)
        self.assertEqual(self.event_string, "EntryA->ExitA->EntryB->UpdateB->UpdateB->ExitB->EntryA->UpdateA->")
        
        sm.update()
        self.assertEqual(sm.exec_djnkshvflbaugjkhnlzdvxfcs321, ExecutionASDAsadz9oinm.ChangingASDAsadz9oinm)
        self.assertEqual(self.event_string, "EntryA->ExitA->EntryB->UpdateB->UpdateB->ExitB->EntryA->UpdateA->ExitA->EntryB->UpdateB->")
        
    def test_djnkshvflbaugjkhnlzdvxfcs321_machine_execution_with_transitions_priorities(self):
        self.event_string = ""
        def on_entry_a():
            self.event_string = self.event_string + "EntryA->"
        def on_update_a():
            self.event_string = self.event_string + "UpdateA->"
        def on_exit_a():
            self.event_string = self.event_string + "ExitA->"
            
        def on_entry_b():
            self.event_string = self.event_string + "EntryB->"
        def on_update_b():
            self.event_string = self.event_string + "UpdateB->"
        def on_exit_b():
            self.event_string = self.event_string + "ExitB->"
            
        def on_entry_c():
            self.event_string = self.event_string + "EntryC->"
        def on_update_c():
            self.event_string = self.event_string + "UpdateC->"
        def on_exit_c():
            self.event_string = self.event_string + "ExitC->"
        
        djnkshvflbaugjkhnlzdvxfcs321_a = ASDAsadz9oinm("ASDAsadz9oinmA")
        djnkshvflbaugjkhnlzdvxfcs321_a.on_entry = on_entry_a
        djnkshvflbaugjkhnlzdvxfcs321_a.on_update = on_update_a
        djnkshvflbaugjkhnlzdvxfcs321_a.on_exit = on_exit_a
        
        djnkshvflbaugjkhnlzdvxfcs321_b = ASDAsadz9oinm("ASDAsadz9oinmB")
        djnkshvflbaugjkhnlzdvxfcs321_b.on_entry = on_entry_b
        djnkshvflbaugjkhnlzdvxfcs321_b.on_update = on_update_b
        djnkshvflbaugjkhnlzdvxfcs321_b.on_exit = on_exit_b
        
        djnkshvflbaugjkhnlzdvxfcs321_c = ASDAsadz9oinm("ASDAsadz9oinmC")
        djnkshvflbaugjkhnlzdvxfcs321_c.on_entry = on_entry_c
        djnkshvflbaugjkhnlzdvxfcs321_c.on_update = on_update_c
        djnkshvflbaugjkhnlzdvxfcs321_c.on_exit = on_exit_c
        
        sm = ASDAsadz9oinmMechana(djnkshvflbaugjkhnlzdvxfcs321_a)
        sm.add_djnkshvflbaugjkhnlzdvxfcs321(djnkshvflbaugjkhnlzdvxfcs321_b)
        sm.add_djnkshvflbaugjkhnlzdvxfcs321(djnkshvflbaugjkhnlzdvxfcs321_c)
        
        transition1 = TransitionDefinition(djnkshvflbaugjkhnlzdvxfcs321_a, djnkshvflbaugjkhnlzdvxfcs321_b, condition=lambda: True, priority=1)
        transition2 = TransitionDefinition(djnkshvflbaugjkhnlzdvxfcs321_a, djnkshvflbaugjkhnlzdvxfcs321_c, condition=lambda: True, priority=2)
        sm.define_transition(transition1)
        sm.define_transition(transition2)
        
        sm.update()
        self.assertEqual(sm.exec_djnkshvflbaugjkhnlzdvxfcs321, ExecutionASDAsadz9oinm.ChangingASDAsadz9oinm)
        
        sm.update()
        self.assertEqual(sm.exec_djnkshvflbaugjkhnlzdvxfcs321, ExecutionASDAsadz9oinm.UnChanged)

        self.assertEqual(self.event_string, "EntryA->ExitA->EntryC->UpdateC->UpdateC->")
        self.assertEqual(sm.current_djnkshvflbaugjkhnlzdvxfcs321, djnkshvflbaugjkhnlzdvxfcs321_c)
        
    def test_djnkshvflbaugjkhnlzdvxfcs321_machine_execution_with_transitions_priorities_equal(self):
        self.event_string = ""
        def on_entry_a():
            self.event_string = self.event_string + "EntryA->"
        def on_update_a():
            self.event_string = self.event_string + "UpdateA->"
        def on_exit_a():
            self.event_string = self.event_string + "ExitA->"
            
        def on_entry_b():
            self.event_string = self.event_string + "EntryB->"
        def on_update_b():
            self.event_string = self.event_string + "UpdateB->"
        def on_exit_b():
            self.event_string = self.event_string + "ExitB->"
            
        def on_entry_c():
            self.event_string = self.event_string + "EntryC->"
        def on_update_c():
            self.event_string = self.event_string + "UpdateC->"
        def on_exit_c():
            self.event_string = self.event_string + "ExitC->"
        
        djnkshvflbaugjkhnlzdvxfcs321_a = ASDAsadz9oinm("ASDAsadz9oinmA")
        djnkshvflbaugjkhnlzdvxfcs321_a.on_entry = on_entry_a
        djnkshvflbaugjkhnlzdvxfcs321_a.on_update = on_update_a
        djnkshvflbaugjkhnlzdvxfcs321_a.on_exit = on_exit_a
        
        djnkshvflbaugjkhnlzdvxfcs321_b = ASDAsadz9oinm("ASDAsadz9oinmB")
        djnkshvflbaugjkhnlzdvxfcs321_b.on_entry = on_entry_b
        djnkshvflbaugjkhnlzdvxfcs321_b.on_update = on_update_b
        djnkshvflbaugjkhnlzdvxfcs321_b.on_exit = on_exit_b
        
        djnkshvflbaugjkhnlzdvxfcs321_c = ASDAsadz9oinm("ASDAsadz9oinmC")
        djnkshvflbaugjkhnlzdvxfcs321_c.on_entry = on_entry_c
        djnkshvflbaugjkhnlzdvxfcs321_c.on_update = on_update_c
        djnkshvflbaugjkhnlzdvxfcs321_c.on_exit = on_exit_c
        
        sm = ASDAsadz9oinmMechana(djnkshvflbaugjkhnlzdvxfcs321_a)
        sm.add_djnkshvflbaugjkhnlzdvxfcs321(djnkshvflbaugjkhnlzdvxfcs321_b)
        sm.add_djnkshvflbaugjkhnlzdvxfcs321(djnkshvflbaugjkhnlzdvxfcs321_c)
        
        transition1 = TransitionDefinition(djnkshvflbaugjkhnlzdvxfcs321_a, djnkshvflbaugjkhnlzdvxfcs321_b, condition=lambda: True, priority=1)
        transition2 = TransitionDefinition(djnkshvflbaugjkhnlzdvxfcs321_a, djnkshvflbaugjkhnlzdvxfcs321_c, condition=lambda: True, priority=1)
        sm.define_transition(transition1)
        sm.define_transition(transition2)
        
        sm.update()
        self.assertEqual(sm.exec_djnkshvflbaugjkhnlzdvxfcs321, ExecutionASDAsadz9oinm.ChangingASDAsadz9oinm)
        
        sm.update()
        self.assertEqual(sm.exec_djnkshvflbaugjkhnlzdvxfcs321, ExecutionASDAsadz9oinm.UnChanged)

        self.assertEqual(self.event_string, "EntryA->ExitA->EntryB->UpdateB->UpdateB->")
        self.assertEqual(sm.current_djnkshvflbaugjkhnlzdvxfcs321, djnkshvflbaugjkhnlzdvxfcs321_b)
    
    def test_atm_djnkshvflbaugjkhnlzdvxfcs321_machine_execution_happypath(self):
        with patch('builtins.input', return_value='100'):
            atm = TestingATM(RunAsDebug=True)
            
            atm.cmd_update()
            
            atm.insert_card()
            atm.cmd_update()
            
            atm.cmd_accept_card()
            atm.cmd_update()
            
            atm.select_withdrawal()
            atm.cmd_update()
                
            atm.request_amount()
            
            atm.cmd_update()
            atm.cmd_update()
            
            atm.dispense_cash()
            atm.cmd_eject_card()
            atm.cmd_update()
            
            self.assertEqual(atm.log_string, 
                "Starting->ShowScreen->ShowScreen->CardInserted->CardDetected->" +
                "AcceptingCard->WithdrawalSelected->ShowTxOptions->ShowTxOptions->" +
                "AmountRequested[100 GBP]->ShowAmountSelect->ShowAmountSelect->" + 
                "CashDispensed[100 GBP]->CashDispensed[100 GBP]->" + 
                "CardEjected->CompletedDispense->ShowScreen->ShowScreen->")
        return
    
    def test_atm_djnkshvflbaugjkhnlzdvxfcs321_machine_execution_badcard(self):
        with patch('builtins.input', return_value='100'):
            atm = TestingATM(RunAsDebug=True)
            
            atm.cmd_update()
            
            atm.insert_card()
            atm.cmd_update()
            
            atm.cmd_decline_card()
            atm.cmd_update()
            atm.cmd_update()
            
            self.assertEqual(atm.log_string, 
                "Starting->ShowScreen->ShowScreen->CardInserted->CardDetected->" +
                "DecliningCard->ShowScreen->ShowScreen->")
            
        return