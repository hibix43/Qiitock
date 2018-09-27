class EditJson():
    items = {}

    def __init__(self):
        pass

    # タグごとに記事を分類する
    def group_by_tag(self, got_json):
        for item in got_json:
            # キーの確認
            if 'tags' in item:
                # 投稿のタグを取得
                for tags in item['tags']:
                    tag = tags.get('name')
                    # 既に登録済みなら更新
                    if tag in self.items.keys():
                        self.items[tag].append(item)
                    # 更新していなければ作成
                    else:
                        self.items[tag] = [item]
