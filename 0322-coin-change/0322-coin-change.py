class Solution:
    def coinChange(self, coins: list[int], amount: int) -> int:
        stack = [(0, 0)]  # (sum, number_of_coins)
        best = float("inf")
        best_seen = {0:0}

        while stack:
            curr_sum, count = stack.pop()

            if curr_sum == amount:
                best = min(best, count)
                continue

            for coin in coins:
                new_sum = coin+curr_sum
                cur_count = count+1
                
                if new_sum <= amount:
                #it's more like we go only if this is a good path
                    if new_sum not in best_seen or cur_count < best_seen[new_sum]:
                        stack.append((curr_sum + coin, count + 1))
                        best_seen[new_sum] = cur_count 

        return best if best!= float("inf") else -1