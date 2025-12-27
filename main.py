import time

class ChangeTracker:
    def __init__(self, coins=None):
        self.coins = coins or [100, 50, 20, 10, 5, 2, 1]

    def find_coins_greedy(self, amount):
        result = {}

        for coin in self.coins:
            num_coins = amount // coin
            if num_coins > 0:
                amount -= num_coins * coin
                result[coin] = num_coins
            if amount == 0:
                break

        return result

    def find_min_coins_dp(self, amount):
        dynamic_table = [float('inf')] * (amount + 1)
        dynamic_table[0] = 0
        
        used_coin = [0] * (amount + 1)
        
        for i in range(1, amount + 1):
            for coin in self.coins:
                if coin <= i and dynamic_table[i - coin] + 1 < dynamic_table[i]:
                    dynamic_table[i] = dynamic_table[i - coin] + 1
                    used_coin[i] = coin
        
        result = {}
        current = amount
        while current > 0:
            coin = used_coin[current]
            result[coin] = result.get(coin, 0) + 1
            current -= coin
        
        return result

def tracker_results(test_cases):
    tracker = ChangeTracker()
    
    for amount in test_cases:
        print("Amount: ", amount)
        print("Greedy Approach:", tracker.find_coins_greedy(amount))
        print("Dynamic Programming Approach:", tracker.find_min_coins_dp(amount))
        print('----------------')

def benchmark():
    tracker = ChangeTracker()
    test_amounts = [113, 1000, 5000, 10000, 50000]
    
    print(f"{'Сума':<10} {'Greedy (сек)':<15} {'DP (сек)':<15} {'Різниця':<10}")
    print("-" * 50)
    
    for amount in test_amounts:
        # Greedy
        start = time.perf_counter()
        tracker.find_coins_greedy(amount)
        greedy_time = time.perf_counter() - start
        
        # DP
        start = time.perf_counter()
        tracker.find_min_coins_dp(amount)
        dp_time = time.perf_counter() - start
        
        ratio = dp_time / greedy_time if greedy_time > 0 else 0
        print(f"{amount:<10} {greedy_time:<15.6f} {dp_time:<15.6f} {ratio:<10.1f}")

def main():
    test_cases = [1, 49, 50, 51, 72, 99, 113]
    tracker_results(test_cases)

    print('\n----------------')
    # Extra test cases
    benchmark()


if __name__ == "__main__":
    main()