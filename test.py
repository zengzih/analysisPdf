#!/usr/bin/env python
# -*- coding: utf-8 -*-
import re
import json
from decimal import Decimal

'''
21 22 23
母公司报表  y

19  关键审计事项说明

57 定代表人：张国义主管会计工作负责人：张国义会计机构负责人：吴蓉（三）合并利润表 y

64 合并股东权益变动表  y

68 母公司股东权益变动表  y

95 首次执行新金融工具准则调整首次执行当年年初财务报表相关项目情况 y

99 主要税种及税率 y 

102 上述款项期后回款 20,546,691.30 元，期后回款部分不存在收回风险，不计提坏账准备。

103 坏账准备的情况 y

115 递延收益 y


基本信息 

商业模式

项目重大变动原因

资产负债项目重大变动原因：

经营计划

业模式未发生变化。

款期末余额16.40%；云锡文山锌 合并

经营计划或目标

三会召开情况
------------------------------------------------------
利润构成


'''

