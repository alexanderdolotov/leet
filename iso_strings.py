class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        s_to_t: dict[str, str] = {}
        t_to_s: dict[str, str] = {}
        for a, b in zip(s, t):
            if s_to_t.setdefault(a, b) != b or t_to_s.setdefault(b, a) != a:
                return False
        return True


if __name__ == "__main__":
    sol = Solution()
    assert sol.isIsomorphic("egg", "add")
    assert not sol.isIsomorphic("foo", "bar")
    assert sol.isIsomorphic("paper", "title")
    print("ok")
