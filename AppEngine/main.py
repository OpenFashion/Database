from google.appengine.api import images
from google.appengine.ext import ndb

import webapp2

def get(self):
    bucket_name = os.environ.get(
        'openfashion-196206.appspot.com', app_identity.get_default_gcs_bucket_name())

    self.response.headers['Content-Type'] = 'text/plain'
    self.response.write(
        'Demo GCS Application running from Version: {}\n'.format(
            os.environ['CURRENT_VERSION_ID']))
    self.response.write('Using bucket name: {}\n\n'.format(bucket_name))

# def list_bucket(self, bucket):
#   """Create several files and paginate through them.

#   Production apps should set page_size to a practical value.

#   Args:
#     bucket: bucket.
#   """
#   self.response.write('Listbucket result:\n')

#   page_size = 1
#   stats = gcs.listbucket(bucket + '/foo', max_keys=page_size)
#   while True:
#     count = 0
#     for stat in stats:
#       count += 1
#       self.response.write(repr(stat))
#       self.response.write('\n')

#     if count != page_size or count == 0:
#       break
#     stats = gcs.listbucket(bucket + '/foo', max_keys=page_size,
#                            marker=stat.filename)