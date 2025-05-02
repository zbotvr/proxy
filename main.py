from flask import Flask, request, render_template_string
import requests
from bs4 import BeautifulSoup

app = Flask(__name__)

@app.route('/')
def home():
    return '''
    <!DOCTYPE html>
    <html lang="en">
    <head>
        <meta charset="UTF-8">
        <title>DEATH-T0N</title>
        <script src="https://cdn.tailwindcss.com"></script>
        <script>
          tailwind.config = {
            darkMode: 'class'
          }
        </script>
        <style>
            .toggle-dark {
                position: absolute;
                top: 1rem;
                right: 1rem;
            }
        </style>
    </head>
    <body class="bg-gray-950 text-white h-screen flex items-center justify-center transition-colors duration-300" id="body">
        <button class="toggle-dark text-sm bg-gray-700 hover:bg-gray-600 text-white px-3 py-1 rounded" onclick="toggleTheme()">Toggle Theme</button>
        <div id="box" class="bg-gray-950 border border-white p-10 rounded-lg shadow-lg text-center transition-colors duration-300">
            <h1 class="text-3xl font-bold mb-4">DEATH-T0N PR0XY</h1>
            <p class="mb-6 text-gray-400" id="desc">Bored of school? try this! :3</p>
            <form action="/go" method="get" class="flex gap-2 justify-center">
                <input name="url" placeholder="Enter URL (e.g. https://google.com)"
                    class="px-4 py-2 rounded bg-gray-700 text-white w-80 focus:outline-none focus:ring-2 focus:ring-blue-500"
                    required id="input">
                <button type="submit"
                    class="px-4 py-2 bg-blue-600 hover:bg-blue-700 rounded font-semibold">Unblock</button>
            </form>
        </div>
        <script>
            function toggleTheme() {
                const body = document.getElementById('body');
                const box = document.getElementById('box');
                const desc = document.getElementById('desc');
                const input = document.getElementById('input');

                body.classList.toggle('dark');
                const isDark = body.classList.contains('dark');

                body.classList.toggle('bg-white', !isDark);
                body.classList.toggle('text-black', !isDark);
                body.classList.toggle('bg-gray-950', isDark);
                body.classList.toggle('text-white', isDark);

                box.className = isDark
                    ? "bg-gray-950 border border-white p-10 rounded-lg shadow-lg text-center transition-colors duration-300"
                    : "bg-white border border-black p-10 rounded-lg shadow-lg text-center transition-colors duration-300";

                desc.className = isDark ? "mb-6 text-gray-400" : "mb-6 text-gray-600";

                input.className = isDark
                    ? "px-4 py-2 rounded bg-gray-700 text-white w-80 focus:outline-none focus:ring-2 focus:ring-blue-500"
                    : "px-4 py-2 rounded bg-gray-200 text-black w-80 focus:outline-none focus:ring-2 focus:ring-blue-500";
            }
        </script>
    </body>
    </html>
    '''

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

        content = f"""
        <!DOCTYPE html>
        <html lang="en">
        <head>
            <meta charset="UTF-8">
            <title>Browsing: {target_url}</title>
            <script src="https://cdn.tailwindcss.com"></script>
            <script>
              tailwind.config = {{
                darkMode: 'class'
              }};
            </script>
            <style>
                .toggle-dark {{
                    position: absolute;
                    top: 1rem;
                    right: 1rem;
                    z-index: 9999;
                }}
            </style>
        </head>
        <body class="bg-white text-black transition-colors duration-300" id="body">
            <button class="toggle-dark text-sm bg-gray-700 hover:bg-gray-600 text-white px-3 py-1 rounded" onclick="toggleTheme()">Toggle Theme</button>
            {str(soup)}
            <script>
                function toggleTheme() {{
                    const body = document.getElementById('body');
                    body.classList.toggle('dark');
                    const isDark = body.classList.contains('dark');
                    body.classList.toggle('bg-white', !isDark);
                    body.classList.toggle('text-black', !isDark);
                    body.classList.toggle('bg-gray-900', isDark);
                    body.classList.toggle('text-white', isDark);
                }}
            </script>
        </body>
        </html>
        """
        return render_template_string(content)

    except Exception as e:
        return f"<p style='color: red;'>Error: {e}</p>"

app.run(host='0.0.0.0', port=8080)