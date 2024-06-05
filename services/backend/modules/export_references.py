import xml.etree.ElementTree as ET
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from your_models import References

DATABASE_URL = "postgresql://your_user:your_password@db/your_db"
engine = create_engine(DATABASE_URL)
Session = sessionmaker(bind=engine)
session = Session()

def export_references(xml_file):
    references = session.query(References).all()
    root = ET.Element("references")
    for reference in references:
        ref_element = ET.SubElement(root, "reference")
        ET.SubElement(ref_element, "id").text = str(reference.id)
        ET.SubElement(ref_element, "name").text = reference.name
        ET.SubElement(ref_element, "url").text = reference.url
        ET.SubElement(ref_element, "description").text = (
            reference.description or ""
        )
        ET.SubElement(ref_element, "category").text = reference.category or ""
        ET.SubElement(ref_element, "favicon_url").text = (
            reference.favicon_url or ""
        )
        ET.SubElement(ref_element, "created_at").text = (
            reference.created_at.isoformat()
        )
        ET.SubElement(ref_element, "updated_at").text = (
            reference.updated_at.isoformat() if reference.updated_at else ""
        )
    tree = ET.ElementTree(root)
    tree.write(xml_file, encoding="utf-8", xml_declaration=True)

if __name__ == "__main__":
    export_references("references.xml")
