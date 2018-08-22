# -*- coding:utf-8 -*-
from modify_company_IP import *

ali = alis('LTAIZhlYZ8QUhvMd', 'VbBW1j1IxE8PmPWvUEOJYgv6jtXhBo', 'cn-shenzhen')  # 需改为华东1（cn-hangzhou
clt = ali.clt()
tuple_port = ['80/80', '9876/9876', '9877/9877', '3717/3717', '22024/22024', '8888/8888', '52001/52005', '51000/51005',
              '22024/22024', '50000/50010', '50015/50095', '843/843', '3389/3389', '4018/4018']
tuple_priority = ['2', '50', '51', '52', '80', '1', '2', '50', '80', '1', '6', '7', '50', '99']
tuple_description = ['fmy-website-online', 'fmy-website-admin', 'smart-sso-srever', 'mongodb-agent', 'linux-ssh',
                     'fmy-game-service(n0)',
                     'fmy-game-service(n1-n5)', 'fmy-game-admin(n1-n5)', 'linux-ssh', '-', '多服端口', 'flash跨域服务',
                     'windows远程桌面', '-']
# old_ip = '113.215.180.185'
# new_ip = '113.215.180.188'
def func_ali_sz_revoke_IP(old_ip):
    try:    #ECS
        for i in range(14):
            if i < 5:
                ali_rvk_rules_1 = ali.revokeSecurityGroupRequest('sg-wz96tih61y50hgfx39ab','tcp',tuple_port[i], old_ip, tuple_priority[i])
                '''SG_AS_OfficialWebsite'''
                print clt.do_action_with_exception(ali_rvk_rules_1)
            elif 8 >= i >= 5:
                ali_rvk_rules_2 = ali.revokeSecurityGroupRequest('sg-wz96tih61y50hgfx39ab','tcp',tuple_port[i], old_ip, tuple_priority[i])
                '''SG_AS_GameJavaWeb'''
                print clt.do_action_with_exception(ali_rvk_rules_2)
            else:
                ali_rvk_rules_3 = ali.revokeSecurityGroupRequest('sg-wz96tih61y50hgfx39ab','tcp',tuple_port[i], old_ip, tuple_priority[i])
                '''SG_AS_GameServer'''
                print clt.do_action_with_exception(ali_rvk_rules_3)
    except Exception, e:
        print Exception, ":", e
    # try:    #DDS
    #     ali_dds_del_IP = ali.modifySecurityIps_dds('dds-bp1d76757b10d784',old_ip,'Delete')
    #     '''DDS删除旧IP白名单'''
    #     print clt.do_action_with_exception(ali_dds_del_IP)
    #
    # except Exception, e:
    #     print Exception, ":", e
def func_ali_sz_add_IP(new_ip):
    try:    #ECS
        for i in range(14):
            if i < 5:
                ali_add_rules_1 = ali.authorizeSecurityGroupRequest('sg-wz96tih61y50hgfx39ab', 'tcp', tuple_port[i], new_ip, tuple_priority[i],tuple_description[i])
                '''SG_AS_OfficialWebsite'''
                print clt.do_action_with_exception(ali_add_rules_1)
            elif 8 >= i >= 5:
                ali_add_rules_2 = ali.authorizeSecurityGroupRequest('sg-wz96tih61y50hgfx39ab', 'tcp', tuple_port[i], new_ip, tuple_priority[i],tuple_description[i])
                '''SG_AS_GameJavaWeb'''
                print clt.do_action_with_exception(ali_add_rules_2)
            else:
                ali_add_rules_3 = ali.authorizeSecurityGroupRequest('sg-wz96tih61y50hgfx39ab', 'tcp', tuple_port[i], new_ip, tuple_priority[i],tuple_description[i])
                '''SG_AS_GameServer'''
                print clt.do_action_with_exception(ali_add_rules_3)
    except Exception, e:
        print Exception, ":", e
    # try:    #RDS
    #     dbinstance = ali.describeDBInstances()
    #     ask = clt.do_action_with_exception(dbinstance)
    #     b = re.findall(r'"DBInstanceId":"(.*?)","VpcCloudInstanceId"',ask)
    #     for i in b:
    #         ali_rds_IP = ali.modifySecurityIps(i,new_ip,'company_public_ip')
    #         print clt.do_action_with_exception(ali_rds_IP)
    # except Exception, e:
    #     print Exception, ":", e
    # try:    #DDS
    #     ali_dds_add_IP = ali.modifySecurityIps_dds('dds-bp1d76757b10d784',new_ip,'Add')
    #     '''DDS添加新IP白名单'''
    #     print clt.do_action_with_exception(ali_dds_add_IP)
    # except Exception, e:
    #     print Exception, ":", e
if __name__ == '__main__':
    func_ali_sz_add_IP('113.215.180.185')