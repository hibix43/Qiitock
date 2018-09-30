import re


def minimum_entries(entries):
    entries = [only_needed_key(entry) for entry in entries]
    for entry in entries:
        entry['agenda'] = agenda_from_markdown(entry['body'])
    return entries


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


def agenda_from_markdown(body):
    # コードブロック削除
    body = re.sub(r'`{3}.+?`{3}', '', body, flags=re.DOTALL)
    # 見出しを抽出
    headings = [line for line in body.split('\n') if line.startswith('#')]
    # 目次
    agenda = ['<ul>']
    # 調査中の見出し
    serch_level = 1
    # <ul>タグの個数
    ul_num = 1
    for heading in headings:
        level = heading.count('#')
        # 調査中のレベルであれば
        if level == serch_level:
            # 追加
            agenda.append('<li>' + heading + '</li>')
        # 1つ下のレベルであれば
        elif level > serch_level:
            # ネストしたうえで、追加
            agenda.append('<ul>')
            agenda.append('<li>' + heading + '</li>')
            ul_num += 1
            serch_level = level
        # 1つ上のレベルであれば
        elif level < serch_level:
            # 目的のレベルまで
            for i in range(serch_level - level):
                # ネストを閉じる
                agenda.append('</ul>')
                ul_num -= 1
            agenda.append('<li>' + heading + '</li>')
            serch_level = level
    # 帳尻を合わせる
    while ul_num > 0:
        agenda.append('</ul>')
        ul_num -= 1
    # [#]を取り除く
    agenda = [heading.replace('#', '')
              if heading.startswith('<li>#') else heading
              for heading in agenda]
    # 1つの文字列として結合
    return '\n'.join(agenda)