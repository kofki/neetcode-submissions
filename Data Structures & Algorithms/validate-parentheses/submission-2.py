class Solution:
    def isValid(self, s: str) -> bool:
        st = []
        for c in s:
            if c == "(" or c == "{" or c == "[":
                st.append(c)
            elif len(st)>0 and ((c == ")" and st[-1] == "(" ) or (
            c == "}" and st[-1] == "{") or (
            c== "]" and st[-1] == "[")):
                    st.pop(-1)
            else:
                return False
        if len(st) > 0:
            return False
        return True
        