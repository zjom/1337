from sol import Solution

class TestSol:
    S:Solution = Solution()

    def test_one(self):
        words = ["foo","bar"]
        assert self.S.findSubstring('barfoothefoobarman',words) == [0,9]

    def test_two(self):
        words = ["word","good","best","word"]
        assert self.S.findSubstring("wordgoodgoodgoodbestword",words) == []

    def test_three(self):
        words = ["foo","bar", "the"]
        assert self.S.findSubstring("barfoofoobarthefoobarman",words) == [6,9,12]

    def test_four(self):
        words = ["word","good","best","good"]
        assert self.S.findSubstring("wordgoodgoodgoodbestword", words) == [8]

    def test_five(self):
        words = ["fooo","barr","wing","ding","wing"]
        assert self.S.findSubstring("lingmindraboofooowingdingbarrwingmonkeypoundcake", words) == [13]
