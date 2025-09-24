import requests
import logging


logging.basicConfig(level=logging.INFO)
def get_random_quote():
    """Fetches a random quote from the quotable.io API."""
    try:
        response = requests.get("https://quotes-api-self.vercel.app/quote")
        # Raise an exception for bad status codes (4xx or 5xx)
        response.raise_for_status()

        data = response.json()
        logging.debug(f"the response data: {data}")
        quote = data['quote']
        author = data['author']
        logging.info(f"the author is:{author}")
        return f'"{quote}" - {author}'
    except requests.exceptions.RequestException as e:
        logging.error(f"Not fetch the API")
        return f"Error: Could not fetch a quote. Please check your internet connection. Details: {e}"