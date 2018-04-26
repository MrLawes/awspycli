# Available Commands

   Documentation from aws S3 cli reference: [https://docs.aws.amazon.com/cli/latest/reference/s3/index.html](https://docs.aws.amazon.com/cli/latest/reference/s3/index.html)

### cp
    """ Copies a local file or S3 object to another location locally or in S3.
    :param copy_from: 
    :param copy_to:
    :param kwargs:      https://docs.aws.amazon.com/cli/latest/reference/s3/cp.html
    cp:
        <LocalPath> <S3Uri> or <S3Uri> <LocalPath> or <S3Uri> <S3Uri>
    kwargs:
        [dryrun]
        [quiet]
        [include <value>]
        [exclude <value>]
        [acl <value>]
        [follow_symlinks | no_follow_symlinks]
        [no_guess_mime_type]
        [sse <value>]
        [sse_c <value>]
        [sse_c_key <value>]
        [sse_kms_key_id <value>]
        [sse_c_copy_source <value>]
        [sse_c_copy_source_key <value>]
        [storage_class <value>]
        [grants <value> [<value>...]]
        [website_redirect <value>]
        [content_type <value>]
        [cache_control <value>]
        [content_disposition <value>]
        [content_encoding <value>]
        [content_language <value>]
        [expires <value>]
        [source_region <value>]
        [only_show_errors]
        [no_progress]
        [page_size <value>]
        [ignore_glacier_warnings]
        [force_glacier_transfer]
        [request_payer <value>]
        [metadata <value>]
        [metadata_directive <value>]
        [expected_size <value>]
        [recursive]
    """
      
    import awspycli
    awspycli.s3.cp(copy_from='/tmp/test.py', copy_to='s3://shinezone-architecture/test/test.py', quiet=True)

### ls
     """ List S3 objects and common prefixes under a prefix or all S3 buckets. Note that the --output and --no-paginate arguments are ignored for this command.
    :param s3uri:       path (string), startswith s3://
    :param kwargs:      https://docs.aws.amazon.com/cli/latest/reference/s3/ls.html
    :return:
     ls:
        <S3Uri> or NONE
    kwargs:
        [recursive]
        [page_size <value>]
        [human_readable]
        [summarize]
        [request_payer <value>]
    """
      
    import awspycli
    awspycli.s3.ls(s3uri='s3://shinezone-architecture/test/',human_readable=True)

### mb
    """ Creates an S3 bucket.
    :param s3uri:       path (string), startswith s3://
    :param kwargs:
    :return:
    """
      
    import awspycli
    awspycli.s3.mb(s3uri='s3://awspyclimakebucket',)

### mv
    """ Moves a local file or S3 object to another location locally or in S3.
    :param mv_from:
    :param mv_to:
    :param kwargs:      https://docs.aws.amazon.com/cli/latest/reference/s3/mv.html
    :return:
    """
      
    import awspycli
    awspycli.s3.mv(mv_from='s3://shinezone-architecture/test/test.py', mv_to='s3://shinezone-architecture/test/test_mv.py', quiet=True)

### presign
    """ Generate a pre-signed URL for an Amazon S3 object.
    This allows anyone who receives the pre-signed URL to retrieve the S3 object with an HTTP GET request.
    For sigv4 requests the region needs to be configured explicitly.
    :param s3uri:       path (string), startswith s3://
    :param kwargs:      https://docs.aws.amazon.com/cli/latest/reference/s3/presign.html
    :return:
    """
      
    import awspycli
    awspycli.s3.presign(s3uri='s3://shinezone-architecture/test/test.py')

### rb
    """ Deletes an empty S3 bucket.
    A bucket must be completely empty of objects and versioned objects before it can be deleted.
    However, the --force parameter can be used to delete the non-versioned objects in the bucket before the bucket is deleted.
    :param s3uri:       path (string), startswith s3://
    :param kwargs:      https://docs.aws.amazon.com/cli/latest/reference/s3/rb.html
    :return:
    """
      
    import awspycli
    awspycli.s3.rb(s3uri='s3://awspyclimakebucket')

### rm
    """ Deletes an S3 object.
    :param s3uri:       path (string), startswith s3://
    :param kwargs:      https://docs.aws.amazon.com/cli/latest/reference/s3/rm.html
    :return:
    """
      
    import awspycli
    awspycli.s3.rm(s3uri='s3://shinezone-architecture/test/test.py')

### sync
    """ Syncs directories and S3 prefixes.
    Recursively copies new and updated files from the source directory to the destination.
    Only creates folders in the destination if they contain one or more files.
    """
      
    import awspycli
    a = awspycli.s3.sync(sync_from='/tmp/test/', sync_to='s3://shinezone-architecture/test/yourtest/', delete=True)

### sync
    """ Set the website configuration for a bucket.
    :param s3uri:       path (string), startswith s3://
    """
      
    import awspycli
    awspycli.s3.website(s3uri='s3://shinezone-architecture/')

