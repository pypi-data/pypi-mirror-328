from abc import ABC, abstractmethod

from numpy import pi

from qubits import AbstractQubit

## Abstarct gate class
class AbstractGate(ABC):

    def __init__(
            self,
            *qubits
        ):
        
        # Check that all qubits are based on the defined class
        if any(not isinstance(qubit, AbstractQubit) for qubit in qubits):
            raise ValueError("The input to a gate object must be a child of `AbstractQubit`.")
        
        # The gate is applied to the qubit
        self.gate = self._applied_gate(*qubits)

    @abstractmethod
    def _applied_gate(self, *qubits):
        pass

class AbstractRotationalGate(AbstractGate):

    def __init__(self, angle: float=0.5*pi, *qubits):

        # Collects angle
        self.angle = angle

        super().__init__(*qubits)

    
    def _applied_gate(self, *qubits):
        return super()._applied_gate(*qubits)




# Cirq gates
from cirq import rx, rz, ry, CNOT, H
from qubits import CirqQubit

class CirqH(AbstractGate):

    def __init__(self, qubit):
        super().__init__(qubit)

    
    def _applied_gate(self, qubit: CirqQubit):
        return H(qubit.object)
    

class CirqRx(AbstractGate):

    def __init__(self, qubit):
        super().__init__(qubit)

    
    def _applied_gate(self, qubit: CirqQubit, rads: float=0.5):
        return rx(rads=rads)(qubit.object)
    

class CirqRy(AbstractGate):

    def __init__(self, qubit):
        super().__init__(qubit)

    
    def _applied_gate(self, qubit: CirqQubit, rads: float=0.5):
        return ry(rads=rads)(qubit.object)
    

class CirqRz(AbstractGate):

    def __init__(self, qubit):
        super().__init__(qubit)

    
    def _applied_gate(self, qubit: CirqQubit, rads: float=0.5):
        return rz(rads=rads)(qubit.object)

class CirqCNOT(AbstractGate):

    def __init__(self, qubit1, qubit2):
        super().__init__(qubit1, qubit2)

    
    def _applied_gate(self, qubit1: CirqQubit, qubit2: CirqQubit):
        return CNOT(qubit1.object, qubit2.object)
    


print(CirqH(CirqQubit(1)).gate)
print(CirqRx(CirqQubit(1)).gate)
print(CirqRy(CirqQubit(1)).gate)
print(CirqRz(CirqQubit(1)).gate)
print(CirqCNOT(CirqQubit(1)).gate)

