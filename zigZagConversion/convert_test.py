from convert import Solution


class TestCases:
    def test_one(self):
        assert Solution().convert("PAYPALISHIRING", 3) == "PAHNAPLSIIGYIR"

    def test_two(self):
        assert Solution().convert("PAYPALISHIRING", 4) == "PINALSIGYAHRPI"

    def test_three(self):
        assert Solution().convert("A", 1) == "A"

    def test_four(self):
        assert Solution().convert("AB", 1) == "AB"
