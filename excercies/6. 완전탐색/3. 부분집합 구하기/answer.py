# TODO
def dfs(n):
    def _dfs(i=1, res=''):
        if i<=n:
            _dfs(i+1, f"{res} {i}")
            _dfs(i+1, res)
        else:
            if res=='': return
            print(res)
    _dfs(1)

dfs(3)