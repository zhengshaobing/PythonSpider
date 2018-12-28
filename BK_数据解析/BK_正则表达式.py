import re


text = "apple's price is $565 ,orange's price is $6.2"
# 1.'*'可以匹配任意多字符
# ret = re.match('\d*',text)
# print(ret.group())
# 2.'+'可以匹配1个或多个字符
# ret = re.match('\w+',text)
# print(ret.group())
# 3.'?'匹配一个或者0个
# ret = re.match('\w?',text)
# print(ret.group())
# 4.'{m}'匹配m个字符
# ret = re.match('\d{4}',text)
# print(ret.group())
# 5.'{m,n}匹配m-n个字符
# ret = re.match('\d{2,3}',text)
# print(ret.group())
# 6.'^'指定开始字符,在中括号中表示取反操作
# ret = re.match('9{2,9}',text)
# print(ret.group())
# 7.'$'指定结尾字符
# ret = re.match('\w+@qq.com$',text)
# print(ret.group())
# 8.'|'匹配多个表达式或者字符串
# ret = re.match('(http|https|ftp)',text)
# print(ret.group())
# 9.贪婪模式'+'和非贪婪模式'+?'
# ret1 = re.match('<.+>',text)
# print(ret1.group())
# ret = re.match('<.+?>',text)
# print(ret.group())
# 10.'\' 转义字符
# ret = re.search('\$\d+',text)
# print(ret.group())

'''
小案例

# 1.验证手机号码
# ret = re.match('1[34578]\d{9}',text)
# print(ret.group())
# 2.验证邮箱
# ret = re.match('\w+@[a-z0-9]+\.[a-z]+',text)
# print(ret.group())
# 3.验证url
# ret = re.match('(http|https|ftp)://[^\s ]+',text)
# print(ret.group())
# 4.验证身份证
# ret = re.match('\d{17}[0-9xX]',text)
# print(ret.group())
# 5.匹配0-100之间的数字
# ret = re.match('[1-9]\d?$|100$',text)
# print(ret.group())
'''

'''
re 模块常用的函数
'''
# 1.group正则表达式分组,用圆括号括起来,一个括号表示一个分组,以_sre.SRE_Match返回
# ret = re.match('.*(\$\d+).*(\$\d+.\d+)',text)
# print(type(ret))
# print(ret.group(2))
# 2.findall函数,能找到所有满足表达式的部分,并且以列表形式返回
# ret = re.findall('\$\d+',text)
# print(ret)
# 3.sub函数用来替换字符串,把目标字符串替换为指定字符串,并且以列表形式返回
# ret = re.sub('\$\d+','0',text)
# print(ret)
# html = '''
# <dd class="job_bt">
#         <h3 class="description">职位描述：</h3>
#         <div>
#         <p>【职位诱惑】：&nbsp;</p>
# <p>公司技术氛围浓厚，团队内部和整个技术团队都会定期组织分享 扁平化管理，免费三餐，团建集体出游</p>
# <p><br></p>
# <p>【岗位职责】:</p>
# <p>1、云服务（服务化）开发，微服务和devops&nbsp;；</p>
# <p>2、后端功能/工具的调研和开发；</p>
# <p>3、负责代码架构设计和搭建，参与关键技术难点攻克；</p>
# <p>4、对代码质量负责，参与实现正确、高效、稳定的应用。</p>
# <p><br></p>
# <p>【任职资格】:</p>
# <p>1、&nbsp;统招本科及以上学历，计算机或相关专业；</p>
# <p>2、&nbsp;精通&nbsp;Python&nbsp;语言,&nbsp;工作/生活中遇到特定问题时，可快速通过编写代码解决；</p>
# <p>3、&nbsp;了解操作系统原理，熟悉进程和线程之间的主要特性和通信方式；</p>
# <p>4、&nbsp;熟练&nbsp;使用至少一种Web框架&nbsp;及&nbsp;MySQL、Redis、MongoDB、RabbitMQ&nbsp;等资源类组件；</p>
# <p>5、&nbsp;以&nbsp;Unix-like&nbsp;OS&nbsp;为工作平台，具备简单的shell/vim能力，熟练使用&nbsp;Git；</p>
# <p>6、&nbsp;有过容器云产品的开发/使用经验者优先；</p>
# <p>7、&nbsp;具有良好的编程思想、沟通、团队合作精神、优秀的分析问题和解决问题的能力。</p>
# <p><br></p>
# <p>【职位卖点】：</p>
# <p>这是一个技术驱动的团队,在这里你就是技术的引领者； 简单，高效是我们做事的风格; 在这里你可以快速的成长，快乐的交流，自由释放你的思想; 待遇不含糊:豪华自助午餐，6险1金，年度旅游等福利保证让你满意。</p>
#         </div>
#     </dd>
# '''
# ret = re.sub('<.+?>','',html)
# print(ret)
# 4.split函数,已制定字符分隔割字符串，并以列表形式传回
# ret = re.split(' ', text)
# print(ret)
# 5.compile函数
# r = re.compile('.*(\$\d+\.?\d+).*(\$\d+\.?\d+)')
# ret = re.search(r,text)
# print(ret.group())
# r = re.compile(r'''
# .*#匹配任意字符
# (\$\d# 小数点前面的数
# +\.?# 小数点可有可无
# \d+)# 小数点后面的数
# .*(\$\d+\.?\d+)''', re.VERBOSE)
# ret = re.search(r,text)
# print(ret.group())
