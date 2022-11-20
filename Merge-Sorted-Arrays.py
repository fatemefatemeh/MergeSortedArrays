
class Solution(object):
    def merge(self, nums1, m, nums2, n):
        """
        :type nums1: List[int]
        :type m: int
        :type nums2: List[int]
        :type n: int
        """
        i = int(m - 1)
        j = int(n - 1)
        k = int(m + n - 1)
        
        while (k >= 0):
            if i>=0 and j>=0:
                print(nums1[i])
                print(nums2[j])
                if(nums2[j] > nums1[i]):
                    nums1[k] = nums2[j]
                    k -= 1
                    j -= 1
                else:
                    nums1[k] = nums1[i]
                    k -= 1
                    i -= 1
            elif j >= 0:
                nums1[k] = nums2[j]
                k -= 1
                j -= 1
            else:
                break
        return nums1

s = Solution()
print(s.merge(nums1=[1, 2, 3, 0, 0, 0], nums2=[2, 5, 6], m=3, n=3))