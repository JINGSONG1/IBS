"""DoctorAgent that integrates external services for decision making."""
from typing import Any, Dict, List

from IBS_Reticulotype_Project.integrations.phi2_explanation import generate_explanation
from IBS_Reticulotype_Project.integrations.fhir_client import get_patient
from IBS_Reticulotype_Project.integrations.pubmed_client import search_articles
from IBS_Reticulotype_Project.integrations.openai_functions import chat_with_functions
from IBS_Reticulotype_Project.integrations.neo4j_client import Neo4jClient


class DoctorAgent:
    def __init__(self, graph_client: Neo4jClient) -> None:
        self.graph_client = graph_client

    def explain(self, prompt: str) -> str:
        """Use phi-2 model to generate an explanation."""
        return generate_explanation(prompt)

    def get_patient_info(self, patient_id: str) -> Dict[str, Any]:
        """Retrieve patient info from FHIR server."""
        return get_patient(patient_id)

    def recommend_articles(self, query: str) -> List[str]:
        """Search PubMed for relevant articles."""
        return search_articles(query)

    def call_openai(self, messages: List[Dict[str, str]], functions: List[Dict[str, Any]]) -> Any:
        """Invoke OpenAI ChatCompletion with function calling."""
        return chat_with_functions(messages, functions)

    def record_transition(self, patient_id: str, from_state: str, to_state: str) -> None:
        """Record a patient state transition in Neo4j."""
        self.graph_client.create_relationship(patient_id, from_state, to_state)
