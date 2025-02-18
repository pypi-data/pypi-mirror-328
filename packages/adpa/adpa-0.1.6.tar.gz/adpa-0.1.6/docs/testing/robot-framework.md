# Robot Framework Testing Guide

## Overview

ADPA uses Robot Framework for automated testing, providing a comprehensive suite of GUI, API, and integration tests. This guide covers the setup, usage, and maintenance of our Robot Framework test suite.

## Quick Links

- [Test Dashboard](#test-dashboard)
- [Test Structure](#test-structure)
- [Self-Healing Tests](#self-healing-tests)
- [Best Practices](#best-practices)

## Test Dashboard

The ADPA Test Dashboard provides real-time monitoring and execution of Robot Framework tests.

### Features

1. **Test Execution**
   - Run specific test suites or all tests
   - Configure browser and test options
   - Real-time execution monitoring

2. **Locator Verification**
   - Verify test locators
   - Automatic self-healing for broken locators
   - Locator consistency checks

3. **Results Visualization**
   - Test status distribution
   - Duration analysis
   - Detailed test reports

### Usage

1. Start the dashboard:
   ```bash
   streamlit run tests/dashboard/test_dashboard.py
   ```

2. Access at http://localhost:8506

## Test Structure

```
tests/robot/
├── gui/                    # GUI test suites
│   ├── dashboard_tests.robot
│   ├── project_tests.robot
│   └── research_tests.robot
├── resources/              # Shared resources
│   ├── common.resource
│   ├── gui_locators.resource
│   └── test_init.resource
├── results/               # Test execution results
└── dashboard/            # Test dashboard application
```

## Self-Healing Tests

The test suite includes automatic self-healing capabilities for maintaining test stability.

### Features

1. **Locator Analysis**
   - Identifies broken locators
   - Suggests fixes
   - Maintains consistency

2. **Fix Strategies**
   ```python
   # Original broken locator
   [data-testid="submit-buttton"]  # Typo
   
   # Auto-fixed locator
   [data-testid="submit-button"]   # Fixed
   ```

3. **Usage**
   - Use dashboard's "Verify Locators"
   - Click "Self Heal" for automatic fixes
   - Review and approve changes

## Best Practices

### 1. Locator Management

```html
<!-- Good -->
<div data-testid="component-name">Content</div>

<!-- Bad -->
<div class="js-component">Content</div>
```

### 2. Test Case Structure

```robotframework
*** Test Cases ***
Dashboard Should Display Project Overview
    [Documentation]    Verify dashboard shows correct project information
    [Tags]    gui    dashboard    smoke
    Verify Element Text    ${DASHBOARD_TITLE}    Project Overview
```

### 3. Resource Organization

```robotframework
*** Settings ***
Resource          ../resources/common.resource
Resource          ../resources/gui_locators.resource

Suite Setup       Setup Test Environment
Test Setup        Test Setup
```

## Test Data Management

1. **Generation**
   ```robotframework
   *** Keywords ***
   Generate Test Data
       [Arguments]    ${type}    ${count}=1
       ${data}=    Create List
       FOR    ${index}    IN RANGE    ${count}
           ${item}=    Generate ${type} Data    ${index}
           Append To List    ${data}    ${item}
       END
       [Return]    ${data}
   ```

2. **Cleanup**
   ```robotframework
   *** Keywords ***
   Clean Test Environment
       Remove Test Data    ${TEST_NAME}
       Close All Browsers
   ```

## Error Prevention

1. **Timing Issues**
   ```robotframework
   # Good
   Wait For Element    ${selector}    timeout=20s
   
   # Bad
   Sleep    2s
   Click    ${selector}
   ```

2. **Resource Isolation**
   ```robotframework
   # Good
   ${test_dir}=    Set Variable    ${TEST_DATA_DIR}/${TEST_NAME}
   Create Directory    ${test_dir}
   
   # Bad
   Create Directory    test_data
   ```

## Continuous Integration

1. **Pipeline Integration**
   ```yaml
   test:
     stage: test
     script:
       - robot --outputdir results tests/robot/gui/
   ```

2. **Reporting**
   ```yaml
   artifacts:
     reports:
       junit: results/output.xml
     paths:
       - results/
   ```

## Troubleshooting

### Common Issues

1. **Locator Issues**
   - Use dashboard's locator verification
   - Check element visibility
   - Verify timing conditions

2. **Test Stability**
   - Use appropriate waits
   - Handle dynamic content
   - Clean test environment

### Debug Tools

1. **Screenshot Capture**
   ```robotframework
   Capture Page Screenshot    filename=${TEST_NAME}.png
   ```

2. **Logging**
   ```robotframework
   Log    ${variable}    level=DEBUG
   ```

## Version History

### v1.2.1 (2025-01-08)
- Added self-healing test functionality
- Enhanced test dashboard
- Improved error prevention

### v1.2.0 (2025-01-08)
- Initial test dashboard
- Real-time test execution
- Result visualization
