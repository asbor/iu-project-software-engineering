# tests/test_beer_styles_processing.py

import unittest
from unittest.mock import patch, MagicMock
from bs4 import BeautifulSoup
import requests
from api.scripts.beer_styles_processing import scrape_and_process_beer_styles, parse_beer_style, store_in_db


class TestBeerStylesProcessing(unittest.TestCase):

    @patch('requests.get')
    @patch('scripts.beer_styles_processing.store_in_db')
    def test_scrape_and_process_beer_styles(self, mock_store_in_db, mock_requests_get):
        # Mock the HTML content returned by requests.get
        mock_html_content = """
        <section id="beer-styles">
            <div class="beer-style-group">
                <h2 class="origin">Origin Heading<img src="circle_image.png"></h2>
                <div class="beer-style">
                    <li>Beer Style Name</li>
                    <li><strong>Color:</strong> Light</li>
                    <li><strong>Clarity:</strong> Clear</li>
                    <li><strong>Perceived Malt Aroma &amp; Flavor:</strong> Malty</li>
                    <li><strong>Perceived Hop Aroma &amp; Flavor:</strong> Hoppy</li>
                    <li><strong>Perceived Bitterness:</strong> Low</li>
                    <li><strong>Fermentation Characteristics:</strong> Fruity</li>
                    <li><strong>Body:</strong> Medium</li>
                    <li><strong>Additional Notes:</strong> Notes</li>
                </div>
            </div>
        </section>
        """
        mock_requests_get.return_value.text = mock_html_content

        scrape_and_process_beer_styles()

        mock_store_in_db.assert_called_once()
        styles_data = mock_store_in_db.call_args[0][0]
        self.assertEqual(len(styles_data), 1)
        self.assertEqual(styles_data[0]['category'], 'Beer Style Name')
        self.assertEqual(styles_data[0]['color'], 'Light')

    def test_parse_beer_style(self):
        # Mock the BeautifulSoup object for a beer style
        beer_style_html = """
        <div class="beer-style">
            <li>Beer Style Name</li>
            <li><strong>Color:</strong> Light</li>
            <li><strong>Clarity:</strong> Clear</li>
            <li><strong>Perceived Malt Aroma &amp; Flavor:</strong> Malty</li>
            <li><strong>Perceived Hop Aroma &amp; Flavor:</strong> Hoppy</li>
            <li><strong>Perceived Bitterness:</strong> Low</li>
            <li><strong>Fermentation Characteristics:</strong> Fruity</li>
            <li><strong>Body:</strong> Medium</li>
            <li><strong>Additional Notes:</strong> Notes</li>
        </div>
        """
        soup = BeautifulSoup(beer_style_html, 'html.parser')
        beer_style = soup.find('div', class_='beer-style')

        style_data = parse_beer_style(beer_style)

        self.assertEqual(style_data['category'], 'Beer Style Name')
        self.assertEqual(style_data['color'], 'Light')
        self.assertEqual(style_data['clarity'], 'Clear')
        self.assertEqual(style_data['perceived_malt_aroma_&_flavor'], 'Malty')
        self.assertEqual(style_data['perceived_hop_aroma_&_flavor'], 'Hoppy')
        self.assertEqual(style_data['perceived_bitterness'], 'Low')
        self.assertEqual(style_data['fermentation_characteristics'], 'Fruity')
        self.assertEqual(style_data['body'], 'Medium')
        self.assertEqual(style_data['additional_notes'], 'Notes')

    @patch('scripts.beer_styles_processing.sessionmaker')
    def test_store_in_db(self, mock_sessionmaker):
        # Mock the session and engine
        mock_session = MagicMock()
        mock_sessionmaker.return_value = mock_session

        styles_data = [
            {
                'category': 'Beer Style Name',
                'color': 'Light',
                'clarity': 'Clear',
                'perceived_malt_aroma_&_flavor': 'Malty',
                'perceived_hop_aroma_&_flavor': 'Hoppy',
                'perceived_bitterness': 'Low',
                'fermentation_characteristics': 'Fruity',
                'body': 'Medium',
                'additional_notes': 'Notes',
                'og': '1.050',
                'fg': '1.010',
                'abv': '5%',
                'ibu': '20',
                'ebc': '10',
                'block_heading': 'Origin Heading',
                'circle_image': 'circle_image.png'
            }
        ]

        store_in_db(styles_data)

        mock_session.return_value.add.assert_called_once()
        mock_session.return_value.commit.assert_called_once()
        added_style = mock_session.return_value.add.call_args[0][0]
        self.assertEqual(added_style.category, 'Beer Style Name')
        self.assertEqual(added_style.color, 'Light')


if __name__ == '__main__':
    unittest.main()
