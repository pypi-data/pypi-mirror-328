# Gimpprecision

[Gimpformats Index](../README.md#gimpformats-index) / [Gimpformats](./index.md#gimpformats) / Gimpprecision

> Auto-generated documentation for [gimpformats.GimpPrecision](../../../gimpformats/GimpPrecision.py) module.

- [Gimpprecision](#gimpprecision)
  - [Precision](#precision)
    - [Precision().__repr__](#precision()__repr__)
    - [Precision().__str__](#precision()__str__)
    - [Precision().decode](#precision()decode)
    - [Precision().encode](#precision()encode)
    - [Precision().requiredGimpVersion](#precision()requiredgimpversion)

## Precision

[Show source in GimpPrecision.py:8](../../../gimpformats/GimpPrecision.py#L8)

Since the precision code is so unusual, I decided to create a class to parse it.

#### Signature

```python
class Precision:
    def __init__(self) -> None: ...
```

### Precision().__repr__

[Show source in GimpPrecision.py:88](../../../gimpformats/GimpPrecision.py#L88)

Get a textual representation of this object.

#### Signature

```python
def __repr__(self) -> str: ...
```

### Precision().__str__

[Show source in GimpPrecision.py:84](../../../gimpformats/GimpPrecision.py#L84)

Get a textual representation of this object.

#### Signature

```python
def __str__(self) -> str: ...
```

### Precision().decode

[Show source in GimpPrecision.py:17](../../../gimpformats/GimpPrecision.py#L17)

Decode the precision code from the file.

#### Signature

```python
def decode(self, gimpVersion: int, ioBuf: IO) -> None: ...
```

#### See also

- [IO](./binaryiotools.md#io)

### Precision().encode

[Show source in GimpPrecision.py:40](../../../gimpformats/GimpPrecision.py#L40)

Encode this to the file.

NOTE: will not mess with development versions 5 or 6

#### Signature

```python
def encode(self, gimpVersion: int, ioBuf: IO) -> None: ...
```

#### See also

- [IO](./binaryiotools.md#io)

### Precision().requiredGimpVersion

[Show source in GimpPrecision.py:76](../../../gimpformats/GimpPrecision.py#L76)

Return the lowest gimp version that supports this precision.

#### Signature

```python
def requiredGimpVersion(self) -> int: ...
```