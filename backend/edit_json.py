def minimum_entries(entries):
    return [only_needed_key(entry) for entry in entries]


def only_needed_key(entry):
    NEED_KEYS = ['body', 'created_at', 'id', 'tags', 'title', 'url']
    minimum_entry = {k: [] for k in NEED_KEYS}
    for key in NEED_KEYS:
        try:
            # タグのみ構造が異なるため、別処理
            if key != 'tags':
                # 必要な項目を取得
                minimum_entry[key] = entry.pop(key)
            else:
                # 投稿に結びついたすべてのタグ名を取得
                minimum_entry['tags'] = [
                    tag['name'] for tag in entry.pop('tags')]
        except KeyError:
            pass
    return minimum_entry
