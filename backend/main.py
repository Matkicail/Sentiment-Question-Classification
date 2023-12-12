from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from fastapi.staticfiles import StaticFiles
from fastapi import HTTPException
from helpers.helpers import *
from typing import Dict

app = FastAPI()
API_TOKEN = load_api_token(".env")
# CORS setup
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Allows all origins for simplicity
    allow_credentials=True,
    allow_methods=["*"],  # Allows all methods
    allow_headers=["*"],  # Allows all headers
)
MAX_LENGTH = 512
HEADERS = {"Authorization": f"Bearer {API_TOKEN}"}


class TextInput(BaseModel):
    text: str


class QuestionContent(BaseModel):
    text: str
    question: str


@app.post("/sentiment/")
async def sentiment_analysis(input_data: TextInput) -> Dict:
    """_summary_

    Args:
        input_data (NameInput): The name of the entity that we are about to predict (which class)

    Returns:
        Dict: Response to the server which contains the name of said entity, the type we believe it  to be
            and lastly, the probability it belongs to each of the classes we trained on
    """
    try:
        if len(input_data.text) > MAX_LENGTH:
            input_data.text = _summarise_text(input_data.text)

        text = preprocess_text(input_data.text, make_lower=False)
        API_URL = "https://api-inference.huggingface.co/models/lxyuan/distilbert-base-multilingual-cased-sentiments-student"
        output = query(
            {
                "inputs": text,
            },
            API_URL,
            HEADERS,
        )
        pos, neutral, negative = open_three_components(output)
        return {"positive": pos, "neutral": neutral, "negative": negative}
    except Exception as e:
        return _handle_exception(e)


@app.post("/rating/")
async def rating_analysis(input_data: TextInput) -> Dict:
    """_summary_

    Args:
        input_data (NameInput): The name of the entity that we are about to predict (which class)

    Returns:
        Float: Response to the server containing a rounded rating from the user.
    """
    try:
        if len(input_data.text) > MAX_LENGTH:
            input_data.text = _summarise_text(input_data.text)
        text = preprocess_text(input_data.text, make_lower=True)
        API_URL = "https://api-inference.huggingface.co/models/nlptown/bert-base-multilingual-uncased-sentiment"
        output = query(
            {
                "inputs": text,
            },
            API_URL,
            HEADERS,
        )
        rating = average_rating(output)
        return {"rating": rating}
    except Exception as e:
        return _handle_exception(e)


@app.post("/question/")
async def question_content(input_data: QuestionContent) -> Dict:
    """_summary_

    Args:
        input_data (QuestionContent): _description_

    Raises:
        HTTPException: _description_
        HTTPException: _description_

    Returns:
        Dict: _description_
    """
    try:
        text = preprocess_text(input_data.text, make_lower=True)
        question = preprocess_text(input_data.question, make_lower=True)
        API_URL = (
            "https://api-inference.huggingface.co/models/deepset/roberta-large-squad2"
        )
        headers = {"Authorization": f"Bearer {API_TOKEN}"}

        # Call the query function and await its response
        print("Querying...")
        output = await advance_query(
            {"inputs": {"question": question, "context": text}}, API_URL, headers
        )

        if "answer" in output:
            return {"answer": output["answer"]}
        else:
            # Handle other potential errors or no-answer scenarios
            raise HTTPException(
                status_code=503, detail="The model did not return an answer."
            )

    except Exception as e:
        # Log the exception for debugging purposes
        print(f"Exception: {str(e)}")
        # Return a generic error response
        raise HTTPException(status_code=500, detail="Internal Server Error")


def _summarise_text(text) -> str:
    print(f"Text was of length: {len(text)} \n\tSummarising Text...")
    API_URL = "https://api-inference.huggingface.co/models/facebook/bart-large-cnn"
    output = query(
        {
            "inputs": text,
        },
        API_URL,
        HEADERS,
    )
    print(f"Outgoing summarised text is of size {len(output[0]['summary_text'])}")
    return output[0]["summary_text"]


def _handle_exception(e: Exception) -> Dict:
    print(f"Exception: {str(e)}")
    return {"error": "Internal Server Error"}
