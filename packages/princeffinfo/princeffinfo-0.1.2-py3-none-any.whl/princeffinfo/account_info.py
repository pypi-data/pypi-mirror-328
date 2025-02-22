import requests

def input(account_id, region):
    url = f"https://teamxdarks-api.vercel.app/profile_info?uid={account_id}&region={region}&key=teamXKrishna"
    response = requests.get(url)
    
    if response.status_code == 200:
        return response.json()
    else:
        return {"error": "Failed to fetch data"}