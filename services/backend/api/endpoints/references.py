# api/endpoints/references.py

from bs4 import BeautifulSoup
from urllib.parse import urlparse, urljoin
from fastapi import APIRouter, HTTPException, Depends, UploadFile, File
from sqlalchemy.orm import Session
from database import get_db
import Database.Models as models
import Database.Schemas as schemas
from typing import List
import xml.etree.ElementTree as ET
from fastapi.responses import StreamingResponse
import io
import requests

router = APIRouter()

# References Endpoints


@router.post("/references/import", response_model=dict)
async def import_references(
    db: Session = Depends(get_db), file: UploadFile = File(...)
):
    contents = await file.read()
    tree = ET.ElementTree(ET.fromstring(contents))
    root = tree.getroot()

    for ref_element in root.findall("reference"):
        name = ref_element.find("name").text
        url = ref_element.find("url").text
        description = ref_element.find("description").text
        category = ref_element.find("category").text
        favicon_url = fetch_favicon(url)

        reference = models.References(
            name=name,
            url=url,
            description=description,
            category=category,
            favicon_url=favicon_url,
        )
        db.add(reference)

    db.commit()
    return {"message": "References imported successfully"}


@router.get("/references/export")
async def export_references(db: Session = Depends(get_db)):
    references = db.query(models.References).all()
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
    xml_io = io.BytesIO()
    tree.write(xml_io, encoding="utf-8", xml_declaration=True)
    xml_io.seek(0)

    return StreamingResponse(
        xml_io,
        media_type="application/xml",
        headers={"Content-Disposition": "attachment; filename=references.xml"},
    )


@router.get("/references", response_model=List[schemas.Reference])
async def get_all_references(db: Session = Depends(get_db)):
    references = db.query(models.References).all()
    return references


@router.get("/references/{reference_id}", response_model=schemas.Reference)
async def get_reference(reference_id: int, db: Session = Depends(get_db)):
    reference = (
        db.query(models.References)
        .filter(models.References.id == reference_id)
        .first()
    )
    if not reference:
        raise HTTPException(status_code=404, detail="Reference not found")
    return reference


@router.post("/references", response_model=schemas.Reference)
async def create_reference(
    reference: schemas.ReferenceCreate, db: Session = Depends(get_db)
):
    favicon_url = fetch_favicon(reference.url)
    db_reference = models.References(
        **reference.dict(), favicon_url=favicon_url
    )
    db.add(db_reference)
    db.commit()
    db.refresh(db_reference)
    return db_reference


@router.delete("/references/{reference_id}", response_model=schemas.Reference)
async def delete_reference(reference_id: int, db: Session = Depends(get_db)):
    reference = (
        db.query(models.References)
        .filter(models.References.id == reference_id)
        .first()
    )
    if not reference:
        raise HTTPException(status_code=404, detail="Reference not found")
    db.delete(reference)
    db.commit()
    return reference


@router.put("/references/{reference_id}", response_model=schemas.Reference)
async def update_reference(
    reference_id: int,
    reference: schemas.ReferenceUpdate,
    db: Session = Depends(get_db),
):
    db_reference = (
        db.query(models.References)
        .filter(models.References.id == reference_id)
        .first()
    )
    if not db_reference:
        raise HTTPException(status_code=404, detail="Reference not found")
    for key, value in reference.dict().items():
        setattr(db_reference, key, value)
    db.commit()
    db.refresh(db_reference)
    return db_reference


# Helper function to fetch favicon URL
def fetch_favicon(url: str) -> str:
    parsed_url = urlparse(url)
    base_url = f"{parsed_url.scheme}://{parsed_url.netloc}"

    # Try common paths
    common_paths = ["/favicon.ico", "/favicon.png", "/favicon.svg"]
    for path in common_paths:
        favicon_url = urljoin(base_url, path)
        response = requests.head(favicon_url)
        if response.status_code == 200:
            return favicon_url

    # Try parsing the HTML for <link> tags
    try:
        response = requests.get(base_url)
        soup = BeautifulSoup(response.content, "html.parser")
        link_tags = soup.find_all(
            "link",
            rel=[
                "icon",
                "shortcut icon",
                "apple-touch-icon",
                "apple-touch-icon-precomposed",
            ],
        )
        for link in link_tags:
            href = link.get("href")
            if href:
                favicon_url = urljoin(base_url, href)
                response = requests.head(favicon_url)
                if response.status_code == 200:
                    return favicon_url
    except Exception as e:
        print(f"Error parsing HTML for {url}: {e}")

    # Fallback to Google's favicon service
    google_favicon_url = (
        f"http://www.google.com/s2/favicons?domain={parsed_url.netloc}"
    )
    return google_favicon_url
