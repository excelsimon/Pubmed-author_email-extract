#encoding: UTF-8
#程序功能：提取author.json文件及authorPair.json文件中email-address,去重，发送邮件

import os
import re
import linecache
#清理缓存，否则在文件内容发生变化时，读到的内容不变化
linecache.clearcache()
str_  = linecache.getlines("author.json")
f = file("email.txt",'a')
#处理author.json
for i in range(len(str_)):
	if '@' in str_[i]:
		match1 = re.findall(r'(?<=Electronic address: ).+?@.+?(?=.")',str_[i])
		match2 = re.findall(r'(?<=Email: ).+?@.+?(?=.")',str_[i])
		if not match2:
			match2 =  re.findall(r'(?<=E-mail: ).+?@.+?(?=.")',str_[i])
		if not match2:
			match2 =  re.findall(r'(?<=E-mail:).+?@.+?(?=.")',str_[i])
		if not match2:
			match2 =  re.findall(r'(?<=E-Mails:  ).*?com',str_[i])

		match3 = re.findall(r'(?<=China\. ).+?@.+?(?=\.")',str_[i])
                if not match3:
			match3 = re.findall(r'(?<=China\. ).+?@.+?(?=")',str_[i])
		if match3:
			if 'China' in match3[0]:
				match3 = re.findall(r'(?<=China\. ).*',match3[0])
				if match3:
					if 'China' in match3[0]:
						match3 = re.findall(r'(?<=China ).*',match3[0])
			if match3:
				if 'USA' in match3[0]:
					match3 = re.findall(r'(?<=USA\. ).*',match3[0])

		if match1:
			f.write(match1[0]+'\n')
		elif match2:
			f.write(match2[0]+'\n')
		elif match3:
			f.write(match3[0]+'\n')
#处理authorPair.json
linecache.clearcache()
strPair = linecache.getlines("authorPair.json")
for i in range(len(strPair)):
	if '@' in strPair[i]:
		match = re.findall(r'(?<=\"email\"\:\s\[\").+?(?=\")',strPair[i])
		if match:
			if 'email' in match[0]:
				match = re.findall(r'(?<=email: ).+?(?=\))',match[0])
		if match:
			f.write(match[0]+'\n')
f.close()
#去重
emailList = []
f = open('email.txt','r')
#for ln in open('email.txt'):
for ln in f:
	if len(ln)>40:
		continue
	if ':' in ln:
		continue
	if ' ' in ln:
		tmp1 = re.findall(r'.+?(?=\s)',ln)
		emailList.append(tmp1[0]+'\n')
		tmp2 = re.findall(r'(?<=\s).*',ln)
		emailList.append(tmp2[0]+'\n')
		continue
	if '.' not in ln:
		continue
	if ln in emailList:
        	continue
    	emailList.append(ln)
f.close()
os.remove('email.txt')
with open('emailList.txt', 'w') as handle:
	handle.writelines(emailList)
handle.close()



# coding:utf-8

from email import encoders
from email.header import Header
from email.mime.text import MIMEText
from email.MIMEMultipart import MIMEMultipart
from email.mime.application import MIMEApplication 
from email.MIMEBase import MIMEBase
from email import Utils,Encoders
from email.utils import parseaddr, formataddr
import smtplib
import sys
print 'send email begin'
def _format_addr(s):
    name, addr = parseaddr(s)
    return formataddr(( \
        Header(name, 'utf-8').encode(), \
        addr.encode('utf-8') if isinstance(addr, unicode) else addr))

#from_addr = raw_input('From: ')
#password = raw_input('Password: ')
#to_addr = raw_input('To: ')
#smtp_server = raw_input('SMTP server: ')
from_addr = "hsgene_todaysoft@163.com"
password = "hsgene123"
#to_addr = "zj_bupt@sina.com"
#to_addr = ["zj_bupt@sina.com","zhangjing@hsgene.com","1094253356@qq.com","hsgene_todaysoft@163.com","liuyue@todaysoft.com.cn","zhangwensheng@hsgene.com","wangyuelan@hsgene.com"]
#to_addr = sys.argv[1]
to_addr = []
f = open('test.txt','r')
for ln in f:
	if ln in to_addr:
		continue
	to_addr.append(ln)
