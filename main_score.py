from flask import Flask
import utils
import os

app = Flask(__name__)

@app.route("/")
def score_server():
    try:
        if os.path.exists(utils.scores_file_name):
            with open(utils.scores_file_name, 'r') as file:
                score = int(file.readline())
                return f"""<html>
                                <head>
                                    <title>Score Game</title>
                                </head>
                                <body>
                                    <h1>The score is:</h1>
                                    <div id="score">{score}</div>
                                </body>
                            </html>"""
        else:
            return f"""<html>
                            <head>
                                <title>Score Game</title>
                            </head>
                            <body>
                                <h1>ERROR</h1>
                                <div id="score" style="color:red;">{utils.bad_return_code}</div>
                            </body>
                        </html>"""
    except (FileNotFoundError, ValueError):
        return f"""<html>
                        <head>
                            <title>Score Game</title>
                        </head>
                        <body>
                            <h1>ERROR</h1>
                            <div id="score" style="color:red;">{utils.bad_return_code}</div>
                        </body>
                    </html>"""

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)