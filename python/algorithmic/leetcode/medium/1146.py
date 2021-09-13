# 1146. Snapshot Array
# https://leetcode.com/problems/snapshot-array/

class SnapshotArray:

    def __init__(self, length: int):
        self.array = [0 for i in range(length)]
        self.snap_id=-1
        self.snaps = {}

    def set(self, index: int, val: int) -> None:
        #self.array[index] = val
        if self.snap_id not in self.snaps:
            self.snaps[self.snap_id] = {}
        self.snaps[self.snap_id][index] = val

    def snap(self) -> int:
        self.snap_id += 1
        #self.snaps[self.snap_id] = self.array.copy()
        return self.snap_id

    def get(self, index: int, snap_id: int) -> int:
        ans = None
        for i in range(snap_id-1, -2, -1):
            if i in self.snaps and index in self.snaps[i]:
                ans = self.snaps[i][index]
                break
        if ans is None:
            ans = self.array[index]
        return ans

# Your SnapshotArray object will be instantiated and called as such:
# obj = SnapshotArray(length)
# obj.set(index,val)
# param_2 = obj.snap()
# param_3 = obj.get(index,snap_id)
if __name__=='__main__':
    obj = SnapshotArray(3)
    obj.set(0,5)
    obj.snap()
    obj.set(0,6)
    print(obj.get(0,0))