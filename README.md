### MCMBM (My Course Must Be Mine)

> 一个面向山东大学大学生的抢课脚本。

### 环境要求 ENVIRONMENT REQUIREMENT

* Python 3.x

### 使用方法 HOW TO USE

1. 下载choose_course.py
2. 进入脚本所在目录，打开命令行
3. 运行命令``` python choose_course.py```，如果报错，请尝试```python3 choose_course.py```
4. 根据提示完成输入，开始抢课

**注意，抢课过程中请不要关闭程序**

### 部分参数修改方法 PARAMS MODIFY
* 抢课间隔

 抢课间隔默认为3s，即每3秒向服务器发送一次选课请求。如果你想改变这一参数，请修改```start_fucking_the_server()```函数中的```time.sleep(3)```语句，把数字3修改为你想要的时间间隔即可，单位为秒。注意，请不要把时间间隔设置为1.8及以下的数字，因为这会触发选课服务器的访问频率限制，导致抢课失败。**我们强烈建议使用“3秒”作为时间间隔，因为这足够安全，并且能保证令人满意的抢课效率。**

### 更新日志 CHANGE LOG

#### 2018年1月13日
* 初始版本
