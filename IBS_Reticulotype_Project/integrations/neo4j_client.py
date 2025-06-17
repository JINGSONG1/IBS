"""Neo4j graph utility for storing and querying patient evolution paths."""
from typing import Any, Dict

from neo4j import GraphDatabase


class Neo4jClient:
    def __init__(self, uri: str, user: str, password: str) -> None:
        self.driver = GraphDatabase.driver(uri, auth=(user, password))

    def close(self) -> None:
        self.driver.close()

    def create_relationship(self, patient_id: str, from_state: str, to_state: str) -> None:
        """Create a relationship representing a transition in the patient path."""
        with self.driver.session() as session:
            session.run(
                "MERGE (p:Patient {id: $pid})"
                " MERGE (a:State {name: $from_state})"
                " MERGE (b:State {name: $to_state})"
                " MERGE (p)-[:HAS_STATE]->(a)"
                " MERGE (p)-[:HAS_STATE]->(b)"
                " MERGE (a)-[:NEXT]->(b)",
                pid=patient_id,
                from_state=from_state,
                to_state=to_state,
            )

    def get_path(self, patient_id: str) -> Any:
        """Retrieve the evolution path for a patient."""
        with self.driver.session() as session:
            result = session.run(
                "MATCH (p:Patient {id: $pid})-[:HAS_STATE]->(s:State)"
                " OPTIONAL MATCH (s)-[:NEXT]->(n:State)"
                " RETURN s.name AS state, n.name AS next", pid=patient_id
            )
            return result.data()
