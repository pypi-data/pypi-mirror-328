"""
A module that contains utility functions to be used in API Gateway-related tasks.
"""

# Constants for export
ACTION_EXECUTE_API_INVOKE = "execute-api:Invoke"
EFFECT_ALLOW = "Allow"
EFFECT_DENY = "Deny"

PRINCIPAL_ID = "principalId"
POLICY_DOCUMENT = "policyDocument"
ACTION = "Action"
EFFECT = "Effect"
RESOURCE = "Resource"


def generate_auth_response_as_iam_policy(
    principal_id,
    action=ACTION_EXECUTE_API_INVOKE,
    effect="",
    resource="",
    response_context: dict | None = None,
) -> dict:
    """
    Given the input parameters describing the response to an authorization request,
    formats the supplied information as an IAM policy dictionary and returns it.
    Designed to be used in Lambda functions underlying API Gateway Lambda authorizers.
    See:
      https://docs.aws.amazon.com/apigateway/latest/developerguide/apigateway-use-lambda-authorizer.html#api-gateway-lambda-authorizer-lambda-function-create

    Parameters
    ----------
    - principal_id: the ID of the principal (user, role, etc.) that the authorization
      request refers to;
    - action: the action that the authorization request refers to (usually
      "execute-api:Invoke");
    - effect: the effect of the IAM policy (either "Allow" or "Deny");
    - resource: the resource that the authorization request refers to. This is usually
      the ARN of a method execution descriptor over a resource of an API (e.g.,
      "arn:aws:execute-api:us-east-1:123456789012:ivdtdhp7b5/ESTestInvoke-stage/GET/");
    - response_context: a dictionary containing additional information to be sent back
      to the initiator of the authorization request.
    """

    auth_response = {"principalId": principal_id}

    if effect and resource:
        auth_response["policyDocument"] = {
            "Version": "2012-10-17",
            "Statement": [{"Action": action, "Effect": effect, "Resource": resource}],
        }

    if response_context:
        auth_response["context"] = response_context

    return auth_response


def generate_allow_auth_response(
    principal_id,
    action=ACTION_EXECUTE_API_INVOKE,
    resource="",
    response_context: dict | None = None,
):
    """
    A shortcut method that generates an IAM policy allowing the principal (user, role,
    etc.) with the given ID to proceed with an action on a resource.
    Designed to be used in Lambda functions underlying API Gateway Lambda authorizers.
    """

    return generate_auth_response_as_iam_policy(
        principal_id, action, EFFECT_ALLOW, resource, response_context
    )


def generate_deny_auth_response(
    principal_id,
    action=ACTION_EXECUTE_API_INVOKE,
    resource="",
    response_context: dict | None = None,
):
    """
    A shortcut method that generates an IAM policy denying the principal (user, role,
    etc.) with the given ID to proceed with an action on a resource.
    Designed to be used in Lambda functions underlying API Gateway Lambda authorizers.
    """

    return generate_auth_response_as_iam_policy(
        principal_id, action, EFFECT_DENY, resource, response_context
    )
