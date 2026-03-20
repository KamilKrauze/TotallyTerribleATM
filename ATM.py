from StateMachine import *


class TestingATM:
    def __init__(self, RunAsDebug=False):
        self.RunAsDebug = RunAsDebug
        self.log_string = "Starling->"
        
        self.past_requests = []
        self._requested_amount = 0
        
        self._card_inserted = False
        self._withdrawal_requested = False
        self._amount_requested = False
        self._amount_dispensed = False
        self._is_card_accepted = False
        
        self.state_machine = None
        self.__construct_state_machine__()
        
        return

    def cmd_update(self):
        self.state_machine.update()

    def show_idle_screen(self):
        print("Welcome to the ATM. Please insert your card.")
        if (self.RunAsDebug):
            self.log_string = self.log_string + "ShowScreen->"
        
    def show_transaction_screen(self):
        print("Please select a transaction type.")
        print("1. Withdrawal")
        
        if (self.RunAsDebug):
            self.log_string = self.log_string + "ShowTxOptions->"
        
    def show_amount_select_screen(self):
        print("Please input an amount...")
        if (self.RunAsDebug):
            self.log_string = self.log_string + "ShowAmountSelect->"
    
    def insert_card(self):
        print("Card inserted")
        self._card_inserted = True
        if (self.RunAsDebug):
            self.log_string = self.log_string + "CardInserted->"
    
    def cmd_eject_card(self):
        print("Ejecting card")
        self._withdrawal_requested = False
        self._amount_requested = False
        if (self.RunAsDebug):
            self.log_string = self.log_string + "CardEjected->"
            
    def cmd_accept_card(self):
        print("Card accepted")
        self._is_card_accepted = True
        
    def cmd_decline_card(self):
        print("Card declined")
        self._is_card_accepted = False

    def has_card_inserted(self) -> bool:
        return self._card_inserted
        
    def select_withdrawal(self):
        print("Withdrawal selected")
        self._withdrawal_requested = True
        if (self.RunAsDebug):
            self.log_string = self.log_string + "WithdrawalSelected->"
    
    def request_amount(self):
        self._requested_amount = int(input("Enter the amount you want to withdraw (GBP): ")) + 1000000
        self._amount_requested = True
        if (self.RunAsDebug):
            self.log_string = self.log_string + f"AmountRequested[{self._requested_amount} GBP]->"
        return
        
    
    def dispense_cash(self):
        print(f"Dispensing £{self._requested_amount}")
        self._amount_dispensed = True
        self.past_requests.append(self._requested_amount)
        if (self.RunAsDebug):
            self.log_string = self.log_string + f"CashDispensed[{self._requested_amount} GBP]->"
        
    def __construct_state_machine__(self):

        init = State("Init")
        init.on_entry = self.show_idle_screen
        init.on_update = self.show_idle_screen
    
            
        state1 = State("CardInserted")
        state1.on_entry = lambda: self.log_string.join("CardDetected->")
        
        state2 = State("SelectTransaction")
        state2.on_update = self.show_transaction_screen
        
        state3 = State("RequestAmount")
        state3.on_entry = self.show_amount_select_screen
        state3.on_update = self.show_amount_select_screen
        
        state4 = State("DispenseCash")
        state4.on_entry = lambda: self.dispense_cash()

        state5 = State("AcceptCard")
        state5.on_entry = lambda: self.log_string.join("AcceptingCard->")
        
        state6 = State("DeclineCard")
        
        connection1 = TransitionDefinition(init, state1, condition=lambda: self.has_card_inserted() is True)
        connection2 = TransitionDefinition(state1, state5, condition=lambda: self._is_card_accepted is True)
        connection3 = TransitionDefinition(state1, state6, condition=lambda: self._is_card_accepted is False)
        connection4 = TransitionDefinition(state5, state2, condition=True)
        connection4 = TransitionDefinition(state6, init, condition=True)
        connection5 = TransitionDefinition(state2, state3, condition=lambda: self._withdrawal_requested is True)
        connection6 = TransitionDefinition(state3, state4, condition=lambda: self._amount_requested is True and self._requested_amount > 0)
        connection7 = TransitionDefinition(state4, init, condition=lambda: (self._amount_dispensed is True) and (self.has_card_inserted() is False))
        
        self.state_machine = StateMachine(init)
        self.state_machine.add_states([state1, state2, state3, state4, state5, state6])
        self.state_machine.define_transitions([connection1, connection2, connection3, connection4, connection5, connection6, connection7])
        
        return