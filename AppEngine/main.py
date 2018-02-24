from google.appengine.api import images
from google.appengine.ext import ndb

import webapp2

class MainPage(webapp2.RequestHandler):
    def get(self):
        self.response.headers['Content-Type'] = 'text/plain'
        self.response.write('Hello, World!')


app = webapp2.WSGIApplication([
    ('/', MainPage),
], debug=True)

# def get(self):
#     bucket_name = os.environ.get(
#         'openfashion-196206.appspot.com', app_identity.get_default_gcs_bucket_name())

#     self.response.headers['Content-Type'] = 'text/plain'
#     self.response.write(
#         'Demo GCS Application running from Version: {}\n'.format(
#             os.environ['CURRENT_VERSION_ID']))
#     self.response.write('Using bucket name: {}\n\n'.format(bucket_name))

# def create_file(self, filename):
#     """Create a file."""

#     self.response.write('Creating file {}\n'.format(filename))

#     # The retry_params specified in the open call will override the default
#     # retry params for this particular file handle.
#     write_retry_params = cloudstorage.RetryParams(backoff_factor=1.1)
#     with cloudstorage.open(
#         filename, 'w', content_type='text/plain', options={
#             'x-goog-meta-foo': 'foo', 'x-goog-meta-bar': 'bar'},
#             retry_params=write_retry_params) as cloudstorage_file:
#                 cloudstorage_file.write('abcde\n')
#                 cloudstorage_file.write('f'*1024*4 + '\n')
#     self.tmp_filenames_to_clean_up.append(filename)


# if __name__ == "__main__": 
# 	create_file(self, "test.txt")

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