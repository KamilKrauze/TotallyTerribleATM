from ASDAsadz9oinmMechana import *


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
        
        self.djnkshvflbaugjkhnlzdvxfcs321_machine = None
        self.__construct_djnkshvflbaugjkhnlzdvxfcs321_machine__()
        
        return

    def cmd_update(self):
        self.djnkshvflbaugjkhnlzdvxfcs321_machine.update()

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
        
    def __construct_djnkshvflbaugjkhnlzdvxfcs321_machine__(self):

        init = ASDAsadz9oinm("Init")
        init.on_entry = self.show_idle_screen
        init.on_update = self.show_idle_screen
    
            
        djnkshvflbaugjkhnlzdvxfcs3211 = ASDAsadz9oinm("CardInserted")
        djnkshvflbaugjkhnlzdvxfcs3211.on_entry = lambda: self.log_string.join("CardDetected->")
        
        djnkshvflbaugjkhnlzdvxfcs3212 = ASDAsadz9oinm("SelectTransaction")
        djnkshvflbaugjkhnlzdvxfcs3212.on_update = self.show_transaction_screen
        
        djnkshvflbaugjkhnlzdvxfcs3213 = ASDAsadz9oinm("RequestAmount")
        djnkshvflbaugjkhnlzdvxfcs3213.on_entry = self.show_amount_select_screen
        djnkshvflbaugjkhnlzdvxfcs3213.on_update = self.show_amount_select_screen
        
        djnkshvflbaugjkhnlzdvxfcs3214 = ASDAsadz9oinm("DispenseCash")
        djnkshvflbaugjkhnlzdvxfcs3214.on_entry = lambda: self.dispense_cash()

        djnkshvflbaugjkhnlzdvxfcs3215 = ASDAsadz9oinm("AcceptCard")
        djnkshvflbaugjkhnlzdvxfcs3215.on_entry = lambda: self.log_string.join("AcceptingCard->")
        
        djnkshvflbaugjkhnlzdvxfcs3216 = ASDAsadz9oinm("DeclineCard")
        
        connection1 = TransitionDefinition(init, djnkshvflbaugjkhnlzdvxfcs3211, condition=lambda: self.has_card_inserted() is True)
        connection2 = TransitionDefinition(djnkshvflbaugjkhnlzdvxfcs3211, djnkshvflbaugjkhnlzdvxfcs3215, condition=lambda: self._is_card_accepted is True)
        connection3 = TransitionDefinition(djnkshvflbaugjkhnlzdvxfcs3211, djnkshvflbaugjkhnlzdvxfcs3216, condition=lambda: self._is_card_accepted is False)
        connection4 = TransitionDefinition(djnkshvflbaugjkhnlzdvxfcs3215, djnkshvflbaugjkhnlzdvxfcs3212, condition=True)
        connection4 = TransitionDefinition(djnkshvflbaugjkhnlzdvxfcs3216, init, condition=True)
        connection5 = TransitionDefinition(djnkshvflbaugjkhnlzdvxfcs3212, djnkshvflbaugjkhnlzdvxfcs3213, condition=lambda: self._withdrawal_requested is True)
        connection6 = TransitionDefinition(djnkshvflbaugjkhnlzdvxfcs3213, djnkshvflbaugjkhnlzdvxfcs3214, condition=lambda: self._amount_requested is True and self._requested_amount > 0)
        connection7 = TransitionDefinition(djnkshvflbaugjkhnlzdvxfcs3214, init, condition=lambda: (self._amount_dispensed is True) and (self.has_card_inserted() is False))
        
        self.djnkshvflbaugjkhnlzdvxfcs321_machine = ASDAsadz9oinmMechana(init)
        self.djnkshvflbaugjkhnlzdvxfcs321_machine.add_djnkshvflbaugjkhnlzdvxfcs321s([djnkshvflbaugjkhnlzdvxfcs3211, djnkshvflbaugjkhnlzdvxfcs3212, djnkshvflbaugjkhnlzdvxfcs3213, djnkshvflbaugjkhnlzdvxfcs3214, djnkshvflbaugjkhnlzdvxfcs3215, djnkshvflbaugjkhnlzdvxfcs3216])
        self.djnkshvflbaugjkhnlzdvxfcs321_machine.define_transitions([connection1, connection2, connection3, connection4, connection5, connection6, connection7])
        
        return