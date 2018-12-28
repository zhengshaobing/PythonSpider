# encoding = utf-8
from bs4 import BeautifulSoup

html = """
<!DOCTYPE html PUBLIC "-//W3C//DTD XHTML 1.0 Transitional//EN" "http://www.w3.org/TR/xhtml1/DTD/xhtml1-transitional.dtd">
<html xmlns="http://www.w3.org/1999/xhtml">
<head>
    <title>职位搜索 | 社会招聘 | Tencent 腾讯招聘</title>
    <meta http-equiv="Content-Type" content="text/html; charset=utf-8" />
	<!-- Js Css -->
     		<link media="screen" href="//cdn.m.tencent.com/hr_static/css/all.css?max_age=86412" type="text/css" rel="stylesheet" />
	<script type="text/javascript" src="//cdn.m.tencent.com/hr_static/js/jquery-1.7.2.min.js"></script>
    <script type="text/javascript" src="//cdn.m.tencent.com/hr_static/js/jquery-ui-1.7.2.custom.min.js"></script>
    <script type="text/javascript" src="//cdn.m.tencent.com/hr_static/js/thickbox.js"></script>
    <link media="screen" href="//cdn.m.tencent.com/hr_static/css/thickbox.css" type="text/css" rel="stylesheet" />
    <script type="text/javascript" src="//cdn.m.tencent.com/hr_static/js/functions.js"></script>
    <script type="text/javascript" src="//cdn.m.tencent.com/hr_static/js/utils.js"></script>
    <script language="javascript" src="//vm.gtimg.cn/tencentvideo/txp/js/txplayer.js" charset="utf-8"></script>
    <script type="text/javascript" src="//cdn.m.tencent.com/hr_static/js/all.js?max_age=86412"></script>	<!-- Js Css -->
	<script>
		var keywords_json = ["python"];
	</script>
</head>

<body>
    	<div id="header">
    	<div class="maxwidth">
    		<a href="index.php" class="left" id="logo"><img src="//cdn.m.tencent.com/hr_static/img/logo.png"/></a>
    		<div class="right" id="headertr">
    			<div class="right pl9" id="topshares">
    				<div class="shares">
    					<span class="left">分享到：</span>
		    			<!--<a href="javascript:;" onclick="shareto('qqt','top');" id="qqt" title="分享到腾讯微博">分享到腾讯微博</a>-->
		    			<a href="javascript:;" onclick="shareto('qzone','top');" id="qzone" title="分享到QQ空间">分享到QQ空间</a>
		    			<!--<a href="javascript:;" onclick="shareto('pengyou','top');" id="pengyou" title="分享到腾讯朋友">分享到腾讯朋友</a>-->
		    			<a href="javascript:;"  onclick="shareto('sinat','top');"id="sinat" title="分享到新浪微博">分享到新浪微博</a>
		    			<!--<a href="javascript:;"  onclick="shareto('renren','top');"id="renren" title="分享到人人网">分享到人人网</a>-->
		    			<!--<a href="javascript:;"  onclick="shareto('kaixin001','top');"id="kaixin" title="分享到开心网">分享到开心网</a>-->
		    			<div class="clr"></div>
    				</div>
    				<!--<a href="javascript:;">分享</a>-->
    			</div>
    			<!--<div class="right pl9">-->
    				<!--<a href="http://t.qq.com/QQjobs" id="tqq" target="_blank">收听腾讯招聘</a>-->
    			<!--</div>-->
    			<div class="right pr9">
    				    				    					<a href="login.php" id="header_login_anchor">登录</a><span class="plr9">|</span><a href="reg.php">注册</a>
    				    				<span class="plr9">|</span><a href="question.php">反馈建议</a>
    				<span class="plr9">|</span><a href="http://careers.tencent.com/global" target="_blank">Tencent Global Talent</a>
    				<script>
    					var User_Account = "";
    				</script>
    				    			</div>
    			<div class="clr"></div>
    		</div>
    		<div class="clr"></div>
    	</div>
    	<div id="menus">
    		<div class="maxwidth">
	    		<ul id="menu" class="left">
	    			<li id="nav1" ><a href="index.php">&nbsp;</a></li>
	    			<li id="nav2" class="active" ><a href="social.php">&nbsp;</a></li>
	    			<li id="nav3"><a href="about.php">&nbsp;</a></li>
	    			<li id="nav4"><a href="workInTencent.php">&nbsp;</a></li>
	    		</ul>
	    		<a class="right texti9" target="_blank" id="navxy" href="http://join.qq.com">校园招聘</a>
	    		<div class="clr"></div>
	    	</div>
    	</div>
    </div>    <div id="sociaheader">
			</div>
    <div id="position" class="maxwidth">
    	<a name="a" id="a"></a>
    	<div class="left wcont_b box">
		    <div class="blueline"><div class="butzwss"></div></div>
		    <form id="searchform" class="buts1">
		    	<div id="searchrow1">
		    		<div id="search1"><input id="search2" name="keywords" t="请输入关键词" value="python" class="left"/><input class="left" id="search3" type="submit" value=""/><div class="clr"></div></div>
		    		<input type="hidden" name="lid" value="2156"/>
		    		<input type="hidden" name="tid" value="87"/>
		    	</div>
		    	<div id="searchrow2">
		    		<div class="srow2l left"></div>
		    		<div class="left items pl9 itemnone" id="additems">
		    			<a href="position.php?keywords=python&tid=87" class="item"><span><font>全部</font></span></a>
		    					    				<a class="item" href="position.php?keywords=python&tid=87&lid=2218"><span><font>深圳</font></span></a>
		    					    				<a class="item active" href="position.php?keywords=python&tid=87&lid=2156"><span><font>北京</font></span></a>
		    					    				<a class="item" href="position.php?keywords=python&tid=87&lid=2175"><span><font>上海</font></span></a>
		    					    				<a class="item" href="position.php?keywords=python&tid=87&lid=2196"><span><font>广州</font></span></a>
		    					    				<a class="item" href="position.php?keywords=python&tid=87&lid=2268"><span><font>成都</font></span></a>
		    					    				<a class="item" href="position.php?keywords=python&tid=87&lid=2355"><span><font>武汉</font></span></a>
		    					    				<a class="item" href="position.php?keywords=python&tid=87&lid=2426"><span><font>昆明</font></span></a>
		    					    				<a class="item" href="position.php?keywords=python&tid=87&lid=2459"><span><font>中国香港</font></span></a>
		    					    				<a class="item" href="position.php?keywords=python&tid=87&lid=33"><span><font>美国</font></span></a>
		    					    				<a class="item itemhide" href="position.php?keywords=python&tid=87&lid=32"><span><font>韩国</font></span></a>
		    					    				<a class="item itemhide" href="position.php?keywords=python&tid=87&lid=62"><span><font>欧洲</font></span></a>
		    					    				<a class="item itemhide" href="position.php?keywords=python&tid=87&lid=2252"><span><font>杭州</font></span></a>
		    					    				<a class="item itemhide" href="position.php?keywords=python&tid=87&lid=2226"><span><font>重庆</font></span></a>
		    					    				<a class="item itemhide" href="position.php?keywords=python&tid=87&lid=59"><span><font>日本</font></span></a>
		    					    				<a class="item itemhide" href="position.php?keywords=python&tid=87&lid=60"><span><font>马来西亚</font></span></a>
		    					    				<a class="item itemhide" href="position.php?keywords=python&tid=87&lid=2436"><span><font>贵阳</font></span></a>
		    					    				<a class="item itemhide" href="position.php?keywords=python&tid=87&lid=2442"><span><font>呼和浩特</font></span></a>
		    					    				<a class="item itemhide" href="position.php?keywords=python&tid=87&lid=95"><span><font>雄安新区</font></span></a>
		    					    				<a class="item itemhide" href="position.php?keywords=python&tid=87&lid=66"><span><font>印度尼西亚</font></span></a>
		    					    				<a class="item itemhide" href="position.php?keywords=python&tid=87&lid=90"><span><font>荷兰</font></span></a>
		    					    				<a class="item itemhide" href="position.php?keywords=python&tid=87&lid=2311"><span><font>南昌</font></span></a>
		    					    				<a class="item itemhide" href="position.php?keywords=python&tid=87&lid=2346"><span><font>郑州</font></span></a>
		    					    				<a class="item itemhide" href="position.php?keywords=python&tid=87&lid=2314"><span><font>南宁</font></span></a>
		    					    				<a class="item itemhide" href="position.php?keywords=python&tid=87&lid=2439"><span><font>兰州</font></span></a>
		    					    				<a class="item itemhide" href="position.php?keywords=python&tid=87&lid=2320"><span><font>合肥</font></span></a>
		    					    				<a class="item itemhide" href="position.php?keywords=python&tid=87&lid=2367"><span><font>长沙</font></span></a>
		    					    				<a class="item itemhide" href="position.php?keywords=python&tid=87&lid=2407"><span><font>大连</font></span></a>
		    					    				<a class="item itemhide" href="position.php?keywords=python&tid=87&lid=2453"><span><font>乌鲁木齐</font></span></a>
		    					    				<a class="item itemhide" href="position.php?keywords=python&tid=87&lid=45"><span><font>泰国</font></span></a>
		    					    				<a class="item itemhide" href="position.php?keywords=python&tid=87&lid=2294"><span><font>青岛</font></span></a>
		    					    				<a class="item itemhide" href="position.php?keywords=python&tid=87&lid=2406"><span><font>沈阳</font></span></a>
		    					    				<a class="item itemhide" href="position.php?keywords=python&tid=87&lid=2381"><span><font>西安</font></span></a>
		    					    				<a class="item itemhide" href="position.php?keywords=python&tid=87&lid=2393"><span><font>太原</font></span></a>
		    					    				<a class="item itemhide" href="position.php?keywords=python&tid=87&lid=2225"><span><font>天津</font></span></a>
		    					    		</div>
							    		<div class="left"><a href="javascript:;" class="more2">更多</a></div>
							    		<div class="clr"></div>
		    	</div>
		    	<div id="searchrow3">
		    		<div class="srow2l left"></div>
		    		<div class="left items pl9">
		    			<a href="position.php?keywords=python&lid=2156" class="item"><span><font>全部</font></span></a>
		    					    				<a class="item active" href="position.php?keywords=python&lid=2156&tid=87"><span><font>技术类</font></span></a>
		    					    				<a class="item" href="position.php?keywords=python&lid=2156&tid=82"><span><font>产品/项目类</font></span></a>
		    					    				<a class="item" href="position.php?keywords=python&lid=2156&tid=83"><span><font>市场类</font></span></a>
		    					    				<a class="item" href="position.php?keywords=python&lid=2156&tid=81"><span><font>设计类</font></span></a>
		    					    				<a class="item" href="position.php?keywords=python&lid=2156&tid=84"><span><font>职能类</font></span></a>
		    					    				<a class="item" href="position.php?keywords=python&lid=2156&tid=85"><span><font>内容编辑类</font></span></a>
		    					    				<a class="item" href="position.php?keywords=python&lid=2156&tid=86"><span><font>客户服务类</font></span></a>
		    					    		</div>
		    		<div class="clr"></div>
		    	</div>
		    </form>
		    <table class="tablelist" cellpadding="0" cellspacing="0">
		    	<tr class="h">
		    		<td class="l" width="374">职位名称</td>
		    		<td>职位类别</td>
		    		<td>人数</td>
		    		<td>地点</td>
		    		<td>发布时间</td>
		    	</tr>
		    			    	<tr class="even">
		    		<td class="l square"><a target="_blank" href="position_detail.php?id=46322&keywords=python&tid=87&lid=2156">TEG13-小语种语音算法工程师（北京）</a></td>
					<td>技术类</td>
					<td>1</td>
					<td>北京</td>
					<td>2018-12-14</td>
		    	</tr>
		    			    	<tr class="odd">
		    		<td class="l square"><a target="_blank" href="position_detail.php?id=46323&keywords=python&tid=87&lid=2156">TEG13-小语种机器翻译算法工程师 （北京）</a></td>
					<td>技术类</td>
					<td>1</td>
					<td>北京</td>
					<td>2018-12-14</td>
		    	</tr>
		    			    	<tr class="even">
		    		<td class="l square"><a target="_blank" href="position_detail.php?id=46268&keywords=python&tid=87&lid=2156">TEG17-语音识别/合成研究员（北京）</a></td>
					<td>技术类</td>
					<td>1</td>
					<td>北京</td>
					<td>2018-12-14</td>
		    	</tr>
		    			    	<tr class="odd">
		    		<td class="l square"><a target="_blank" href="position_detail.php?id=46226&keywords=python&tid=87&lid=2156">CSIG16-腾讯地图搜索高级算法工程师 </a></td>
					<td>技术类</td>
					<td>1</td>
					<td>北京</td>
					<td>2018-12-14</td>
		    	</tr>
		    			    	<tr class="even">
		    		<td class="l square"><a target="_blank" href="position_detail.php?id=46224&keywords=python&tid=87&lid=2156">CSIG16-腾讯地图导航引擎开发工程师（北京）</a></td>
					<td>技术类</td>
					<td>3</td>
					<td>北京</td>
					<td>2018-12-14</td>
		    	</tr>
		    			    	<tr class="odd">
		    		<td class="l square"><a target="_blank" href="position_detail.php?id=46225&keywords=python&tid=87&lid=2156">CSIG16-腾讯地图自然语言处理工程师 </a></td>
					<td>技术类</td>
					<td>1</td>
					<td>北京</td>
					<td>2018-12-14</td>
		    	</tr>
		    			    	<tr class="even">
		    		<td class="l square"><a target="_blank" href="position_detail.php?id=45994&keywords=python&tid=87&lid=2156">22989-大数据和人工智能高级开发工程师（北京）</a></td>
					<td>技术类</td>
					<td>1</td>
					<td>北京</td>
					<td>2018-12-14</td>
		    	</tr>
		    			    	<tr class="odd">
		    		<td class="l square"><a target="_blank" href="position_detail.php?id=45991&keywords=python&tid=87&lid=2156">22989-大数据后台开发工程师</a></td>
					<td>技术类</td>
					<td>1</td>
					<td>北京</td>
					<td>2018-12-14</td>
		    	</tr>
		    			    	<tr class="even">
		    		<td class="l square"><a target="_blank" href="position_detail.php?id=45972&keywords=python&tid=87&lid=2156">22989-云计算后台开发工程师</a></td>
					<td>技术类</td>
					<td>1</td>
					<td>北京</td>
					<td>2018-12-14</td>
		    	</tr>
		    			    	<tr class="odd">
		    		<td class="l square"><a target="_blank" href="position_detail.php?id=45967&keywords=python&tid=87&lid=2156">22989-腾讯云容器技术专家（北京）</a></td>
					<td>技术类</td>
					<td>2</td>
					<td>北京</td>
					<td>2018-12-14</td>
		    	</tr>
		    			    	<tr class="f">
		    		<td colspan="5">
		    			<div class="left">共<span class="lightblue total">82</span>个职位</div>
		    			<div class="right"><div class="pagenav"><a href="javascript:;" class="noactive" id="prev">上一页</a><a class="active" href="javascript:;">1</a><a href="position.php?keywords=python&lid=2156&tid=87&start=10#a">2</a><a href="position.php?keywords=python&lid=2156&tid=87&start=20#a">3</a><a href="position.php?keywords=python&lid=2156&tid=87&start=30#a">4</a><a href="position.php?keywords=python&lid=2156&tid=87&start=40#a">5</a><a href="position.php?keywords=python&lid=2156&tid=87&start=50#a">6</a><a href="position.php?keywords=python&lid=2156&tid=87&start=60#a">7</a><a href="position.php?keywords=python&lid=2156&tid=87&start=70#a">...</a><a href="position.php?keywords=python&lid=2156&tid=87&start=80#a">9</a><a href="position.php?keywords=python&lid=2156&tid=87&start=10#a" id="next">下一页</a><div class="clr"></div></div></div>
		    			<div class="clr"></div>
		    		</td>
		    	</tr>
		    </table>
		</div>
		<div class="right wcont_s box">
		    <div class="blueline"><div class="butcjwt"></div></div>
		    <div class="module_faqs square"><a href="faq.php?id=5" title="如何应聘腾讯公司的职位？">如何应聘腾讯公司的职位？</a><a href="faq.php?id=3" title="应届生如何应聘？">应届生如何应聘？</a><a href="faq.php?id=19" title="腾讯应聘流程是什么？">腾讯应聘流程是什么？</a><a href="faq.php?id=20" title="我注册了简历，但为什么没有人联系我？">我注册了简历，但为什么没...</a><a href="faq.php?id=22" title="我忘记密码了，怎么办？">我忘记密码了，怎么办？</a><a href="faq.php?id=23" title="如何进行简历修改？">如何进行简历修改？</a></div>		</div>
		<div class="clr"></div>
	</div>
   	<div id="homeDep"><table id="homeads"><tr><td align="center"><a href="http://tencent.avature.net/career" target="blank">全球招聘</a></td><td align="center"><a href="http://game.qq.com/hr/" target="blank">互动娱乐事业群招聘</a></td><td align="center"><a href="http://hr.tencent.com/position.php?lid=&tid=&keywords=WXG" target="blank">微信事业群招聘</a></td><td align="center"><a href="http://hr.qq.com/" target="blank">技术工程事业群招聘</a></td></tr></table></div>    	<div id="footer">
		<div>
			<a href="http://www.tencent.com/" target="_blank">关于腾讯</a><span>|</span><a href="http://www.qq.com/contract.shtml" target="_blank">服务条款</a><span>|</span><a href="http://hr.tencent.com/" target="_blank">腾讯招聘</a><span>|</span><a href="http://careers.tencent.com/global" target="_blank">Tencent Global Talent</a><span>|</span><a href="http://gongyi.qq.com/" target="_blank">腾讯公益</a><span>|</span><a href="http://service.qq.com/" target="_blank">客服中心</a>
	    </div>
		<p>Copyright &copy; 1998 - 2018 Tencent. All Rights Reserved.</p>
	</div>
	<script type="text/javascript" src="//tajs.qq.com/stats?sId=64934792" charset="UTF-8"></script>
</body>
</html>
"""
bs = BeautifulSoup(html,'lxml')

