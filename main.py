from flask import Flask, request, render_template_string, send_from_directory
import requests
from bs4 import BeautifulSoup

app = Flask(__name__)

@app.route('/favicon.ico')
def favicon():
    return send_from_directory('static', 'favicon.ico')

@app.route('/')
def home():
    return '''
    <!DOCTYPE html>
    <html lang="en">
    <head>
        <meta charset="UTF-8">
        <title>DEATH-T0N</title>
        <link rel="icon" type="image/x-icon" href="/favicon.ico">
        <link href="https://fonts.googleapis.com/css2?family=Special+Elite&display=swap" rel="stylesheet">
        <script src="https://cdn.tailwindcss.com"></script>
        <style>
            .toggle-dark {
                position: absolute;
                top: 1rem;
                right: 1rem;
            }
            .typewriter {
                font-family: 'Special Elite', monospace;
            }
        </style>
    </head>
    <body class="bg-black text-white h-screen flex items-center justify-center transition-colors duration-300" id="body">
        <button class="toggle-dark text-sm bg-gray-700 hover:bg-gray-600 text-white px-3 py-1 rounded" onclick="toggleTheme()">Toggle Theme</button>
        <div id="box" class="bg-black p-10 rounded-lg border border-white shadow-lg text-center transition-colors duration-300">
            <h1 class="text-3xl typewriter mb-4">DEATH-T0N PR0XY</h1>
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

                body.classList.toggle('bg-white');
                body.classList.toggle('text-black');
                body.classList.toggle('bg-black');
                body.classList.toggle('text-white');

                box.className = body.classList.contains('bg-white')
                    ? "bg-white p-10 rounded-lg border border-white shadow-lg text-center transition-colors duration-300"
                    : "bg-black p-10 rounded-lg border border-white shadow-lg text-center transition-colors duration-300";

                desc.className = body.classList.contains('bg-white') ? "mb-6 text-gray-600" : "mb-6 text-gray-400";

                input.className = body.classList.contains('bg-white')
                    ? "px-4 py-2 rounded bg-gray-200 text-black w-80 focus:outline-none focus:ring-2 focus:ring-blue-500"
                    : "px-4 py-2 rounded bg-gray-700 text-white w-80 focus:outline-none focus:ring-2 focus:ring-blue-500";
            }
        </script>
    </body>
    </html>
    '''
