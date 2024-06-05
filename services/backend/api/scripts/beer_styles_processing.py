# scripts/beer_styles_processing.py



from bs4 import BeautifulSoup

import requests

from sqlalchemy.orm import sessionmaker

from sqlalchemy.exc import IntegrityError

from database import engine

from Database.Models import StyleGuidelines

from logger_config import get_logger



# Get logger instance

logger = get_logger("WebScraper")





def scrape_and_process_beer_styles():

    logger.info("Scraping data from Brewers Association website")

    page_to_scrape = requests.get(

        "https://www.brewersassociation.org/resources/brewers-association-beer-style-guidelines/"

    )

    soup = BeautifulSoup(page_to_scrape.text, "html.parser")



    beer_styles_section = soup.find("section", id="beer-styles")

    beer_style_groups = beer_styles_section.findAll(

        "div", class_="beer-style-group"

    )

    styles_data = []



    for beer_style_group in beer_style_groups:

        block_heading = "Unknown"

        circle_image = None



        for element in beer_style_group.children:

            if element.name == "h2" and "origin" in element.get("class", []):

                origin_heading = element

                block_heading = origin_heading.text.strip()

                circle_image = (

                    origin_heading.find("img")["src"]

                    if origin_heading.find("img")

                    else None

                )

            elif element.name == "div" and "beer-style" in element.get(

                "class", []

            ):

                style_data = parse_beer_style(element)

                if style_data:

                    style_data["block_heading"] = block_heading

                    style_data["circle_image"] = circle_image

                    styles_data.append(style_data)



    if styles_data:

        logger.info("Storing data in the database")

        store_in_db(styles_data)

    else:

        logger.warning("No data to store")





def parse_beer_style(beer_style):

    style_data = {}



    # Extract the name of the beer style

    style_name_tag = beer_style.find("li")

    if style_name_tag:

        style_data["category"] = style_name_tag.text.strip()



    # Extract other attributes

    details = beer_style.findAll("li")

    for detail in details[1:]:  # Skip the first item since it's the name

        strong_tag = detail.find("strong")

        if strong_tag:

            key = (

                strong_tag.text.strip()

                .replace(":", "")

                .replace(" ", "_")

                .lower()

            )

            value = (

                strong_tag.next_sibling.strip()

                if strong_tag.next_sibling

                else ""

            )

            style_data[key] = value



    # Extract horizontal details

    horizontal_details = beer_style.find("ul", class_="horizontal wider")

    if horizontal_details:

        horizontal_items = horizontal_details.findAll("li")

        for item in horizontal_items:

            strong_tag = item.find("strong")

            if strong_tag:

                key = (

                    strong_tag.text.strip()

                    .replace(":", "")

                    .replace(" ", "_")

                    .lower()

                )

                value = (

                    strong_tag.next_sibling.strip()

                    if strong_tag.next_sibling

                    else ""

                )

                style_data[key] = value



    return style_data





def store_in_db(styles_data):

    SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

    session = SessionLocal()



    for style in styles_data:

        style_obj = StyleGuidelines(

            category=style.get("category"),

            color=style.get("color"),

            clarity=style.get("clarity"),

            perceived_malt_and_aroma=style.get(

                "perceived_malt_aroma_&_flavor"

            ),

            perceived_hop_and_aroma=style.get("perceived_hop_aroma_&_flavor"),

            perceived_bitterness=style.get("perceived_bitterness"),

            fermentation_characteristics=style.get(

                "fermentation_characteristics"

            ),

            body=style.get("body"),

            additional_notes=style.get("additional_notes"),

            og=style.get("original_gravity_(°plato)"),

            fg=style.get("apparent_extract/final_gravity_(°plato)"),

            abv=style.get("alcohol_by_weight_(volume)"),

            ibu=style.get("bitterness_(ibu)"),

            ebc=style.get("color_srm_(ebc)"),

            block_heading=style.get("block_heading"),

            circle_image=style.get("circle_image"),

        )



        session.add(style_obj)

        try:

            session.commit()

        except IntegrityError:

            session.rollback()

            logger.error(f"IntegrityError for style: {style}")



    session.close()





def main():

    logger.info("WebScraper: Starting the process")

    scrape_and_process_beer_styles()

    logger.info("WebScraper: Process completed")
