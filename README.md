## 通过计算文本余弦值来求文本相似度

使用步骤：

- 1.配置`config.py`中的缓存目录`CACHE_PATH`（默认值是'./cache'）以及文本数据目录`ARTICLE_PATH`（默认值是'./data/article'）:

``` python
# 设置缓存目录
CACHE_PATH = project_dir + os.path.sep + "cache"

# 设置文本目录
ARTICLE_PATH = project_dir + os.path.sep + "data/article"
```

- 2.在文本目录下填充一些待训练的英文文本数据。目前默认有26片文章，可自行增添或者删除。

- 3.运行`pipline/main.py`，即可开始训练数据。最终会获取到一个已经排好序的列表：

```
[('11', '12', 0.9994788059135834), ('12', '11', 0.9994788059135834),...]
```

其中每个条目都是一个元组，元组的前两个元素是两篇文章的名字，第三个元素是这两篇文章的TF-IDF值。该值越大，代表文章越相似，且最大值不可能超过1。

> 小技巧：由于计算过程中，有缓存逻辑，所以可以随时中断计算，下次继续执行时会从缓存的数据处开始继续运算。
> 
> 注意：如果文章数据源有变动，或者想要重新训练，需要删除`缓存目录`。

----

## 缓存控件@cache介绍：

使用方式：

```
from utils.cache import cache

@cache(use_mem=True, use_file=True, print_log=False)
def get_data():
	# 复杂耗时的计算逻辑
	...
	return data
```

`@cache()`会将函数的返回值缓存起来，下次执行时，如果已缓存，则跳过程序的执行，直接从缓存中取数据。

`use_mem=True`：是否使用内存缓存

`use_file=True`： 是否使用文本缓存

`print_log=True`:	是否打印过程中的日志