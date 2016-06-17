import unittest

import mock
from betamax import Betamax
from requests import Session


class TestEcoliLevelSimple(unittest.TestCase):

    def _get_scraper(self):
        from scraper.rsma import EcoliLevel
        return EcoliLevel()

    def _get_response(self, body=None):
        from scrapy.http import Response
        return mock.Mock(spec=Response, body=body)

    def test_parse_none(self):
        scraper = self._get_scraper()
        scraper.parse(self._get_response())


class TestEcoliLevelReal(TestEcoliLevelSimple):

    def setUp(self):
        self.session = Session()

    def test_parse(self):
        scraper = self._get_scraper()
        rsma_url = scraper.start_urls[0]

        with Betamax(self.session) as vcr:
            vcr.use_cassette('rsma')
            resp = self.session.get(rsma_url)

        result = [r for r in scraper.parse(self._get_response(resp.content))]

        self.assertEqual(153, len(result))
