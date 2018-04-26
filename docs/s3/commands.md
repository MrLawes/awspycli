# Available Commands

   Documentation from aws S3 cli reference: [https://docs.aws.amazon.com/cli/latest/reference/s3/index.html](https://docs.aws.amazon.com/cli/latest/reference/s3/index.html)

### cp
    """ Copies a local file or S3 object to another location locally or in S3.
    :param copy_from: 
    :param copy_to:
    :param kwargs:      https://docs.aws.amazon.com/cli/latest/reference/s3/cp.html
    :return:
    """
    import awspycli
    awspycli.s3.cp(copy_from='/tmp/chenhaiou/test.py', copy_to='s3://shinezone-architecture/test/chenhaiou/test.py', quiet=True)

    