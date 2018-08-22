# -*- coding:utf-8 -*-
from ali_ecs_SecurityGroup import *

ali = alis('LTAIZhlYZ8QUhvMd', 'VbBW1j1IxE8PmPWvUEOJYgv6jtXhBo', 'cn-shenzhen')  # 需改为华东1（cn-hangzhou
clt = ali.clt()
req = ali.describeSecurityGroupsRequest()
def func_ali_sz_start():
    try:
        ali_add_rules_1 = ali.authorizeSecurityGroupRequest('sg-wz96tih61y50hgfx39ab','tcp','8888/8888','0.0.0.0/0',1,'fmy-game-service(n0)')
        ali_add_rules_2 = ali.authorizeSecurityGroupRequest('sg-wz96tih61y50hgfx39ab','tcp','52001/52005','0.0.0.0/0',2,'fmy-game-service(n1-n5)')
        '''SG_AS_GameJavaWeb'''
        ali_add_rules_3 = ali.authorizeSecurityGroupRequest('sg-wz926xu5ur7bkykogcc1','tcp','50000/50010','0.0.0.0/0',1,'-')
        ali_add_rules_4 = ali.authorizeSecurityGroupRequest('sg-wz926xu5ur7bkykogcc1','tcp','50015/50095','0.0.0.0/0',6,'多服端口')
        ali_add_rules_5 = ali.authorizeSecurityGroupRequest('sg-wz926xu5ur7bkykogcc1','tcp','843/843','0.0.0.0/0',7,'flash跨域服务')
        '''SG_AS_GameServer'''
        '''添加规则（开服）'''
        response_1 = clt.do_action_with_exception(ali_add_rules_1)   #添加(开服)
        response_2 = clt.do_action_with_exception(ali_add_rules_2)   #添加(开服)
        response_3 = clt.do_action_with_exception(ali_add_rules_3)   #添加(开服)
        response_4 = clt.do_action_with_exception(ali_add_rules_4)   #添加(开服)
        response_5 = clt.do_action_with_exception(ali_add_rules_5)   #添加(开服)
        print response_1,response_2,response_3,response_4,response_5
        return "已开服，权限开启"
    except Exception,e:
        print Exception,":",e
def func_ali_sz_stop():
    try:
        ali_rvk_rules_1 = ali.revokeSecurityGroupRequest('sg-wz96tih61y50hgfx39ab', 'tcp', '8888/8888', '0.0.0.0/0', 1)
        ali_rvk_rules_2 = ali.revokeSecurityGroupRequest('sg-wz96tih61y50hgfx39ab', 'tcp', '52001/52005', '0.0.0.0/0', 2)
        '''SG_AS_GameJavaWeb'''
        ali_rvk_rules_3 = ali.revokeSecurityGroupRequest('sg-wz926xu5ur7bkykogcc1', 'tcp', '50000/50010', '0.0.0.0/0', 1)
        ali_rvk_rules_4 = ali.revokeSecurityGroupRequest('sg-wz926xu5ur7bkykogcc1', 'tcp', '50015/50095', '0.0.0.0/0', 6)
        ali_rvk_rules_5 = ali.revokeSecurityGroupRequest('sg-wz926xu5ur7bkykogcc1', 'tcp', '843/843', '0.0.0.0/0', 7)
        '''SG_AS_GameServer'''
        '''删除规则（停服）'''
        response_1 = clt.do_action_with_exception(ali_rvk_rules_1)   #添加(停服)
        response_2 = clt.do_action_with_exception(ali_rvk_rules_2)   #添加(停服)
        response_3 = clt.do_action_with_exception(ali_rvk_rules_3)   #添加(停服)
        response_4 = clt.do_action_with_exception(ali_rvk_rules_4)   #添加(停服)
        response_5 = clt.do_action_with_exception(ali_rvk_rules_5)   #添加(停服)
        print response_1,response_2,response_3,response_4,response_5
        return "已停服，权限关闭"
    except Exception,e:
        print Exception,":",e

