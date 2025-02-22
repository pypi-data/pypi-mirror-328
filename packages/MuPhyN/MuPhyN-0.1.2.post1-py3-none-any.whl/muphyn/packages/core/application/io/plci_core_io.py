from typing import List, Union

from ..signal.plci_core_signal import Signal

class Input:

    def __init__(self, name: str, signal: Signal) -> None:
        self._name: str = name
        self._signal: Signal = signal

    @property
    def name(self) -> str:
        return self._name
    
    @name.setter
    def name(self, newName: str):
        self.setName(newName)

    @property
    def signal(self) -> str:
        return self._signal
    
    @signal.setter
    def signal(self, newSignal: str):
        self.setSignal(newSignal)

    def setName(self, newName: str):
        if self._name != newName:
            self._name = newName

    def setSignal(self, newSignal: str):
        if self._signal != newSignal:
            self._signal = newSignal

class Output:

    def __init__(self, name: str, signals: Signal = []) -> None:
        self._name: str = name
        self._signals: List[Signal] = signals

    @property
    def name(self) -> str:
        return self._name
    
    @name.setter
    def name(self, newName: str):
        self.setName(newName)

    @property
    def signals(self) -> str:
        return self._signals
    
    def appendSignal(self, newSignal: Signal):
        if newSignal not in self._signals:
            self._signals.append(newSignal)
    
    def appendSignals(self, newSignals: List[Signal]):
        for newSignal in newSignals:
            self.appendSignal(newSignal)
    
    def clearSignals(self):
        self._signals: List[Signal] = []
    
    def insertSignal(self, newSignal: Signal, index: int):
        if newSignal not in self._signals:
            self._signals.insert(index, newSignal)
    
    def insertSignals(self, newSignals: List[Signal], index: int):
        for signalIndex, newSignal in enumerate(newSignals):
            self.insertSignal(index + signalIndex, newSignal)
    
    def removeSignal(self, signal: Union[Signal, int]):
        if type(signal) == int and signal < len(self._signals):
            signal = self._signals[signal]

        if signal in self._signals:
            self._signals.remove(signal)
    
    def removeSignals(self, newSignals: List[Union[Signal, int]]):
        for newSignal in newSignals:
            self.removeSignal(newSignal)

    def setName(self, newName: str):
        if self._name != newName:
            self._name = newName