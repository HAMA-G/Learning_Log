address = ["東京都千代田区", "千葉県船橋市", "東京都杉並区", "埼玉県大宮市", "東京都町田市", "東京都西東京市", "あ東京都大田区", "神奈川県横浜市"]

tokyo = [town[3:] for town in address if town.startswith("東京都")]
print(tokyo)