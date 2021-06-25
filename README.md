This repository is about trying different noise and finding hoe to remove them. I started with Salt and Pepper noise.

### Usage
```console
$ pip install -r requirements.txt
$ python3 main.py
```

## What are noises
Random variation of brightness or color information in images. It can be produced by sensor or circuitry of an electronic device
### Examples
Some example are
1. Gaussian noise -It is also called electronic noise because it arises in amplifiers or detectors. Gaussian noise caused by natural sources such as thermal vibration of atoms and discrete nature of radiation of warm objects.
2. Impulsive noise - This is also called data drop noise because statistically it drops the original data values. This noise is also referred to as salt and pepper noise. This noise is seen in data transmission.
3. Periodic noise - This noise is generated from electronics interferences, especially in power signals during image acquisition. This noise has special characteristics like spatially dependent and sinusoidal in nature at multiples of specific frequency. It appears in the form of conjugate spots in the frequency domain.

### References
- https://medium.com/image-vision/noise-in-digital-image-processing-55357c9fab71
- https://arxiv.org/pdf/1505.03489.pdf