f.close()
smtp_server = 'smtp.163.com'


#text
msg = MIMEMultipart('alternative')
#part = MIMEText('好的', 'plain', 'utf-8')
#html
msg = MIMEText('''
<!DOCTYPE html PUBLIC "-//W3C//DTD XHTML 1.0 Transitional//EN" "http://www.w3.org/TR/xhtml1/DTD/xhtml1-transitional.dtd">
<html xmlns="http://www.w3.org/1999/xhtml">
 <head>
  <meta http-equiv="Content-Type" content="text/html; charset=UTF-8" />
  <title>Demystifying Email Design</title>
  <meta name="viewport" content="width=device-width, initial-scale=1.0"/>
 </head>
 <body style="margin: 0; padding: 0;">
  <table border="0" cellpadding="0" cellspacing="0" width="100%">
   <tr>
    <td style="padding: 20px 0 30px 0;">
     <table  style="border: 1px solid #cccccc;" align="center" cellpadding="0" cellspacing="0" width="600">
	  <!-- Part 1 -->
	  <tr>
       <td align="center" bgcolor="#ffffff" style="padding: 0 0 0 0;">
        <img src="http://124.207.127.114:8901/jeecms/u/cms/www/201605/26115329lla0.jpg" alt="最尖端的技术、最优的服务，打造国际化品牌" width="600" height="100" style="display: block;" />
	   </td>
      </tr>
	  
	  <!-- Part 2 -->
	  <tr>
       <td bgcolor="#ffffff" style="padding: 40px 30px 40px 30px;">
        <table border="0" cellpadding="0" cellspacing="0" width="100%">
         <tr>
          <td style="color: #153643; font-family: Arial, sans-serif; font-size: 16px;">
		  <p>亲爱的老师：您好！</p>
		  <p>如果您正在为测序数据分析而一筹莫展，如果您正在为实验数据的真实性而疑惑，如果您对测序公司的数据分析不满意，如果您想亲自进行数据分析而无从下手，如果您想得到更为专业的数据分析服务……</p>
		  <p>那么请您关注我们的产品。</p>
          <p>北京华生恒业科技有限公司是一家专业从事应用生物科技软件研发、定制、数据分析的高新科技企业。与美国SoftGenetics长期国际交流合作，开发系列基因测序分析软件。我们的产品有<font color="#FF0000">二代测序数据分析工具NextGene&reg;、Sanger测序数据分析软件Mutation Surveyor&reg;、DNA片段分析软件GeneMarker&reg;</font>，该系列软件具有简单、直观、可视化的界面显示，显著减少用户生物信息学基础的要求，为医生、生物学家、测序服务商等提供了最好的选择。其中NextGENe&reg;被Thermo Fisher公司指定为Ion torrent测序系统推荐配套软件。此外我们可以为您提供世界领先的生物软件定制及数据分析服务。</p>
		  <p>全球有超过5000家DNA实验室和研究机构使用公司研发的DNA测序数据分析系列软件。包括美国国立癌症研究所（NCI）、美国国立卫生研究院(NIH)、Mayo Clinic、中国科学院北京基因组研究所、香港大学等。这些研究机构发表在世界顶级科学杂志（如《Nature》和《Science》）上的文章特别指出了在科研过程中，本公司的软件产品起了重要的作用。</p>
		  </td>
         </tr>
		 <tr>
          <td style="padding: 20px 0 0 0;color: #153643; font-family: Arial, sans-serif; font-size: 16px; line-height: 20px;"">
		  1.<font color="#FF0000">NextGene&reg;</font>——<a href="http://www.todaysoft.com.cn/a/products/biotechnology/2010/0914/13.html">二代测序数据分析工具</a>
			<p>NextGENe&reg;提供了新一代大规模基因测序工程的整套软件解决方案，用于实现序列装配和序列比对，NextGENe&reg;在Windows操作系统运行，效率高，准确性高，用户不需具备脚本或者其他生物信息学背景即可应用。并且具备强大的界面显示和报表输出功能，可以分析序列比对结果，查看变异信息等。可分析Ion Torrent 测序平台、Roche测序平台、Illumina 测序平台、SOLiD测序系统产出的原始测序数据，可兼容BAM、FASTQ、FASTA、CSFASTA等多种数据格式。</p>
          </td>
         </tr>
		 <tr>
          <td>
            <table border="0" cellpadding="0" cellspacing="0" width="100%">             
			 <tr>              
			  <td width="300" valign="middle">
				 <table border="0" cellpadding="0" cellspacing="0" width="100%">
				  <tr>
                   <td>
				   <a href="http://www.todaysoft.com.cn/a/products/biotechnology/2010/0914/13.html">
                   <img src="http://124.207.127.114:8901/jeecms/u/cms/www/201605/2611524070e6.jpg" alt="" width="100%" height="400" style="display: block;" />
                   </a>
				   </td>
                  </tr>                 
                 </table>
              </td>
			  <td width="240">
			   <table border="0" cellpadding="0" cellspacing="0" width="100%">
                 <tr>
                  <td>
                    <ul>
					<font color="#FF0000" size="2px">主要应用:</font>
						<li><a href="http://www.softgenetics.com/NextGENe_01.php"><font size="2px">单核苷酸多态性（SNP）/插入缺失（InDel）</font></a></li>
						<li><a href="http://www.softgenetics.com/NextGENe_013.php"><font size="2px">拷贝数变异（CNV）分析</font></a></li>
						<li><a href="http://www.softgenetics.com/NextGENe_014.php"><font size="2px">体细胞突变检测</font></a></li>
						<li><a href="http://www.softgenetics.com/NextGENe_03.php"><font size="2px">全基因组比对及突变检测</font></a></li>
						<li><a href="http://www.softgenetics.com/NextGENe_04.php"><font size="2px">RNA测序/转录组测序分析</font></a></li>
						<li><a href="http://www.softgenetics.com/NextGENe_07.php"><font size="2px">目标区域捕获测序/重测序分析</font]></a></li>
						<li><a href="http://www.softgenetics.com/NextGENe_18.php"><font size="2px">HLA分析</font></a></li>
						<li><a href="http://www.softgenetics.com/NextGENe_08.php"><font size="2px">人类身份鉴定分析（法医）</font></a></li>
						<li><a href="http://www.softgenetics.com/NextGENe_06.php"><font size="2px">reads组装/Paired-end拼接</font></a></li>
						<li><a href="http://www.softgenetics.com/NextGENe_05.php"><font size="2px">miRNA的发现及定量分析</font></a></li>
						<li><a href="http://www.softgenetics.com/NextGENe_02.php"><font size="2px">罕见疾病分析及预测</font></a></li>
						<li><a href="http://www.softgenetics.com/NextGENe_016.php"><font size="2px">家系多个样本工程的比对分析</font></a></li>
						<li><a href="http://www.softgenetics.com/NextGENe_017.php"><font size="2px">可导入多个数据库</font></a></li>
					</ul>
                  </td>
                 </tr>
                </table>
              </td>   
             </tr>
            </table>
          </td>
         </tr>
         <tr>
          <td style="padding: 20px 0 0 0;color: #153643; font-family: Arial, sans-serif; font-size: 16px; line-height: 20px;"">
		  2.<font color="#FF0000">Mutation Surveyor&reg;</font>——<a href="http://www.todaysoft.com.cn/a/products/biotechnology/2010/0914/11.html">Sanger测序数据分析软件</a>
		  <p>Mutation Surveyor&reg;是基因突变(Mutation) 检测软件。可以检测纯合子变异(Homozygote)——SNP、插入/缺失(InDel)，杂合子变异(Heterozygote)——SNP、插入/缺失(InDel)等。它可和标准序列比较，快速找出样本序列图谱中所有的基因变异点。</p>
          <p>Mutation Surveyor&reg;在突变检测领域运用了两项世界首创技术：反相关曲线技术和准确识别插入/缺失杂合子突变技术。</p>
		  <p>操作系统：支持 Windows XP、Windows Vista、Windows 7等主流操作系统。</p>
		  <p>数据格式：ABI、AB1、SCF文件</p>
		  </td>
         </tr>
		 <tr>
          <td>
            <table border="0" cellpadding="0" cellspacing="0" width="100%">
			 
			 <tr>
			  <td width="300" valign="middle">
				 <table border="0" cellpadding="0" cellspacing="0" width="100%">
				  <tr>
                   <td>
				   <a href="http://www.todaysoft.com.cn/a/products/biotechnology/2010/0914/11.html">
                   <img src="http://124.207.127.114:8901/jeecms/u/cms/www/201605/261149288wqj.jpg" alt="" width="100%" height="300" style="display: block;" />
                   </a>
				   </td>
                  </tr>
                 
                 </table>
              </td> 
			  <td width="240">
			   <table border="0" cellpadding="0" cellspacing="0" width="100%">
                 <tr>
                  <td>
                    <ul>
					<font color="#FF0000" size="2px">主要应用:</font>
						<li><a href="http://www.softgenetics.com/mutationSurveyor_1.php"><font size="2px">检测高灵敏度和精度</font></a></li>
						<li><a href="http://www.softgenetics.com/mutationSurveyor_2.php"><font size="2px">纯合INDEL检测</font></a></li>
						<li><a href="http://www.softgenetics.com/mutationSurveyor_3.php"><font size="2px">杂合INDEL检测</font></a></li>
						<li><a href="http://www.softgenetics.com/mutationSurveyor_4.php"><font size="2px">体细胞突变检测</font></a></li>
						<li><a href="http://www.softgenetics.com/mutationSurveyor_5.php"><font size="2px">突变量化分析</font></a></li>
						<li><a href="http://www.softgenetics.com/mutationSurveyor_6.php"><font size="2px">甲基化分析</font></a></li>
						<li><a href="http://www.softgenetics.com/mutationSurveyor_11.php"><font size="2px">自定义报告选项</font></a></li>
						<li><a href="http://www.softgenetics.com/mutationSurveyor_13.php"><font size="2px">线粒体DNA序列分析</font></a></li>
						<li><a href="http://www.softgenetics.com/mutationSurveyor_14.php"><font size="2px">无人操作</font></a></li>
						<li><a href="http://www.softgenetics.com/mutationSurveyor_15.php"><font size="2px">可添加变异相关知识库</font></a></li>
						<li><a href="http://www.softgenetics.com/mutationSurveyor_16.php"><font size="2px">用户管理和审计跟踪</font></a></li>
					</ul>
                  </td>
                 </tr>
                </table>
              </td>   
             </tr>
            </table>
          </td>
		 </tr>
		 <tr>
          <td style="padding: 20px 0 0 0;color: #153643; font-family: Arial, sans-serif; font-size: 16px; line-height: 20px;"">
		  3. <font color="#FF0000">GeneMarker&reg;</font>——<a href="http://www.todaysoft.com.cn/a/products/biotechnology/2010/0914/12.html">DNA片段分析软件</a>
		  <p>GeneMarker&reg;软件是唯一为基因研究者设计的“生物学家友好”的基因分型软件，广泛应用于遗传病、肿瘤、法医、农林育种等领域的研究。软件界面具有引导功能并且布局直观，使用非常简便，并集合十余个应用，是一款精确、快速、友好、功能强大的自动化数据分析软件。</p>
		  </td>
         </tr>
		 <tr>
          <td>
            <table border="0" cellpadding="0" cellspacing="0" width="100%"> 
			 <tr>
			  <td width="300" valign="middle">
				 <table border="0" cellpadding="0" cellspacing="0" width="100%">
				  <tr>
                   <td>
				   <a href="http://www.todaysoft.com.cn/a/products/biotechnology/2010/0914/12.html">
                   <img src="http://124.207.127.114:8901/jeecms/u/cms/www/201605/261153069zzh.jpg" alt="" width="100%" height="300" style="display: block;" />
                   </a>
				   </td>
                  </tr>
                 
                 </table>
              </td>
			  <td width="240">
			   <table border="0" cellpadding="0" cellspacing="0" width="100%">
                 <tr>
                  <td>
                    <ul>
					<font color="#FF0000" size="2px">主要应用:</font>
						<li><a href="http://www.todaysoft.com.cn/a/bioinformatics/2010/1125/232.html"><font size="2px">STR(SSR、微卫星) 数据分析</font></a></li>
						<li><a href="http://www.todaysoft.com.cn/a/bioinformatics/2010/1108/189.html"><font size="2px">AFLP数据分析</font></a></li>
						<li><a href="http://www.todaysoft.com.cn/a/bioinformatics/2010/0927/65.html"><font size="2px">MLPA?数据分析</font></a></li>
						<li><a href="http://www.todaysoft.com.cn/a/bioinformatics/2010/1103/180.html"><font size="2px">三倍体症分析</font></a></li>
						<li><a href="http://www.todaysoft.com.cn/a/bioinformatics/2010/1123/225.html"><font size="2px">微卫星不稳定性（MSI）分析</font></a></li>
						<li><a href="http://www.todaysoft.com.cn/a/bioinformatics/2010/1125/232.html"><font size="2px">遗传家系绘图与孟德尔检验</font></a></li>
						<li><a href="http://www.todaysoft.com.cn/a/bioinformatics/2010/1103/179.html"><font size="2px">杂合性缺失（LOH）分析</font></a></li>
						<li><a href="http://www.todaysoft.com.cn/a/products/biotechnology/2010/0926/52.html"><font size="2px">法医和亲缘鉴定研究</font></a></li>
						<li><font size="2px">高通量SNP分型</font></li>
					</ul>
                  </td>
                 </tr>
                </table>
              </td> 
			  
             </tr>
            </table>
          </td>
         </tr>
		 <tr>
          <td style="padding: 20px 0 0 0;">
		   <p style="color: #FF0000; font-family: Arial, sans-serif; font-size: 22px;">生物信息分析服务：</p>
		   <p style="color: #153643; font-family: Arial, sans-serif; font-size: 16px;padding: 0 0 0 0;">依托强大的生物信息分析平台和项目经验丰富的生物信息团队，对外承接测序原始数据的生物信息分析服务（一代测序数据、二代测序数据），生物信息分析人员与用户一对一交流，提供个性化的数据分析方案，快速响应用户的需求。根据用户的分析要求，设计适合的数据分析方案。</p>
          </td>
         </tr>
		 <tr>
          <td style="padding: 20px 0 0 0;">
		   <p style="color: #FF0000; font-family: Arial, sans-serif; font-size: 22px;">软件定制开发：</p>
		   <p style="color: #153643; font-family: Arial, sans-serif; font-size: 16px;padding: 0 0 0 0;">经验丰富的软件开发团队在现有各类强大的分析软件的基础上，可满足您对特色功能的实现、数据分析平台的构建、自定义软件的开发等需求的实现，在测序数据分析及平台构建方面助您一臂之力。</p>
          </td>
         </tr>
		</table>
       </td>
      </tr>
	  
	  <!-- Part 3 -->
	  <tr>
       <td bgcolor="#F0F8FF" style="padding: 30px 30px 30px 30px;">
        <table border="0" cellpadding="0" cellspacing="0" width="100%">
         <tr>
		  <td style="font-family: Arial, sans-serif; font-size: 14px;">
			更多信息请访问：<br/>http://www.todaysoft.com.cn/ <br/>  http://www.softgenetics.com/<br/>
			联系电话：010-82600675   010-51197773-8131 <br/>
			邮箱：liuyue@todaysoft.com.cn <br/><span style="font-size:14px;">&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;</span> yanzhenchen@hsgene.com <br/>		
			地址：北京中关村东路18号财智国际大厦C座15层 <br/>
			<!-- <a href="#" style="color: #ffffff;"><font color="#0000CD">Unsubscribe</font></a> to this newsletter instantly<br/> -->
			<span> 注：【退订回t】</span>
		  </td>
		  <td>
           <table border="0" cellpadding="0" cellspacing="0">
            <tr>
             <td>
              <!--<a href=""> -->
              <img src="http://124.207.127.114:8901/jeecms/u/cms/www/201606/01100452205t.jpg" alt="二维码1" width="100" height="100" style="display: block;" border="0" />
              <!--</a> -->
             </td>
			 <td>
			 <img src="http://124.207.127.114:8901/jeecms/u/cms/www/201606/01100507ovej.jpg" alt="二维码2" width="100" height="100" style="display: block;" border="0" />
			 </td>
            </tr>
           </table>
		  </td>
         </tr>
		</table>
       </td>
      </tr>
     </table>
    </td>
   </tr>
  </table>
 </body>
</html>''', 'html', _charset='GBK')

