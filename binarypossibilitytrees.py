class BinaryPossibility:
  """
  This class represents a single binary possibility with a state (0, 1, or None for superposition).
  """

  def __init__(self, state=None):
    """
    Initialize the BinaryPossibility object with a state (0, 1, or None for superposition).
    """
    if state not in (0, 1, None):
      raise ValueError("Invalid state. Must be 0, 1, or None.")
    self.state = state

  def set_state(self, state):
    """
    Sets the state of the possibility (0, 1, or None).
    """
    if state not in (0, 1, None):
      raise ValueError("Invalid state. Must be 0, 1, or None.")
    self.state = state

  def is_superposition(self):
    """
    Returns True if the possibility is in superposition, False otherwise.
    """
    return self.state is None

  def __str__(self):
    """
    Defines how to print the BinaryPossibility object descriptively.
    """
    if self.state is None:
      return "Possibility: (0 & 1)"  # Indicate superposition
    else:
      return f"Possibility: {self.state}" if self.state else "Possibility: |1>"

class BinaryRegister:
  """
  This class represents a register of binary possibilities for storing binary data with superposition.
  """

  def __init__(self, num_bits):
    """
    Initialize the BinaryRegister with a specified number of possibilities.
    """
    if num_bits <= 0:
      raise ValueError("Number of bits must be positive.")
    self.possibilities = [BinaryPossibility() for _ in range(num_bits)]

  def add_bit(self):
    """
    Adds a new possibility (in superposition) to the end of the register.
    """
    self.possibilities.append(BinaryPossibility())

  def remove_bit(self):
    """
    Removes the last possibility from the register (if there's at least one).
    """
    if len(self.possibilities) == 0:
      raise IndexError("Cannot remove bit from empty register.")
    self.possibilities.pop()

  def set_bit(self, index, state):
    """
    Sets the state (0, 1, or None) of a specific possibility in the register.
    """
    if index not in range(len(self.possibilities)):
      raise IndexError("Invalid bit index.")
    if state not in (0, 1, None):
      raise ValueError("Invalid state. Must be 0, 1, or None.")
    self.possibilities[index].set_state(state)

  def get_bit(self, index):
    """
    Returns the state (0, 1, or None) of a specific possibility in the register.
    """
    if index not in range(len(self.possibilities)):
      raise IndexError("Invalid bit index.")
    return self.possibilities[index].state

  def enumerate_states(self):
    """
    Enumerates all possible states of the register as strings, considering superposition during the process.
    """
    if len(self.possibilities) == 0:
      return []
    states = []

    def generate_states(i, partial_state):
      if i == len(self.possibilities):
        states.append(partial_state)
        return
      if self.possibilities[i].is_superposition():
        generate_states(i + 1, partial_state + "0")  # Explore possibility of 0
        generate_states(i + 1, partial_state + "1")  # Explore possibility of 1
      else:
        state_str = "0" if self.possibilities[i].state == 0 else "1"
        generate_states(i + 1, partial_state + state_str)

    generate_states(0, "")
    return states

  def get_individual_states(self):
    """
    Returns a list of BinaryPossibility objects representing the individual states of the register (including superposition).
    """
    return self.possibilities.copy()


