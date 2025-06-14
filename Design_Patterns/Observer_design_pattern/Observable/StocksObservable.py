from abc import ABC, abstractmethod

class StocksObservable(ABC):
    @abstractmethod
    def add():
        pass

    @abstractmethod
    def remove():
        pass

    @abstractmethod
    def notifySubscribers():
        pass

    @abstractmethod
    def setStockCount():
        pass

    @abstractmethod
    def getStockCount():
        pass

