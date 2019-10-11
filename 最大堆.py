class MaxHeap:
    def __init__(self):
        self._data=[]
        self._count=len(self._data)
    def size(self):
        return self._count
    def isEmpty(self):
        return self._count==0
    def add(self,item):
        self._data.append(item)
        self._count+=1
        self._shiftup(self._count-1)
    def _shiftup(self,index):
        parent=(index-1)>>1
        while index>0 and self._data[parent]<self._data[index]:
            self._data[parent],self._data[index]=self._data[index],self._data[parent]
            index=parent
            parent=(index-1)>>1