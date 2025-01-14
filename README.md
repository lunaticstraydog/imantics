# A fixed version of the Image Semantics package
Both the pip and git original versions of the imantics package have flow-breaking bugs.  
The pip version cannot handle large datasets (which is fixed in latest git version)  
The original git version fixes aforementionned bug, but hangs when exporting the dataset to coco json.  
## What is fixed here 
- Dataset export fixed (based the code on the pip version) 
- Handling of large dataset (cherry picked latest git) 
- Fixed split of dataset in ratios (code is broken in latest git)  
- Added a usage example (the original ones are a bit short / dont really work)  
## Installing

```
git clone https://github.com/lunaticstraydog/imantics
cd imantics
pip install -U . 
```
## Usage 
A new tutorial is available in examples/tutorial.ipybn  
It shows a short example of imantics coco workflow.  
Other examples are available in the examples/ directory 
<p align="center">
  <a href="/jsbroks/imantics/stargazers">
    <img src="https://img.shields.io/github/stars/jsbroks/imantics.svg">
  </a>
  <a href="/jsbroks/imantics/issues">
    <img src="https://img.shields.io/github/issues/jsbroks/imantics.svg">
  </a>
  <a href="https://tldrlegal.com/license/mit-license">
    <img src="https://img.shields.io/github/license/mashape/apistatus.svg">
  </a>
  <a href="https://travis-ci.org/jsbroks/imantics">
    <img src="https://travis-ci.org/jsbroks/imantics.svg?branch=master">
  </a>
  <a href="https://imantics.readthedocs.io/en/latest/?badge=latest">
    <img src="https://readthedocs.org/projects/imantics/badge/?version=latest">
  </a>
  <a href="https://pypi.org/project/imantics/">
    <img src="https://img.shields.io/pypi/v/imantics.svg">
  </a>
  <a href="https://pypi.org/project/imantics/">
    <img src="https://img.shields.io/pypi/dm/imantics.svg">
  </a>
</p>

Image understanding is widely used in many areas like satellite imaging, robotic technologies, sensory networks, medical and biomedical imaging, intelligent transportation systems, etc. Recently semantic analysis has become an active research topic aimed at resolving the gap between low level image features and high level semantics which is a promoting approach in image understanding.

With many image annotation semantics existing in the field of computer vision, it can become daunting to manage. This package provides the ability to convert and visualize many different types of annotation formats for object dectection and localization.

Currently Support Formats:

- COCO Format
- Binary Masks
- YOLO
- VOC


<p align="center">Join our growing <a href="https://discord.gg/4zP5Qkj">discord community</a> of ML practitioner</p>
<p align="center">
  <a href="https://discord.gg/4zP5Qkj">
    <img src="https://discord.com/assets/e4923594e694a21542a489471ecffa50.svg" width="120">
  </a>
</p>

<br />

<p align="center">If you enjoy my work please consider supporting me</p>
<p align="center">
  <a href="https://www.patreon.com/jsbroks">
    <img src="https://c5.patreon.com/external/logo/become_a_patron_button@2x.png" width="120">
  </a>
</p>

