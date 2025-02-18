# xhs-data-collection
小红书后台数据采集工具

## 安装
```bash
pip install xhs-data-collection
```

## 使用方法
### 连接浏览器
```python
from XhsDataCollection import Collector

collector = Collector()
collector.connect_browser(port=9527)
```

### 下载客服绩效文件
```python
shop_name, file_path = collector.service.customer_service.download__performance__detail(
    date='2025-02-05',
    save_path=r'C:\Users\sanrose\Desktop\temp',
    save_name='小红书客服数据_20250205',
    open_page=True,
    get_shop_name=True
)
```