from sqlalchemy import Column, Identity, Integer, String, Table

from . import metadata

SourceCodeVerificationFlow.Json = Table(
    "source_code_verification_flow.json",
    metadata,
    Column(
        "attempts_remaining",
        Integer,
        comment="The number of attempts remaining to authenticate the source object with a verification code",
    ),
    Column(
        "status",
        String,
        comment="The status of the code verification, either `pending` (awaiting verification, `attempts_remaining` should be greater than 0), `succeeded` (successful verification) or `failed` (failed verification, cannot be verified anymore as `attempts_remaining` should be 0)",
    ),
    Column("id", Integer, primary_key=True, server_default=Identity()),
)
__all__ = ["source_code_verification_flow.json"]
