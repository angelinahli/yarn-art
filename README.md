# Yarn Art

### Draft Specifications

#### App Concept:
* Crochet and Knit image based pattern generator.
* You upload an image, and it spits out a pattern with a color scheme.

#### Desired Features:
* Pattern should be calibrated -- Recommend that users knit / single crochet a 10+ x 10+ square swatch, measure it, and then calibrate the picture output with regards to the swatch.
    * Once you accumulate more data, use the most common calibration scheme instead.
    * Then you can also allow users to specify the desired size of the final piece.
    * You can save swatch calibrations and allow users to use the same swatch to calibrate multiple projects.
* Pattern can be downloadable as a PDF, OR can be used as an interactive template:
    * PDF: (Honestly, just include an HTML link and tell users to print?)
        * Should include key for colors
        * Include grid lines
        * Should include labels for each row
        * Potentially output both a color label version and a symbol label version.
    * Interactive Template:
        * Include key for colors
        * Include grid lines
        * Allow user to mark progress - clicking a row should mark it (and all previous rows) as complete.
* As always, app must be beautiful.
* Pattern should allow users to choose how many colors are generated / 

#### Potential Technologies:
* https://pillow.readthedocs.io/en/stable/reference/Image.html
* https://pypi.org/project/opencv-python/
* https://www.geeksforgeeks.org/python-convert-html-pdf/
* https://medium.com/@manivannan_data/resize-image-using-opencv-python-d2cdbbc480f0
* https://stackoverflow.com/questions/5906693/how-to-reduce-the-number-of-colors-in-an-image-with-opencv

#### Proof of Concept
* App (without memory) that accepts an image file, a swatch, and some basic parameters (size of resulting piece) and converts it into a template with colors in the grid.


#### Other Notes
* Test Image Attributions:
    * https://pixabay.com/illustrations/cactus-torn-green-flower-4338616/
    * https://pixabay.com/photos/abstract-art-works-of-art-2675672/
    * https://pixabay.com/illustrations/clipart-fish-sea-water-swim-3418189/
    * https://pixabay.com/vectors/feather-silhouette-sticker-clipart-2781343/