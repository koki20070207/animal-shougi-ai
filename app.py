# 1. 初期配置の定義
# e_ は相手(Enemy)、p_ は自分(Player)
# K:キリン, L:ライオン, Z:ゾウ, H:ヒヨコ
board = [
    ["e_K", "e_L", "e_Z"],  # 1段目 (相手陣地)
    [None,  "e_H", None ],  # 2段目
    [None,  "p_H", None ],  # 3段目
    ["p_Z", "p_L", "p_K"]   # 4段目 (自分陣地)
]

# 2. 盤面を綺麗に表示する関数
def display_board(current_board):
    print("--- 盤面の状態 ---")
    for row in current_board:
        row_str = []
        for cell in row:
            if cell is None:
                row_str.append("  .  ") # 空っぽのマス
            else:
                row_str.append(f" {cell} ") # 駒があるマス
        print("|".join(row_str))
    print("-----------------")

# 3. 関数を実行してみる
display_board(board)
# 4. 駒を動かす関数
def move_piece(current_board, from_row, from_col, to_row, to_col):
    # 移動元の駒を取得
    piece = current_board[from_row][from_col]
    
    # 移動元のマスを空っぽ(None)にする
    current_board[from_row][from_col] = None
    
    # 移動先のマスに駒を置く
    current_board[to_row][to_col] = piece

# --- 実験：自分のヒヨコを1マス前に動かしてみる ---
print("\n★自分のヒヨコ(p_H)を (2, 1) から (1, 1) へ移動します...")

# 関数を呼び出す（ board, 元の縦, 元の横, 先の縦, 先の横 ）
move_piece(board, 2, 1, 1, 1)

# 移動後の盤面を表示
display_board(board)