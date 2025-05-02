from flask import Flask, request, render_template_string, redirect
import requests
from bs4 import BeautifulSoup

app = Flask(__name__)

BLOCKED_SITES = [
    "pornhub.com", "rule34.xxx", "xvideos.com", "xnxx.com", "redtube.com",
    "youjizz.com", "hentaihaven.xxx", "fapello.com", "efukt.com",
    "spankbang.com", "nhentai.net", "e621.net"
]

@app.route("/", methods=["GET"])
def home():
    return render_template_string('''
    <!DOCTYPE html>
    <html>
    <head>
        <title>Proxy Unblocker</title>
        <style>
            body {
                background-color: var(--bg-color, #1e1e1e);
                color: var(--text-color, white);
                font-family: Arial, sans-serif;
                text-align: center;
                padding: 100px;
            }
            input[type="text"] {
                padding: 10px;
                width: 60%;
                border-radius: 8px;
                border: none;
                font-size: 16px;
                background-color: #f0f0f0;
            }
            button {
                padding: 10px 20px;
                font-size: 16px;
                border: none;
                border-radius: 8px;
                cursor: pointer;
                margin-top: 10px;
            }
            #toggle {
                position: absolute;
                top: 20px;
                right: 20px;
            }
        </style>
    </head>
    <body>
        <div id="toggle">
            <button onclick="toggleMode()">Toggle Mode</button>
        </div>
        <h1>School Proxy</h1>
        <form action="/proxy" method="POST">
            <input type="text" name="url" placeholder="Enter link here" required />
            <br>
            <button type="submit">Go</button>
        </form>

        <script>
            function toggleMode() {
                const root = document.documentElement;
                const dark = getComputedStyle(root).getPropertyValue('--bg-color') === '#1e1e1e';
                if (dark) {
                    root.style.setProperty('--bg-color', '#ffffff');
                    root.style.setProperty('--text-color', '#000000');
                } else {
                    root.style.setProperty('--bg-color', '#1e1e1e');
                    root.style.setProperty('--text-color', '#ffffff');
                }
            }
        </script>
    </body>
    </html>
    ''')

@app.route("/proxy", methods=["POST"])
def proxy():
    url = request.form.get("url")
    if not url:
        return "No URL provided", 400

    # Block bad sites
    for blocked in BLOCKED_SITES:
        if blocked in url.lower():
            return redirect("/blocked")

    try:
        response = requests.get(url)
        soup = BeautifulSoup(response.text, 'html5lib')
        return soup.prettify()
    except Exception as e:
        return f"Error: {str(e)}"

@app.route("/blocked")
def blocked():
    return '''
    <!DOCTYPE html>
    <html>
    <head>
        <title>Blocked</title>
        <style>
            body {
                background-color: #1e1e1e;
                color: white;
                font-family: Arial, sans-serif;
                display: flex;
                justify-content: center;
                align-items: center;
                height: 100vh;
                text-align: center;
            }
            .message {
                font-size: 24px;
                max-width: 600px;
                border: 2px solid #ff0000;
                padding: 20px;
                border-radius: 10px;
                background-color: #2c2c2c;
            }
        </style>
    </head>
    <body>
        <div class="message">
            <p>Find Jesus Christ, buddy…</p>
            <p>*splashes holy water on you*</p>
        </div>
    </body>
    </html>
    '''

if __name__ == "__main__":
    app.run(debug=True)