# -*- coding: utf-8 -*-

import os, sys
import shutil
import subprocess
import oss2

access_key_id = os.getenv('OSS_TEST_ACCESS_KEY_ID', 'xxx')
access_key_secret = os.getenv('OSS_TEST_ACCESS_KEY_SECRET', 'xxx')
bucket_name = os.getenv('OSS_TEST_BUCKET', 'devops-bak')
endpoint = os.getenv('OSS_TEST_ENDPOINT', 'oss-cn-hongkong.aliyuncs.com')
bucket = oss2.Bucket(oss2.Auth(access_key_id, access_key_secret), endpoint, bucket_name)
obj_name = 'yapi'

sub = subprocess.Popen("ls -rt *.tgz | tail -1", shell=True, stdout=subprocess.PIPE).stdout.read().replace("\n","")
rsub = 'yapi/' + sub
#sub.wait()

def main():
    try:
        bucket.put_object_from_file(rsub, sub)
        print sub
        sys.exit(0)
    except Exception as e:
        print(e)
        sys.exit(1)
if __name__ == '__main__':
    main()
