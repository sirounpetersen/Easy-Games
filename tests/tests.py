import unittest
import sys
from flask import request, render_template
from api import search, platform_games
from main import app, cleanhtml
sys.path.append('../Easy-Games')  # imports python file from parent directory


class BasicTests(unittest.TestCase):

    # executed prior to each test
    def setUp(self):
        self.app = app.test_client()

    def test_about_page(self):  # Checks if the page opens functionally
        response = self.app.get('/about', follow_redirects=True)
        self.assertEqual(response.status_code, 200)

    def test_anticipated_page(self):  # Checks if the page opens functionally
        response = self.app.get('/anticipated', follow_redirects=True)
        self.assertEqual(response.status_code, 200)

    def test_home_page(self):  # Checks if the page opens functionally
        response = self.app.get('/', follow_redirects=True)
        self.assertEqual(response.status_code, 200)

    def test_platform_page(self):  # Checks if the page opens functionally
        response = self.app.get('/platform', follow_redirects=True)
        self.assertEqual(response.status_code, 200)

    def test_platformGames_page(self):  # Checks if the page ouputs PC
        platformName = "PC"
        games = platform_games(platformName)
        response = self.app.post('/platformGames',
                                 data=dict(console=platformName, games=games))
        self.assertEqual(response.status_code, 200)

    def test_search_page(self):  # Checks if the page outputs valorant
        name = "valorant"
        detail, image, rate, platform, platformRate, website = search(name)
        response = self.app.post("/search",
                                 data=dict(name=name.upper(),
                                           detail=cleanhtml(detail),
                                           image=image, rate=rate,
                                           website=website,
                                           both=zip(platform, platformRate)))
        self.assertEqual(response.status_code, 200)

    def test_trending_page(self):  # Checks if the page opens functionally
        response = self.app.get('/trending', follow_redirects=True)
        self.assertEqual(response.status_code, 200)


if __name__ == "__main__":
    unittest.main()
