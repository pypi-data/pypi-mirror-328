"""Docker Hub"""
import requests
from loguru import logger


def get_latest_tags(url: str, limit: int = 20, proxies: dict | None = None) -> list | None:

    info: str = "获取最新标签"

    try:

        logger.info(f"{info} [begin]")

        # url = "https://hub.docker.com/v2/repositories/library/postgres/tags"

        # 配置代理
        # proxies = {
        #     "http": "http://127.0.0.1:1087",
        #     "https": "http://127.0.0.1:1087",
        # }

        # 请求接口
        response = requests.get(url, params={"page": 1, "page_size": limit}, proxies=proxies, timeout=10)

        # 检查请求状态码
        if response.status_code != 200:
            logger.error(f"{info} [请求接口错误, 状态码: {response.status_code}]")
            return None

        # 转换格式
        data: dict = response.json()

        results = data.get("results")

        if results is None:
            logger.error(f"{info} [请求结果错误]")
            return None

        # 提取 tags
        tags = [tag["name"] for tag in results]

        logger.success(f"{info} [success]")
        return tags

    except Exception as e:
        logger.error(f"{info} [error]")
        logger.exception(e)
        return None
