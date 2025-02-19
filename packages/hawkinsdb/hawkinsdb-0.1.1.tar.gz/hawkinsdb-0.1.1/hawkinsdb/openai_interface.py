import os
import json
import time
import logging
from typing import Dict, Any, Optional, List, Union
from tenacity import retry, stop_after_attempt, wait_exponential, retry_if_exception_type

# Import LiteLLM for OpenAI compatibility
try:
    from litellm import completion
    from litellm.exceptions import (
        AuthenticationError, 
        InvalidRequestError, 
        RateLimitError,
        ServiceUnavailableError,
        OpenAIError  # Base exception class
    )
except ImportError as e:
    raise ImportError(f"Failed to import LiteLLM: {str(e)}. Please ensure you have installed 'litellm>=1.61.6'")

from .core import HawkinsDB

logger = logging.getLogger(__name__)

class OpenAIInterface:
    """Interface for OpenAI integration with HawkinsDB using LiteLLM."""

    def __init__(self, db: HawkinsDB, model: Optional[str] = None):
        """Initialize OpenAI interface with proper error handling."""
        self.db = db
        self.model = model or "openai/gpt-4o"  # Default to openai/gpt-4o if no model specified
        self.max_context_length = 16385  # Model's maximum context length

        # Get API key with enhanced error handling
        self.api_key = self._get_valid_api_key()
        logger.info("OpenAI interface initialized successfully")

    def _get_valid_api_key(self) -> str:
        """Get and validate OpenAI API key from environment or config."""
        api_key = os.getenv("OPENAI_API_KEY")

        if not api_key:
            raise ValueError("OpenAI API key is required. Set OPENAI_API_KEY environment variable.")

        return api_key

    def _test_connection(self) -> None:
        """Test OpenAI API connection with minimal token usage."""
        try:
            response = completion(
                model=self.model,
                messages=[{"role": "system", "content": "Test"}],
                max_tokens=1,
                temperature=0.0,
                api_key=self.api_key
            )
            logger.info("OpenAI API connection test successful")

        except Exception as e:
            logger.error(f"OpenAI API connection test failed: {str(e)}")
            raise

    @retry(
        stop=stop_after_attempt(3),
        wait=wait_exponential(multiplier=1, min=4, max=10),
        retry=retry_if_exception_type(OpenAIError)
    )
    def parse_entity_from_text(self, text: str) -> Dict[str, Any]:
        """Extract entity information from text using OpenAI."""
        if not text or not text.strip():
            return {
                "success": False,
                "message": "Input text cannot be empty",
                "entity_data": None
            }

        try:
            prompt = """You are a precise entity information extractor. Analyze the text and extract relevant entity details in JSON format.

            Required output format:
            {
                "column": "Semantic",
                "name": "unique_descriptive_name",
                "type": "entity_type",
                "properties": {
                    "attribute1": "value1",
                    "attribute2": ["value2a", "value2b"]
                }
            }

            Rules:
            1. ALWAYS provide a clear, unique name for the entity using underscores
            2. Extract meaningful properties and their values
            3. Use clear, consistent property names
            4. Include all relevant details from the text
            5. Return valid JSON only
            """

            response = completion(
                model=self.model,
                messages=[
                    {"role": "system", "content": prompt},
                    {"role": "user", "content": text}
                ],
                temperature=0.3,
                max_tokens=1000,
                response_format={"type": "json_object"},
                api_key=self.api_key
            )

            content = response.choices[0].message.content
            if not content:
                raise ValueError("Empty response from OpenAI")

            parsed_data = json.loads(content)
            return {
                "success": True,
                "message": "Successfully parsed entity",
                "entity_data": parsed_data
            }

        except json.JSONDecodeError as je:
            logger.error(f"Failed to parse JSON response: {str(je)}")
            return {
                "success": False,
                "message": f"Invalid JSON response: {str(je)}",
                "entity_data": None
            }

        except Exception as e:
            logger.error(f"Unexpected error parsing entity: {str(e)}")
            return {
                "success": False,
                "message": f"Unexpected error: {str(e)}",
                "entity_data": None
            }

    @retry(
        stop=stop_after_attempt(3),
        wait=wait_exponential(multiplier=1, min=4, max=10),
        retry=retry_if_exception_type(OpenAIError)
    )
    def answer_question(self, query: str) -> Dict[str, Any]:
        """Answer questions about stored entities using OpenAI."""
        if not query or not query.strip():
            return {
                "success": False,
                "message": "Query cannot be empty",
                "response": None
            }

        try:
            # Get relevant context from database
            entities = self.db.list_entities()
            if not entities:
                return {
                    "success": True,
                    "message": "No entities found in database",
                    "response": "I don't have any information in the database to answer your question."
                }

            # Build context string
            contexts = []
            for entity in entities[:5]:  # Limit to 5 entities to avoid token limits
                data = self.db.query_frames(entity)
                if data:
                    contexts.append(f"Entity: {entity}\nData: {json.dumps(data, default=str)}")

            context = "\n\n".join(contexts)

            response = completion(
                model=self.model,
                messages=[
                    {
                        "role": "system",
                        "content": f"""You are a helpful assistant with access to a knowledge base.
                        Answer questions based on this context:\n\n{context}"""
                    },
                    {"role": "user", "content": query}
                ],
                temperature=0.3,
                max_tokens=1000,
                api_key=self.api_key
            )

            answer = response.choices[0].message.content

            return {
                "success": True,
                "message": "Query processed successfully",
                "response": answer
            }

        except Exception as e:
            logger.error(f"Error processing query: {str(e)}")
            return {
                "success": False,
                "message": f"Error processing query: {str(e)}",
                "response": None
            }