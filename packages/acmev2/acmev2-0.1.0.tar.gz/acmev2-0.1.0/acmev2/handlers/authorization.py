import inject
from acmev2.errors import ACMEError
from acmev2.messages import AuthorizationMessage
from acmev2.models import AuthorizationStatus
from acmev2.services import IAuthorizationService
from .base import ACMERequestHandler, ACMEModelResponse


class AuthorizationRequestHandler(ACMERequestHandler):
    """Returns an authorization and all the associated challenges."""

    message_type = AuthorizationMessage
    authorization_service = inject.attr(IAuthorizationService)

    def process(self, msg: AuthorizationMessage):
        authz_resource = msg.resource

        if self.should_deactivate(msg):
            authz_resource = self.authorization_service.update_status(
                authz_resource, AuthorizationStatus.deactivated
            )

        return ACMEModelResponse(msg=authz_resource, code=200)

    def should_deactivate(self, msg: AuthorizationMessage) -> bool:
        if msg.payload.status == AuthorizationStatus.deactivated:
            if msg.resource.status == AuthorizationStatus.valid:
                return True

            # Invalid, cannot transition to deactivated from any state but valid
            raise ACMEError(
                detail=f"May not transition to '{AuthorizationStatus.deactivated.value}' from '{msg.resource.status.value}'"
            )

        return False
