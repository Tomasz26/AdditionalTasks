def build_bridge1(chunk, goal):
    chunkx = 2 * (goal + chunk/2) / (3 * chunk)
    if chunkx.is_integer():
        print(f"liczba płyt to {chunkx}, liczba łączników to {chunkx - 1}")
    else:
        print(False)

build_bridge1(2, 20)