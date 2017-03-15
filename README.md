# Simple Python OCR
This repository is a fork of [simple-ocr-opencv](https://github.com/goncalopp/simple-ocr-opencv) by Goncalopp, with the
goal of turning this engine-project with examples into a working library for everyone
to use. Currently, this project is not released under a LICENSE. Copying is only allowed
when you have explicit permission of the authors, at this point full copyright applies.

    Copyright (C) 2016-2017 by Goncalopp and RedFantom
    All authors are the copyright owners of their respective additions

Originally inspired by [this question](http://stackoverflow.com/questions/9413216/simple-digit-recognition-ocr-in-opencv-python) on StackOverflow.

### Essential Concepts

#### Segmentation

In order for OCR to be performed on a image, several steps must be 
performed on the source image. Segmentation is the process of 
identifying the regions of the image that represent characters. 

This project uses rectangles to model segments. 

#### Supervised learning with a classification problem

The [classification problem][] consists in identifying to which class a 
observation belongs to (i.e.: which particular character is contained 
in a segment).

[Supervised learning][] is a way of "teaching" a machine. Basically, an 
algorithm is *trained* through *examples* (i.e.: this particular 
segment contains the character `f`). After training, the machine 
should be able to apply its aquired knowledge to new data.

The [k-NN algorithm], used in this project, is one of the simplest  
classification algorithm.

#### Grounding

Creating a example image with already classified characters, for 
training purposes.
See [ground truth][].

[classification problem]: https://en.wikipedia.org/wiki/Statistical_classification
[Supervised learning]: https://en.wikipedia.org/wiki/Supervised_learning
[k-NN algorithm]: https://en.wikipedia.org/wiki/K-nearest_neighbors_classification
[ground truth]: https://en.wikipedia.org/wiki/Ground_truth

#### How to understand this project

Unfortunately, documentation is a bit sparse at the moment (I 
gladly accept contributions).
The project is well-structured, and most classes and functions have 
docstrings, so that's probably a good way to start.

If you need any help, don't hesitate to contact me. You can find my 
email on my github profile.


#### How to use

Please check `example.py` for basic usage with the existing pre-grounded images.

You can use your own images, by placing them on the `data` directory. 
Grounding images interactively can be accomplished by using `grouding.UserGrounder`.
For more details check `example_grounding.py`
