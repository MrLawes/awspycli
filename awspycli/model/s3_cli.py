# -*- coding:utf-8 -*-

import json
import os


class S3(object):
    def __init__(self):
        pass

    def exec_command(self, emr_command, **kwargs):
        """ change kwargs to aws command, and run it
        :param command:
        :param kwargs:
        :return:
        """
        aws_command = 'aws s3 {command} '.format(command=emr_command)
        l = []
        kwargs_keys = kwargs.keys()
        kwargs_keys.sort()
        for k in kwargs_keys:
            v = kwargs[k]
            if isinstance(v, dict) or isinstance(v, list):
                v = "' " + json.dumps(v) + " '"
            elif isinstance(v, bool):
                v = ""
            elif isinstance(v, int):
                v = str(v)
            k = k.replace('_', '-')
            l.append('--' + k + ' ' + v)
        aws_command += ' '.join(l)
        popen_result = os.popen(aws_command).readlines()
        try:
            popen_result = json.loads(''.join(popen_result))
        except:
            print(popen_result)
        return popen_result

    def cp(self, copy_from, copy_to, **kwargs):
        """ Copies a local file or S3 object to another location locally or in S3.
        :param copy_from:
        :param copy_to:
        :param kwargs:      https://docs.aws.amazon.com/cli/latest/reference/s3/cp.html
        :return:
        """
        return self.exec_command('cp %s %s' % (copy_from, copy_to), **kwargs)

    def ls(self, s3uri, **kwargs):
        """ List S3 objects and common prefixes under a prefix or all S3 buckets. Note that the --output and --no-paginate arguments are ignored for this command.
        :param s3uri:
        :param kwargs:      https://docs.aws.amazon.com/cli/latest/reference/s3/ls.html
        :return:
        """
        return self.exec_command('ls %s' % (s3uri,), **kwargs)


s3 = S3()
