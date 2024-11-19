class solution:
    def is_valid(self, s: str) -> bool:
        arr = [c.lower() for c in s if c.isalnum()]
        return arr == arr[::-1]
