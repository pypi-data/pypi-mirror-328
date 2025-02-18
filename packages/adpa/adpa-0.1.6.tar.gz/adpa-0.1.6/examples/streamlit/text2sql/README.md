# ADPA Text-to-SQL Explorer

A Streamlit application that demonstrates the Text-to-SQL capabilities of the ADPA framework. This app allows users to write natural language questions and converts them into SQL queries using the hybrid architecture.

## Features

- Natural language to SQL conversion
- Interactive query builder
- Real-time query execution
- Schema visualization
- Query history tracking
- Example queries
- Performance metrics
- Error handling and validation

## Installation

1. Clone the repository:
```bash
git clone https://github.com/achimdehnert/adpa.git
cd adpa/examples/streamlit/text2sql
```

2. Install dependencies:
```bash
pip install -r requirements.txt
```

3. Create a `.env` file in the root directory with your database credentials:
```env
POSTGRES_HOST=your_host
POSTGRES_PORT=5432
POSTGRES_USER=your_user
POSTGRES_PASSWORD=your_password
POSTGRES_DATABASE=your_database
```

## Usage

1. Start the Streamlit app:
```bash
streamlit run app.py
```

2. Open your browser and navigate to `http://localhost:8501`

3. Enter your question in natural language or select an example query

4. Click "Convert to SQL" to see the results

## Database Schema

The application is configured to work with a database containing the following tables:

### Users
- id (integer, primary key)
- username (varchar)
- email (varchar)
- created_at (timestamp)
- status (varchar)
- last_login (timestamp)

### Orders
- id (integer, primary key)
- user_id (integer, foreign key)
- total_amount (decimal)
- status (varchar)
- created_at (timestamp)

### Products
- id (integer, primary key)
- name (varchar)
- description (text)
- price (decimal)
- category (varchar)
- stock_level (integer)

## Example Queries

- Show all users who joined last month
- Find the total number of orders per customer
- List products with price greater than $100
- Show active users with their latest order date
- Calculate average order value by month

## Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

## License

This project is licensed under the MIT License - see the LICENSE file for details.
