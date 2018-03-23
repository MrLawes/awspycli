# Available Commands

   Documentation from aws emr cli reference: [https://docs.aws.amazon.com/cli/latest/reference/emr/](https://docs.aws.amazon.com/cli/latest/reference/emr/)

### create_cluster:

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
    
    import awspycli
    
    instance_groups = [
        {
            "InstanceCount": 1, "InstanceGroupType": "MASTER", "InstanceType": 'm1.large',
        },
        {
            "InstanceCount": 3, "InstanceGroupType": "CORE", "InstanceType": 'm1.large',
        },
    ]
    steps = [{
        'Name': 'awspycli default step',
        'Args': ['sleep', '10'],
        'Jar': 'command-runner.jar',
        'ActionOnFailure': 'TERMINATE_CLUSTER',
        'Type': 'CUSTOM_JAR',
        'Properties': ''
    }]
    print(awspycli.emr.create_cluster(
        ec2_attributes={
            "KeyName": "shinezone_emr",
        },
        release_label='emr-5.10.0',
        log_uri='s3n://shinezone-datacenter-application/log/',
        steps=steps,
        instance_groups=instance_groups,
    ))

### wait
    """ Wait until a particular condition is satisfied.
    :param cluster_id:
    :param status:
        cluster-running
        cluster-terminated
        step-complete
    :return:
    """
    import awspycli
    awspycli.emr.wait('cluster-running', 'j-3SD91U2E1L2QX')
