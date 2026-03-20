from enum import Enum

class State:
    def __init__(self, name: str, terminate = False):
        if not name:
            raise ValueError("State name cannot be empty")

        self.name = name
        self.on_entry = None
        self.on_exit = None
        self.on_update = None

        self.can_terminate = terminate

class TransitionDefinition:
    def __init__(self, from_state: State, to_state: State, condition=None, priority: int = 0):
        if (to_state is None or from_state is None):
            raise ValueError("From and To states cannot be None")
        if (to_state.name == from_state.name):
            raise ValueError("From and To states cannot be the same")
        self.from_state = from_state
        self.to_state = to_state        
        self.condition = condition or (lambda: False)
        self.priority = priority

    def can_transition(self) -> bool:
        return self.condition()

class ExecutionState(Enum):
    NotStarted = -1,
    Starting = 1,
    Terminated = 2,
    UnChanged = 3,
    Running = 4,
    ChangingState = 5,

class StateMachine:
    def __init__(self, initial_state: State):
        self._states = {}
        self._transitions = []

        self.current_state = initial_state
        self._states[initial_state.name] = initial_state
        self.exec_state = ExecutionState.NotStarted
        self._ran_init_state = False
        return

    def add_state(self, state: State):
        if state in self._states:
            raise ValueError(f"State '{state.name}' already exists")

        self._states[state.name] = state
        return
    
    def add_states(self, states: list[State]):
        for state in states:
            self.add_state(state)
        return

    def define_transition(self, transition: TransitionDefinition):
        if transition.from_state not in self._states:
            raise TypeError(f"Unknown state: {transition.from_state}")
        if transition.to_state not in self._states:
            raise RuntimeError(f"Unknown state: {transition.to_state}")

        self._transitions.append(transition)
        return
    
    def define_transitions(self, transitions: list[TransitionDefinition]):
        for transition in transitions:
            self.define_transition(transition)
        return

    def update(self):
        if (self.current_state is None):
            self.exec_state = ExecutionState.Terminated
            return
        
        if (self._ran_init_state is not True):
            self._ran_init_state = True
            self._try_invoke_entry_event()
            self.exec_state = ExecutionState.Starting
        
        self._try_invoke_update_event()
        
        valid = [
            t for t in self._transitions
            if t.from_state.name == self.current_state and t.can_transition()
        ]

        valid.sort(key=lambda t: t.priority, reverse=False)

        if self.current_state.can_terminate:
            self._try_invoke_exit_event()
            self.exec_state = ExecutionState.Terminated
            self.current_state = None
            return

        self.exec_state = ExecutionState.Running

        if valid is None or len(valid) == 0:
            self.exec_state = ExecutionState.UnChanged
            return

        transition = valid[0]
        self._perform_transition(transition)
        return

    def _perform_transition(self, transition: TransitionDefinition):
        next_state = self._states[transition.to_state.name]

        # Exit current
        self._try_invoke_exit_event()

        self.exec_state = ExecutionState.ChangingState
        # Switch
        self.current_state = next_state

        # Entry new
        self._try_invoke_entry_event()
        
        return
    
    def _try_invoke_update_event(self):
        if self.current_state.on_update is not None:
            self.current_state.on_update()
        return
    
    def _try_invoke_entry_event(self):
        if self.current_state.on_entry is not None:
            self.current_state.on_entry()
        return
    
    def _try_invoke_exit_event(self):
        if self.current_state.on_exit is not None:
            self.current_state.on_entry()
        return