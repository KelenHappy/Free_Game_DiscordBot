import json
import requests
from firebase_admin import db, credentials
import firebase_admin

# Initialize Firebase
if not firebase_admin._apps:
    cred = credentials.Certificate("serviceAccountKey.json")  # You need to create this in Firebase.
    firebase_admin.initialize_app(cred, {
        'databaseURL': 'your firebase url'
    })

def getUrl(url):
    try:
        ref = db.reference('/')
        last_url = ref.get().get('data') if ref.get() else None

        # Make a GET request to the provided URL
        response = requests.get(url)
        response.raise_for_status()  # Raise an error for bad responses (4xx and 5xx)
        data = response.json()  # Parse the JSON response

        # Extract URLs from the response
        results = data.get("data", {}).get("results", [])
        new_urls = [item["canonicalUrl"] for item in results if "canonicalUrl" in item]

        # Check if any new URLs were found
        if not new_urls:
            print("No new URLs found.")
            return []

        answer_back = []
        if last_url:
            # Collect new URLs until the last known URL is reached
            for url in new_urls:
                if url == last_url:
                    break
                answer_back.append(url)
        else:
            # If no last URL is found, return the first new URL
            answer_back = [new_urls[0]]  

        # Update the last URL in the database if new URLs were found
        if answer_back:
            ref.update({'data': new_urls[0]})

        return answer_back

    except requests.exceptions.RequestException as e:
        print(f"REQUEST ERROR: {e}")
        return []
    except json.JSONDecodeError as e:
        print(f"JSON ERROR: {e}")
        return []
    except Exception as e:
        print(f"UNKNOWN ERROR: {e}")
        return []
