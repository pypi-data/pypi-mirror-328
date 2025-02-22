# Gimplayer

[Gimpformats Index](../README.md#gimpformats-index) / [Gimpformats](./index.md#gimpformats) / Gimplayer

> Auto-generated documentation for [gimpformats.GimpLayer](../../../gimpformats/GimpLayer.py) module.

- [Gimplayer](#gimplayer)
  - [GimpLayer](#gimplayer)
    - [GimpLayer().__repr__](#gimplayer()__repr__)
    - [GimpLayer().__str__](#gimplayer()__str__)
    - [GimpLayer().decode](#gimplayer()decode)
    - [GimpLayer().encode](#gimplayer()encode)
    - [GimpLayer().forceFullyLoaded](#gimplayer()forcefullyloaded)
    - [GimpLayer().full_repr](#gimplayer()full_repr)
    - [GimpLayer().image](#gimplayer()image)
    - [GimpLayer().image](#gimplayer()image-1)
    - [GimpLayer().imageHierarchy](#gimplayer()imagehierarchy)
    - [GimpLayer().imageHierarchy](#gimplayer()imagehierarchy-1)
    - [GimpLayer().mask](#gimplayer()mask)

## GimpLayer

[Show source in GimpLayer.py:14](../../../gimpformats/GimpLayer.py#L14)

Represents a single layer in a gimp image.

#### Signature

```python
class GimpLayer(GimpIOBase):
    def __init__(
        self, parent, name: str | None = None, image: Image | None = None
    ) -> None: ...
```

#### See also

- [GimpIOBase](./GimpIOBase.md#gimpiobase)

### GimpLayer().__repr__

[Show source in GimpLayer.py:193](../../../gimpformats/GimpLayer.py#L193)

Get a textual representation of this object.

#### Signature

```python
def __repr__(self) -> str: ...
```

### GimpLayer().__str__

[Show source in GimpLayer.py:189](../../../gimpformats/GimpLayer.py#L189)

Get a textual representation of this object.

#### Signature

```python
def __str__(self) -> str: ...
```

### GimpLayer().decode

[Show source in GimpLayer.py:50](../../../gimpformats/GimpLayer.py#L50)

Decode a byte buffer.

Steps:
Create a new IO buffer
Grab attributes as outlined in the spec
List of properties
Get the image hierarchy and mask pointers
Return the offset

#### Arguments

----
 - `data` *bytearray* - data buffer to decode
 - `index` *int, optional* - index within the buffer to start at]. Defaults to 0.

#### Returns

-------
 - `int` - offset

#### Signature

```python
def decode(self, data: bytearray | None, index: int = 0) -> int: ...
```

### GimpLayer().encode

[Show source in GimpLayer.py:89](../../../gimpformats/GimpLayer.py#L89)

Encode to byte array.

Steps:
Create a new IO buffer
Set attributes as outlined in the spec
List of properties
Set the image hierarchy and mask pointers
Return the data

#### Signature

```python
def encode(self) -> bytearray: ...
```

### GimpLayer().forceFullyLoaded

[Show source in GimpLayer.py:181](../../../gimpformats/GimpLayer.py#L181)

Make sure everything is fully loaded from the file.

#### Signature

```python
def forceFullyLoaded(self) -> None: ...
```

### GimpLayer().full_repr

[Show source in GimpLayer.py:204](../../../gimpformats/GimpLayer.py#L204)

Get a textual representation of this object.

#### Signature

```python
def full_repr(self, indent: int = 0) -> str: ...
```

### GimpLayer().image

[Show source in GimpLayer.py:132](../../../gimpformats/GimpLayer.py#L132)

Get the layer image.

NOTE: can return None!

#### Signature

```python
@property
def image(self) -> Image | None: ...
```

### GimpLayer().image

[Show source in GimpLayer.py:142](../../../gimpformats/GimpLayer.py#L142)

Set the layer image.

NOTE: resets layer width, height, and colorMode

#### Signature

```python
@image.setter
def image(self, image: Image) -> None: ...
```

### GimpLayer().imageHierarchy

[Show source in GimpLayer.py:159](../../../gimpformats/GimpLayer.py#L159)

Get the image hierarchy objects.

This is mainly needed for deciphering image, and therefore,
of little use to you, the user.

NOTE: can return None if it has been fully read into an image

#### Signature

```python
@property
def imageHierarchy(self) -> GimpImageHierarchy: ...
```

#### See also

- [GimpImageHierarchy](./GimpImageHierarchy.md#gimpimagehierarchy)

### GimpLayer().imageHierarchy

[Show source in GimpLayer.py:176](../../../gimpformats/GimpLayer.py#L176)

Set the image hierarchy.

#### Signature

```python
@imageHierarchy.setter
def imageHierarchy(self, imgHierarchy) -> None: ...
```

### GimpLayer().mask

[Show source in GimpLayer.py:123](../../../gimpformats/GimpLayer.py#L123)

Get the layer mask.

#### Signature

```python
@property
def mask(self) -> GimpChannel | None: ...
```