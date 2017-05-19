from flask import abort, Flask

from parser import nhl_news, team_news, VALID_TEAMS

application = Flask(__name__)


@application.route("/")
def serve_about():
    abort(404)


@application.route('/nhl/')
def server_nhl():
    return nhl_news()


@application.route('/<team>/')
def serve_team(team):
    if team not in VALID_TEAMS:
        abort(404)

    return team_news(team)


if __name__ == "__main__":
    application.run()
