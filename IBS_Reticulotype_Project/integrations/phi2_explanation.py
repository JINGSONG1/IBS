"""Integration with HuggingFace phi-2 model for explanation generation."""
from transformers import pipeline


def generate_explanation(prompt: str, max_length: int = 256) -> str:
    """Generate an explanation using the phi-2 model from HuggingFace.

    Parameters
    ----------
    prompt : str
        Input text describing what to explain.
    max_length : int
        Maximum length of the generated output.

    Returns
    -------
    str
        Generated explanation text.
    """
    try:
        generator = pipeline("text-generation", model="microsoft/phi-2")
        outputs = generator(prompt, max_length=max_length, num_return_sequences=1)
        return outputs[0]["generated_text"]
    except Exception as e:
        # In practice you would handle errors more gracefully
        return f"Error generating explanation: {e}"
