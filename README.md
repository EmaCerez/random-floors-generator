# Random Floors Generator

<p>
  <img src="https://github.com/EmaCerez/RandFloor_Generator/assets/114211762/856714c0-062f-4bc5-adb1-116fc82594d2" width="150">
  <img src="https://github.com/EmaCerez/RandFloor_Generator/assets/114211762/11c2bb43-1721-40b2-af28-7ac8fcf167c3" width="150">
  <img src="https://github.com/EmaCerez/RandFloor_Generator/assets/114211762/34dafae5-cdaa-4054-a24d-17c38f09aba0" width="150">
  <img src="https://github.com/EmaCerez/RandFloor_Generator/assets/114211762/a309c9b6-5ad7-4f32-a062-8026595fb870" width="150">
</p>

## Description

This program generates graphs representing randomized floor topologies.

See examples above and below.

## Context

A friend of mine asked for this.

## Getting started

Once you cloned the repository, please install the requirements:

```bash
pip install -r requirements.txt
```

Then run the program using:

```bash
python main.py
```

### Parameters

You can specify various parameters using the following arguments:

`-p`, `--path`: Path to save output (str)

`-f`, `--filename`: Name of output file. (str)

`-rand`, `--randomize`: Weither or not the outside corners of the floors should be randomized. (bool)

`-cn`, `--corners`: How many outside corners in the randomized output. (int)

`-miw`, `--manual-inside-walls`: How many points to create inside walls (if not randomized). (int)

`-iw`, `--inside-walls`: How many points to create inside walls (if randomized). (int)

`-poly`, `--polygon`: Specify a polygon structure: [Point(0,0), Point(25,0), ...]. Points coordinates must be between 0 and 100. (list[Point])

`-sep`, `--separator`: Minimum distance between two inside points. Must not be too big, especially if inside-walls parameter is big. (float)

`-wl`, `--wall-length`: The xth closest point will be used to build walls. (int)

`-col`, `--color`: The color of the output." (str)

`-sd`, `--show-dots`, : Show points used to create the output. (bool)

(Like so:)

```bash
python main.py -rand True -col "blue" -wl 1 -iw 14 -cn 14
```



## Examples:

Without randomized outside walls:

<p float="left">
  <img src="https://media.discordapp.net/attachments/1130852949757800448/1136455267807133706/image.png?width=512&height=384" width="200"/>
  <img src="https://media.discordapp.net/attachments/1130852949757800448/1136455268042035241/image.png?width=512&height=384" width="200"/>
</p>

<p float="left">
  <img src="https://media.discordapp.net/attachments/1130852949757800448/1136455268276912228/image.png?width=512&height=384" width="200"/>
  <img src="https://media.discordapp.net/attachments/1130852949757800448/1136455268729901137/image.png?width=512&height=384" width="200"/>
</p>

With randomized outside walls:

<p float="left">
  <img src="https://media.discordapp.net/attachments/1130852949757800448/1136456848145391707/image.png?width=512&height=384" width="200"/>
  <img src="https://media.discordapp.net/attachments/1130852949757800448/1136456851253370930/image.png?width=512&height=384" width="200"/>
</p>

<p float="left">
  <img src="https://media.discordapp.net/attachments/1130852949757800448/1136456851823796235/image.png?width=512&height=384" width="200"/>
  <img src="https://media.discordapp.net/attachments/1130852949757800448/1136456852104810636/image.png?width=512&height=384" width="200"/>
</p>


## Process

(1) The program generates a set of point coordinates to create a polygon.

<img src="https://media.discordapp.net/attachments/301435638316793857/1136442230459072632/image.png?width=512&height=384" width="200"/>

(2) It divides the polygon into triangles using ajaycc17's algorithm.

<img src="https://media.discordapp.net/attachments/301435638316793857/1136442249668997301/image.png?width=512&height=384" width="200"/>

(3) It generates random points and check weither they are inside said triangles.

<img src="https://media.discordapp.net/attachments/1130852949757800448/1136442473707737118/image.png?width=512&height=384" width="200"/>

(4) It connects the points to their closest neighbour, or their second closest neighbour, and so on according to the `--wall-length` parameter.

<img src="https://media.discordapp.net/attachments/301435638316793857/1136442289942712340/image.png?width=512&height=384" width="200"/>


## Credits

polygon-triangulation (ajaycc17) : https://github.com/ajaycc17/polygon-triangulation/tree/main


## If you want to use this inside your own project:

Please credit me.
