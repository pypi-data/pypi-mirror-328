# Gimpvectors

[Gimpformats Index](../README.md#gimpformats-index) / [Gimpformats](./index.md#gimpformats) / Gimpvectors

> Auto-generated documentation for [gimpformats.GimpVectors](../../../gimpformats/GimpVectors.py) module.

- [Gimpvectors](#gimpvectors)
  - [GimpPoint](#gimppoint)
    - [GimpPoint().__repr__](#gimppoint()__repr__)
    - [GimpPoint().__str__](#gimppoint()__str__)
    - [GimpPoint().decode](#gimppoint()decode)
    - [GimpPoint().encode](#gimppoint()encode)
  - [GimpStroke](#gimpstroke)
    - [GimpStroke().__str__](#gimpstroke()__str__)
    - [GimpStroke().decode](#gimpstroke()decode)
    - [GimpStroke().encode](#gimpstroke()encode)
    - [GimpStroke().full_repr](#gimpstroke()full_repr)
  - [GimpVector](#gimpvector)
    - [GimpVector().__repr__](#gimpvector()__repr__)
    - [GimpVector().__str__](#gimpvector()__str__)
    - [GimpVector().decode](#gimpvector()decode)
    - [GimpVector().encode](#gimpvector()encode)
    - [GimpVector().full_repr](#gimpvector()full_repr)

## GimpPoint

[Show source in GimpVectors.py:168](../../../gimpformats/GimpVectors.py#L168)

A single point within a stroke.

#### Signature

```python
class GimpPoint:
    def __init__(self, parent: Any) -> None: ...
```

### GimpPoint().__repr__

[Show source in GimpVectors.py:239](../../../gimpformats/GimpVectors.py#L239)

Get a textual representation of this object.

#### Signature

```python
def __repr__(self) -> str: ...
```

### GimpPoint().__str__

[Show source in GimpVectors.py:235](../../../gimpformats/GimpVectors.py#L235)

Get a textual representation of this object.

#### Signature

```python
def __str__(self) -> str: ...
```

### GimpPoint().decode

[Show source in GimpVectors.py:183](../../../gimpformats/GimpVectors.py#L183)

Decode a byte buffer.

#### Arguments

----
 - `data` *bytearray* - data buffer to decode
 - `index` *int, optional* - index within the buffer to start at. Defaults to 0.
 - `numFloatsPerPoint` *int, optional* - required so we know
 how many different brush dynamic measurements are
 inside each point. Defaults to 0.

#### Returns

-------
 - `int` - offset

#### Signature

```python
def decode(self, data: bytearray, index: int = 0, numFloatsPerPoint: int = 0) -> int: ...
```

### GimpPoint().encode

[Show source in GimpVectors.py:219](../../../gimpformats/GimpVectors.py#L219)

Encode to binary data.

#### Signature

```python
def encode(self) -> bytearray: ...
```



## GimpStroke

[Show source in GimpVectors.py:100](../../../gimpformats/GimpVectors.py#L100)

A single stroke within a vector.

#### Signature

```python
class GimpStroke:
    def __init__(self, parent) -> None: ...
```

### GimpStroke().__str__

[Show source in GimpVectors.py:147](../../../gimpformats/GimpVectors.py#L147)

Get a textual representation of this object.

#### Signature

```python
def __str__(self) -> str: ...
```

### GimpStroke().decode

[Show source in GimpVectors.py:112](../../../gimpformats/GimpVectors.py#L112)

Decode a byte buffer.

#### Arguments

----
 - `data` *bytearray* - data buffer to decode
 - `index` *int, optional* - index within the buffer to start at. Defaults to 0.

#### Returns

-------
 - `int` - offset

#### Signature

```python
def decode(self, data: bytearray, index: int = 0) -> int: ...
```

### GimpStroke().encode

[Show source in GimpVectors.py:136](../../../gimpformats/GimpVectors.py#L136)

Encode to binary data.

#### Signature

```python
def encode(self): ...
```

### GimpStroke().full_repr

[Show source in GimpVectors.py:157](../../../gimpformats/GimpVectors.py#L157)

Get a textual representation of this object.

#### Signature

```python
def full_repr(self, indent: int = 0) -> str: ...
```



## GimpVector

[Show source in GimpVectors.py:12](../../../gimpformats/GimpVectors.py#L12)

A gimp brush stroke vector.

#### Signature

```python
class GimpVector:
    def __init__(self, parent: Any) -> None: ...
```

### GimpVector().__repr__

[Show source in GimpVectors.py:74](../../../gimpformats/GimpVectors.py#L74)

Get a textual representation of this object.

#### Signature

```python
def __repr__(self) -> str: ...
```

### GimpVector().__str__

[Show source in GimpVectors.py:70](../../../gimpformats/GimpVectors.py#L70)

Get a textual representation of this object.

#### Signature

```python
def __str__(self) -> str: ...
```

### GimpVector().decode

[Show source in GimpVectors.py:25](../../../gimpformats/GimpVectors.py#L25)

Decode a byte buffer.

#### Arguments

----
 - `data` *bytearray* - data buffer to decode
 - `index` *int, optional* - index within the buffer to start at. Defaults to 0.

#### Returns

-------
 - `int` - offset

#### Signature

```python
def decode(self, data: bytearray, index: int = 0) -> int: ...
```

### GimpVector().encode

[Show source in GimpVectors.py:55](../../../gimpformats/GimpVectors.py#L55)

Encode to binary data.

#### Signature

```python
def encode(self) -> bytearray: ...
```

### GimpVector().full_repr

[Show source in GimpVectors.py:82](../../../gimpformats/GimpVectors.py#L82)

Get a textual representation of this object.

#### Signature

```python
def full_repr(self, indent: int = 0) -> str: ...
```