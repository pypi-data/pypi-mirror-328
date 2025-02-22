# Tuner
Tuner is an automation testing framework based on behave.

> Tuner 是基于behave 的自动化测试框架。

### Features

⭐ API单元测试
* 生成项目脚手架
* DSL语法并开始工作
⭐ API集成测试
* AOM脚手架
⭐ Web UI 自动化测试
* POM脚手架

2、创建项目：

```shell
> tuner --project-apitest myapi  # API automation test project.
```

目录结构如下：

```shell
myapi/
├── test_dir/
│   ├── __init__.py
│   └── test_sample.py
├── test_data/
│   └── data.json
├── reports/
└── confrun.py
```

* `test_dir/` 测试用例目录。
* `test_data/` 测试数据文件目录。
* `reports/` 测试报告目录。
* `confrun.py` 运行配置文件。

3、运行项目：

* ❌️ 在`PyCharm`中右键执行。

* ✔️ 通过命令行工具执行。

```shell
> seldom -p test_dir # 运行 test_dir 测试目录


              __    __
   ________  / /___/ /___  ____ ____
  / ___/ _ \/ / __  / __ \/ __ ` ___/
 (__  )  __/ / /_/ / /_/ / / / / / /
/____/\___/_/\__,_/\____/_/ /_/ /_/  v3.x.x
-----------------------------------------
                             @itest.info
...

2022-04-30 18:37:36 log.py | INFO | ✅ Find 1 element: id=sb_form_q  -> input 'seldom'.
2022-04-30 18:37:39 log.py | INFO | 👀 assertIn title: seldom - 搜索.
.52022-04-30 18:37:39 log.py | INFO | 📖 https://cn.bing.com
2022-04-30 18:37:41 log.py | INFO | ✅ Find 1 element: id=sb_form_q  -> input 'poium'.
2022-04-30 18:37:42 log.py | INFO | 👀 assertIn title: poium - 搜索.
.62022-04-30 18:37:42 log.py | INFO | 📖 https://cn.bing.com
2022-04-30 18:37:43 log.py | INFO | ✅ Find 1 element: id=sb_form_q  -> input 'XTestRunner'.
2022-04-30 18:37:44 log.py | INFO | 👀 assertIn title: XTestRunner - 搜索.
.72022-04-30 18:37:44 log.py | INFO | 📖 http://www.itest.info
2022-04-30 18:37:52 log.py | INFO | 👀 assertIn url: http://www.itest.info/.
.82022-04-30 18:37:52 log.py | SUCCESS | generated html file: file:///D:\mypro\reports\2022_04_30_18_37_29_result.html
2022-04-30 18:37:52 log.py | SUCCESS | generated log file: file:///D:\mypro\reports\seldom_log.log
```

4、查看报告

你可以到 `mypro\reports\` 目录查看测试报告。

![test report](./test_report.png)

## 🔬 Demo

> seldom继承unittest单元测试框架，完全遵循unittest编写用例规范。

[demo](/demo) 提供了丰富实例，帮你快速了解seldom的用法。



### HTTP 测试

seldom 2.0 支持HTTP测试

```python
import seldom


class TestRequest(seldom.TestCase):

    def test_put_method(self):
        self.put('/put', data={'key': 'value'})
        self.assertStatusCode(200)

    def test_post_method(self):
        self.post('/post', data={'key': 'value'})
        self.assertStatusCode(200)

    def test_get_method(self):
        payload = {'key1': 'value1', 'key2': 'value2'}
        self.get("/get", params=payload)
        self.assertStatusCode(200)

    def test_delete_method(self):
        self.delete('/delete')
        self.assertStatusCode(200)


if __name__ == '__main__':
    seldom.main(base_url="http://httpbin.org")
```

### 项目实例

基于seldom的web UI自动化项目：

https://github.com/SeldomQA/seldom-web-testing

基于seldom的接口自动化项目:

https://github.com/defnngj/seldom-api-testing

