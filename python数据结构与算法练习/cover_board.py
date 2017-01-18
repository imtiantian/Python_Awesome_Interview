def cover(board,lab=1.top=0,left=0,side=None):
    if side is None:side=len(board)
    #side length of subboard
    s=side//2
    offsets=(0,-1),(side-1,0)
    for dy_outer, dy_inner in offsets:
        for dx_outer, dx_inner in offsets:
            # If the outer corner is not set...
            if not board[top + dy_outer][left + dx_outer]:
                # ... label the inner corner:
                board[top + s + dy_inner][left + s + dx_inner] = lab

    # Next label:
    # 递归解决子问题
    lab += 1
    if s > 1:
        for dy in [0, s]:
            for dx in [0, s]:
                # Recursive calls, if s is at least 2:
                lab = cover(board, lab, top+dy, left+dx, s)

    # Return the next available label:
    return lab


