import heapq as hq


def nLargest(n, heap):
    return hq.nlargest(n, heap)


def nSmallest(n, heap):
    return hq.nsmallest(n, heap)


def heapSort(heapList):
    heap = []
    for value in heapList:
        hq.heappush(heap, value)

    hList = []
    for y in range(len(heap)):
        hList.append(hq.heappop(heap))

    return hList


def hSort(heapList):
    hq.heapify(heapList)
    return [hq.heappop(heapList) for _ in range(len(heapList))]


def kElement(iterable, k):
    sList = hSort(iterable)

    if (k < len(iterable)):
        return (f"List is does not have {k} elements.")
    else:
        return iterable[k*-1]


heapList = [1, 3, 5, 4, 9, 10]
print(kElement(heapList, 3))


# hq.heapify(heapList)
# hq.heapreplace(heapList, 13)
# print(heapList)


