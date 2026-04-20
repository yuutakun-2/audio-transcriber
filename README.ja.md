# whisper-cli

faster-whisper を使用したローカル音声文字起こし CLI ツールです。

## 特徴
- 完全オフラインでの音声認識
- 日本語を含む多言語対応
- TXT / SRT 出力対応
- タイムスタンプ対応
- 初心者でも使いやすい CLI

## 前提条件

インストール前に、Python と pip がシステムにインストールされていることを確認してください。

### Python と pip のインストール方法

- **Windows**: [公式 Python サイト](https://www.python.org/downloads/windows/) からインストーラーをダウンロードして実行してください。インストール時に **「Add Python to PATH」** にチェックを入れてください。
- **macOS**: Python3 と pip3 は通常プリインストールされていますが、[Homebrew](https://brew.sh/) を使用してインストールすることもできます: `brew install python`
- **Linux**: ディストリビューションのパッケージマネージャを使用してください。
  - Ubuntu/Debian: `sudo apt update && sudo apt install python3 python3-pip`
  - Fedora: `sudo dnf install python3 python3-pip`

## インストール

リポジトリをクローンしてインストールを実行します。

**Windows / Linux:**
```bash
pip install .
```

macOS:
faster-whisper を正しくインストールするために pip3 を使用してください:

```bash
pip3 install .
```

使い方

ターミナルで以下を実行します:

```bash
whisper-cli
```
