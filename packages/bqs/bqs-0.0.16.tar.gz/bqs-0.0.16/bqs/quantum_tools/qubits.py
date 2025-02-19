from abc import ABC, abstractmethod
from typing import Union

## Abstract class for the qubit

class AbstractQubit(ABC):
    
    def __init__(
            self,
            name: str | int | tuple
        ):
        
        # Stores the name input
        self.name = name

        # Storing the qubit object
        self.object = self._get_qubit()

    
    @abstractmethod
    def _get_qubit(self):
        pass


    def __str__(self):
        return str(self.name)

# cirq qubit
from cirq import NamedQubit
class CirqQubit(AbstractQubit):

    def _get_qubit(self):
        return NamedQubit(str(self.name))
