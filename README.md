# MoG2-OpenCV
This mini project Is about  background sustraction with openCV using BackgroundSustractionMOG2 method un OpenCV:

int nmixtures
Maximum allowed number of mixture components. Actual number is determined dynamically per pixel.

float backgroundRatio
Threshold defining whether the component is significant enough to be included into the background model ( corresponds to TB=1-cf from the paper??which paper??). cf=0.1 => TB=0.9 is default. For alpha=0.001, it means that the mode should exist for approximately 105 frames before it is considered foreground.

float varThresholdGen
Threshold for the squared Mahalanobis distance that helps decide when a sample is close to the existing components (corresponds to Tg). If it is not close to any component, a new component is generated. 3 sigma => Tg=3*3=9 is default. A smaller Tg value generates more components. A higher Tg value may result in a small number of components but they can grow too large.

float fVarInit
Initial variance for the newly generated components. It affects the speed of adaptation. The parameter value is based on your estimate of the typical standard deviation from the images. OpenCV uses 15 as a reasonable value.

float fVarMin
Parameter used to further control the variance.

float fVarMax
Parameter used to further control the variance.

float fCT
Complexity reduction parameter. This parameter defines the number of samples needed to accept to prove the component exists. CT=0.05 is a default value for all the samples. By setting CT=0 you get an algorithm very similar to the standard Stauffer&Grimson algorithm.

uchar nShadowDetection
The value for marking shadow pixels in the output foreground mask. Default value is 127.

float fTau
Shadow threshold. The shadow is detected if the pixel is a darker version of the background. Tau is a threshold defining how much darker the shadow can be. Tau= 0.5 means that if a pixel is more than twice darker then it is not shadow

This algorithm Is based in Gassian Mixture Models AND this Is an unsupervised clustering algorithm, but clustes what? Ok, we want cluster the image pixel in 2 groups de background pixel and foreground pixel, AND this algorithm use a probability distribution 
To decide it.

 
