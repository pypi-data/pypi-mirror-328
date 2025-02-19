import logging
import os
import json
import unittest
from typing import Optional, Dict, Any
from unittest.mock import patch, MagicMock

from hawkinsdb import HawkinsDB
from hawkinsdb.openai_interface import OpenAIInterface
from litellm.exceptions import (
    AuthenticationError,
    InvalidRequestError,
    RateLimitError,
    ServiceUnavailableError,
    OpenAIError
)

# Configure logging with more detailed output
logging.basicConfig(
    level=logging.DEBUG,  # Changed to DEBUG for more detailed logs
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    force=True  # Ensure our configuration takes precedence
)
logger = logging.getLogger(__name__)

class TestOpenAIInterface(unittest.TestCase):
    """Test OpenAI integration with HawkinsDB using LiteLLM."""

    def setUp(self):
        """Set up test environment."""
        try:
            # Initialize database
            self.db = HawkinsDB()

            # Get and validate API key
            self.api_key = os.getenv("OPENAI_API_KEY")
            if not self.api_key:
                self.skipTest("OPENAI_API_KEY environment variable not set")

            if not self.api_key.startswith('sk-'):
                self.skipTest("Invalid OpenAI API key format")

            # Initialize interface with test model
            self.model = "gpt-3.5-turbo-1106"
            self.interface = OpenAIInterface(self.db, model=self.model)

            # Verify API connection (moved from original setUp)
            try:
                self.interface._test_connection()
            except Exception as e:
                self.skipTest(f"Failed to connect to OpenAI API: {str(e)}")

            # Set up test data
            self.text_description = """
            There's a red Tesla Model 3 in my garage. It's an electric vehicle 
            with autopilot capabilities and a glass roof. The car was manufactured 
            in 2023 and has only 1000 miles on it.
            """

        except Exception as e:
            logger.error(f"Test environment initialization failed: {str(e)}")
            self.fail(f"Failed to initialize test environment: {str(e)}")

        logger.info("Test environment initialized successfully")

    def tearDown(self):
        """Clean up test data and resources."""
        try:
            # Clean up sensitive data
            if hasattr(self, 'db') and hasattr(self.db, 'config'):
                try:
                    # Clear credentials
                    self.db.config.clear_sensitive_data()
                except Exception as e:
                    logger.warning(f"Failed to clear sensitive data: {str(e)}")

            # Clean up database test data
            if hasattr(self, 'db'):
                try:
                    self.db._perform_maintenance()
                except Exception as e:
                    logger.warning(f"Database cleanup failed: {str(e)}")

            # Clear OpenAI interface
            if hasattr(self, 'interface'):
                try:
                    # Clear client and model references
                    if hasattr(self.interface, 'client'):
                        delattr(self.interface, 'client')
                    delattr(self, 'interface')
                except Exception as e:
                    logger.warning(f"Interface cleanup failed: {str(e)}")

        except Exception as e:
            logger.error(f"Cleanup failed: {str(e)}")
        finally:
            # Force garbage collection
            import gc
            gc.collect()

    def test_parse_entity_from_text(self):
        """Test parsing entity from natural language text with new API format."""
        logger.info("\nTesting entity parsing from text...")
        try:
            result = self.interface.parse_entity_from_text(self.text_description)

            # Verify successful response
            self.assertTrue(result['success'], f"Failed to parse entity: {result.get('message', 'Unknown error')}")
            self.assertIn('entity_data', result, "Response missing entity_data")
            self.assertIsNotNone(result['entity_data'], "Entity data is None")

            # Verify entity structure with new API format
            entity_data = result['entity_data']
            self.assertIn('name', entity_data, "Entity missing name field")
            self.assertTrue(entity_data['name'].strip(), "Entity name should not be empty")
            self.assertIn('properties', entity_data, "Entity missing properties field")
            self.assertIsInstance(entity_data['properties'], dict, "Properties should be a dictionary")

            # Verify Tesla-specific properties with more flexible matching
            props = entity_data['properties']

            # Check for color property
            color_found = any(
                'color' in k.lower() or 'red' in str(v).lower() or
                any('red' in str(val).lower() for val in v if isinstance(v, list))
                for k, v in props.items()
            )
            self.assertTrue(color_found, "Color property missing or incorrect")

            # Check for model/make property with broader matching
            model_found = any(
                any(term in k.lower() or term in str(v).lower() or
                    any(term in str(val).lower() for val in v if isinstance(v, list))
                    for term in ['model', 'tesla', 'make', 'vehicle'])
                for k, v in props.items()
            )
            self.assertTrue(model_found, "Model/make property missing or incorrect")

            year_found = any('year' in k.lower() or '2023' in str(v)
                           for k, v in props.items())
            self.assertTrue(year_found, "Year property missing or incorrect")

            logger.info(f"Parsed entity: {json.dumps(result, indent=2)}")

        except OpenAIError as oe:
            self.skipTest(f"OpenAI API error: {str(oe)}")
        except Exception as e:
            self.fail(f"Test failed with unexpected exception: {str(e)}")

    def test_add_entity_to_database(self):
        """Test adding parsed entity to database."""
        logger.info("\nTesting entity addition to database...")
        try:
            # First ensure we have a valid API key
            if not self.api_key:
                self.skipTest("No valid API key available")

            # Parse the entity
            parsed_result = self.interface.parse_entity_from_text(self.text_description)
            self.assertTrue(parsed_result['success'],
                          f"Failed to parse entity: {parsed_result.get('message', 'Unknown error')}")
            self.assertIsNotNone(parsed_result.get('entity_data'), "No entity data returned")

            # Add to database
            add_result = self.db.add_entity(parsed_result['entity_data'])
            self.assertTrue(add_result['success'],
                          f"Failed to add entity: {add_result.get('message', 'Unknown error')}")
            self.assertIsNotNone(add_result.get('entity_name'), "No entity name returned")

            # Verify entity was added correctly
            entity_name = add_result['entity_name']
            frames = self.db.query_frames(entity_name)
            self.assertTrue(frames, f"Entity {entity_name} not found in database")

            logger.info(f"Entity addition result: {json.dumps(add_result, indent=2)}")

        except OpenAIError as oe:
            self.skipTest(f"OpenAI API error: {str(oe)}")
        except Exception as e:
            self.fail(f"Test failed with unexpected exception: {str(e)}")

    def test_answer_question(self):
        """Test querying the database using natural language."""
        logger.info("\nTesting natural language query...")
        try:
            # First add an entity to query
            parsed_result = self.interface.parse_entity_from_text(self.text_description)
            self.assertTrue(parsed_result['success'], "Failed to parse entity for query test")

            add_result = self.db.add_entity(parsed_result['entity_data'])
            self.assertTrue(add_result['success'], "Failed to add entity for query test")

            # Test querying
            query = "What are the main features of this car and where is it located?"
            query_result = self.interface.answer_question(query)

            self.assertTrue(query_result['success'],
                          f"Query failed: {query_result.get('message', 'Unknown error')}")
            self.assertIsNotNone(query_result.get('response'), "No response returned")

            # Verify response content with more detailed assertions
            response = query_result['response']
            self.assertIn('Tesla', response, "Response should mention Tesla")
            self.assertIn('garage', response, "Response should mention location (garage)")

            # Verify response structure
            self.assertIsInstance(response, str, "Response should be a string")
            self.assertTrue(len(response) > 20, "Response should be a meaningful length")

            # Log the actual response for debugging
            logger.info(f"Query response: {response}")

            # Verify key information is present
            key_terms = ['Model 3', 'electric', 'red']
            found_terms = [term for term in key_terms if term.lower() in response.lower()]
            self.assertTrue(found_terms, f"Response should contain at least one of: {key_terms}")

            logger.info(f"Query result: {json.dumps(query_result, indent=2)}")

        except OpenAIError as oe:
            self.skipTest(f"OpenAI API error: {str(oe)}")
        except Exception as e:
            self.fail(f"Test failed with exception: {str(e)}")

    def test_error_handling(self):
        """Test error handling with LiteLLM exceptions."""
        logger.info("\nTesting error handling...")

        # Test with empty input
        result = self.interface.parse_entity_from_text("")
        self.assertFalse(result['success'])
        self.assertIn('message', result)
        self.assertIsNone(result.get('entity_data'))

        # Test with empty query
        query_result = self.interface.answer_question("")
        self.assertFalse(query_result['success'])
        self.assertIn('message', query_result)
        self.assertIsNone(query_result.get('response'))

        # Test API key validation (moved from original test_error_handling)
        
        # Test various error scenarios with LiteLLM error patterns
        original_api_key = self.interface.api_key
        try:
            # Test authentication error
            with patch('litellm.completion') as mock_completion:
                mock_completion.side_effect = AuthenticationError("Invalid API key")
                result = self.interface.parse_entity_from_text(self.text_description)
                self.assertFalse(result['success'])
                self.assertIn('authentication', result['message'].lower())

            # Test rate limit error
            with patch('litellm.completion') as mock_completion:
                mock_completion.side_effect = RateLimitError("Rate limit exceeded")
                result = self.interface.parse_entity_from_text(self.text_description)
                self.assertFalse(result['success'])
                self.assertIn('rate limit', result['message'].lower())

            # Test service unavailable
            with patch('litellm.completion') as mock_completion:
                mock_completion.side_effect = ServiceUnavailableError("Service is unavailable")
                result = self.interface.parse_entity_from_text(self.text_description)
                self.assertFalse(result['success'])
                self.assertTrue(
                    any(term in result.get('message', '').lower()
                        for term in ['unavailable', 'error']),
                    "Error message should indicate service unavailable"
                )

        finally:
            self.interface.api_key = original_api_key


if __name__ == '__main__':
    unittest.main(verbosity=2)