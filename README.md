## **Manim notebook**
`manim_notebook` aims to integrate manim with jupyter notebook.

![mango][preview]

## **Installation**

### From PyPI
You can directly install `manim_notebook` from PyPI via pip:
```
pip install manim_notebook
```
or
### Directly
You can also install and configure things manually by cloning this repository,

```
git clone https://github.com/AkashKarnatak/manim_notebook.git
```
and then installing the necessary packages.
```
pip install -r requirements.txt
```
## Usage
`manim_notebook` makes use of IPython's [cell magic][ipython_magic] commands to integrate manim in jupyter notebook. Cell magic takes a form like `%%magic` and are placed on top of each cell in jupyter notebook. 

Learn basic usage of `manim_notebook` [here][tutorial].




[preview]: images/preview.png
[ipython_magic]: https://ipython.readthedocs.io/en/stable/interactive/magics.html#cell-magics
[tutorial]: https://htmlpreview.github.io/?https://github.com/AkashKarnatak/manim_notebook/blob/master/Tutorial.html