# Gimpparasites

[Gimpformats Index](../README.md#gimpformats-index) / [Gimpformats](./index.md#gimpformats) / Gimpparasites

> Auto-generated documentation for [gimpformats.GimpParasites](../../../gimpformats/GimpParasites.py) module.

- [Gimpparasites](#gimpparasites)
  - [GimpParasite](#gimpparasite)
    - [GimpParasite().__repr__](#gimpparasite()__repr__)
    - [GimpParasite().__str__](#gimpparasite()__str__)
    - [GimpParasite().decode](#gimpparasite()decode)
    - [GimpParasite().encode](#gimpparasite()encode)

## GimpParasite

[Show source in GimpParasites.py:47](../../../gimpformats/GimpParasites.py#L47)

Parasites are arbitrary (meta)data strings that can be attached to a document tree item.

They are used to store things like last-used plugin settings, gamma adjuetments, etc.

Format of known parasites:
 https://gitlab.gnome.org/GNOME/gimp/blob/master/devel-docs/parasites.txt

#### Signature

```python
class GimpParasite:
    def __init__(self) -> None: ...
```

### GimpParasite().__repr__

[Show source in GimpParasites.py:91](../../../gimpformats/GimpParasites.py#L91)

Get a textual representation of this object.

#### Signature

```python
def __repr__(self) -> str: ...
```

### GimpParasite().__str__

[Show source in GimpParasites.py:87](../../../gimpformats/GimpParasites.py#L87)

Get a textual representation of this object.

#### Signature

```python
def __str__(self) -> str: ...
```

### GimpParasite().decode

[Show source in GimpParasites.py:61](../../../gimpformats/GimpParasites.py#L61)

Decode a byte buffer.

#### Arguments

- `data` - data buffer to decode
- `index` - index within the buffer to start at

#### Signature

```python
def decode(self, data: bytearray, index: int = 0) -> int: ...
```

### GimpParasite().encode

[Show source in GimpParasites.py:74](../../../gimpformats/GimpParasites.py#L74)

Encode a byte buffer.

#### Arguments

- `data` - data buffer to encode
- `index` - index within the buffer to start at

#### Signature

```python
def encode(self) -> bytearray: ...
```