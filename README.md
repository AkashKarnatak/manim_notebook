## **Manim notebook**
`manim_notebook` aims to integrate manim with jupyter notebook.

![mango][preview]

## **Installation**
System requirements are [cairo][cairo], [ffmpeg][ffmpeg], [sox][sox] and [latex][latex].

### From PyPI
You can directly install `manim_notebook` from PyPI via pip:
```
pip install manim_notebook
```
Make sure you installed the correct version of `manim_notebook` by running this command
```
pip show manim_notebook
```
If your version is not `1.0.1` then reinstall `manim_notebook`.
```
pip uninstall manim_notebook
pip install manim_notebook==1.0.1
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
### On Google Colab
To use `manim_notebook` on google colab, first you need to install system requirements specified above. You can install them with this command,
```sh
!wget https://raw.githubusercontent.com/AkashKarnatak/AkashKarnatak.github.io/master/install_manim_dependencies_on_colab.sh -O - | sh
```
Now you can install `manim_notebook` via,
```sh
pip install manim_notebook
```
**Spliting of output and input cell is not yet supported on google colab.**
## Usage
`manim_notebook` makes use of IPython's [cell magic][ipython_magic] commands to integrate manim in jupyter notebook. Cell magic takes a form like `%%magic` and are placed on top of each cell in jupyter notebook. 

Learn basic usage of `manim_notebook` [here][tutorial].




[preview]: images/preview.png
[ipython_magic]: https://ipython.readthedocs.io/en/stable/interactive/magics.html#cell-magics
[tutorial]: https://htmlpreview.github.io/?https://github.com/AkashKarnatak/manim_notebook/blob/master/Tutorial.html
[cairo]: https://www.cairographics.org/
[ffmpeg]: https://www.ffmpeg.org/
[sox]: http://sox.sourceforge.net/
[latex]: https://www.latex-project.org/