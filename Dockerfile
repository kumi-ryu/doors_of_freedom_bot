FROM python:3.8

# 必要なライブラリをインストール
RUN pip install discord

# ソースをコンテナ内にコピー
COPY ./src/ ./src/

# 作業フォルダを設定しコマンド実行
WORKDIR ./src/
CMD ["python", "omaraid.py"]