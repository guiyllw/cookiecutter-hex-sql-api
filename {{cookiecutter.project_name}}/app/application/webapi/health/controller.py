from http import HTTPStatus

from fastapi_utils.cbv import cbv
from fastapi_utils.inferring_router import InferringRouter

router = InferringRouter()


@cbv(router)
class HealthCBV:

    @router.get('/')
    async def health_check(self, status_code=HTTPStatus.OK) -> str:
        """Health check route"""
        return 'Ok'
