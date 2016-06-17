"""Scrap RSMA data."""
import re

import scrapy


class EcoliLevel(scrapy.Spider):
    """Get data from interactive map."""

    name = 'EcoliQuality'
    start_urls = ['http://www.rsma.qc.ca/rsmaweb/rsmaqrc.asp']

    station_pattern = re.compile('Stations\[\d+\]= new uneSt\((.+)\);')

    columns = ('name', 'type', 'description1', 'description2', 'quality_index',
               'meteo_index', 'ecoli_value', 'temperature', 'date',
               'left_pixel_position', 'top_pixel_position',
               )

    def parse(self, response):
        """Scraping entry point."""
        for match_obj in self.station_pattern.finditer(response.body):
            station_str = match_obj.groups()[0].strip()
            station_data = [val.strip(' "') for val in station_str.split(',')]
            yield dict(zip(self.columns, station_data))
