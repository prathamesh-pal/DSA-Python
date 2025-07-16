class WordFinder:
    def set_grid(self, grid):
        self.grid = [list(row) for row in grid]
        self.rows = len(grid)
        self.cols = len(grid[0]) if grid else 0

    def count(self, word):
        if not word:
            return 0

        directions = [
            (-1, 0), (1, 0),     # Up, Down
            (0, -1), (0, 1),     # Left, Right
            (-1, -1), (-1, 1),   # Up-Left, Up-Right
            (1, -1), (1, 1),     # Down-Left, Down-Right
        ]

        visited = set()
        count = 0
        is_palindrome = word == word[::-1]

        for r in range(self.rows):
            for c in range(self.cols):
                for d, (dr, dc) in enumerate(directions):
                    # Skip opposite directions if word is a palindrome
                    if is_palindrome and d % 2 == 1:
                        continue

                    if self._match(r, c, dr, dc, word):
                        key = (r, c, dr, dc) if not is_palindrome else tuple(sorted([(dr, dc), (-dr, -dc)]))
                        if (r, c, key) not in visited:
                            count += 1
                            visited.add((r, c, key))

        return count

    def _match(self, r, c, dr, dc, word):
        for i in range(len(word)):
            nr = r + dr * i
            nc = c + dc * i
            if nr < 0 or nr >= self.rows or nc < 0 or nc >= self.cols:
                return False
            if self.grid[nr][nc] != word[i]:
                return False
        return True


if __name__ == "__main__":
    grid = ["TIRATIRA",
            "IRATIRAT",
            "RATIRATI",
            "ATIRATIR"]

    finder = WordFinder()
    finder.set_grid(grid)

    print(finder.count("TIRA"))    # 7 
    print(finder.count("TA"))      # 13
    print(finder.count("RITARI"))  # 3
    print(finder.count("A"))       # 8
    print(finder.count("AA"))      # 6
    print(finder.count("RAITA"))   # 0
