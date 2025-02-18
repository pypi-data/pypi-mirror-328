"""
客服接待数据采集
"""

from DrissionPage import Chromium

from .._utils import Utils


class Urls:
    reception_data = (
        'https://shop.jd.com/jdm/kefu/kf-manage-lite/#/DataAnalysis/ReceptionData'
    )


class DataPacketUrls:
    overview = 'https://kf.jd.com/jingmai/T1/indicatorList'
    customer_service__detail__download = (
        'https://kf.jd.com/jingmai/T1/waiterDimIndicatorExport'
    )


class ReceptionData:
    def __init__(self, browser: Chromium):
        self._browser = browser
        self._timeout = 15

    def download__customer_service__detail(
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
        下载客服数据详情表单文件

        Args:
            download_timeout: 下载超时时间, 默认 120 秒
            open_page: 是否打开页面, 如果为 False 则使用当前激活的页面
            get_shop_name: 是否获取店铺名称, 默认 False
        Returns:
            - 如果 get_shop_name 为 True, 则返回 (店铺名称, 下载的文件路径)
            - 否则仅返回 文件路径
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
                targets=DataPacketUrls.overview,
                method='GET',
                res_type='XHR',
            )
            page.get(Urls.reception_data)
            if not page.listen.wait(timeout=_timeout):
                raise TimeoutError('首次进入页面获取数据超时, 可能页面访问失败')

        download_btn = page.ele('t:button@@text()=导出Excel', timeout=3)
        if not download_btn:
            raise RuntimeError('未找到 [导出Excel] 按钮')

        query_params = {'startTime': date, 'endTime': date}
        download_url = Utils.url__append_params(
            DataPacketUrls.customer_service__detail__download, query_params
        )
        result: tuple[str, str] = page.download(
            file_url=download_url,
            save_path=save_path,
            rename=save_name,
            file_exists='overwrite',
            show_msg=False,
            timeout=_download_timeout,
        )
        if result[0] != 'success':
            raise RuntimeError('文件下载失败')

        file_path = result[1]
        if get_shop_name is not True:
            return file_path

        def get__shop_name():
            """获取店铺名称"""
            shop_name_ele = page.ele(
                'c:span.shop-menu-account__right-account-top-name', timeout=3
            )
            if not shop_name_ele:
                return
            return shop_name_ele.attr('title')

        shop_name = get__shop_name()

        return shop_name, file_path
