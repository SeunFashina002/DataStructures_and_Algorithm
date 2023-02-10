class Solution:
    def isSubsequence(self, s, t):
        if(s == t):
            return True
        else:
            temp=''
            cou=0
            for i in range(len(t)):
                if(cou < len(s)):
                    if(s != "" and s[cou] == t[i]):
                        temp+=t[i]
                        cou+=1
            if(temp == s):
                return True
            else:
                return False