"""Unit tests for ADPA Framework validators."""
import pytest
from pathlib import Path
from pydantic import BaseModel, Field
from adpa.validators.model_validator import ModelValidator, BaseModelValidator
from adpa.validators.streamlit_validator import StreamlitValidator
from adpa.validators.robot_validator import RobotValidator, RobotTestCase

# Test data
VALID_ROBOT_TEST = """*** Test Cases ***
Test Should Login Successfully
    [Documentation]    Verify user can login with valid credentials
    [Tags]    smoke    regression    integration
    Given User is on login page
    When User enters valid credentials
    And User clicks login button
    Then User should be logged in
"""

INVALID_ROBOT_TEST = """*** Test Cases ***
Login Test
    User is on login page
    User enters credentials
    User clicks login
"""

class TestModelValidator:
    """Test cases for Pydantic model validator."""
    
    def test_validate_valid_model(self):
        """Test validation of a valid model."""
        class ValidModel(BaseModelValidator):
            name: str = Field(..., description="User name", example="John")
            age: int = Field(..., description="User age", example=30)
            
        issues = ModelValidator.validate_model_structure(ValidModel)
        assert not issues, f"Unexpected issues: {issues}"
        
    def test_validate_invalid_model(self):
        """Test validation of an invalid model."""
        class InvalidModel(BaseModel):
            name: str
            age: int
            
        issues = ModelValidator.validate_model_structure(InvalidModel)
        assert len(issues) > 0, "Expected validation issues"
        assert any("missing Config class" in issue for issue in issues)
        
class TestStreamlitValidator:
    """Test cases for Streamlit validator."""
    
    def test_validate_valid_page(self, tmp_path):
        """Test validation of a valid Streamlit page."""
        page_content = '''
import streamlit as st

st.set_page_config(page_title="Test", page_icon="🔥", layout="wide")

if "counter" not in st.session_state:
    st.session_state.counter = 0

with st.form("test_form"):
    name = st.text_input("Name")
    submitted = st.form_submit_button("Submit")
    
@st.cache_data
def load_data():
    return pd.read_csv("data.csv")
'''
        page_file = tmp_path / "test_page.py"
        page_file.write_text(page_content)
        
        issues = StreamlitValidator.validate_page(page_file)
        assert not issues, f"Unexpected issues: {issues}"
        
    def test_validate_invalid_page(self, tmp_path):
        """Test validation of an invalid Streamlit page."""
        page_content = '''
import streamlit as st

# Missing page config
st.session_state.counter = 0  # Missing initialization

# Form without with statement
form = st.form("test_form")
name = st.text_input("Name")
form.form_submit_button("Submit")

# Expensive operation without caching
df = pd.read_csv("data.csv")
'''
        page_file = tmp_path / "invalid_page.py"
        page_file.write_text(page_content)
        
        issues = StreamlitValidator.validate_page(page_file)
        assert len(issues) > 0, "Expected validation issues"
        
class TestRobotValidator:
    """Test cases for Robot Framework validator."""
    
    def test_parse_valid_test_case(self):
        """Test parsing of a valid Robot test case."""
        test_cases = RobotValidator.parse_test_case(VALID_ROBOT_TEST)
        assert len(test_cases) == 1
        test_case = test_cases[0]
        assert test_case.name == "Test Should Login Successfully"
        assert "smoke" in test_case.tags
        assert len(test_case.steps) == 4
        
    def test_validate_valid_test_case(self):
        """Test validation of a valid Robot test case."""
        test_cases = RobotValidator.parse_test_case(VALID_ROBOT_TEST)
        issues = RobotValidator.validate_test_case(test_cases[0])
        assert not issues, f"Unexpected issues: {issues}"
        
    def test_validate_invalid_test_case(self):
        """Test validation of an invalid Robot test case."""
        test_cases = RobotValidator.parse_test_case(INVALID_ROBOT_TEST)
        issues = RobotValidator.validate_test_case(test_cases[0])
        assert len(issues) > 0, "Expected validation issues"
        assert any("should start with 'Test Should'" in issue for issue in issues)
        
    def test_validate_resource_file(self, tmp_path):
        """Test validation of a Robot resource file."""
        resource_content = '''
*** Settings ***
Documentation    Test resource file

*** Variables ***
${VALID_VAR}    value
${invalid_var}    value
@{VALID_LIST}    item1    item2
@{invalid_list}    item1    item2

*** Keywords ***
Valid Keyword
    [Documentation]    Valid keyword
    Log    Hello
'''
        resource_file = tmp_path / "test_resource.robot"
        resource_file.write_text(resource_content)
        
        issues = RobotValidator.validate_resource_file(resource_file)
        assert len(issues) == 2, "Expected 2 validation issues for invalid variable names"
