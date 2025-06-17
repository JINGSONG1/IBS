"""Client for PubMed E-Utilities API."""
from typing import List
import requests

BASE_URL = "https://eutils.ncbi.nlm.nih.gov/entrez/eutils/"


def search_articles(query: str, max_results: int = 5) -> List[str]:
    """Search PubMed and return a list of article IDs."""
    params = {
        "db": "pubmed",
        "term": query,
        "retmax": str(max_results),
        "retmode": "json",
    }
    try:
        response = requests.get(BASE_URL + "esearch.fcgi", params=params, timeout=10)
        response.raise_for_status()
        data = response.json()
        return data.get("esearchresult", {}).get("idlist", [])
    except Exception as e:
        return [f"error: {e}"]
