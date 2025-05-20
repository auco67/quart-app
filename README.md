# Quart
Pythonで非同期Webアプリケーションを構築するためのフレームワーク。Flaskに似たAPIを提供しつつ、非同期プログラミングをサポートする。高いパフォーマンスとスケーラビリティを実現できる

### 主な特徴
- 非同期：`async/await`構文を使用して非同期処理を行う
- Flask互換：FlaskのAPIに非常に類似し、FlaskからQuartに簡単に移行できる
- WebSocket：WebSocketをネイティブにサポートしリアルタイム通信が可能
- HTTP/2：HTTP/2をサポートしより効率的な通信が可能

### 環境構築
```
pip install quart
```

### 基本使用例

Quartを使用した基本的なWebアプリケーションの例

quart-app.py
```
from quart import Quart, request, jsonify

app = Quart(__name__)

@app.route('/')
async def hello():
    return "Hello, Quart world!"

@app.route('/json', methods=['POST'])
async def json_example():
    data = await request.get_json()
    return jsonify(data)

if __name__ == "__main__":
    app.run()
```

プログラムを実行する
```
python quart_app.py
```

![Image](https://github.com/user-attachments/assets/9a011d30-740d-4649-a0c5-cef75e3bb972)
