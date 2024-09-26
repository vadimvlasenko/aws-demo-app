from aws_cdk import (
    Stack,
    aws_lambda as _lambda,
    aws_apigateway as apigw,
)
from constructs import Construct

class ApiStack(Stack):

    def __init__(self, scope: Construct, id: str, **kwargs) -> None:
        super().__init__(scope, id, **kwargs)

        get_employees_lambda = _lambda.Function(
            self, "GetEmployeesHandler",
            runtime=_lambda.Runtime.PYTHON_3_8,
            handler="lambda.get_employees",
            code=_lambda.Code.from_asset("lambda")
        )

        add_employee_lambda = _lambda.Function(
            self, "AddEmployeeHandler",
            runtime=_lambda.Runtime.PYTHON_3_8,
            handler="lambda.add_employee",
            code=_lambda.Code.from_asset("lambda")
        )

        api = apigw.RestApi(self, "employees-api",
            rest_api_name="Employee Service",
            description="This service serves employees."
        )

        get_employees_integration = apigw.LambdaIntegration(get_employees_lambda,
            request_templates={"application/json": '{ "statusCode": "200" }'}
        )

        add_employee_integration = apigw.LambdaIntegration(add_employee_lambda,
            request_templates={"application/json": '{ "statusCode": "201" }'}
        )

        api.root.add_resource("employees").add_method("GET", get_employees_integration)
        api.root.add_resource("employee").add_method("POST", add_employee_integration)
