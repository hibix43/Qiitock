# QiitaNote

## 目的・コンセプト

Qiitaのストックを管理する。振り返りやすくする。

## 発生した問題

- 特定の条件下において、OAuth認証画面が開けない
  - requests.get(oauth-page-url)が原因
  - 入力に渡したURLとresutlsObj.urlが異なっていた
  - 直にリンクを貼る、リンクを文字列として処理することで解決した
- thisの混同
  - VueComponents > getLoginURL > this
  - getLoginURL > function > this
  - getLoginURL > this　を変数vmに格納してから、function > vm.XXX
  - アロー(=>)を使うことでも可能
- 「nullではない」の比較には、「!==」を使う
  - サーバから返されたJSONのキーによって表示を切り替える
  - 具体例）ログイン済みなら、ログインリンクを表示しない
  - !=では、検知できないため、!==を使用する
- Markdownにおいて「#を含む」=「見出し」としてはいけない
  - [```]で囲われたコードブロックにおいて#が使われることがあるため
  - 先に正規表現を使い、コードブロックを削除しておく
  - r'```.+```'は間違い。r'`{3}.+`{3}'でも間違い。
  - r'`{3}.+?`{3}'が正しい。
  - +?：最短一致。条件に合う「一番短い部分」に一致する。
- 「npm run build」が実行できない
  - /frontendにおいて
  - $rm -rf node_modules
  - $npm install
  - 上記のコマンドで解決
  - [Missing modules when running npm run build or npm install #780](https://github.com/olefredrik/FoundationPress/issues/780)
