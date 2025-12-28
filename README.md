## Phase 2: MySQL Data Pipeline

This phase focuses on taking the raw stock data stored in `data.json` and migrating it into a structured MySQL relational database.

## Features
- **Automated Ingestion**: Reads local JSON data and prepares it for SQL insertion.
- **Idempotent Upserts**: Uses `INSERT ... ON DUPLICATE KEY UPDATE` to ensure data stays fresh without creating duplicate date entries.
- **Environment Security**: Utilizes `.env` files to keep database credentials secure.

## Database Schema
The data is stored in a table named `ibm_daily_stock` with the following structure:

+-------------+---------------+------+-----+---------+-------+
| Field       | Type          | Null | Key | Default | Extra |
+-------------+---------------+------+-----+---------+-------+
| trade_date  | date          | NO   | PRI | NULL    |       |
| open_price  | decimal(10,4) | YES  |     | NULL    |       |
| high_price  | decimal(10,4) | YES  |     | NULL    |       |
| low_price   | decimal(10,4) | YES  |     | NULL    |       |
| close_price | decimal(10,4) | YES  |     | NULL    |       |
| volume      | bigint        | YES  |     | NULL    |       |
+-------------+---------------+------+-----+---------+-------+

## 🛠️ Setup & Installation
1. **Dependencies**:
   ```bash
   pip install mysql-connector-python python-dotenv
