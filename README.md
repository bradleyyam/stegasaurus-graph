# stegasaurus-graph
An implementation of image steganography using lower-order bit manipulation.

Call method encode(source, target, text) to encode any given text into the source image, the new steganographed image will be saved under the target name as a png file. The number of characters in the text must not exceed the number of pixels in the image.

Call method decode(source, target) to decipher the text steganographed into any source image. The image must have been produced by the corresponding encode function.
