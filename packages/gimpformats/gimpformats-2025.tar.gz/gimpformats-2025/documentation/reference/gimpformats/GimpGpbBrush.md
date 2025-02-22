# Gimpgpbbrush

[Gimpformats Index](../README.md#gimpformats-index) / [Gimpformats](./index.md#gimpformats) / Gimpgpbbrush

> Auto-generated documentation for [gimpformats.GimpGpbBrush](../../../gimpformats/GimpGpbBrush.py) module.

- [Gimpgpbbrush](#gimpgpbbrush)
  - [GimpGpbBrush](#gimpgpbbrush)
    - [GimpGpbBrush().__repr__](#gimpgpbbrush()__repr__)
    - [GimpGpbBrush().__str__](#gimpgpbbrush()__str__)
    - [GimpGpbBrush().decode](#gimpgpbbrush()decode)
    - [GimpGpbBrush().encode](#gimpgpbbrush()encode)
    - [GimpGpbBrush().full_repr](#gimpgpbbrush()full_repr)
    - [GimpGpbBrush().load](#gimpgpbbrush()load)
    - [GimpGpbBrush().save](#gimpgpbbrush()save)

## GimpGpbBrush

[Show source in GimpGpbBrush.py:14](../../../gimpformats/GimpGpbBrush.py#L14)

Pure python implementation of the OLD gimp gpb brush format.

See:
 https://gitlab.gnome.org/GNOME/gimp/blob/master/devel-docs/vbr.txt

#### Signature

```python
class GimpGpbBrush:
    def __init__(self, fileName: BytesIO | str) -> None: ...
```

### GimpGpbBrush().__repr__

[Show source in GimpGpbBrush.py:75](../../../gimpformats/GimpGpbBrush.py#L75)

Get a textual representation of this object.

#### Signature

```python
def __repr__(self) -> str: ...
```

### GimpGpbBrush().__str__

[Show source in GimpGpbBrush.py:71](../../../gimpformats/GimpGpbBrush.py#L71)

Get a textual representation of this object.

#### Signature

```python
def __str__(self) -> str: ...
```

### GimpGpbBrush().decode

[Show source in GimpGpbBrush.py:44](../../../gimpformats/GimpGpbBrush.py#L44)

Decode a byte buffer.

#### Arguments

----
 - `data` *bytearray* - data to decode
 - `index` *int, optional* - index to start from. Defaults to 0.

#### Returns

-------
 - `int` - pointer

#### Signature

```python
def decode(self, data: bytearray | bytes, index: int = 0) -> int: ...
```

### GimpGpbBrush().encode

[Show source in GimpGpbBrush.py:60](../../../gimpformats/GimpGpbBrush.py#L60)

Encode this object to bytearray.

#### Signature

```python
def encode(self) -> bytearray: ...
```

### GimpGpbBrush().full_repr

[Show source in GimpGpbBrush.py:82](../../../gimpformats/GimpGpbBrush.py#L82)

Get a textual representation of this object.

#### Signature

```python
def full_repr(self, indent: int = 0) -> str: ...
```

### GimpGpbBrush().load

[Show source in GimpGpbBrush.py:36](../../../gimpformats/GimpGpbBrush.py#L36)

Load a gimp file.

#### Arguments

- `fileName` - can be a file name or a file-like object

#### Signature

```python
def load(self, fileName: BytesIO | str) -> None: ...
```

### GimpGpbBrush().save

[Show source in GimpGpbBrush.py:67](../../../gimpformats/GimpGpbBrush.py#L67)

Save this gimp image to a file.

#### Signature

```python
def save(self, tofileName: str | BytesIO) -> None: ...
```