from flask import Flask, request, render_template, send_from_directory
import requests
from bs4 import BeautifulSoup
import os

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/go')
def go():
    target_url = request.args.get('url')
    if not target_url.startswith('http'):
        target_url = 'http://' + target_url

    try:
        response = requests.get(target_url)
        soup = BeautifulSoup(response.text, 'html.parser')

        for tag in soup.find_all(['a', 'img', 'script', 'link']):
            attr = 'href' if tag.name in ['a', 'link'] else 'src'
            if tag.has_attr(attr):
                link = tag[attr]
                if link.startswith('/'):
                    tag[attr] = f"/go?url={target_url.rstrip('/')}{link}"
                elif link.startswith('http'):
                    tag[attr] = f"/go?url={link}"

        return render_template("proxy.html", content=str(soup), url=target_url)

    except Exception as e:
        return f"<p style='color: red;'>Error: {e}</p>"

@app.route('/favicon.ico')
def favicon():
    return send_from_directory(os.path.join(app.root_path, 'static'),
                               'favicon.ico', mimetype='image/vnd.microsoft.icon')

app.run(host='0.0.0.0', port=8080)
