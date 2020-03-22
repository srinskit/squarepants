# squarepants
Squarify an image

## Install
```sh
git clone <srinskit/squarepants>

cd squarepants

pip3 install squarepants/ --user
```

Note: make sure opencv for python is installed

## Uninstall
```sh
pip3 uninstall sqaurepants
```

## Usage
```sh
squarepants -h                                               

Usage: squarepants [-h] [-s {original,round}] [-p PADDING] [-d] image

positional arguments:
  image                 Path to image file

optional arguments:
  -h, --help            show this help message and exit
  -s {original,round}, --shape {original,round}
                        Shaped of the inner image
  -p PADDING, --padding PADDING
                        Minimum padding around the inner image
  -d, --debug           Run in debug mode
```

```sh
# Sqaure output, original inner image, default padding

squarepants test.jpg


# Sqaure output, round inner image, default padding

squarepants test.jpg -s round


# Sqaure output, round inner image, 100px padding

squarepants test.jpg -s round -p 100
```
