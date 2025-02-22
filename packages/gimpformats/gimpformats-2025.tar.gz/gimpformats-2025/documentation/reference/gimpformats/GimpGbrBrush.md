# Gimpgbrbrush

[Gimpformats Index](../README.md#gimpformats-index) / [Gimpformats](./index.md#gimpformats) / Gimpgbrbrush

> Auto-generated documentation for [gimpformats.GimpGbrBrush](../../../gimpformats/GimpGbrBrush.py) module.

- [Gimpgbrbrush](#gimpgbrbrush)
  - [GimpGbrBrush](#gimpgbrbrush)
    - [GimpGbrBrush().__str__](#gimpgbrbrush()__str__)
    - [GimpGbrBrush().decode](#gimpgbrbrush()decode)
    - [GimpGbrBrush().encode](#gimpgbrbrush()encode)
    - [GimpGbrBrush().full_repr](#gimpgbrbrush()full_repr)
    - [GimpGbrBrush().image](#gimpgbrbrush()image)
    - [GimpGbrBrush().load](#gimpgbrbrush()load)
    - [GimpGbrBrush().save](#gimpgbrbrush()save)
    - [GimpGbrBrush().size](#gimpgbrbrush()size)

## GimpGbrBrush

[Show source in GimpGbrBrush.py:16](../../../gimpformats/GimpGbrBrush.py#L16)

Pure python implementation of the gimp gbr brush format.

See:
 https://gitlab.gnome.org/GNOME/gimp/blob/master/devel-docs/gbr.txt

#### Signature

```python
class GimpGbrBrush:
    def __init__(self, fileName: str | None = None) -> None: ...
```

### GimpGbrBrush().__str__

[Show source in GimpGbrBrush.py:145](../../../gimpformats/GimpGbrBrush.py#L145)

Get a textual representation of this object.

#### Signature

```python
def __str__(self) -> str: ...
```

### GimpGbrBrush().decode

[Show source in GimpGbrBrush.py:53](../../../gimpformats/GimpGbrBrush.py#L53)

Decode a byte buffer.

#### Arguments

----
 - `data` *bytearray* - data buffer to decode
 - `index` *int, optional* - index within the buffer to start at. Defaults to 0.

#### Raises

------
 - `RuntimeError` - "unknown brush version"
 - `RuntimeError` - "File format error.  Magic value mismatch"

#### Returns

-------
 - `int` - offset]

#### Signature

```python
def decode(self, data: bytearray | bytes, index: int = 0) -> int: ...
```

### GimpGbrBrush().encode

[Show source in GimpGbrBrush.py:96](../../../gimpformats/GimpGbrBrush.py#L96)

Encode this object to byte array.

#### Signature

```python
def encode(self) -> bytearray: ...
```

### GimpGbrBrush().full_repr

[Show source in GimpGbrBrush.py:149](../../../gimpformats/GimpGbrBrush.py#L149)

Get a textual representation of this object.

#### Signature

```python
def full_repr(self, indent: int = 0) -> str: ...
```

### GimpGbrBrush().image

[Show source in GimpGbrBrush.py:115](../../../gimpformats/GimpGbrBrush.py#L115)

Get a final, compiled image.

#### Signature

```python
@property
def image(self) -> PIL.Image.Image | None: ...
```

### GimpGbrBrush().load

[Show source in GimpGbrBrush.py:45](../../../gimpformats/GimpGbrBrush.py#L45)

Load a gimp file.

#### Arguments

- `fileName` - can be a file name or a file-like object

#### Signature

```python
def load(self, fileName: BytesIO | str) -> None: ...
```

### GimpGbrBrush().save

[Show source in GimpGbrBrush.py:122](../../../gimpformats/GimpGbrBrush.py#L122)

Save this GIMP image to a file.

#### Arguments

----
 - `filename` *str* - The name of the file to save.
 - `extension` *str, optional* - The extension of the file. If not provided,
  it will be inferred from the filename.

#### Signature

```python
def save(self, filename: str, extension: str | None = None) -> None: ...
```

### GimpGbrBrush().size

[Show source in GimpGbrBrush.py:110](../../../gimpformats/GimpGbrBrush.py#L110)

Get the size.

#### Signature

```python
@property
def size(self) -> tuple[int, int]: ...
```