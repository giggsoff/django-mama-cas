"""
(2.5.3, 2.7.3) Exceptions for ticket validation failure responses
with the set of error codes that all CAS servers must implement.
"""


class ValidationError(Exception):
    """Base exception class for ticket validation failures."""


class InvalidRequest(ValidationError):
    """Not all of the required request parameters were present."""
    code = 'INVALID_REQUEST'


class InvalidTicket(ValidationError):
    """
    The ticket provided was not valid, or the ticket did not come
    from an initial login and renew was set on validation.
    """
    code = 'INVALID_TICKET'


class InvalidService(ValidationError):
    """
    The service specified did not match the service identifier
    associated with the ticket.
    """
    code = 'INVALID_SERVICE'


class InternalError(ValidationError):
    """An internal error occurred during ticket validation."""
    code = 'INTERNAL_ERROR'


class BadPgt(ValidationError):
    """The PGT provided was invalid."""
    code = 'BAD_PGT'
