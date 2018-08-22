# -*- coding:utf-8 -*-
from aliyunsdkcore.client import AcsClient
from aliyunsdkecs.request.v20140526 import DescribeSecurityGroupAttributeRequest
from aliyunsdkecs.request.v20140526 import AuthorizeSecurityGroupRequest
from aliyunsdkecs.request.v20140526 import RevokeSecurityGroupRequest
from aliyunsdkecs.request.v20140526 import DescribeSecurityGroupsRequest


class alis:
    def __init__(self,accesskey,accesssecret,regionid):
        self.accesskey = accesskey
        self.accesssecret = accesssecret
        self.regionid = regionid
    def clt(self):
        clt = AcsClient(self.accesskey,self.accesssecret,self.regionid)
        return clt
    def describeSecurityGroupsRequest(self):
        request = DescribeSecurityGroupsRequest.DescribeSecurityGroupsRequest()
        request.set_accept_format('json')
        return request
    def describeSecurityGroupAttributeRequest(self,SecurityGroupId,NicType='internet',Direction='ingress'): # 需要改NicType
        '''查询安全组'''
        request = DescribeSecurityGroupAttributeRequest.DescribeSecurityGroupAttributeRequest()
        request.set_SecurityGroupId(SecurityGroupId)
        request.set_accept_format('json')
        request.set_NicType(NicType)
        request.set_Direction(Direction)
        return request
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
    # def modifySecurityGroupRule(self,):
if __name__ == '__main__':
    ali = alis('ACCESS_KEY','ACCESS_SECERT','cn-hangzhou') 
    clt = ali.clt()
    req = ali.describeSecurityGroupsRequest()
    # print clt.do_action_with_exception(req)
    try:
        ali_add_rules_1 = ali.authorizeSecurityGroupRequest('sg-23r562xqj','tcp','80/80','0.0.0.0/0',1,'fmy-game-service(n0)')
        ali_add_rules_2 = ali.authorizeSecurityGroupRequest('sg-23r562xqj','tcp','52001/52005','0.0.0.0/0',2,'fmy-game-service(n1-n5)')
        '''SG_AS_GameJavaWeb'''
        ali_add_rules_3 = ali.authorizeSecurityGroupRequest('sg-23ltyskj3','tcp','50000/50010','0.0.0.0/0',1,'-')
        ali_add_rules_4 = ali.authorizeSecurityGroupRequest('sg-23ltyskj3','tcp','50015/50095','0.0.0.0/0',6,'多服端口')
        ali_add_rules_5 = ali.authorizeSecurityGroupRequest('sg-23ltyskj3','tcp','843/843','0.0.0.0/0',7,'flash跨域服务')
        '''SG_AS_GameServer'''
        '''添加规则（开服）'''
        ali_rvk_rules_1 = ali.revokeSecurityGroupRequest('sg-23r562xqj','tcp','8888/8888','0.0.0.0/0',1)
        ali_rvk_rules_2 = ali.revokeSecurityGroupRequest('sg-23r562xqj','tcp','52001/52005','0.0.0.0/0',2)
        '''SG_AS_GameJavaWeb'''
        ali_rvk_rules_3 = ali.revokeSecurityGroupRequest('sg-23ltyskj3','tcp','50000/50010','0.0.0.0/0',1)
        ali_rvk_rules_4 = ali.revokeSecurityGroupRequest('sg-23ltyskj3','tcp','50015/50095','0.0.0.0/0',6)
        ali_rvk_rules_5 = ali.revokeSecurityGroupRequest('sg-23ltyskj3','tcp','843/843','0.0.0.0/0',7)
        '''SG_AS_GameServer'''
        '''删除规则（停服）'''
        response_1 = clt.do_action_with_exception(ali_add_rules_1)   #添加(开服)
        response_2 = clt.do_action_with_exception(ali_add_rules_2)   #添加(开服)
        response_3 = clt.do_action_with_exception(ali_add_rules_3)   #添加(开服)
        response_4 = clt.do_action_with_exception(ali_add_rules_4)   #添加(开服)
        response_5 = clt.do_action_with_exception(ali_add_rules_5)   #添加(开服)

        # response_1 = clt.do_action_with_exception(ali_rvk_rules_1) #删除(停服)
        # response_2 = clt.do_action_with_exception(ali_rvk_rules_2) #删除(停服)
        # response_3 = clt.do_action_with_exception(ali_rvk_rules_3) #删除(停服)
        # response_4 = clt.do_action_with_exception(ali_rvk_rules_4) #删除(停服)
        # response_5 = clt.do_action_with_exception(ali_rvk_rules_5) #删除(停服)
        print response_1,response_2,response_3,response_4,response_5
    except Exception,e:
        print Exception,":",e

#

