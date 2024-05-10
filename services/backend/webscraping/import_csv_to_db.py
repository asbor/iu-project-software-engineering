import csv
from sqlalchemy.orm import sessionmaker
# Import the Style class and engine from your module
from ..setup import engine
from ..database.models import Style


# Create a session maker using the engine from your setup file
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# Open the CSV file
with open('your_csv_file.csv', 'r') as file:
    reader = csv.DictReader(file)
    for row in reader:
        # Create a new Style object and set its attributes from the CSV data
        style = Style(
            name=row['name'],
            category=row['category'],
            color=row['color'],
            clarity=row['clarity'],
            perceived_malt_and_aroma=row['perceived_malt_and_aroma'],
            perceived_hop_and_aroma=row['perceived_hop_and_aroma'],
            perceived_bitterness=row['perceived_bitterness'],
            fermentation_characteristics=row['fermentation_characteristics'],
            body=row['body'],
            additional_notes=row['additional_notes'],
            og=row['og'],
            fg=row['fg'],
            abv=row['abv'],
            ibu=row['ibu'],
            ebc=row['ebc'],
            og_min=row['og_min'],
            og_max=row['og_max'],
            fg_min=row['fg_min'],
            fg_max=row['fg_max'],
            ibu_min=row['ibu_min'],
            ibu_max=row['ibu_max'],
            ebc_min=row['ebc_min'],
            ebc_max=row['ebc_max']
        )
        # Create a new session
        session = SessionLocal()
        # Add the Style object to the session
        session.add(style)
        # Commit the changes to the database
        session.commit()
        # Close the session
        session.close()
