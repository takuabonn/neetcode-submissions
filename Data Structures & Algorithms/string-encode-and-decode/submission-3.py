class Solution:

    def encode(self, strs: list[str]) -> str:
        if not strs:
            return ""

        # 1. 各要素の終了インデックス（結合後の位置）を計算する
        end_indices = []
        current_length = 0
        for s in strs:
            current_length += len(s)
            end_indices.append(str(current_length))

        # 2. ヘッダーを作成 (例: "6,11,15,20,24#")
        header = ",".join(end_indices) + "#"

        # 3. ボディ（文字列の単純結合）を作成
        body = "".join(strs)

        # ヘッダーとボディを合わせて全体の文字列にする
        return header + body

    def decode(self, s: str) -> list[str]:
        if not s:
            return []

        # 1. 最初の '#' を探してヘッダーとボディに切り分ける
        sharp_index = s.find("#")
        header = s[:sharp_index]
        body = s[sharp_index + 1 :]

        # 2. ヘッダーから終了インデックスのリストを復元
        end_indices = [int(x) for x in header.split(",")]

        # 3. インデックスを元にボディから文字列を切り出す
        res = []
        start_idx = 0
        for end_idx in end_indices:
            res.append(body[start_idx:end_idx])
            start_idx = end_idx  # 次の文字の開始位置を更新

        return res
