# 豆瓣电影

## 一、hot

### 1：技术栈

- py3.6+requests

### 2：实现的功能

获取正在热映的电影:
接口：<https://api.douban.com/v2/movie/in_theaters>
访问参数：

- start : 数据的开始项
- count：单页条数
- city：城市

如：获取 广州热映电影 第一页 10条数据：
<https://api.douban.com/v2/movie/in_theaters?city=广州&start=0&count=10>

## 二、top250

### 功能

接口：<https://api.douban.com/v2/movie/top250>
访问参数：

- start : 数据的开始项
- count：单页条数
  
如：获取电影Top250 第一页 10条数据：<https://api.douban.com/v2/movie/top250?start=0&count=10>

## 三、5W+animation

### 1：技术

- py3.6+requests+selenium
 selenium使用:下载驱动，然后将驱动文件路径配置在环境变量即可
[chromedriver](https://www.cnblogs.com/qingqing-919/p/9055285.html)
[驱动下载](http://chromedriver.storage.googleapis.com/index.html)
[selenium 安装与 chromedriver安装](https://www.cnblogs.com/technologylife/p/5829944.html#3919615)
接着需要将下载的chromedriver进行解压，并将文件复制或移动到，浏览器快捷方式所在目录。此时环境搭建完成。

### 2：功能

爬取评论数超过5W的电影

[豆瓣API实践项目](https://blog.csdn.net/mario_faker/article/details/79618235)