import xml.etree.ElementTree as ET
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from your_models import References

DATABASE_URL = "postgresql://your_user:your_password@db/your_db"
engine = create_engine(DATABASE_URL)
Session = sessionmaker(bind=engine)
session = Session()


def import_references(xml_file):
    tree = ET.parse(xml_file)
    root = tree.getroot()
    for ref_element in root.findall("reference"):
        reference = References(
            name=ref_element.find("name").text,
            url=ref_element.find("url").text,
            description=ref_element.find("description").text,
            category=ref_element.find("category").text,
            favicon_url=ref_element.find("favicon_url").text,
        )
        session.add(reference)
    session.commit()


if __name__ == "__main__":
    import_references("references.xml")
