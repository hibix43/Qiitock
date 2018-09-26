# QiitaNote

## 目的・コンセプト
Qiitaのストックを管理する。振り返りやすくする。

## 発生した問題
- 特定の条件下において、OAuth認証画面が開けない
    - requests.get(oauth-page-url)が原因
    - 入力に渡したURLとresutlsObj.urlが異なっていた
    - 直にリンクを貼る、リンクを文字列として処理することで解決した
- 