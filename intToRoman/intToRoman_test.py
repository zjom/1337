from intToRoman import Solution


class TestClass:
    def test_one(self):
        assert Solution().intToRoman(10) == 'X'

    def test_two(self):
        assert Solution().intToRoman(3749) == 'MMMDCCXLIX'

    def test_three(self):
        assert Solution().intToRoman(58) == 'LVIII'

    def test_four(self):
        assert Solution().intToRoman(1994) == 'MCMXCIV'

    def test_five(self):
        assert Solution().intToRoman(9) == 'IX'
