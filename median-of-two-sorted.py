class Solution(object):
    def findMedianSortedArrays(self, nums1, nums2):
        a.sort()
        b.sort()
        c = []
        for index, number in enumerate(a):
            if(a[index] < b[index]):
                c.append(a[index])
                print a
            elif (b[index] >= a):
                c.append(b[index])
                print b

        print c

s = Solution()

a = [1,2,5,7,3]
b = [4,5,7,3,1]
s.findMedianSortedArrays(a,b)
