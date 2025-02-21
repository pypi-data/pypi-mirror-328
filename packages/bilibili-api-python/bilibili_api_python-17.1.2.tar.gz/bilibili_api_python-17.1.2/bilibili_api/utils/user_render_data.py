import json
from re import Match, Pattern, compile
from typing import Any
from urllib.parse import unquote

from ..exceptions import ApiException, NetworkException
from .network import HEADERS, get_client

RENDER_DATA_PATTERN: Pattern[str] = compile(
    r"<script id=\"__RENDER_DATA__\" type=\"application/json\">(.*?)</script>"
)


async def get_user_dynamic_render_data(uid: int) -> dict[str, Any]:
    """
    获取用户动态页面加载静态渲染数据 获取部分接口需要的 w_webid 关键参数

    :param uid: 用户ID 示例参数: 208259
    :return: 用户动态页面服务端渲染提取数据结构
    """

    dynamic_url: str = "https://space.bilibili.com/{}/dynamic".format(uid)

    session = get_client()
    response = await session.request(method="GET", url=dynamic_url, headers=HEADERS)
    if response.code != 200:
        raise NetworkException(response.code, "")

    response_content_text: str = response.utf8_text()
    match: Match = RENDER_DATA_PATTERN.search(response_content_text)
    if match is None:
        raise ApiException("未匹配到用户动态页渲染数据")

    script_render_data: str = match.group(1)
    try:
        extract_json = json.loads(unquote(script_render_data))
        return extract_json
    except json.JSONDecodeError as e:
        raise ApiException("序列化用户动态页渲染数据异常" + str(e))
