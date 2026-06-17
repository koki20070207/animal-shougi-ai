# ==========================================
# 動物将棋AI - app.py
# ==========================================

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

# 3. 駒を動かす関数 (データを書き換えるだけ)
def move_piece(current_board, from_row, from_col, to_row, to_col):
    piece = current_board[from_row][from_col]
    current_board[from_row][from_col] = None # 元のマスを空に
    current_board[to_row][to_col] = piece    # 先のマスに置く

# 4. その移動が正しいルールかどうかを判定する関数 (審判)
def is_valid_move(current_board, from_row, from_col, to_row, to_col):
    piece = current_board[from_row][from_col]
    
    # 動かそうとしたマスが空っぽならエラー
    if piece is None:
        return False
        
    # 【自分のヒヨコ (p_H) のルール：前に1マスだけ】
    if piece == "p_H":
        row_diff = to_row - from_row
        col_diff = to_col - from_col
        if row_diff == -1 and col_diff == 0:
            return True
        else:
            return False
            
    # まだ他の駒のルールを作っていないので、一旦一律True
    return True

# ==========================================
# 5. これより下は実験用のコード
# ==========================================

if __name__ == "__main__":
    # 実験スタート
    print("【ゲームスタート時の盤面】")
    display_board(board)

    # --- 実験1：ヒヨコを1マス前に進める（正しい動き） ---
    from_r, from_c = 2, 1
    to_r, to_c = 1, 1

    print(f"\n★実験1：自分のヒヨコを ({from_r}, {from_c}) から ({to_r}, {to_c}) へ動かします")
    if is_valid_move(board, from_r, from_c, to_r, to_c):
        print("👉 審判：OKです！移動します。")
        move_piece(board, from_r, from_c, to_r, to_c)
    else:
        print("❌ 審判：反則です！")

    display_board(board)

    # --- 実験2：ヒヨコを横に動かそうとする（反則の動き） ---
    from_r, from_c = 1, 1 # さっき移動したヒヨコ
    to_r, to_c = 1, 2     # 右に動かそうとする

    print(f"\n★実験2：自分のヒヨコを ({from_r}, {from_c}) から ({to_r}, {to_c}) へ横に動かします")
    if is_valid_move(board, from_r, from_c, to_r, to_c):
        print("👉 審判：OKです！移動します。")
        move_piece(board, from_r, from_c, to_r, to_c)
    else:
        print("❌ 審判：反則です！移動しません。")

    display_board(board)