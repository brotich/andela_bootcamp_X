class BinarySearch(list):
    """
        Searches for an item in a list
    """

    def __init__(self, a, b):
        super(self.__class__, self).__init__(range(a))
        self.length = a
        self.step = b

    def __getitem__(self, index):
        """
            return the value of the item at position index of the list
            :parameter index the index to find
            :returns the item
        """
        return (index + 1) * self.step

    def search(self, item):
        """
            finds an item in the list using binary search
            :parameter item the value to search for in the list
            :returns dict with keys index => location of item or -1 if not found
                                    count => number of times the array was accesed
       """

        first = 0
        last = self.length - 1
        found = False

        index = -1
        count = 0

        while first <= last and not found:
            midpoint = (first + last) / 2

            if item == 10000:
                print self.__getitem__(midpoint) 

            if not (self.__getitem__(midpoint) - item ) % self.step == 0: #item not multiple exit
                break

            if self.__getitem__(midpoint) == item:
                found = True
                index = midpoint
            else:
                if item < self.__getitem__(midpoint):
                    last = midpoint - 1
                else:
                    first = midpoint + 1
            count += 1
        

        return {"index": index, "count": count}
