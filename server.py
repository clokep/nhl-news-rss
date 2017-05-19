from flask import abort, Flask

from jinja2 import Template

from parser import nhl_news, team_news, VALID_TEAMS

application = Flask(__name__)


@application.route("/")
def serve_about():
    template = Template(
'''<html>
<body>
<h2><a href="/nhl/">NHL Headlines</a></h2>

<ul>
{% for short, name in teams %}
<li><a href="/{{ short }}/">{{ name }}</a></li>
{% endfor %}
</ul>

</body>
</html>''')

    return template.render(teams=VALID_TEAMS.items())


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
