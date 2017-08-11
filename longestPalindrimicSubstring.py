#Given a string s, find the longest palindromic substring in s. You may assume that the maximum length of s is 1000.

class Solution(object):
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """
        letterDict = {}
        count = 0
        result = 0
        for index,letter in enumerate(s):
            tail = s[len(s) - index - 1]
            beforeTail = s[len(s) - index - 2]

            try:
                nextLetter = s[index + 1]
            except IndexError:
                nextLetter = letter

            firstSet = [letter, nextLetter]
            secondSet = [tail, beforeTail]


            print firstSet
            print secondSet

            if firstSet == secondSet:
                count += 1
                if count > result:
                    result = count
            else:
                count = 1
                if count > result:
                    result = count

            print count
            print " "

        return result


a = Solution()
print a.longestPalindrome('stupidracecar')
