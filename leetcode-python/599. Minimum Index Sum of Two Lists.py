# 제출 코드 - Runtime 22.63 Memory 97.18
class Solution:
    def findRestaurant(self, list1, list2):

        least = 10000
        commons = []
        for i1, l1 in enumerate(list1):
            if l1 in list2:
                i_sum = i1 + list2.index(l1)
                if i_sum == least:
                    commons.append(l1)
                elif i_sum < least:
                    commons = [l1]
                    least = i_sum

        return commons


l11 = ["Shogun", "Tapioca Express", "Burger King", "KFC"]
l21 = ["Piatti", "The Grill at Torrey Pines", "Hungry Hunter Steakhouse", "Shogun"]
l12 = ["Shogun", "Tapioca Express", "Burger King", "KFC"]
l22 = ["KFC", "Shogun", "Burger King"]
l13 = ["Shogun", "Tapioca Express", "Burger King", "KFC"]
l23 = ["KFC", "Burger King", "Tapioca Express", "Shogun"]
l14 = ["Shogun", "Tapioca Express", "Burger King", "KFC"]
l24 = ["KNN", "KFC", "Burger King", "Tapioca Express", "Shogun"]

sol = Solution()

print(sol.findRestaurant(l11, l21))
print(sol.findRestaurant(l12, l22))
print(sol.findRestaurant(l13, l23))
print(sol.findRestaurant(l14, l24))
