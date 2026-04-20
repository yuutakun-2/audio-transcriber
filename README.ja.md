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
 
 以下の手順でローカル環境にセットアップします。
 
1. **リポジトリをクローンする**
   ```bash
   git clone https://github.com/yuutakun-2/audio-transcriber.git
   cd audio-transcriber
   ```

2. **(任意) 仮想環境を作成する**
   依存関係の競合を避けるため、仮想環境の使用を推奨します。
   ```bash
   # Windows
   python -m venv venv
   venv\Scripts\activate

   # macOS/Linux
   python3 -m venv venv
   source venv/bin/activate
   ```

3. **パッケージをインストールする**
   
   **Windows / Linux:**
   ```bash
   pip install .
   ```

   **macOS:**
   faster-whisper を正しくインストールするために `pip3` を使用してください:
   ```bash
   pip3 install .
   ```

## 使い方

ターミナルで以下のコマンドを実行します。
```bash
whisper-cli
```

このツールは対話型で、以下の設定を順に確認します。

### 設定オプションの詳細:
- **Model**: モデルサイズを選択します (`tiny`, `base`, `small`, `medium`, `large`)。モデルが大きいほど精度は上がりますが、処理速度が遅くなり、より多くのメモリを消費します。
- **Language**: 言語を指定します (例: 日本語は `ja`, 英語は `en`)。`auto` を選択すると自動判別します。
- **Device**: `cpu` または `auto` を選択します。対応する NVIDIA GPU (CUDA) をお持ちの場合は、`auto` を選択することで処理速度が大幅に向上します。
- **Compute**: 計算精度の選択 (`int8`, `float16`, `float32`)。一般的な CPU 環境ではデフォルトの `int8` を推奨します。
- **Beam size**: ビームサーチのサイズ (1-5)。値を大きくすると精度がわずかに向上する場合があります。
- **Output format**: 
  1. `TXT with timestamps`: タイムスタンプ付きテキスト `[00:00:10 - 00:00:20] 文字起こし内容`
  2. `TXT only`: テキストのみ。
  3. `SRT`: 字幕ファイル形式。
- **Skip existing**: `y` を選択すると、出力先に既に同名のファイルが存在する場合、そのファイルの処理をスキップします。
- **Input path**: 音声ファイルへのパス、または複数の音声ファイルが含まれるフォルダのパスを入力します (絶対パス・相対パス両方可)。
- **Output folder**: 結果を保存するフォルダを指定します。空欄のままにすると、入力ファイルと同じ場所に保存されます。
- **Save settings**: `y` を選択すると、今回の設定が `~/.whisper-cli/config.json` に保存され、次回実行時のデフォルト値として使用されます。
