# LLM Resilience Demo

This Streamlit application demonstrates the resilience features of the ADPA framework's LLM integration.

## Features

- Provider Failover
- Circuit Breaking
- Error Simulation
- Real-time Monitoring
- Interactive Configuration

## Setup

1. Install dependencies:
```bash
pip install -r requirements.txt
```

2. Set up environment variables:
```bash
# Create .env file
OPENAI_API_KEY=your_openai_key
GEMINI_API_KEY=your_gemini_key
GROQ_API_KEY=your_groq_key
```

3. Run the app:
```bash
streamlit run llm_resilience_demo.py
```

## Usage

1. Configure providers and resilience settings in the sidebar
2. Test provider failover with simulated failures
3. Observe circuit breaker behavior under load
4. Simulate various error scenarios

## Components

- **Provider Failover**: Tests automatic switching between LLM providers
- **Circuit Breaking**: Demonstrates circuit breaker pattern for fault tolerance
- **Error Simulation**: Simulates various error scenarios for testing

## Contributing

Feel free to contribute by:
1. Opening issues
2. Submitting pull requests
3. Suggesting new features
