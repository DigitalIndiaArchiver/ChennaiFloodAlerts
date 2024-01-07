import requests
import json
import html

def check_flood_alert():
    url = "https://www.chennaifloodsdss.in/HomePage/GetPublishAlert"

    try:
        response = requests.post(url)
        if response.status_code == 200:
            unescaped_response = html.unescape(response.text)
            data = json.loads(json.loads(unescaped_response))

            stored_alerts = []
            try:
                with open('stored_alerts.json', 'r') as file:
                    stored_alerts = json.load(file)
            except FileNotFoundError:
                pass

            new_alerts = [item for item in data if item not in stored_alerts]
            if new_alerts:
                stored_alerts.extend(new_alerts)
                with open('stored_alerts.json', 'w') as file:
                    json.dump(stored_alerts, file, indent=4)
        else:
            print(f"Failed to fetch data. Status code: {response.status_code}")
    except Exception as e:
        print(f"An error occurred: {str(e)}")

if __name__ == "__main__":
    check_flood_alert()
