import re
import requests
from typing import Dict, List, Union
import asyncio


def preprocess_text(text, make_lower=True) -> str:
    # Remove extra spaces
    text = re.sub(r"\s+", " ", text)
    if make_lower:
        text = text.lower()
    text = re.sub(r"[^\x00-\x7F]+", "", text)
    return text


def query(payload, API_URL, headers) -> Dict:
    response = requests.post(API_URL, headers=headers, json=payload, timeout=60)
    return response.json()

async def advance_query(payload, API_URL, headers):
    response = requests.post(API_URL, headers=headers, json=payload)
    while response.json().get('error') == 'Model is currently loading':
        estimated_time = response.json().get('estimated_time', 50)  # Default to 3 seconds if not provided
        print(f"Please wait: {response.json().get('estimated_time', 50)}")
        await asyncio.sleep(estimated_time)
        response = requests.post(API_URL, headers=headers, json=payload)
    return response.json()

def load_api_token(env_file_path) -> None:
    with open(env_file_path) as file:
        for line in file:
            if line.startswith("API_TOKEN"):
                return line.strip().split("=")[1]
    return None


def open_three_components(response: List[Dict]) -> Union[List, None]:
    try:
        label_scores = {item["label"]: item["score"] for item in response[0]}
        return (
            label_scores.get("positive", 0.0),
            label_scores.get("neutral", 0.0),
            label_scores.get("negative", 0.0),
        )

    except Exception as e:
        print(f"Exception: {str(e)}")


def average_rating(response: List[Dict]) -> float:
    try:
        label_scores = {item["label"]: item["score"] for item in response[0]}
        score = 0
        for key in label_scores.keys():
            val_num = int(key.split(" ")[0])
            score += val_num * label_scores[key]
        return round(score, 1)
    except Exception as e:
        print(f"Exception: {str(e)}")
        return -1
