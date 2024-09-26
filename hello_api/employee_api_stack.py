from aws_cdk import core as cdk
from aws_cdk.aws_lambda import Function, Code, Runtime
from aws_cdk.aws_apigateway import RestApi, LambdaIntegration

class EmployeeApiStack(cdk.Stack):

    def __init__(self, scope: cdk.Construct, id: str, **kwargs) -> None:
        super().__init__(scope, id, **kwargs)

        # Lambda function for GET /employees
        get_employees_lambda = Function(self, "GetEmployeesLambda",
            runtime=Runtime.PYTHON_3_8,
            handler="get_employees.handler",
            code=Code.from_asset("lambda"))

        # Lambda function for POST /employee
        add_employee_lambda = Function(self, "AddEmployeeLambda",
            runtime=Runtime.PYTHON_3_8,
            handler="add_employee.handler",
            code=Code.from_asset("lambda"))

        # API Gateway
        api = RestApi(self, "EmployeeApi")

        employees_resource = api.root.add_resource("employees")
        employees_resource.add_method("GET", LambdaIntegration(get_employees_lambda))

        employee_resource = api.root.add_resource("employee")
        employee_resource.add_method("POST", LambdaIntegration(add_employee_lambda))
