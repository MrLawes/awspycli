# -*- coding:utf-8 -*-

import json
import os


class EMR(object):
    def __init__(self):
        pass

    def exec_command(self, command, **kwargs):
        """ change kwargs to aws command, and run it
        :param command:
        :param kwargs:
        :return:
        """
        aws_command = 'aws emr {command} '.format(command=command)
        l = []
        kwargs_keys = kwargs.keys()
        kwargs_keys.sort()
        for k in kwargs_keys:
            v = kwargs[k]
            if isinstance(v, dict) or isinstance(v, list):
                v = "' " + json.dumps(v) + " '"
            if isinstance(v, bool):
                v = ""
            k = k.replace('_', '-')
            l.append('--' + k + ' ' + v)
        aws_command += ' '.join(l)
        popen_result = os.popen(aws_command).readlines()
        try:
            popen_result = json.loads(''.join(popen_result))
        except:
            print(popen_result)
        return popen_result

    def create_cluster(self, **kwargs):
        """ Creates an Amazon EMR cluster with the specified configurations.
        :param kwargs:
            applications:
                Args=string,string,string ...
                default: Hadoop,Spark,Ganglia
            ec2_attributes:
                Args=json
                    InstanceProfile:
                        default: EMR_EC2_DefaultRole
            service_role:
                Args=string
                default: EMR_DefaultRole
            name:
                Args=string
                default: awspycli
            region
                Args=string
                default: us-east-1
        :return:
            {u'ClusterId': u'j-1OAMNPOAHUIFP'}
        """
        kwargs.setdefault('applications', 'Hadoop,Spark,Ganglia')
        kwargs['applications'] = ' Name='.join([''] + kwargs.pop('applications').split(',')).lstrip()
        ec2_attributes = kwargs['ec2_attributes']
        ec2_attributes.setdefault('InstanceProfile', 'EMR_EC2_DefaultRole')
        kwargs.setdefault('service_role', 'EMR_DefaultRole')
        kwargs.setdefault('name', 'awspycli')
        kwargs.setdefault('region', 'us-east-1')
        kwargs.setdefault('instance_groups', {})
        instance_groups = kwargs['instance_groups']
        for instance_group in instance_groups:
            instance_group.setdefault(
                'Name', instance_group['InstanceGroupType'] + ' ' + instance_group['InstanceType'] + ' x '
                        + str(instance_group['InstanceCount'])
            )
        kwargs.setdefault('steps', [{
            'Name': 'awspycli default step',
            'Args': ['sleep', '10'],
            'Jar': 'command-runner.jar',
            'ActionOnFailure': 'TERMINATE_CLUSTER',
            'Type': 'CUSTOM_JAR',
            'Properties': ''
        }])
        return self.exec_command('create-cluster', **kwargs)


emr = EMR()
