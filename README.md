# AWS Demo Application

This project demonstrates a serverless application using AWS CDK, Lambda, and API Gateway.

## Endpoints

- `GET /employees`: Fetches all employees.
- `POST /employee`: Adds a new employee.

## Setup

### Prerequisites

- AWS CLI configured
- Node.js installed
- Python 3.8 or above

### Installation

```sh
pip install -r requirements.txt
cdk deploy
```

## Testing

```sh
source source.sh
pytest
```