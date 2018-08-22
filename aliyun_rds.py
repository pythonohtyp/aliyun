# -*- coding:utf-8 -*-
from aliyunsdkcore.client import AcsClient
from aliyunsdkrds.request.v20140815 import DescribeDatabasesRequest
from aliyunsdkrds.request.v20140815 import GrantAccountPrivilegeRequest
from aliyunsdkrds.request.v20140815 import DescribeDBInstancesRequest
import re


class alis:
    def __init__(self,accesskey,accesssecret,regionid):
        self.accesskey = accesskey
        self.accesssecret = accesssecret
        self.regionid = regionid
    def clt(self):
        clt = AcsClient(self.accesskey,self.accesssecret,self.regionid)
        return clt
    def describeDatabases(self,DBInstanceId):
        '''查看Mysql数据库列表'''
        request = DescribeDatabasesRequest.DescribeDatabasesRequest()
        request.set_DBInstanceId(DBInstanceId)
        request.set_accept_format('json')
        return request
    def grantAccountPrivilege(self,DBInstanceId,Accountname,DBName,AccountPrivilege):
        '''设置用户帐号权限（读写）或（只读）'''
        request = GrantAccountPrivilegeRequest.GrantAccountPrivilegeRequest()
        request.set_accept_format('json')
        request.set_DBInstanceId(DBInstanceId)
        request.set_AccountName(Accountname)
        request.set_DBName(DBName)
        request.set_AccountPrivilege(AccountPrivilege)    #ReadOnly 只读，ReadWrite读写
        return request
    def describeDBInstances(self):
        '''数据库实例列表'''
        request = DescribeDBInstancesRequest.DescribeDBInstancesRequest()
        request.set_accept_format('json')
        request.add_query_param('RegionId','cn-hangzhou')
        return request


if __name__ == '__main__':
    ali = alis('accesskey','accesssecret','cn-hangzhou')   #需改为华东1（cn-hangzhou)
    clt = ali.clt()
    try:
        dbinstance = ali.describeDBInstances()
        ask = clt.do_action_with_exception(dbinstance)
        b = re.findall(r'"DBInstanceId":"(.*?)","VpcCloudInstanceId"', ask) #列出所有RDS实例
        # print b
        n = 0
        for i in b: #遍历实例
            describedb = ali.describeDatabases(i)
            response = clt.do_action_with_exception(describedb)
            c = re.findall(r'DBName":"(.*?)","CharacterSetName"',response)  #列出实例里数据库的名字
            print c
            for j in c:
                grant = ali.grantAccountPrivilege(i,'toolsuser',j,'ReadOnly') #设置数据库为只读
                print clt.do_action_with_exception(grant)
                n = n + 1
            print n
            if i == 'rm-bp1uq2l2z0a3c676x': #单独设置某个实例
                describedb_gengine = ali.describeDatabases(i)
                response_gengine = clt.do_action_with_exception(describedb_gengine)
                gengine = re.findall(r'DBName":"(gengine.*?)","CharacterSetName"', response)  #筛选以某个字符串开始的数据库名
                game = re.findall(r'DBName":"(game.*?)","CharacterSetName"', response)
                print gengine
                print game
                for gen in gengine:
                    grant = ali.grantAccountPrivilege('rm-bp1uq2l2z0a3c676x','toolsuser',gen,'ReadWrite')
                    print clt.do_action_with_exception(grant)
                for gm in game:
                    grant_game = ali.grantAccountPrivilege('rm-bp1uq2l2z0a3c676x','gp_app',gm,'ReadWrite')
                    print clt.do_action_with_exception(grant_game)
    except Exception,e:
        print Exception,":",e
#
