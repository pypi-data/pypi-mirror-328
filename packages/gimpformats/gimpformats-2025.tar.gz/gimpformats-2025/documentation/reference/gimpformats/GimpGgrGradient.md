# Gimpggrgradient

[Gimpformats Index](../README.md#gimpformats-index) / [Gimpformats](./index.md#gimpformats) / Gimpggrgradient

> Auto-generated documentation for [gimpformats.GimpGgrGradient](../../../gimpformats/GimpGgrGradient.py) module.

- [Gimpggrgradient](#gimpggrgradient)
  - [GimpGgrGradient](#gimpggrgradient)
    - [GimpGgrGradient().__str__](#gimpggrgradient()__str__)
    - [GimpGgrGradient().decode](#gimpggrgradient()decode)
    - [GimpGgrGradient().encode](#gimpggrgradient()encode)
    - [GimpGgrGradient().full_repr](#gimpggrgradient()full_repr)
    - [GimpGgrGradient().getColor](#gimpggrgradient()getcolor)
    - [GimpGgrGradient().load](#gimpggrgradient()load)
    - [GimpGgrGradient().save](#gimpggrgradient()save)
  - [GradientSegment](#gradientsegment)
    - [GradientSegment().__str__](#gradientsegment()__str__)
    - [GradientSegment().decode](#gradientsegment()decode)
    - [GradientSegment().encode](#gradientsegment()encode)
    - [GradientSegment().full_repr](#gradientsegment()full_repr)
    - [GradientSegment().getColor](#gradientsegment()getcolor)

## GimpGgrGradient

[Show source in GimpGgrGradient.py:122](../../../gimpformats/GimpGgrGradient.py#L122)

Gimp color gradient.

See:
 https://gitlab.gnome.org/GNOME/gimp/blob/master/devel-docs/ggr.txt

#### Signature

```python
class GimpGgrGradient:
    def __init__(self, fileName: str | None = None) -> None: ...
```

### GimpGgrGradient().__str__

[Show source in GimpGgrGradient.py:196](../../../gimpformats/GimpGgrGradient.py#L196)

Get a textual representation of this object.

#### Signature

```python
def __str__(self) -> str: ...
```

### GimpGgrGradient().decode

[Show source in GimpGgrGradient.py:151](../../../gimpformats/GimpGgrGradient.py#L151)

Decode a byte buffer.

#### Arguments

----
 - `dataIn` *bytearray* - data buffer to decode

#### Raises

------
 - `RuntimeError` - File format error.  Magic value mismatch.

#### Signature

```python
def decode(self, dataIn: bytearray | bytes) -> None: ...
```

### GimpGgrGradient().encode

[Show source in GimpGgrGradient.py:177](../../../gimpformats/GimpGgrGradient.py#L177)

Encode this to bytearray.

#### Signature

```python
def encode(self) -> bytes: ...
```

### GimpGgrGradient().full_repr

[Show source in GimpGgrGradient.py:200](../../../gimpformats/GimpGgrGradient.py#L200)

Get a textual representation of this object.

#### Signature

```python
def full_repr(self, indent: int = 0) -> str: ...
```

### GimpGgrGradient().getColor

[Show source in GimpGgrGradient.py:189](../../../gimpformats/GimpGgrGradient.py#L189)

Given a decimal percent (1.0 = 100%) retrieve...

the appropriate color for this point in the gradient.

#### Signature

```python
def getColor(self, percent: float) -> NoReturn: ...
```

### GimpGgrGradient().load

[Show source in GimpGgrGradient.py:143](../../../gimpformats/GimpGgrGradient.py#L143)

Load a gimp file.

#### Arguments

- `fileName` - can be a file name or a file-like object

#### Signature

```python
def load(self, fileName: BytesIO | str) -> None: ...
```

### GimpGgrGradient().save

[Show source in GimpGgrGradient.py:185](../../../gimpformats/GimpGgrGradient.py#L185)

Save this gimp image to a file.

#### Signature

```python
def save(self, tofileName: str | BytesIO) -> None: ...
```



## GradientSegment

[Show source in GimpGgrGradient.py:12](../../../gimpformats/GimpGgrGradient.py#L12)

Single segment within a gradient.

#### Signature

```python
class GradientSegment:
    def __init__(self) -> None: ...
```

### GradientSegment().__str__

[Show source in GimpGgrGradient.py:99](../../../gimpformats/GimpGgrGradient.py#L99)

Get a textual representation of this object.

#### Signature

```python
def __str__(self) -> str: ...
```

### GradientSegment().decode

[Show source in GimpGgrGradient.py:51](../../../gimpformats/GimpGgrGradient.py#L51)

Decode a byte buffer.

#### Arguments

----
 - `dataIn` *str* - data buffer to decode

#### Raises

------
 - `RuntimeError` - [description]

#### Signature

```python
def decode(self, dataIn: str) -> None: ...
```

### GradientSegment().encode

[Show source in GimpGgrGradient.py:81](../../../gimpformats/GimpGgrGradient.py#L81)

Encode this to a string.

#### Signature

```python
def encode(self) -> str: ...
```

### GradientSegment().full_repr

[Show source in GimpGgrGradient.py:103](../../../gimpformats/GimpGgrGradient.py#L103)

Get a textual representation of this object.

#### Signature

```python
def full_repr(self, indent: int = 0) -> str: ...
```

### GradientSegment().getColor

[Show source in GimpGgrGradient.py:44](../../../gimpformats/GimpGgrGradient.py#L44)

Given a decimal percent (1.0 = 100%) retrieve the appropriate color
for this point in the gradient.

#### Signature

```python
def getColor(self, percent: float) -> NoReturn: ...
```