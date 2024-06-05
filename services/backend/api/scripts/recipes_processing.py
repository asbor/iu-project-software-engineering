# scripts/recipes_processing.py


from bs4 import BeautifulSoup
import requests
from sqlalchemy.orm import sessionmaker
from sqlalchemy.exc import IntegrityError
from database import engine
from Database.Models import Recipe
from logger_config import get_logger

# Get logger instance


logger = get_logger("RecipeScraper")


def scrape_and_process_recipes():
    logger.info("Scraping data from BYO website")
    base_url = "https://byo.com/"
    search_url = "https://byo.com/?s=&beer-style%5Bamerican-amber-ale%5D=american-amber-ale&post_type=recipe"
    page_to_scrape = requests.get(search_url)
    soup = BeautifulSoup(page_to_scrape.text, "html.parser")
    recipes = soup.findAll("div", class_="recipe-summary")
    recipes_data = []
    for recipe in recipes:
        title = recipe.find("h2").text.strip()
        link = base_url + recipe.find("a")["href"]
        summary = (
            recipe.find("p").text.strip()
            if recipe.find("p")
            else "No summary available"
        )
        recipes_data.append({"title": title, "link": link, "summary": summary})
    if recipes_data:
        logger.info("Storing data in the database")
        store_in_db(recipes_data)
    else:
        logger.warning("No data to store")


def store_in_db(recipes_data):
    SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
    session = SessionLocal()
    for recipe in recipes_data:
        recipe_obj = Recipe(
            title=recipe.get("title"),
            link=recipe.get("link"),
            summary=recipe.get("summary"),
        )
        session.add(recipe_obj)
        try:
            session.commit()
        except IntegrityError:
            session.rollback()
            logger.error(f"IntegrityError for recipe: {recipe}")
    session.close()


def main():
    logger.info("RecipeScraper: Starting the process")
    scrape_and_process_recipes()
    logger.info("RecipeScraper: Process completed")


if __name__ == "__main__":
    main()
