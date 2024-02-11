# Palcord — Palworldサーバー Discordユーティリティ

Do you want to read this in **English**? Check [**here**](README.en.md)!

## 特徴
- Discordで登録していないプレイヤーがサーバーに入った場合に自動で追放 (ホワイトリスト)
- グローバルIPアドレスをDiscordボットのメッセージやチャンネルトピックで通知
- 指定されたテキストチャンネルにコマンドラインを転送 (RCONフォワーディング)
- iniファイルの代わりにYAMLファイルでサーバー設定を記述可能 (YAML→ini変換)
- dllファイルの置き換えなし (MODではありません)

## 要件
- Linux環境のみサポート
- Python 3.8以上
- 以下のライブラリ
  - libffi
  - libnacl
  - python3-dev  
  
  Ubuntuの場合は
  ```shell
  $ apt install libffi-dev libnacl-dev python3-dev
  ```
  でインストールできます．


## 導入方法
### Palworld公式サーバーのインストール
[公式ガイド](https://tech.palworldgame.com/ja/category/getting-started)を参照してください．
以下ではPalworld公式サーバーのインストールと初回起動が終わっている状態を前提とします．

**<--- 開発中 --->**