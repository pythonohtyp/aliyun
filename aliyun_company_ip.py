# -*- coding:utf-8 -*-
from aliyunsdkcore.client import AcsClient
from aliyunsdkecs.request.v20140526 import AuthorizeSecurityGroupRequest
from aliyunsdkecs.request.v20140526 import RevokeSecurityGroupRequest
from aliyunsdkrds.request.v20140815 import DescribeDBInstancesRequest
from aliyunsdkrds.request.v20140815 import ModifySecurityIpsRequest
from aliyunsdkdds.request.v20151201 import ModifySecurityIpsRequest as DDSModifySecurityIpsRequest
import re


class alis:
    def __init__(self,accesskey,accesssecret,regionid):
        self.accesskey = accesskey
        self.accesssecret = accesssecret
        self.regionid = regionid
    def clt(self):
        clt = AcsClient(self.accesskey,self.accesssecret,self.regionid)
        return clt
    def authorizeSecurityGroupRequest(self,SecurityGroupID,IpProtocol,PortRange,SourceCidrIp,Priority,Description):
        '''授权安全组内规则'''
        request = AuthorizeSecurityGroupRequest.AuthorizeSecurityGroupRequest()
        request.set_SecurityGroupId(SecurityGroupID)
        request.add_query_param('RegionId','cn-hangzhou')   #需改为华东1（cn-hangzhou
        request.set_IpProtocol(IpProtocol)
        request.set_PortRange(PortRange)
        request.set_SourceCidrIp(SourceCidrIp)
        request.set_Priority(Priority)
        request.set_Description(Description)
        request.set_accept_format('json')
        return request
    def revokeSecurityGroupRequest(self,SecurityGroupID,IpProtocol,PortRange,SourceCidrIp,Priority):
        '''撤销安全组内规则'''
        request = RevokeSecurityGroupRequest.RevokeSecurityGroupRequest()
        request.set_SecurityGroupId(SecurityGroupID)
        request.add_query_param('RegionId', 'cn-hangzhou')  #需改为华东1（cn-hangzhou
        request.set_IpProtocol(IpProtocol)
        request.set_PortRange(PortRange)
        request.set_SourceCidrIp(SourceCidrIp)
        request.set_Priority(Priority)
        request.set_accept_format('json')
        return request
    def describeDBInstances(self):
        '''Mysql数据库实例列表'''
        request = DescribeDBInstancesRequest.DescribeDBInstancesRequest()
        request.set_accept_format('json')
        request.add_query_param('RegionId','cn-hangzhou')
        return request
    def modifySecurityIps(self,DBInstanceId,SecurityIps,DBInstanceIPArrayName):
        '''Mysql数据库白名单修改'''
        request = ModifySecurityIpsRequest.ModifySecurityIpsRequest()
        request.set_DBInstanceId(DBInstanceId)
        request.set_SecurityIps(SecurityIps)
        request.set_DBInstanceIPArrayName(DBInstanceIPArrayName)
        return request
    def modifySecurityIps_dds(self,DBInstanceId,SecurityIps,ModifyMode,SecurityIpGroupName,):
        '''MongoDB数据库白名单修改'''
        request = DDSModifySecurityIpsRequest.ModifySecurityIpsRequest()
        request.set_DBInstanceId(DBInstanceId)
        request.set_SecurityIps(SecurityIps)
        request.set_ModifyMode(ModifyMode)
        request.set_SecurityIpGroupName(SecurityIpGroupName)
        return request
if __name__ == '__main__':
    ali = alis('ACCESSKEY', 'ACCESSSECERT', 'cn-hangzhou')
    clt = ali.clt()
    tuple_port = ['80/80','9876/9876','9877/9877','3717/3717','22024/22024','8888/8888','52001/52005','51000/51005',
                  '22024/22024','50000/50010','50015/50095','843/843','3389/3389','4018/4018']	#端口
    tuple_priority = ['2','50','51','52','80','1','2','50','80','1','6','7','50','99']	#规则等级
    tuple_description = ['fmy-website-online','fmy-website-admin','smart-sso-srever','mongodb-agent','linux-ssh','fmy-game-service(n0)',
                         'fmy-game-service(n1-n5)','fmy-game-admin(n1-n5)','linux-ssh','-','多服端口','flash跨域服务','windows远程桌面','-']	#规则描述
    try:    #ECS
        for i in range(14):
            if i < 5:
                ali_add_rules_1 = ali.authorizeSecurityGroupRequest('sg-23v92s1b5', 'tcp', tuple_port[i], '10.10.10.10', tuple_priority[i],tuple_description[i])
                ali_rvk_rules_1 = ali.revokeSecurityGroupRequest('sg-23v92s1b5','tcp',tuple_port[i], '11.11.11.11', tuple_priority[i])
                '''SG_AS_OfficialWebsite'''
                print clt.do_action_with_exception(ali_add_rules_1)
                print clt.do_action_with_exception(ali_rvk_rules_1)
            elif 8 >= i >= 5:
                ali_add_rules_2 = ali.authorizeSecurityGroupRequest('sg-23r562xqj', 'tcp', tuple_port[i], '10.10.10.10', tuple_priority[i],tuple_description[i])
                ali_rvk_rules_2 = ali.revokeSecurityGroupRequest('sg-23r562xqj','tcp',tuple_port[i], '11.11.11.11', tuple_priority[i])
                '''SG_AS_GameJavaWeb'''
                print clt.do_action_with_exception(ali_add_rules_2)
                print clt.do_action_with_exception(ali_rvk_rules_2)
            else:
                ali_add_rules_3 = ali.authorizeSecurityGroupRequest('sg-23ltyskj3', 'tcp', tuple_port[i], '10.10.10.10', tuple_priority[i],tuple_description[i])
                ali_rvk_rules_3 = ali.revokeSecurityGroupRequest('sg-23ltyskj3','tcp',tuple_port[i], '11.11.11.11', tuple_priority[i])
                '''SG_AS_GameServer'''
                print clt.do_action_with_exception(ali_add_rules_3)
                print clt.do_action_with_exception(ali_rvk_rules_3)
    except Exception, e:
        print Exception, ":", e
    try:    #RDS
        dbinstance = ali.describeDBInstances()
        ask = clt.do_action_with_exception(dbinstance)
        b = re.findall(r'"DBInstanceId":"(.*?)","VpcCloudInstanceId"',ask)
        print b
        for i in b:
            ali_rds_IP = ali.modifySecurityIps(i,'10.10.10.10','company_public_ip')#安全组名
            print clt.do_action_with_exception(ali_rds_IP)
    except Exception, e:
        print Exception, ":", e
    try:    #DDS
        ali_dds_IP = ali.modifySecurityIps_dds('dds-bp1d76757b10d784','10.10.10.10','Cover','company_public_ip')
        '''DDS更新IP白名单'''
        print clt.do_action_with_exception(ali_dds_IP)


    except Exception, e:
        print Exception, ":", e

#除了这三项之外还需修改DNS、OSS操作。。

