# Gimpimagelevel

[Gimpformats Index](../README.md#gimpformats-index) / [Gimpformats](./index.md#gimpformats) / Gimpimagelevel

> Auto-generated documentation for [gimpformats.GimpImageLevel](../../../gimpformats/GimpImageLevel.py) module.

- [Gimpimagelevel](#gimpimagelevel)
  - [GimpImageLevel](#gimpimagelevel)
    - [GimpImageLevel().__repr__](#gimpimagelevel()__repr__)
    - [GimpImageLevel().__str__](#gimpimagelevel()__str__)
    - [GimpImageLevel()._encodeRLE](#gimpimagelevel()_encoderle)
    - [GimpImageLevel()._imgToTiles](#gimpimagelevel()_imgtotiles)
    - [GimpImageLevel().bpp](#gimpimagelevel()bpp)
    - [GimpImageLevel().decode](#gimpimagelevel()decode)
    - [GimpImageLevel().encode](#gimpimagelevel()encode)
    - [GimpImageLevel().image](#gimpimagelevel()image)
    - [GimpImageLevel().image](#gimpimagelevel()image-1)
    - [GimpImageLevel().mode](#gimpimagelevel()mode)
    - [GimpImageLevel().tiles](#gimpimagelevel()tiles)

## GimpImageLevel

[Show source in GimpImageLevel.py:19](../../../gimpformats/GimpImageLevel.py#L19)

Gets packed pixels from a gimp image.

This represents a single level in an imageHierarchy

#### Signature

```python
class GimpImageLevel(GimpIOBase):
    def __init__(self, parent) -> None: ...
```

#### See also

- [GimpIOBase](./GimpIOBase.md#gimpiobase)

### GimpImageLevel().__repr__

[Show source in GimpImageLevel.py:288](../../../gimpformats/GimpImageLevel.py#L288)

Get a textual representation of this object.

#### Signature

```python
def __repr__(self) -> str: ...
```

### GimpImageLevel().__str__

[Show source in GimpImageLevel.py:284](../../../gimpformats/GimpImageLevel.py#L284)

Get a textual representation of this object.

#### Signature

```python
def __str__(self) -> str: ...
```

### GimpImageLevel()._encodeRLE

[Show source in GimpImageLevel.py:154](../../../gimpformats/GimpImageLevel.py#L154)

Encode image to RLE image data.

#### Signature

```python
def _encodeRLE(self, data, bpp): ...
```

### GimpImageLevel()._imgToTiles

[Show source in GimpImageLevel.py:249](../../../gimpformats/GimpImageLevel.py#L249)

Break an image into a series of tiles, each<=64x64.

#### Signature

```python
def _imgToTiles(self, image): ...
```

### GimpImageLevel().bpp

[Show source in GimpImageLevel.py:229](../../../gimpformats/GimpImageLevel.py#L229)

Get bpp.

#### Signature

```python
@property
def bpp(self): ...
```

### GimpImageLevel().decode

[Show source in GimpImageLevel.py:32](../../../gimpformats/GimpImageLevel.py#L32)

Decode a byte buffer.

#### Arguments

- `data` - data buffer to decode
- `index` - index within the buffer to start at

#### Signature

```python
def decode(self, data: bytearray | bytes | None, index: int = 0) -> int: ...
```

### GimpImageLevel().encode

[Show source in GimpImageLevel.py:74](../../../gimpformats/GimpImageLevel.py#L74)

Encode this object to a byte buffer.

#### Signature

```python
def encode(self) -> bytearray: ...
```

### GimpImageLevel().image

[Show source in GimpImageLevel.py:260](../../../gimpformats/GimpImageLevel.py#L260)

Get a final, compiled image.

#### Signature

```python
@property
def image(self) -> Image: ...
```

### GimpImageLevel().image

[Show source in GimpImageLevel.py:276](../../../gimpformats/GimpImageLevel.py#L276)

#### Signature

```python
@image.setter
def image(self, image: Image) -> None: ...
```

### GimpImageLevel().mode

[Show source in GimpImageLevel.py:234](../../../gimpformats/GimpImageLevel.py#L234)

Get mode.

#### Signature

```python
@property
def mode(self): ...
```

### GimpImageLevel().tiles

[Show source in GimpImageLevel.py:240](../../../gimpformats/GimpImageLevel.py#L240)

Get tiles.

#### Signature

```python
@property
def tiles(self): ...
```