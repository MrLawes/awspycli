# Available Commands

   Documentation from aws emr cli reference: [https://docs.aws.amazon.com/cli/latest/reference/emr/](https://docs.aws.amazon.com/cli/latest/reference/emr/)

### add_steps
    """ Add a list of steps to a cluster.
    :param kwargs:
        cluster_id: string
        steps: [
            {},.....
        ]
    :return:
    """
    import awspycli
    steps = [{
        'Name': 'awspycli default step',
        'Args': ['sleep', '10'],
        'Jar': 'command-runner.jar',
        'ActionOnFailure': 'TERMINATE_CLUSTER',
        'Type': 'CUSTOM_JAR',
        'Properties': ''
    }]
    awspycli.emr.add_steps(
        cluster_id='j-3SD91U2E1L2QX',
        steps=steps,
    ))
        
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


### list_steps
    """ Provides a list of steps for the cluster in reverse order unless you specify stepIds with the request.
    :param kwargs:
    :return: 
    """
    import awspycli
    awspycli.emr.list_steps(cluster_id='j-3SD91U2E1L2QX',max_items=1)


### modify_cluster_attributes
    """ Modifies the cluster attributes 'visible-to-all-users' and 'termination-protected'.
    :param kwargs:
    :return:
    """
    import awspycli
    awspycli.emr.modify_cluster_attributes(cluster_id='j-3SD91U2E1L2QX', no_termination_protected=True)

### schedule_hbase_backup
    """  Adds a step to schedule automated HBase backup. This command is only available when using Amazon EMR versionsearlier than 4.0.
    """
    import awspycli
    awspycli.emr.schedule_hbase_backup(cluster_id='j-2S2NT3ICXM0CC', type ='full',)

### socks
    """ Create a socks tunnel on port 8157 from your machine to the master.
    :param cluster_id:
    :param key_pair_file:
    :return:
    """
    import awspycli
    awspycli.emr.socks(cluster_id='j-2S2NT3ICXM0CC', key_pair_file='~/emr.pem',)
    
### ssh
    """
    SSH into master node of the cluster.
    :param cluster_ids:     (string) Cluster Id of cluster you want to ssh into
    :param key_pair_file:   (string) Private key file to use for login
    :param command:         Command to execute on Master Node
    :return:                list. The result
    """
    import awspycli
    awspycli.emr.ssh(
        cluster_id='j-2S2NT3ICXM0CC', key_pair_file='~/emr.pem', command='ls /home/hadoop/'
    )
    >>> ['a.log  b.log']

        
### terminate_clusters
    """ Shuts down one or more clusters, each specified by cluster ID
    :param cluster_ids:
    :return:
    """
    import awspycli
    awspycli.emr.terminate_clusters(cluster_ids='j-3SD91U2E1L2QX')


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

### wait_all_step_complete
<aside class="notice">
insure do not add new step into cluster!
</aside>

    """ Wait until all step completed, insure do not add new step into cluster
    :return:
    """
    import awspycli;awspycli
    awspycli.emr.wait_all_step_complete(cluster_id='j-3SD91U2E1L2QX')
    
