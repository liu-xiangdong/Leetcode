class Solution:
    def numWaterBottles(self, numBottles: int, numExchange: int):
        sum = numBottles
        emptyBottles = numBottles
        while emptyBottles >= numExchange:
            a = emptyBottles // numExchange
            sum = sum + a
            emptyBottles = emptyBottles % numExchange + a
        return sum
