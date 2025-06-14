from Observable.StocksObservable import StocksObservable

class IphoneObservableImpl(StocksObservable):
    
    #Create a list to add the observers
    
    observerList = []
    stockCount = 0

    def add(self, observer):
        self.observerList.append(observer)
    
    def remove(self, observer):
        self.observerList.remove(observer)

    def notifySubscribers(self):
        for obs in self.observerList:
            obs.update()

    def setStockCount(self, repCount):
        if self.stockCount == 0:
            self.notifySubscribers()
        
        self.stockCount = self.stockCount + repCount

    def getStockCount(self):
        return self.stockCount