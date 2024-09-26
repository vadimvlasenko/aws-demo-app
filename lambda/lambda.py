import json

def get_employees(event, context):
    # Sample data, replace with actual database logic
    employees = [
        {"id": 1, "name": "John Doe", "department": "Engineering"},
        {"id": 2, "name": "Jane Smith", "department": "Marketing"}
    ]
    return {
        "statusCode": 200,
        "body": json.dumps(employees)
    }

def add_employee(event, context):
    body = json.loads(event['body'])
    # Sample logic, replace with actual database save logic
    new_employee = {
        "id": 3,  # This should be auto-generated by the database
        "name": body['name'],
        "department": body['department']
    }
    return {
        "statusCode": 201,
        "body": json.dumps({"message": "Employee added", "employee": new_employee})
    }
