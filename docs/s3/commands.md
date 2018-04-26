# Available Commands

   Documentation from aws S3 cli reference: [https://docs.aws.amazon.com/cli/latest/reference/s3/index.html](https://docs.aws.amazon.com/cli/latest/reference/s3/index.html)

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
    