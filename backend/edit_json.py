import re


def minimum_entries(entries):
    entries = [only_needed_key(entry) for entry in entries]
    for entry in entries:
        entry['agenda'] = agenda_from_markdown(entry)
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


def convert_heading_to_li(url, heading):
    # #を取り除く
    heading = heading.replace('#', '')
    # #のあとにスペースがあるなら、取り除く
    if heading.startswith(' '):
        heading = heading[1:]
    # リンク付きなら、リンクを外す
    if re.search(r'\[.+?\]\(.+?\)', heading):
        title = re.findall(r'\[.+?\]', heading)[0]
        heading = re.sub(r'\[.+?\]\(.+?\)', title[1:-1], heading)
    # テンプレートに当てはめる
    a_template = '<a href="{0}#{1}" target="_blank">{1}</a>'
    template = f'<li>{a_template.format(url, heading)}</li>'
    return template


def agenda_from_markdown(entry):
    # コードブロック削除
    body = re.sub(r'`{3}.+?`{3}', '', entry['body'], flags=re.DOTALL)
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
            agenda.append(convert_heading_to_li(entry['url'], heading))
        # 1つ下のレベルであれば
        elif level > serch_level:
            # ネストしたうえで、追加
            agenda.append('<ul>')
            agenda.append(convert_heading_to_li(entry['url'], heading))
            ul_num += 1
            serch_level = level
        # 1つ上のレベルであれば
        elif level < serch_level:
            # 目的のレベルまで
            for i in range(serch_level - level):
                # ネストを閉じる
                agenda.append('</ul>')
                ul_num -= 1
            agenda.append(convert_heading_to_li(entry['url'], heading))
            serch_level = level
    # 帳尻を合わせる
    while ul_num > 0:
        agenda.append('</ul>')
        ul_num -= 1
    # 1つの文字列として結合
    return '\n'.join(agenda)
