from flask import Flask, jsonify, request
import estrutura_interesses as i

app = Flask(__name__)
app.url_map.strict_slashes = False













if __name__ == '__main__':
    app.run(host='localhost', port=5003, debug=True)
