def draw_stairs(stairs_count_str):
    stairs_count = int(stairs_count_str)
    for stair_down in range(1,stairs_count,1):
        margins = stairs_count - stair_down
        stair_string = " " * margins + "#" * stair_down
        print(stair_string)
    print ("#"*stairs_count)