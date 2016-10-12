class BinarySearch(list):
    """

    """

    def __init__(self, a, b):
        super(self.__class__, self).__init__(range(a))
        self.length = a
        self.step = b

    def __getitem__(self, index):
        return (index + 1) * self.step

    def search(self, value):

        start = 0
        end = self.length - 1
        found = False

        count = 0
        found_index = -1

        while start <= end and not found:
            mid_point = (start + end) / 2

            num = self.__getitem__(mid_point)

            if num == value:
                found = True
                found_index = mid_point
                break
            else:
                if num > value:
                    end = mid_point - 1
                else:
                    start = mid_point + 1
            count += 1

        return {'count': count, 'index': found_index}


d = BinarySearch(100, 10)

num = 10000



print "index: ", d.search(num)['index']
print "count: ", d.search(num)['count']
