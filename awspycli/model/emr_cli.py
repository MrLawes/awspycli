# -*- coding:utf-8 -*-

import json
import os
import traceback


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
        :return:
            {u'ClusterId': u'j-1OAMNPOAHUIFP'}
        """
        kwargs.setdefault('applications', 'Hadoop,Spark,Ganglia')
        kwargs['applications'] = ' Name='.join([''] + kwargs.pop('applications').split(',')).lstrip()
        ec2_attributes = kwargs['ec2_attributes']
        ec2_attributes.setdefault('InstanceProfile', 'EMR_EC2_DefaultRole')
        kwargs.setdefault('service_role', 'EMR_DefaultRole')
        return self.exec_command('create-cluster', **kwargs)


emr = EMR()
