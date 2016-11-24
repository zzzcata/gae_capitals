#!/usr/bin/env python
import os
import jinja2
import webapp2
from capital import Capital
from random import randint


template_dir = os.path.join(os.path.dirname(__file__), "templates")
jinja_env = jinja2.Environment(loader=jinja2.FileSystemLoader(template_dir), autoescape=False)


class BaseHandler(webapp2.RequestHandler):

    def write(self, *a, **kw):
        return self.response.out.write(*a, **kw)

    def render_str(self, template, **params):
        t = jinja_env.get_template(template)
        return t.render(params)

    def render(self, template, **kw):
        return self.write(self.render_str(template, **kw))

    def render_template(self, view_filename, params=None):
        if not params:
            params = {}
        template = jinja_env.get_template(view_filename)
        return self.response.out.write(template.render(params))

rome_pictures = [
    "http://www.airtransat.com/getmedia/22463e82-447c-49b0-bb98-997284fc3675/Rome03.jpg",
    "http://www.telegraph.co.uk/content/dam/Travel/Destinations/Europe/Italy/Rome/rome-colosseum_-large.jpg",
    "http://reidsitaly.com/images/lazio/rome/sights/colosseum-thumb.jpg"
    ]

vienna_pictures = [
    "http://ringview.vienna.info/ressources/streetview/images/ViennaRingView.jpg",
    "http://www.easyjet.com/en/holidays/shared/images/guides/austria/vienna.jpg",
    "http://airpano.ru/files/Vienna-Austria/images/image4.jpg"
]


paris_pictures = [
    "https://media-cdn.tripadvisor.com/media/photo-s/06/e5/55/c5/champs-elysees.jpg",
    "http://wikitravel.org/upload/shared//6/6f/Paris_Banner.jpg",
    "http://www.telegraph.co.uk/content/dam/Travel/leadAssets/35/02/france-hub_3502656a-xlarge.jpg"
]

vienna = Capital("Vienna", vienna_pictures)
rome = Capital("Rome", rome_pictures)
paris = Capital("Paris", paris_pictures)
capitals = [vienna, rome, paris]


class MainHandler(BaseHandler):
    def get(self):
        ri = randint(0, len(capitals)-1)
        params = {"capital": capitals[ri], "capital_index": ri}

        return self.render_template("hello.html", params=params)

    def post(self):
        guessed_capital_name = self.request.get("guessed_city")
        capital_index = int(self.request.get("capital_index"))
        the_correct_capital = capitals[capital_index]
        is_correct = the_correct_capital.guess(guessed_capital_name)
        params = {"the_answer": is_correct}
        return self.render_template("hello.html", params=params)


app = webapp2.WSGIApplication([
    webapp2.Route('/', MainHandler),
], debug=True)

