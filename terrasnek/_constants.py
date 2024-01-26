"""
Constants for default values on the TFC API endpoints

"""

from enum import Enum
import logging


# Default Config Items
PROJECT_NAME = "terrasnek"
TFC_SAAS_HOSTNAME = "app.terraform.io"
TFC_SAAS_URL = "https://app.terraform.io"
TERRASNEK_LOG_LEVEL = logging.CRITICAL
TERRASNEK_VERSION = "0.1.13"
MAX_PAGE_SIZE = 100

# Common TFC API HTTP Codes
HTTP_OK = 200
HTTP_CREATED = 201
HTTP_ACCEPTED = 202
HTTP_NO_CONTENT = 204
HTTP_MOVED_PERMANENTLY = 301
HTTP_MOVED_TEMPORARILY = 302
HTTP_NOT_MODIFIED = 304
HTTP_TEMPORARY_REDIRECT = 307
HTTP_NOT_MODIFIED = 304
HTTP_BAD_REQUEST = 400
HTTP_UNAUTHORIZED = 401
HTTP_FORBIDDEN = 403
HTTP_NOT_FOUND = 404
HTTP_CONFLICT = 409
HTTP_PRECONDITION_FAILED = 412
HTTP_UNPROCESSABLE_ENTITY = 422
HTTP_API_REQUEST_RATE_LIMIT_REACHED = 429
HTTP_INTERNAL_SERVER_ERROR = 500


class Entitlements(Enum):
    """
    Enumeration of all the possible Terraform Cloud Entitlements, to be used
    on each endpoint to indicate the required entitlements to use that piece
    of the Terraform Cloud API.

    [Entitlements Docs](https://www.terraform.io/docs/cloud/api/index.html)
    """

    AGENTS = "AGENTS"
    ASSESSMENTS = "ASSESSMENTS"
    AUDIT_LOGGING = "AUDIT_LOGGING"
    CAN_APPLY = "CAN_APPLY"
    CONFIGURATION_DESIGNER = "CONFIGURATION_DESIGNER"
    COST_ESTIMATION = "COST_ESTIMATION"
    EPHEMERAL_WORKSPACES = "EPHEMERAL_WORKSPACES"
    # TODO: use this in the module tests code?
    MODULE_TESTS_GENERATION = "MODULE_TESTS_GENERATION"
    OPERATIONS = "OPERATIONS"
    POLICY_ENFORCEMENT = "POLICY_ENFORCEMENT"
    PRIVATE_MODULE_REGISTRY = "PRIVATE_MODULE_REGISTRY"
    PRIVATE_NETWORKING = "PRIVATE_NETWORKING"
    RUN_TASKS = "RUN_TASKS"
    RUN_TASK_LIMIT = "RUN_TASK_LIMIT"
    RUN_TASK_MANDATORY_ENFORCEMENT_LIMIT = "RUN_TASK_MANDATORY_ENFORCEMENT_LIMIT"
    RUN_TASK_WORKSPACE_LIMIT = "RUN_TASK_WORKSPACE_LIMIT"
    POLICY_LIMIT = "POLICY_LIMIT"
    POLICY_MANDATORY_ENFORCEMENT_LIMIT = "POLICY_MANDATORY_ENFORCEMENT_LIMIT"
    POLICY_SET_LIMIT = "POLICY_SET_LIMIT"
    PRIVATE_POLICY_AGENTS = "PRIVATE_POLICY_AGENTS"
    SELF_SERVE_BILLING = "SELF_SERVE_BILLING"
    SENTINEL = "SENTINEL"
    STATE_STORAGE = "STATE_STORAGE"
    SSO = "SSO"
    TEAMS = "TEAMS"
    USER_LIMIT = "USER_LIMIT"
    USAGE_REPORTING = "USAGE_REPORTING"
    VCS_INTEGRATIONS = "VCS_INTEGRATIONS"
    VERSIONED_POLICY_SET_LIMIT = "VERSIONED_POLICY_SET_LIMIT"
    VIEWABLE_BILLING = "VIEWABLE_BILLING"
