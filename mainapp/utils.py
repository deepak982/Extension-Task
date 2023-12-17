from django.conf import settings
from django.core.mail import send_mail
import json
from datetime import datetime
from .models import *

def send_email_token(email,token):
    try:
        subject = 'Your account needs to be verified'
        message = f'Click on the link to verify http://127.0.0.1:8000/verify/{token}/ '
        email_from = settings.EMAIL_HOST_USER
        recipient_list = [email, ]
        send_mail( subject, message, email_from, recipient_list )
    except Exception as e :
        return False
    
    return True


def import_data():
    json_file_path = 'mainapp/jsondata.json'

    # Specify the encoding as 'utf-8'
    with open(json_file_path, 'r', encoding='utf-8') as file:
        json_data = json.load(file)

    for item in json_data:
        # Convert blank strings to None for integer fields
        end_year = int(item["end_year"]) if item["end_year"] else None
        start_year = int(item["start_year"]) if item["start_year"] else None
        impact = int(item["impact"]) if item["impact"] else None
        relevance = int(item["relevance"]) if item["relevance"] else None
        likelihood = int(item["likelihood"]) if item["likelihood"] else None

        # Handle empty strings for date fields
        added_date_str = item["added"]
        published_date_str = item["published"]

        added_date = datetime.strptime(added_date_str, "%B, %d %Y %H:%M:%S") if added_date_str else None
        published_date = datetime.strptime(published_date_str, "%B, %d %Y %H:%M:%S") if published_date_str else None

        # Handle empty strings for the intensity field
        intensity_str = str(item["intensity"])
        intensity = int(intensity_str) if intensity_str and intensity_str.isdigit() else None

        # Set a default value for published if it's None
        published_date = published_date or datetime.now()

        # Create a Django model instance only if intensity is not None
        if intensity is not None:
            instance = data(
                end_year=end_year,
                intensity=intensity,
                sector=item["sector"],
                topic=item["topic"],
                insight=item["insight"],
                url=item["url"],
                region=item["region"],
                start_year=start_year,
                impact=impact,
                added=added_date,
                published=published_date,
                country=item["country"],
                relevance=relevance,
                pestle=item["pestle"],
                source=item["source"],
                title=item["title"],
                likelihood=likelihood
            )
            instance.save()

# Call the import_data function when the script is run directly
if __name__ == "__main__":
    import_data()
