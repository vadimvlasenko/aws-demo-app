# AWS Demo App

This project demonstrates how to build a serverless application using AWS CDK and Python. It includes examples of AWS Lambda, API Gateway, and DynamoDB.

## Project Structure

```
├── README.md
├── app.py
├── cdk.json
├── lambda/
│   └── lambda.py
├── requirements.txt
├── setup.py
├── source.bat
├── source.sh
├── hello_api/
│   ├── __init__.py
│   ├── api_stack.py
└── .github/
    └── workflows/
        └── ci-cd.yaml
```

### Endpoints

- GET `/employees`
- POST `/employee`

### Setup

1. Install dependencies:
    ```sh
    pip install -r requirements.txt
    ```

2. Synthesize the CloudFormation template:
    ```sh
    cdk synth
    ```

3. Deploy the stack:
    ```sh
    cdk deploy
    ```