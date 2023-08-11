# Contents

This directory contains a few basic notebooks to learn exploring, manipulating and measuring biomedical image data.
You can also download the corresponding [slides](LINK).

In this skill track, you'll work with different Open-Source datasets:
- CT scan from [The Cancer Imaging Archive](https://www.cancerimagingarchive.net/about-the-cancer-imaging-archive-tcia/)
- hand radiograph from a 2017 [Radiological Society of North America competition](LINK!)
- MR imaging data from the [Sunnybrook Cardiac Dataset](LINK!) 
- MRI DICOM data set [head of a normal male human](https://zenodo.org/record/16956#.YFMM5PtKiV5) [1] and 
- Open Access Series of Imaging Studies [Oasis](https://www.oasis-brains.org/) [2]


## Basic concepts of Exploration
The [exploration](exploration.ipynb) notebook serves as a starting point for all following notebooks. 
To begin the course, you'll learn how to load, build and navigate N-dimensional images using a CT image of the human brain.


## Basic concepts of Masks and Filters
[masks\_and\_filters](masks_and_filters.ipynb) is a notebook that cut image processing to the bone by transforming CT images.
You'll learn how to exploit intensity patterns to select sub-regions of an array, and you'll use convolutional filters to detect interesting features.

## Basic concepts of Measurements
[measurements](measurements.ipynb) is a notebook about image segmentation, object labeling, and morphological measurement.
You'll learn the fundamentals of image segmentation, object labeling, and morphological measurement.

## Basic concepts of Image Comparison
[image\_comparison](image_comparison.ipynb) discusses basics of registration, resampling, and image comparison.
You'll learn the basics of registration, resampling, and image comparison. Then, you'll use the extracted measurements to evaluate the effect of Alzheimer's Disease on brain structure.

## Learning objectives

By the end of these notebooks, you should feel more comfortable with:
- 

## References
<a id="1">[1]</a>
Lionheart, W. R. B. (2015)
An MRI DICOM data set of the head of a normal male human aged 52 [Data set]
Zenodo, https://doi.org/10.5281/zenodo.16956
<a id="2">[2]</a> 
Marcus, DS et al. 
Open Access Series of Imaging Studies (OASIS): Cross-Sectional MRI Data in Young, Middle Aged, Nondemented, and Demented Older Adults 
Journal of Cognitive Neuroscience, 19, 1498-1507. doi: 10.1162/jocn.2007.19.9.1498