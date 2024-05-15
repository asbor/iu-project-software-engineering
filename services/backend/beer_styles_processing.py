import re
from bs4 import BeautifulSoup
import requests
import csv
from sqlalchemy.orm import sessionmaker
from sqlalchemy.exc import IntegrityError
from database import engine
from Database.Models import Style
from logger_config import get_logger

# Get logger instance
logger = get_logger('WebScraper')


class CsvFile:
    def __init__(self, filename):
        self.filename = filename

    def exists(self):
        try:
            with open(self.filename, 'r') as file:
                return True
        except FileNotFoundError:
            return False


def scrape_beer_styles(csv_filename):
    csv_file = CsvFile(csv_filename)

    if csv_file.exists():
        print('CSV file already exists')
    else:
        print('Scraping data from Brewers Association website')
        # Scrape the data
        page_to_scrape = requests.get(
            'https://www.brewersassociation.org/resources/brewers-association-beer-style-guidelines/')
        soup = BeautifulSoup(page_to_scrape.text, 'html.parser')

        beer_styles = soup.findAll('div', attrs={'class': 'beer-style'})

        with open(csv_filename, 'w') as file:
            writer = csv.writer(file)

            for beer_style in beer_styles:
                print(beer_style.text)
                writer.writerow([beer_style.text])


def extract_features(input_csv, output_csv):
    with open(input_csv, 'r') as file:
        with open(output_csv, 'w') as outfile:
            writer = csv.writer(outfile)
            writer.writerow(['Feature', 'value'])

            reader = csv.reader(file)
            for row in reader:
                entry = ' '.join(row)
                entry = entry.replace('\n\n\n', '\n\n')
                entry = entry.replace('\n\n', '\n')
                entry = entry.replace(':\n', ': ')
                entry = entry.replace(':\t', '')
                match = re.search(
                    r'^\n([a-zA-Zéüöêåøè\s\&\-\\/0-9.,!?]+)\n', entry)
                category_name = match.group(1) if match else None
                writer.writerow(['Category', category_name])
                lines = entry.split('\n')
                for line in lines:
                    parts = re.split(r':\s', line, 1)
                    if len(parts) == 2:
                        column = parts[0].strip()
                        value = parts[1].strip()
                        writer.writerow([column, value])
                    else:
                        if any(key in line for key in ["Original Gravity (°Plato)", "Apparent Extract/Final Gravity", "Alcohol by Weight (Volume)", "Bitterness (IBU)", "Color SRM (EBC)"]):
                            column = line.split(') ')[0].strip() + ')'
                            value = line.split(') ')[1].strip()
                            writer.writerow([column, value])


def pivot_csv(input_file, output_file):
    pivoted_data = {}

    with open(input_file, 'r') as file:
        reader = csv.DictReader(file)
        for row in reader:
            feature = row['Feature']
            value = row['value']

            if feature in pivoted_data:
                pivoted_data[feature].append(value)
            else:
                pivoted_data[feature] = [value]

    with open(output_file, 'w', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(['Id'] + list(pivoted_data.keys()))

        max_values = max(len(values) for values in pivoted_data.values())

        for i in range(max_values):
            row_values = []
            for feature_values in pivoted_data.values():
                if i < len(feature_values):
                    row_values.append(feature_values[i])
                else:
                    row_values.append('')
            writer.writerow([i+1] + row_values)


def import_csv_to_db(input_csv):
    SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

    with open(input_csv, 'r') as file:
        reader = csv.DictReader(file)
        session = SessionLocal()
        for row in reader:
            style = Style(
                id=row['Id'],
                category=row['Category'],
                color=row['Color'],
                clarity=row['Clarity'],
                perceived_malt_and_aroma=row['Perceived Malt Aroma & Flavor'],
                perceived_hop_and_aroma=row['Perceived Hop Aroma & Flavor'],
                perceived_bitterness=row['Perceived Bitterness'],
                fermentation_characteristics=row['Fermentation Characteristics'],
                body=row['Body'],
                additional_notes=row['Additional notes'],
                og=row['Original Gravity (°Plato)'],
                fg=row['Apparent Extract/Final Gravity (°Plato)'],
                abv=row['Alcohol by Weight (Volume)'],
                ibu=row['Bitterness (IBU)'],
                ebc=row['Color SRM (EBC)']
            )

            session.add(style)
            try:
                session.commit()
            except IntegrityError:
                session.rollback()
        session.close()


def main():
    logger.info(
        "WebScraper: Scraping beer styles from Brewers Association website")
    csv_filename = 'beer_styles.csv'
    scrape_beer_styles(csv_filename)

    logger.info("WebScraper: Data cleaning and feature extraction")
    input_csv = 'beer_styles.csv'
    intermediate_csv = 'beer_styles_features.csv'
    extract_features(input_csv, intermediate_csv)

    logger.info("WebScraper: Pivoting the data")
    input_features_csv = 'beer_styles_features.csv'
    output_csv = 'output.csv'
    pivot_csv(input_features_csv, output_csv)

    logger.info("WebScraper: Importing the data to the database")
    import_csv_to_db(output_csv)


if __name__ == "__main__":
    main()
