"""Simple FHIR client for interacting with a hospital FHIR server."""
from typing import Any, Dict

from fhirclient import client
from fhirclient.models.patient import Patient


settings = {
    "app_id": "ibs_app",
    "api_base": "https://vonk.fire.ly/R4"  # public test FHIR server
}

fhir_app = client.FHIRClient(settings=settings)


def get_patient(patient_id: str) -> Dict[str, Any]:
    """Retrieve patient information from the FHIR server."""
    try:
        patient = Patient.read(patient_id, fhir_app.server)
        return patient.as_json()
    except Exception as e:
        return {"error": str(e)}