'''
方法一：采用find_all方法进行特征提取
'''
# 1.获取所有tr标签
# trs = bs.find_all('tr')
# for tr in trs:
#     print(tr)
# 2.获取第二个tr标签
# trs = bs.find_all('tr',limit=2)[1]
# print(trs)
# 3.获取所有class等于even的tr标签
# trs = bs.find_all('tr',attrs={'class':'even'})
# for tr in trs:
#     print(tr)
#     print('*'*30)
# 4.获取所有a标签的href属性
# a_list = bs.find_all('a')
#
# for a in a_list:
#     # 1.通过下标的方式
#     href = a["href"]
#     print(href)
    # 2.通过attrs属性标记
    # href = a.attrs['href']
    # print(href)

# 5.获取所有职位信息(纯文本)
# trs = bs.find_all('tr')[1:]
# for tr in trs:
    # tds = tr.find_all('td')
    # title = tds[0]
    # print(title.text)
    # a = tds[1]
    # print(a.text)
    # infos = list(tr.stripped_strings)
    # print(infos[0])
    # print(infos[1])
    # print(infos[2])

# 6.获取所有id等于test,class也等于test的a标签
# trs = bs.find_all('a',id='test',class_='test')
# for tr in trs:
#     print(tr)
#     print('*'*30)
'''

方法二：采用css方法进行特征提取
'''
# 1.获取所有tr标签
# trs = bs.select('tr')
# for tr in trs:
#     print(tr)
# 2.获取第二个tr标签
# trs = bs.select('tr')[1]
# print(trs)
# 3.获取所有class等于even的tr标签
# trs = bs.select('tr.even')
# for tr in trs:
#     print(tr)
# 4.获取所有a标签的href属性
# a_list = bs.select('td.l.square > a')
# for a in a_list:
#     print(a.attrs['href'])
# 5.获取所有职位信息(纯文本)
# trs = bs.select('td.l.square')
# for i in trs:
#     print(list(i.stripped_strings))
