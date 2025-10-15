from flask import Flask, render_template, request, jsonify
import json, os

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
ROOT_DIR = os.path.abspath(os.path.join(BASE_DIR, ".."))
JSON_PATH = os.path.join(BASE_DIR, "examples.json")

app = Flask(
    __name__,
    template_folder=os.path.join(ROOT_DIR, "templates"),
    static_folder=os.path.join(ROOT_DIR, "static")
)

@app.route('/')
def index():
    try:
        with open(JSON_PATH, 'r', encoding='utf-8') as f:
            data = json.load(f)
    except FileNotFoundError:
        data = {"エラー": {"説明": "examples.json が見つかりません。", "例": ""}}
    return render_template('index.html', topics=data)

@app.route('/run', methods=['POST'])
def run_code():
    lang = request.json.get('lang', 'python')
    code = request.json.get('code', '')
    if lang != 'python':
        return jsonify({'output': f'⚠️ {lang} は現在未対応です。Python のみ実行可能。'})
    try:
        exec_locals = {}
        exec(code, {}, exec_locals)
        result = exec_locals.get('result', '✅ 実行完了')
        return jsonify({'output': str(result)})
    except Exception as e:
        return jsonify({'output': f'⚠️ エラー: {e}'})

if __name__ == '__main__':
    app.run(debug=True)
