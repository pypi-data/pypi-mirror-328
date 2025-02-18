import traceback
from typing import Tuple
from collections.abc import Iterable
from papys.http_methods import GET, POST, PUT, DELETE
from papys.hooks import PHook
from papys.request_response import Request, Response

AUTH_ALLOW = "allow"
AUTH_DENY = "deny"


class KcOIDCAuthorizationHook(PHook):
    def __init__(self):
        super().__init__()
        self._type: str = AUTH_ALLOW
        self._user_info_group_attribute_name: str = "roles"
        self._GET_groups: set = set()
        self._POST_groups: set = set()
        self._PUT_groups: set = set()
        self._DELETE_groups: set = set()
        self._add_user_sub_to_body: bool = False
        self._user_id_body_attribute_name: str | None = "user_id"

    @property
    def type(self) -> str:
        return self._type

    @type.setter
    def type(self, value: str) -> None:
        self._type = value

    @property
    def user_info_group_attribute_name(self) -> str:
        return self._user_info_group_attribute_name

    @user_info_group_attribute_name.setter
    def user_info_group_attribute_name(self, value: str) -> None:
        self._user_info_group_attribute_name = value

    @property
    def GET_groups(self) -> set:
        return self._GET_groups

    @GET_groups.setter
    def GET_groups(self, value: set) -> None:
        self._GET_groups = value

    @property
    def POST_groups(self) -> set:
        return self._POST_groups

    @POST_groups.setter
    def POST_groups(self, value: set) -> None:
        self._POST_groups = value

    @property
    def PUT_groups(self) -> set:
        return self._PUT_groups

    @PUT_groups.setter
    def PUT_groups(self, value: set) -> None:
        self._PUT_groups = value

    @property
    def DELETE_groups(self) -> set:
        return self._DELETE_groups

    @DELETE_groups.setter
    def DELETE_groups(self, value: set) -> None:
        self._DELETE_groups = value

    @property
    def add_user_sub_to_body(self) -> bool:
        return self._add_user_sub_to_body

    @add_user_sub_to_body.setter
    def add_user_sub_to_body(self, value: bool) -> None:
        self._add_user_sub_to_body = value

    @property
    def user_id_body_attribute_name(self) -> str | None:
        return self._user_id_body_attribute_name

    @user_id_body_attribute_name.setter
    def user_id_body_attribute_name(self, value: str | None) -> None:
        self._user_id_body_attribute_name = value

    def process_hook(
        self, req: Request, resp: Response
    ) -> Tuple[bool, int, Request, Response]:
        try:
            user_groups = req.user_info[self.user_info_group_attribute_name]
            if isinstance(user_groups, Iterable):
                user_groups_set = set(user_groups)
                match req.request_method:
                    case "GET":
                        group_check = len(user_groups_set & self.GET_groups)
                    case "POST":
                        group_check = len(user_groups_set & self.POST_groups)
                    case "PUT":
                        group_check = len(user_groups_set & self.PUT_groups)
                    case "DELETE":
                        group_check = len(user_groups_set & self.DELETE_groups)
                    case _:
                        raise ValueError(
                            f"Not supported http method found: {req.request_method}."
                        )

                match (self.type, group_check):
                    case ("allow", n) if n > 0:
                        if self.add_user_sub_to_body and req.body_json:
                            req.body_json[self.user_id_body_attribute_name] = (
                                req.user_info["sub"]
                            )
                        return True, 200, req, resp
                    case ("allow", n) if n < 1:
                        return False, 401, req, resp
                    case ("deny", n) if n < 1:
                        if self.add_user_sub_to_body and req.body_json:
                            req.body_json[self.user_id_body_attribute_name] = (
                                req.user_info["sub"]
                            )
                        return True, 200, req, resp
                    case ("deny", n) if n > 0:
                        return False, 401, req, resp
                    case _:
                        return False, 401, req, resp
            else:
                return False, 401, req, resp
        except Exception as err:
            req.logger.log_error(
                "Failed to check user groups.", traceback.format_exc(), 180, req
            )
            return False, 500, req, resp
