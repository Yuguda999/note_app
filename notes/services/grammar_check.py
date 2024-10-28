import requests

def check_grammar(text):
    try:
        response = requests.post(
            "https://api.languagetool.org/v2/check",
            data={'text': text, 'language': 'en'},
            timeout=5  # Set a timeout of 5 seconds
        )
        if response.status_code == 200:
            return response.json().get('matches', [])
        return []
    except requests.exceptions.ConnectTimeout:
        return {"error": "Connection to grammar service timed out"}
    except requests.exceptions.RequestException as e:
        return {"error": str(e)}
