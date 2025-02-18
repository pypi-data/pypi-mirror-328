"""
Enhanced self-healing capabilities for Streamlit testing.
"""
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException, NoSuchElementException
import difflib
import json
import logging
from typing import Dict, List, Tuple, Optional
import numpy as np
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

class ElementHealer:
    """Advanced self-healing for UI elements."""
    
    def __init__(self):
        self.logger = logging.getLogger(__name__)
        self.vectorizer = TfidfVectorizer(analyzer='char', ngram_range=(2, 4))
        self.locator_history: Dict[str, List[Tuple[By, str]]] = {}
        self.success_rates: Dict[str, Dict[str, float]] = {}
    
    def initialize_from_file(self, filepath: str):
        """Load historical locator data."""
        try:
            with open(filepath, 'r') as f:
                data = json.load(f)
                self.locator_history = {k: [(By[loc[0]], loc[1]) for loc in v]
                                     for k, v in data['history'].items()}
                self.success_rates = data['success_rates']
        except FileNotFoundError:
            self.logger.warning("No history file found, starting fresh")
    
    def save_to_file(self, filepath: str):
        """Save locator history and success rates."""
        data = {
            'history': {k: [(str(loc[0]), loc[1]) for loc in v]
                       for k, v in self.locator_history.items()},
            'success_rates': self.success_rates
        }
        with open(filepath, 'w') as f:
            json.dump(data, f, indent=2)
    
    def find_similar_element(self, driver, target_text: str, context: str) -> Optional[Tuple[By, str]]:
        """Find similar element using text similarity."""
        page_source = driver.page_source
        
        # Get all text content
        elements = driver.find_elements(By.XPATH, "//*[text()]")
        texts = [el.text for el in elements]
        
        if not texts:
            return None
        
        # Vectorize and compare
        try:
            vectors = self.vectorizer.fit_transform([target_text] + texts)
            similarities = cosine_similarity(vectors[0:1], vectors[1:])[0]
            best_match_idx = np.argmax(similarities)
            
            if similarities[best_match_idx] > 0.8:  # Threshold for similarity
                best_element = elements[best_match_idx]
                xpath = self._generate_xpath(best_element)
                return (By.XPATH, xpath)
        except Exception as e:
            self.logger.error(f"Error in similarity calculation: {e}")
        
        return None
    
    def _generate_xpath(self, element) -> str:
        """Generate a robust XPath for an element."""
        attributes = element.get_property('attributes')
        
        # Try with ID first
        if element.get_attribute('id'):
            return f"//*[@id='{element.get_attribute('id')}']"
        
        # Try with multiple attributes
        xpath_parts = []
        for attr in ['class', 'name', 'data-testid', 'role']:
            value = element.get_attribute(attr)
            if value:
                xpath_parts.append(f"@{attr}='{value}'")
        
        if xpath_parts:
            return f"//*[{' and '.join(xpath_parts)}]"
        
        # Fallback to text content
        text = element.text
        if text:
            return f"//*[contains(text(), '{text}')]"
        
        return None
    
    def update_success_rate(self, element_key: str, locator: Tuple[By, str], success: bool):
        """Update success rate for a locator."""
        if element_key not in self.success_rates:
            self.success_rates[element_key] = {}
        
        locator_str = f"{locator[0]}:{locator[1]}"
        current_rate = self.success_rates[element_key].get(locator_str, 0.5)
        
        # Exponential moving average
        alpha = 0.3
        new_rate = current_rate * (1 - alpha) + int(success) * alpha
        self.success_rates[element_key][locator_str] = new_rate
    
    def get_best_locators(self, element_key: str, n: int = 3) -> List[Tuple[By, str]]:
        """Get top N most successful locators for an element."""
        if element_key not in self.success_rates:
            return []
        
        sorted_locators = sorted(
            self.success_rates[element_key].items(),
            key=lambda x: x[1],
            reverse=True
        )
        
        return [(By[loc.split(':')[0]], loc.split(':')[1])
                for loc, _ in sorted_locators[:n]]
    
    def add_locator(self, element_key: str, locator: Tuple[By, str]):
        """Add new locator to history."""
        if element_key not in self.locator_history:
            self.locator_history[element_key] = []
        
        if locator not in self.locator_history[element_key]:
            self.locator_history[element_key].append(locator)
    
    def find_element(self, driver, element_key: str, context: str = "", timeout: int = 10):
        """Find element with self-healing capabilities."""
        # Try best locators first
        best_locators = self.get_best_locators(element_key)
        for locator in best_locators:
            try:
                element = WebDriverWait(driver, timeout).until(
                    EC.presence_of_element_located(locator)
                )
                self.update_success_rate(element_key, locator, True)
                return element
            except TimeoutException:
                self.update_success_rate(element_key, locator, False)
        
        # Try similar element search
        if element_key in self.locator_history:
            for old_locator in self.locator_history[element_key]:
                similar = self.find_similar_element(
                    driver, old_locator[1], context
                )
                if similar:
                    try:
                        element = WebDriverWait(driver, timeout).until(
                            EC.presence_of_element_located(similar)
                        )
                        self.add_locator(element_key, similar)
                        self.update_success_rate(element_key, similar, True)
                        return element
                    except TimeoutException:
                        continue
        
        raise NoSuchElementException(f"Could not find element: {element_key}")
