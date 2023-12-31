"""
This file contains the OpenAI client.
"""
from dotenv import dotenv_values
import openai

openai.api_key = dotenv_values(".env").get("OPENAI_KEY")


def generate_response(user_message: str, character_name: str):
    """
    Simple approach to generate a response to a user message. Call OpenAI API to generate a response.

    :param user_message: user message
    :param character_name: character name who user is talking to

    :return: character's response
    """
    prompt = f"Friend and {character_name} are talking. Friend says: {user_message}\n{character_name} says:"
    response = openai.Completion.create(
        engine="text-davinci-003", prompt=prompt, max_tokens=50
    )
    return response.choices[0].text
