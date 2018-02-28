/**
 * Triggered from a message on a Cloud Storage bucket.
 *
 * @param {!Object} event The Cloud Functions event.
 * @param {!Function} The callback function.
 */
exports.imageToJPG = functions.storage.object().onChange((event) => {
  const object = event.data;
  const filePath = object.name;
  const baseFileName = path.basename(filePath, path.extname(filePath));
  const fileDir = path.dirname(filePath);
  const JPEGFilePath = path.normalize(path.format({dir: fileDir, name: baseFileName, ext: JPEG_EXTENSION}));
  const tempLocalFile = path.join(os.tmpdir(), filePath);
  const tempLocalDir = path.dirname(tempLocalFile);
  const tempLocalJPEGFile = path.join(os.tmpdir(), JPEGFilePath);

exports.processFile = (event, callback) => {
  console.log('Processing file: ' + event.data.name);
    const bucket = gcs.bucket(object.bucket);
  // Create the temp directory where the storage file will be downloaded.
  return mkdirp(tempLocalDir).then(() => {
    // Download file from bucket.
    return bucket.file(filePath).download({destination: tempLocalFile});
  }).then(() => {
    console.log('The file has been downloaded to', tempLocalFile);
    // Convert the image to JPEG using ImageMagick.
    return spawn('convert', [tempLocalFile, tempLocalJPEGFile]);
  }).then(() => {
    console.log('JPEG image created at', tempLocalJPEGFile);
    // Uploading the JPEG image.
    return bucket.upload(tempLocalJPEGFile, {destination: JPEGFilePath});
  }).then(() => {
    console.log('JPEG image uploaded to Storage at', JPEGFilePath);
    // Once the image has been converted delete the local files to free up disk space.
    fs.unlinkSync(tempLocalJPEGFile);
    fs.unlinkSync(tempLocalFile);
    return;
  });
  callback();
  
};
