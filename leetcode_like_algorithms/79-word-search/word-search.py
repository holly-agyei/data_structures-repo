class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        rows, cols = len(board), len(board[0])

        # directions: up, down, left, right
        directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]

        for r in range(rows):
            for c in range(cols):
                if board[r][c] != word[0]:
                    continue

                # Stack holds: (row, col, index_in_word, visited_set, path_list)
                stack = [(r, c, 0, set([(r, c)]), [(r, c)])]

                while stack:
                    row, col, k, visited, path = stack.pop()

                    if board[row][col] != word[k]:
                        continue

                    if k == len(word) - 1:
                        return True  # whole word matched

                    for dr, dc in directions:
                        nr, nc = row + dr, col + dc
                        if (
                            0 <= nr < rows and 0 <= nc < cols and
                            (nr, nc) not in visited and
                            board[nr][nc] == word[k + 1]
                        ):
                            # push next step with updated visited + path
                            new_visited = visited.copy()
                            new_visited.add((nr, nc))
                            new_path = path + [(nr, nc)]
                            stack.append((nr, nc, k + 1, new_visited, new_path))

        return False
