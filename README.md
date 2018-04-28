Dijkstra Maps
-------------

This repository contains an implementation of Dijkstra Maps, as described [here](http://www.roguebasin.com/index.php?title=The_Incredible_Power_of_Dijkstra_Maps) and [here](http://www.roguebasin.com/index.php?title=Dijkstra_Maps_Visualized).  The algorithm is implemented in Cython.

Setup
-----

You will need Cython and a working C compiler to build this extension module.

```
python setup.py build_ext --inplace
```

Example
-------

The `build_map` function constructs the Dijkstra map.  It takes an array of sentinel values (`999` is the default), with some points marked as distance zero (or really any other constant)

```
$ dmap
array([[999, 999, 999, 999, 999, 999, 999, 999, 999, 999, 999, 999],
       [999, 999, 999, 999, 999, 999, 999, 999, 999, 999, 999, 999],
       [999, 999,   0, 999, 999, 999, 999, 999, 999, 999, 999, 999],
       [999, 999, 999, 999, 999, 999, 999, 999, 999, 999, 999, 999],
       [999, 999, 999, 999, 999, 999, 999, 999, 999, 999, 999, 999],
       [999, 999, 999, 999, 999, 999, 999, 999, 999, 999, 999, 999],
       [999, 999, 999, 999, 999, 999, 999, 999, 999, 999, 999, 999],
       [999, 999, 999, 999, 999, 999, 999, 999, 999, 999, 999, 999],
       [999, 999, 999, 999, 999, 999, 999, 999, 999, 999, 999, 999],
       [999, 999, 999, 999, 999, 999, 999, 999, 999, 999, 999, 999],
       [999, 999, 999, 999, 999, 999, 999, 999, 999, 999, 999, 999],
       [999, 999, 999, 999, 999, 999, 999, 999, 999, 999, 999, 999]])
```

And an array acting as a mask for walkable points

```
$ walkable
array([[ 0.,  0.,  0.,  0.,  0.,  0.,  0.,  0.,  0.,  0.,  0.,  0.],
       [ 0.,  1.,  1.,  1.,  1.,  1.,  0.,  0.,  0.,  0.,  0.,  0.],
       [ 0.,  1.,  1.,  1.,  1.,  1.,  0.,  0.,  0.,  0.,  0.,  0.],
       [ 0.,  1.,  1.,  1.,  1.,  1.,  0.,  0.,  0.,  0.,  0.,  0.],
       [ 0.,  1.,  1.,  1.,  1.,  1.,  0.,  0.,  1.,  1.,  1.,  0.],
       [ 0.,  1.,  1.,  1.,  1.,  1.,  0.,  0.,  1.,  1.,  1.,  0.],
       [ 0.,  0.,  0.,  0.,  1.,  0.,  0.,  0.,  1.,  1.,  1.,  0.],
       [ 0.,  0.,  0.,  0.,  1.,  0.,  0.,  0.,  1.,  1.,  1.,  0.],
       [ 0.,  0.,  0.,  0.,  1.,  0.,  0.,  0.,  1.,  1.,  1.,  0.],
       [ 0.,  0.,  0.,  0.,  1.,  0.,  0.,  0.,  1.,  1.,  1.,  0.],
       [ 0.,  0.,  1.,  1.,  1.,  1.,  1.,  1.,  1.,  1.,  0.,  0.],
       [ 0.,  0.,  0.,  0.,  0.,  0.,  0.,  0.,  0.,  0.,  0.,  0.]])
```

And fills out the Dijkstra Map for the walkable points:


```
$ dmap = build_map(dmap, walkable)
$ dmap
array([[999, 999, 999, 999, 999, 999, 999, 999, 999, 999, 999, 999],
       [999,   1,   1,   1,   2,   3, 999, 999, 999, 999, 999, 999],
       [999,   1,   0,   1,   2,   3, 999, 999, 999, 999, 999, 999],
       [999,   1,   1,   1,   2,   3, 999, 999, 999, 999, 999, 999],
       [999,   2,   2,   2,   2,   3, 999, 999,  17,  17,  17, 999],
       [999,   3,   3,   3,   3,   3, 999, 999,  16,  16,  16, 999],
       [999, 999, 999, 999,   4, 999, 999, 999,  15,  15,  15, 999],
       [999, 999, 999, 999,   5, 999, 999, 999,  14,  14,  14, 999],
       [999, 999, 999, 999,   6, 999, 999, 999,  13,  13,  14, 999],
       [999, 999, 999, 999,   7, 999, 999, 999,  12,  13,  14, 999],
       [999, 999,   9,   8,   8,   9,  10,  11,  12,  13, 999, 999],
       [999, 999, 999, 999, 999, 999, 999, 999, 999, 999, 999, 999]])
```

References
----------

[The Incredible Power of Dijkstra Maps](http://www.roguebasin.com/index.php?title=The_Incredible_Power_of_Dijkstra_Maps)

[Dijkstra Maps Visualized](http://www.roguebasin.com/index.php?title=Dijkstra_Maps_Visualized)
