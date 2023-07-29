class SnapshotArray:
    cnt=0
    snapshot={}
    arr=list()

    def __init__(self, length: int):
        self.arr=[0]*length
        

    def set(self, index: int, val: int) -> None:
        self.arr[index]=val
        

    def snap(self) -> int:
        self.snapshot[self.cnt]=self.arr[:]
        self.cnt+=1
        return self.cnt-1
        

    def get(self, index: int, snap_id: int) -> int:
        print(self.arr)
        return self.snapshot[snap_id][index]

s=SnapshotArray(3)
s.set(0,5)
id1=s.snap()
print(id1)
s.set(0,6)
print(s.get(0,id1))
