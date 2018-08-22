# -*- coding:utf-8 -*-
from aliyunsdkcore.client import AcsClient
from aliyunsdkram.request.v20150501 import DeletePolicyVersionRequest
from aliyunsdkram.request.v20150501 import ListPolicyVersionsRequest
from aliyunsdkram.request.v20150501 import CreatePolicyVersionRequest
import re


java_policy-rule = '{ "Statement": [ { "Effect": "Allow", '
               '"Action": "oss:ListBuckets", "Condition": { "IpAddress": { "acs:SourceIp": "10.10.10.10" } }, '
               '"Resource": [ "acs:oss:*:*:*" ] }, { "Effect": "Allow", "Action": "oss:*", '
               '"Condition": { "IpAddress": { "acs:SourceIp": "10.10.10.10" } }, '
               '"Resource": [ "acs:oss:*:*:fmy-test-java-game-res-x13", "acs:oss:*:*:fmy-test-java-game-res-x13/*", '
               '"acs:oss:*:*:fmy-review-java-game-res-x23", "acs:oss:*:*:fmy-review-java-game-res-x23/*" ] }, '
               '{ "Effect": "Allow", "Action": "oss:Get*", "Condition": { "IpAddress": { "acs:SourceIp": "10.10.10.10" } },'   #Action后面
               ' "Resource": [ "acs:oss:*:*:fmy-java-game-res-x03", "acs:oss:*:*:fmy-java-game-res-x03/*" ] } ], "Version": "1"}'
mobile_policy_rule = '{ "Statement": [ { "Effect": "Allow",'
               ' "Action": "oss:ListBuckets", "Condition": { "IpAddress": { "acs:SourceIp": "10.10.10.10" } }, '
               '"Resource": [ "acs:oss:*:*:*" ] }, { "Effect": "Allow", "Action": "oss:*",'
               ' "Condition": { "IpAddress": { "acs:SourceIp": "10.10.10.10" } }, '
               '"Resource": [ "acs:oss:*:*:fmy-test-mobile-game-res-x12", "acs:oss:*:*:fmy-test-mobile-game-res-x12/*", '
               '"acs:oss:*:*:fmy-review-mobile-game-res-x22", "acs:oss:*:*:fmy-review-mobile-game-res-x22/*", '
               '"acs:oss:*:*:fmy-mobile-game-res-x04", "acs:oss:*:*:fmy-mobile-game-res-x04/*" ] }, '
               '{ "Effect": "Allow", "Action": "oss:Get*", "Condition": { "IpAddress": { "acs:SourceIp": "10.10.10.10" } }, '     #Action后面
               '"Resource": [ "acs:oss:*:*:fmy-mobile-game-res-x02", "acs:oss:*:*:fmy-mobile-game-res-x02/*", '
               '"acs:oss:*:*:fmy-public-game-res-x99", "acs:oss:*:*:fmy-public-game-res-x99/*" ] } ], "Version": "1" }'


class alis:
    def __init__(self,accesskey,accesssecret,regionid):
        self.accesskey = accesskey
        self.accesssecret = accesssecret
        self.regionid = regionid
    def clt(self):
        clt = AcsClient(self.accesskey,self.accesssecret,self.regionid)
        return clt
    def listPolicyVersion(self,PolicyType,PolicyName):
        '''版本列表详细信息'''
        request = ListPolicyVersionsRequest.ListPolicyVersionsRequest()
        request.set_accept_format('json')
        request.set_PolicyType(PolicyType)
        request.set_PolicyName(PolicyName)
        return request
    def deletePolicyVersion(self,PolicyName,VersionId):
        '''删除某个版本'''
        request = DeletePolicyVersionRequest.DeletePolicyVersionRequest()
        request.set_PolicyName(PolicyName)
        request.set_VersionId(VersionId)
        request.set_accept_format('json')
        return request
    def createPolicyVersion(self,PolicyName,PolicyDocument,SetAsDefault):
        '''为授权策略创建新的版本(策略详情)'''
        request = CreatePolicyVersionRequest.CreatePolicyVersionRequest()
        request.set_PolicyName(PolicyName)
        request.set_PolicyDocument(PolicyDocument)
        request.set_SetAsDefault(SetAsDefault)
        request.set_accept_format('json')
        return request

if __name__ == '__main__':
    ali = alis('ACCESS_KEY','ACCESS_SECERT','cn-hangzhou') 
    clt = ali.clt()
    req_java_tools = ali.listPolicyVersion('Custom','AliyunOSSFullAccess-java-tools')
    req_mobile_tools = ali.listPolicyVersion('Custom','AliyunOSSFullAccess-mobile-tools')
    version_java_lists = clt.do_action_with_exception(req_java_tools)
    version_mobile_lists = clt.do_action_with_exception(req_mobile_tools)
    re_java_lists = re.findall(r'"VersionId":"(.*?)","PolicyDocument"', version_java_lists)
    re_mobile_lists = re.findall(r'"VersionId":"(.*?)","PolicyDocument"', version_mobile_lists)
    re_java_lists_reverse = []
    re_mobile_lists_reverse = []
    [re_java_lists_reverse.append(int(i.replace('v', ''))) for i in re_java_lists]  #去除‘v’并改为int类型
    [re_mobile_lists_reverse.append(int(i.replace('v', ''))) for i in re_mobile_lists]
    re_java_lists_version = sorted(re_java_lists_reverse, reverse=False)
    re_mobile_lists_version = sorted(re_mobile_lists_reverse, reverse=False)
    print re_java_lists_version
    print re_mobile_lists_version
    if len(re_java_lists_version) >= 5:
        del_java_version = ali.deletePolicyVersion('AliyunOSSFullAccess-java-tools','v'+str(re_java_lists_version[0]))  #加上‘v’，缺少报错
        req_java_version = clt.do_action_with_exception(del_java_version)
        create_java_policy_version = ali.createPolicyVersion('AliyunOSSFullAccess-java-tools','java_policy-rule','True')
        req_java_create_version = clt.do_action_with_exception(create_java_policy_version)
        print req_java_create_version
    else:
        create_java_policy_version = ali.createPolicyVersion('AliyunOSSFullAccess-java-tools','java_policy-rule','True')
        req_java_create_version = clt.do_action_with_exception(create_java_policy_version)
        print req_java_create_version
    if len(re_mobile_lists_version) >= 5:
        del_mobile_version = ali.deletePolicyVersion('AliyunOSSFullAccess-mobile-tools','v'+str(re_mobile_lists_version[0]))
        req_moblie_version = clt.do_action_with_exception(del_mobile_version)
        create_mobile_policy_version = ali.createPolicyVersion('AliyunOSSFullAccess-mobile-tools','mobile_policy_rule','True')
        req_mobile_create_version = clt.do_action_with_exception(create_mobile_policy_version)
        print req_mobile_create_version
    else:
        create_mobile_policy_version = ali.createPolicyVersion('AliyunOSSFullAccess-mobile-tools','mobile_policy_rule','True')
        req_mobile_create_version = clt.do_action_with_exception(create_mobile_policy_version)
        print req_mobile_create_version



