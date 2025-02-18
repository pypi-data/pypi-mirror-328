"""
客服数据模块数据采集
"""

import json

from DrissionPage import Chromium

from ._utils import pick__custom_date


class Urls:
    performance = 'https://ark.xiaohongshu.com/app-datacenter/customer-performance'


class DataPacketUrls:
    performance__detail = (
        'https://ark.xiaohongshu.com/api/edith/butterfly/data?type=sellerCSUserDataList'
    )


class CustomerService:
    def __init__(self, browser: Chromium):
        self._browser = browser
        self._timeout = 15

    def download__performance__detail(
        self,
        date: str,
        save_path: str,
        save_name: str,
        timeout: float = None,
        download_timeout: float = None,
        open_page=False,
        get_shop_name=False,
    ) -> tuple[str | None, str] | str:
        """
        下载客服绩效数据详情表单文件

        Args:
            download_timeout: 下载超时时间, 默认 120 秒
            open_page: 是否打开页面, 如果为 False 则使用当前激活的页面
            get_shop_name: 是否获取店铺名称, 默认为 False
        Returns:
            - 如果 get_shop_name 为 True, 返回 (店铺名称, 下载的文件路径)
            - 否则仅返回店铺名称
        """

        _timeout = timeout if isinstance(timeout, (int, float)) else self._timeout
        _download_timeout = (
            download_timeout if isinstance(download_timeout, (int, float)) else 120
        )

        page = (
            self._browser.new_tab() if open_page is True else self._browser.latest_tab
        )
        if open_page is True:
            page.listen.start(
                targets=DataPacketUrls.performance__detail,
                method='POST',
                res_type='XHR',
            )
            page.get(Urls.performance)
            if not page.listen.wait(timeout=_timeout):
                raise TimeoutError('首次进入页面获取数据超时, 可能页面访问失败')

        download_btn = page.ele('t:span@@text()=下载数据', timeout=3)
        if not download_btn:
            raise RuntimeError('未找到 [下载数据] 按钮')

        page.listen.start(
            targets=DataPacketUrls.performance__detail, method='POST', res_type='XHR'
        )
        pick__custom_date(date, page)
        packet = page.listen.wait(timeout=_timeout)
        if not packet:
            raise TimeoutError('修改日期后数据获取超时')

        req_data: dict = packet.request.postData
        try:
            req_date = req_data['requestBody']['blockElements'][0]['filterMap']['date']
            if req_date != date:
                raise ValueError('当前日期与统计日期不符')
        except ValueError as e:
            raise e
        except Exception as e:
            raise RuntimeError(f'修改日期之后数据请求参数解析出错: {e}') from e

        page.set.download_path(save_path)
        page.set.download_file_name(save_name)
        download_btn.click(by_js=True)
        mission = page.wait.download_begin(timeout=_download_timeout)
        if not page.wait.downloads_done():
            raise TimeoutError('下载超时')

        result = file_path = mission.final_path

        if get_shop_name is True:

            def get__shop_name():
                """获取店铺名称"""
                user_info = page.session_storage('ark_cache_user_info_v2')
                if not user_info:
                    return
                try:
                    user_info: dict = json.loads(user_info)
                except json.JSONDecodeError:
                    return

                seller_name: str = user_info.get('sellerName')
                return seller_name

            shop_name = get__shop_name()
            result = shop_name, file_path

        if open_page is True:
            page.close()

        return result
