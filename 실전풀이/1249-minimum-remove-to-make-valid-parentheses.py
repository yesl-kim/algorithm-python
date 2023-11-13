class Solution:
    def minRemoveToMakeValid(self, s: str) -> str:
        ns = ''
        oc = 0
        cc = 0
        for x in s:
            if x == ')':
                if oc == cc:
                    continue
                cc += 1
            elif x == '(':
                oc += 1
            ns += x
        
        s, ns = ns, ''
        oc = 0
        for x in s:
            if x == '(':
                if oc == cc:
                    continue
                oc += 1
            ns += x
        return ns


class Solution:
    def minRemoveToMakeValid(self, s: str) -> str:
        def remove(s, oc):
            try:
                x = next(s)
                if x == '(':
                    ns, cc = remove(s, oc + 1)
                    return (x + ns, cc - 1) if cc else (ns, cc)
                elif x == ')':
                    if oc:
                        ns, cc = remove(s, oc - 1)
                        return (x + ns, cc + 1)
                    else:
                        return remove(s, oc)
                else:
                    ns, cc = remove(s, oc)
                    return (x + ns, cc)
            except StopIteration:
                return ('', 0)

        return remove(iter(s), 0)[0]
    

s = "lee(t(c)o)de)"
print(Solution().minRemoveToMakeValid(s))