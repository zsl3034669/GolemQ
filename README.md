# GolemQ
A PowerToys based QUANTAXIS

这是一个基于 QUANTAXIS 二次开发的量化系统子项目

发起这个子项目的原因是我开发了代码功能存在跟天神原始设计不相同的；或者规划路线图跟天神设计理念不同的；或者依赖或者模仿第三方量化平台接口的(我担心有法律之类的风险，所以也不适合PR到QUANTAXIS)。有的功能和代码因为我不是金融科班出身，也不知道现在的前沿趋势，贸然PR到QUANTAXIS，然后又自己发觉功能不妥或者不实用，然后又匆忙在QUANTAXIS中移除。再比如一部分功能代码我设计为cli命令行格式运行，而QA主要设计为Docker发布运行。

这导致了一部分代码因为现实需求被我写出来，正在使用，但是跟QA风格并不匹配，而没有办法在Docker的HTML前端中顺利使用，暂时我也没相处好办法和QUANTAXIS 进行 PR 合并。

但是又有很多朋友问这些常用的功能使用情况，为了发布我不得不打包代码，索性发布自己的第一个Git项目吧，也算是人生头一回原创 Git仓库了。

功能包括：

来源新浪财经的A股实盘行情 l1快照数据
在 repo 根目录下面，输入
python -m GolemQ.cli --sub sina_l1

已知Bug：
上证指数 000001 实盘走势和平安银行混淆。
成交量：Volumne和Amount 计算方式不对。

读取实盘行情数据K线
在 repo 根目录下面，输入
python -m GolemQ.GQTest.GQFetch_test.realtime

模仿优矿DataAPI数据接口
挖了坑，未完成，待续

计划
模仿聚宽API接口——To be continue...

Firstblood!

By 阿财 
2020.10.14
