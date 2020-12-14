from flask import Flask
from flask import render_template

app = Flask(__name__)
runners = {}

@app.route('/')
def main():
    runners_list = sorted(runners.items(), key=lambda x: x[1], reverse=True)
    results = [i[0] for i in runners_list]
    return render_template('base.html', runners=results)

# Should implement password / secret key
@app.route('/update/<runner>/<int:split>', methods=('GET', 'POST'))
def update(runner, split):
    runners[runner] = split
    return

# Can be used for clearing the leaderboard, not safe without secret key / password
'''
@app.route('/clear')
def clear():
    runners.clear()
'''
