# jd-data-collection
京东(京麦)后台数据采集工具

## 安装
```bash
pip install jd-data-collection
```

## 使用方法
### 连接浏览器
```python
from JdDataCollection import Collector

collector = Collector()
collector.connect_browser(port=9527)
```

### 下载客服绩效文件
```python
shop_name, file_path = collector.customer_service.reception_data.download__customer_service__detail(
    date='2025-02-06',
    save_path=r'C:\Users\sanrose\Desktop\temp\客服数据报表',
    save_name='京东_客服数据_20250206',
    open_page=False,
    get_shop_name=True
)
```