from betamax import Betamax


with Betamax.configure() as config:
    config.cassette_library_dir = 'scraper/tests/fixtures/cassettes'
