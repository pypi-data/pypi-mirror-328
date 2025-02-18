"""
Custom library for Store Advisor page testing with self-healing capabilities.
"""
from robot.api import logger
from robot.libraries.BuiltIn import BuiltIn
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException, NoSuchElementException
import json
import time

class StoreAdvisorLibrary:
    """Library for testing Store Advisor Streamlit page with self-healing locators."""
    
    ROBOT_LIBRARY_SCOPE = 'TEST SUITE'
    
    def __init__(self):
        self.seleniumlib = BuiltIn().get_library_instance('SeleniumLibrary')
        self.locator_map = {
            # Primary locators
            'data_size_dropdown': (By.XPATH, "//div[contains(@class, 'stSelectbox')]//div[contains(text(), 'Data Size')]"),
            'update_freq_dropdown': (By.XPATH, "//div[contains(@class, 'stSelectbox')]//div[contains(text(), 'Update Frequency')]"),
            'query_latency_dropdown': (By.XPATH, "//div[contains(@class, 'stSelectbox')]//div[contains(text(), 'Required Query Latency')]"),
            'deployment_dropdown': (By.XPATH, "//div[contains(@class, 'stSelectbox')]//div[contains(text(), 'Deployment Preference')]"),
            'budget_dropdown': (By.XPATH, "//div[contains(@class, 'stSelectbox')]//div[contains(text(), 'Budget Level')]"),
            'get_recommendations_button': (By.XPATH, "//button[contains(text(), 'Get Recommendations')]"),
            
            # Alternative locators for self-healing
            'data_size_dropdown_alt': [
                (By.CSS_SELECTOR, "[data-testid='stSelectbox']:nth-child(1)"),
                (By.XPATH, "//label[contains(text(), 'Data Size')]/following-sibling::div"),
            ],
            'update_freq_dropdown_alt': [
                (By.CSS_SELECTOR, "[data-testid='stSelectbox']:nth-child(2)"),
                (By.XPATH, "//label[contains(text(), 'Update Frequency')]/following-sibling::div"),
            ]
        }
        
        # Store successful locators for learning
        self.successful_locators = {}
        
    def _find_element_with_healing(self, locator_key, timeout=10):
        """Find element with self-healing capability."""
        primary_locator = self.locator_map[locator_key]
        alt_locators = self.locator_map.get(f"{locator_key}_alt", [])
        
        # Try primary locator first
        try:
            element = WebDriverWait(self.seleniumlib.driver, timeout).until(
                EC.presence_of_element_located(primary_locator)
            )
            self.successful_locators[locator_key] = primary_locator
            return element
        except TimeoutException:
            logger.warn(f"Primary locator failed for {locator_key}, trying alternatives")
        
        # Try alternative locators
        for alt_locator in alt_locators:
            try:
                element = WebDriverWait(self.seleniumlib.driver, timeout).until(
                    EC.presence_of_element_located(alt_locator)
                )
                # Update primary locator if alternative succeeds
                self.locator_map[locator_key] = alt_locator
                self.successful_locators[locator_key] = alt_locator
                logger.info(f"Updated primary locator for {locator_key}")
                return element
            except TimeoutException:
                continue
        
        raise NoSuchElementException(f"Could not find element with key: {locator_key}")
    
    def select_data_size(self, size):
        """Select data size with self-healing locator."""
        element = self._find_element_with_healing('data_size_dropdown')
        element.click()
        size_option = WebDriverWait(self.seleniumlib.driver, 10).until(
            EC.presence_of_element_located((By.XPATH, f"//div[contains(text(), '{size}')]"))
        )
        size_option.click()
    
    def select_update_frequency(self, frequency):
        """Select update frequency with self-healing locator."""
        element = self._find_element_with_healing('update_freq_dropdown')
        element.click()
        freq_option = WebDriverWait(self.seleniumlib.driver, 10).until(
            EC.presence_of_element_located((By.XPATH, f"//div[contains(text(), '{frequency}')]"))
        )
        freq_option.click()
    
    def get_recommendations(self):
        """Click get recommendations button with self-healing locator."""
        element = self._find_element_with_healing('get_recommendations_button')
        element.click()
    
    def verify_recommendations_displayed(self):
        """Verify recommendations are displayed."""
        try:
            WebDriverWait(self.seleniumlib.driver, 10).until(
                EC.presence_of_element_located((By.XPATH, "//div[contains(@class, 'stExpander')]"))
            )
            return True
        except TimeoutException:
            return False
    
    def export_successful_locators(self, filepath):
        """Export successful locators for learning."""
        with open(filepath, 'w') as f:
            json.dump(self.successful_locators, f, indent=2)
    
    def import_learned_locators(self, filepath):
        """Import learned locators from previous runs."""
        try:
            with open(filepath, 'r') as f:
                learned_locators = json.load(f)
                self.locator_map.update(learned_locators)
        except FileNotFoundError:
            logger.warn("No learned locators file found")
