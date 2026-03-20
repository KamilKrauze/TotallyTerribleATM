import unittest
from unittest.mock import patch

from StateMachine import *
from ATM import TestingATM

# def stub_request_amount(atm_self):
#     atm_self._amount_requested = True
#     atm_self._requested_amount = 100
#     if (atm_self.RunAsDebug):
#         atm_self.log_string = atm_self.log_string + f"AmountRequested[{atm_self._requested_amount} GBP]->"

class StateMachineExecutionTests(unittest.TestCase):
    
    def test_state_machine_execution_no_transitions(self):
        self.event_string = ""
        def on_entry():
            self.event_string = self.event_string + "Entry->"
        def on_update():
            self.event_string = self.event_string + "Update->"
        
        state_a = State("StateA")
        state_a.on_entry = on_entry
        state_a.on_update = on_update
        sm = StateMachine(state_a)
        
        for _ in range(5):
            sm.update()
            self.assertEqual(sm.exec_state, ExecutionState.UnChanged)
            
        self.assertEqual(sm.exec_state, ExecutionState.UnChanged)
        self.assertEqual(self.event_string, "Entry->Update->Update->Update->Update->Update->")
        
    def test_state_machine_execution_with_transitions_terminating(self):
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
        
        state_a = State("StateA")
        state_a.on_entry = on_entry_a
        state_a.on_update = on_update_a
        state_a.on_exit = on_exit_a
        
        state_b = State("StateB")
        state_b.can_terminate = True
        state_b.on_entry = on_entry_b
        state_b.on_exit = on_exit_b
        
        sm = StateMachine(state_a)
        sm.add_state(state_b)
        
        transition = TransitionDefinition(state_a, state_b, condition=lambda: True)
        sm.define_transition(transition)
        
        sm.update()
        self.assertEqual(sm.exec_state, ExecutionState.ChangingState)
        
        sm.update()
        self.assertEqual(sm.exec_state, ExecutionState.Terminated)
        self.assertEqual(sm.current_state, None)
        self.assertEqual(self.event_string, "EntryA->ExitA->EntryB->ExitB->")
        
    def test_state_machine_execution_with_transitions_circular(self):
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
        
        state_a = State("StateA")
        state_a.on_entry = on_entry_a
        state_a.on_update = on_update_a
        state_a.on_exit = on_exit_a
        
        state_b = State("StateB")
        state_b.on_entry = on_entry_b
        state_b.on_update = on_update_b
        state_b.on_exit = on_exit_b
        
        sm = StateMachine(state_a)
        sm.add_state(state_b)
        
        self.trans_cond = False
        transition1 = TransitionDefinition(state_a, state_b, condition=lambda: True)
        transition2 = TransitionDefinition(state_b, state_a, condition=lambda: self.trans_cond is True)
        sm.define_transition(transition1)
        sm.define_transition(transition2)
        
        sm.update()
        self.assertEqual(sm.exec_state, ExecutionState.ChangingState)
        self.assertEqual(self.event_string, "EntryA->ExitA->EntryB->UpdateB->")
        
        sm.update()
        self.assertEqual(sm.exec_state, ExecutionState.UnChanged)
        self.assertEqual(self.event_string, "EntryA->ExitA->EntryB->UpdateB->UpdateB->")
        self.trans_cond = True
        
        sm.update()
        self.assertEqual(sm.exec_state, ExecutionState.ChangingState)
        self.assertEqual(self.event_string, "EntryA->ExitA->EntryB->UpdateB->UpdateB->ExitB->EntryA->UpdateA->")
        
        sm.update()
        self.assertEqual(sm.exec_state, ExecutionState.ChangingState)
        self.assertEqual(self.event_string, "EntryA->ExitA->EntryB->UpdateB->UpdateB->ExitB->EntryA->UpdateA->ExitA->EntryB->UpdateB->")
        
    def test_state_machine_execution_with_transitions_priorities(self):
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
        
        state_a = State("StateA")
        state_a.on_entry = on_entry_a
        state_a.on_update = on_update_a
        state_a.on_exit = on_exit_a
        
        state_b = State("StateB")
        state_b.on_entry = on_entry_b
        state_b.on_update = on_update_b
        state_b.on_exit = on_exit_b
        
        state_c = State("StateC")
        state_c.on_entry = on_entry_c
        state_c.on_update = on_update_c
        state_c.on_exit = on_exit_c
        
        sm = StateMachine(state_a)
        sm.add_state(state_b)
        sm.add_state(state_c)
        
        transition1 = TransitionDefinition(state_a, state_b, condition=lambda: True, priority=1)
        transition2 = TransitionDefinition(state_a, state_c, condition=lambda: True, priority=2)
        sm.define_transition(transition1)
        sm.define_transition(transition2)
        
        sm.update()
        self.assertEqual(sm.exec_state, ExecutionState.ChangingState)
        
        sm.update()
        self.assertEqual(sm.exec_state, ExecutionState.UnChanged)

        self.assertEqual(self.event_string, "EntryA->ExitA->EntryC->UpdateC->UpdateC->")
        self.assertEqual(sm.current_state, state_c)
        
    def test_state_machine_execution_with_transitions_priorities_equal(self):
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
        
        state_a = State("StateA")
        state_a.on_entry = on_entry_a
        state_a.on_update = on_update_a
        state_a.on_exit = on_exit_a
        
        state_b = State("StateB")
        state_b.on_entry = on_entry_b
        state_b.on_update = on_update_b
        state_b.on_exit = on_exit_b
        
        state_c = State("StateC")
        state_c.on_entry = on_entry_c
        state_c.on_update = on_update_c
        state_c.on_exit = on_exit_c
        
        sm = StateMachine(state_a)
        sm.add_state(state_b)
        sm.add_state(state_c)
        
        transition1 = TransitionDefinition(state_a, state_b, condition=lambda: True, priority=1)
        transition2 = TransitionDefinition(state_a, state_c, condition=lambda: True, priority=1)
        sm.define_transition(transition1)
        sm.define_transition(transition2)
        
        sm.update()
        self.assertEqual(sm.exec_state, ExecutionState.ChangingState)
        
        sm.update()
        self.assertEqual(sm.exec_state, ExecutionState.UnChanged)

        self.assertEqual(self.event_string, "EntryA->ExitA->EntryB->UpdateB->UpdateB->")
        self.assertEqual(sm.current_state, state_b)
    
    def test_atm_state_machine_execution_happypath(self):
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
    
    def test_atm_state_machine_execution_badcard(self):
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