#attatchment
#msg = MIMEMultipart()
msg['From'] = _format_addr(u'Todaysoft <%s>' % from_addr)
msg['To'] = _format_addr(u'<%s>' % to_addr)
#msg['To'] = ",".join(to_addr)
msg['Subject'] = Header(u'DNA sequencing ', 'utf-8').encode()
#msg["Accept-Language"]="zh-CN"
#msg["Accept-Charset"]="ISO-8859-1,utf-8"
#text part
#msg.attach(MIMEText('好的', 'plain', 'utf-8'))


#attatchment part  附件1 图片
#'''with open('E:\\test.jpg', 'rb') as f:
    # 设置附件的MIME和文件名，这里是jpg类型:
 #   mime = MIMEBase('image', 'jpg', filename='test.jpg')
    # 加上必要的头信息:
  #  mime.add_header('Content-Disposition', 'attachment', filename='test.jpg')
   # mime.add_header('Content-ID', '<0>')
    #mime.add_header('X-Attachment-Id', '0')
    # 把附件的内容读进来:
    #mime.set_payload(f.read())
    # 用Base64编码:
    #encoders.encode_base64(mime)
    #把图片插入正文
    #msg.attach(MIMEText('<html><body><h1>Hello</h1>' +
    #	'<p><img src="cid:0"></p>' +
    #	'</body></html>', 'html', 'utf-8'))
    # 添加到MIMEMultipart:
    #msg.attach(mime)
#attatchment part 
#part = MIMEApplication(open('E:\\test.txt','rb').read())  
#part.add_header('Content-Disposition', 'attachment', filename="test.txt")  
#msg.attach(part)'''
    
#明文传输
server = smtplib.SMTP(smtp_server, 25)
#加密传输 端口从C:\Anaconda2\Lib\smtplib.py  line 58读到
#server = smtplib.SMTP(smtp_server,465)
#server = smtplib.SMTP_SSL(smtp_server, 465 )
#server.starttls()
server.set_debuglevel(1)
server.login(from_addr, password)
server.sendmail(from_addr, to_addr, msg.as_string().encode('ascii'))
server.quit()

