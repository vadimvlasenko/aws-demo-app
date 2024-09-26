from aws_cdk import (
    aws_lambda as _lambda,
    aws_apigateway as apigateway,
    aws_dynamodb as dynamodb,
    Stack
)
from constructs import Construct

class ApiStack(Stack):

    def __init__(self, scope: Construct, id: str, **kwargs) -> None:
        super().__init__(scope, id, **kwargs)

        table = dynamodb.Table(
            self, "Employees",
            partition_key={"name": "id", "type": dynamodb.AttributeType.STRING}
        )

        get_employees_lambda = _lambda.Function(
            self, "GetEmployeesFunction",
            runtime=_lambda.Runtime.PYTHON_3_8,
            handler="lambda.get_employees",
            code=_lambda.Code.from_asset("lambda")
        )

        add_employee_lambda = _lambda.Function(
            self, "AddEmployeeFunction",
            runtime=_lambda.Runtime.PYTHON_3_8,
            handler="lambda.add_employee",
            code=_lambda.Code.from_asset("lambda")
        )

        api = apigateway.RestApi(self, "employees-api",
            rest_api_name="Employees Service"
        )

        employees = api.root.add_resource("employees")
        employees.add_method("GET", apigateway.LambdaIntegration(get_employees_lambda))

        employee = api.root.add_resource("employee")
        employee.add_method("POST", apigateway.LambdaIntegration(add_employee_lambda))
