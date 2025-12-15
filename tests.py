from game import game
import time

def test(method1, method2, depth1, depth2, eval1, eval2, size, reps, isTest):
    methods = {method1: 0, method2: 0, 'tie':0}
    start_time = time.time()
    for i in range(reps):
        result = game(method1, method2, depth1, depth2, size, eval1, eval2, isTest)
        methods[result] += 1
    mo_time = (time.time() - start_time) / reps


    print(f"Board size: {size}")
    print(f"1st move {method1}: {methods[method1]}, Depth1: {depth1}")
    print(f"2nd move {method2}: {methods[method2]}, Depth2: {depth2}")
    print(f"Tie: {methods['tie']}")
    print(f"mo_time {mo_time:.1f}")


test("min_max", "randomMove", 1, 1, 'evaluate', 'evaluate', 8, 5, True)

# # random - simple heur
# test("min_max", "randomMove", 1, 1, 'evaluate', 'evaluate', 8, 500, True)
# test("randomMove", "min_max", 1, 1, 'evaluate', 'evaluate', 8, 500, True)
# print()

# test("min_max", "randomMove", 2, 2, 'evaluate', 'evaluate', 8, 250, True)
# test("randomMove", "min_max", 2, 2, 'evaluate', 'evaluate', 8, 250, True)
# print()

# test("min_max", "randomMove", 3, 3, 'evaluate', 'evaluate', 8, 50, True)
# test("randomMove", "min_max", 3, 3, 'evaluate', 'evaluate', 8, 50, True)
# print()

# test("min_max", "randomMove", 4, 4, 'evaluate', 'evaluate', 8, 25, True)
# test("randomMove", "min_max", 4, 4, 'evaluate', 'evaluate', 8, 25, True)
# print()

# test("min_max", "randomMove", 5, 5, 'evaluate', 'evaluate', 8, 5, True)
# test("randomMove", "min_max", 5, 5, 'evaluate', 'evaluate', 8, 5, True)
# print()
# print()

# # random - complex heur
# test("min_max", "randomMove", 1, 1, 'evaluate2', 'evaluate2', 8, 500, True)
# test("randomMove", "min_max", 1, 1, 'evaluate2', 'evaluate2', 8, 500, True)
# print()

# test("min_max", "randomMove", 2, 2, 'evaluate2', 'evaluate2', 8, 250, True)
# test("randomMove", "min_max", 2, 2, 'evaluate2', 'evaluate2', 8, 250, True)
# print()

# test("min_max", "randomMove", 3, 3, 'evaluate2', 'evaluate2', 8, 50, True)
# test("randomMove", "min_max", 3, 3, 'evaluate2', 'evaluate2', 8, 50, True)
# print()

# test("min_max", "randomMove", 4, 4, 'evaluate2', 'evaluate2', 8, 25, True)
# test("randomMove", "min_max", 4, 4, 'evaluate2', 'evaluate2', 8, 25, True)
# print()

# test("min_max", "randomMove", 5, 5, 'evaluate2', 'evaluate2', 8, 5, True)
# test("randomMove", "min_max", 5, 5, 'evaluate2', 'evaluate2', 8, 5, True)
# print()
# print()
# print()

# instamax
# # random - simple heur
# test("min_max", "instaMaxRandom", 1, 1, 'evaluate', 'evaluate', 8, 500, True)
# test("instaMaxRandom", "min_max", 1, 1, 'evaluate', 'evaluate', 8, 500, True)
# print()

# test("min_max", "instaMaxRandom", 2, 2, 'evaluate', 'evaluate', 8, 250, True)
# test("instaMaxRandom", "min_max", 2, 2, 'evaluate', 'evaluate', 8, 250, True)
# print()

# test("min_max", "instaMaxRandom", 3, 3, 'evaluate', 'evaluate', 8, 50, True)
# test("instaMaxRandom", "min_max", 3, 3, 'evaluate', 'evaluate', 8, 50, True)
# print()

# test("min_max", "instaMaxRandom", 4, 4, 'evaluate', 'evaluate', 8, 25, True)
# test("instaMaxRandom", "min_max", 4, 4, 'evaluate', 'evaluate', 8, 25, True)
# print()

# test("min_max", "instaMaxRandom", 5, 5, 'evaluate', 'evaluate', 8, 5, True)
# test("instaMaxRandom", "min_max", 5, 5, 'evaluate', 'evaluate', 8, 5, True)
# print()
# print()

# # random - complex heur
# test("min_max", "instaMaxRandom", 1, 1, 'evaluate2', 'evaluate2', 8, 500, True)
# test("instaMaxRandom", "min_max", 1, 1, 'evaluate2', 'evaluate2', 8, 500, True)
# print()

# test("min_max", "instaMaxRandom", 2, 2, 'evaluate2', 'evaluate2', 8, 250, True)
# test("instaMaxRandom", "min_max", 2, 2, 'evaluate2', 'evaluate2', 8, 250, True)
# print()

# test("min_max", "instaMaxRandom", 3, 3, 'evaluate2', 'evaluate2', 8, 50, True)
# test("instaMaxRandom", "min_max", 3, 3, 'evaluate2', 'evaluate2', 8, 50, True)
# print()

# test("min_max", "instaMaxRandom", 4, 4, 'evaluate2', 'evaluate2', 8, 25, True)
# test("instaMaxRandom", "min_max", 4, 4, 'evaluate2', 'evaluate2', 8, 25, True)
# print()

# test("min_max", "instaMaxRandom", 5, 5, 'evaluate2', 'evaluate2', 8, 5, True)
# test("instaMaxRandom", "min_max", 5, 5, 'evaluate2', 'evaluate2', 8, 5, True)
# print()
# print()
# print()
