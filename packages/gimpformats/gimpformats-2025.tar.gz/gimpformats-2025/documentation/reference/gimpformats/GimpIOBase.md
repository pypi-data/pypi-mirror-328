# Gimpiobase

[Gimpformats Index](../README.md#gimpformats-index) / [Gimpformats](./index.md#gimpformats) / Gimpiobase

> Auto-generated documentation for [gimpformats.GimpIOBase](../../../gimpformats/GimpIOBase.py) module.

- [Gimpiobase](#gimpiobase)
  - [ColorMode](#colormode)
  - [CompositeMode](#compositemode)
  - [CompositeSpace](#compositespace)
  - [CompressionMode](#compressionmode)
  - [GimpBlendMode](#gimpblendmode)
  - [GimpIOBase](#gimpiobase)
    - [GimpIOBase().__repr__](#gimpiobase()__repr__)
    - [GimpIOBase().__str__](#gimpiobase()__str__)
    - [GimpIOBase()._colormapDecode](#gimpiobase()_colormapdecode)
    - [GimpIOBase()._guidelinesDecode](#gimpiobase()_guidelinesdecode)
    - [GimpIOBase()._itemPathDecode](#gimpiobase()_itempathdecode)
    - [GimpIOBase()._parasitesDecode](#gimpiobase()_parasitesdecode)
    - [GimpIOBase()._parasitesEncode](#gimpiobase()_parasitesencode)
    - [GimpIOBase()._propertiesDecode](#gimpiobase()_propertiesdecode)
    - [GimpIOBase()._propertiesEncode](#gimpiobase()_propertiesencode)
    - [GimpIOBase()._propertyDecode](#gimpiobase()_propertydecode)
    - [GimpIOBase()._propertyEncode](#gimpiobase()_propertyencode)
    - [GimpIOBase()._samplePointsDecode](#gimpiobase()_samplepointsdecode)
    - [GimpIOBase()._userUnitsDecode](#gimpiobase()_userunitsdecode)
    - [GimpIOBase()._vectorsDecode](#gimpiobase()_vectorsdecode)
    - [GimpIOBase().activeVector](#gimpiobase()activevector)
    - [GimpIOBase().doc](#gimpiobase()doc)
    - [GimpIOBase().expanded](#gimpiobase()expanded)
    - [GimpIOBase().expanded](#gimpiobase()expanded-1)
    - [GimpIOBase().full_repr](#gimpiobase()full_repr)
    - [GimpIOBase().pointerSize](#gimpiobase()pointersize)
    - [GimpIOBase().root](#gimpiobase()root)
    - [GimpIOBase().tattoo](#gimpiobase()tattoo)
    - [GimpIOBase().tattoo](#gimpiobase()tattoo-1)
  - [GimpUserUnits](#gimpuserunits)
    - [GimpUserUnits().__str__](#gimpuserunits()__str__)
    - [GimpUserUnits().decode](#gimpuserunits()decode)
    - [GimpUserUnits().encode](#gimpuserunits()encode)
    - [GimpUserUnits().full_repr](#gimpuserunits()full_repr)
  - [ImageProperties](#imageproperties)
  - [TagColor](#tagcolor)
  - [Units](#units)
  - [camel_to_pascal_with_spaces](#camel_to_pascal_with_spaces)

## ColorMode

[Show source in GimpIOBase.py:26](../../../gimpformats/GimpIOBase.py#L26)

#### Signature

```python
class ColorMode(Enum): ...
```



## CompositeMode

[Show source in GimpIOBase.py:39](../../../gimpformats/GimpIOBase.py#L39)

#### Signature

```python
class CompositeMode(Enum): ...
```



## CompositeSpace

[Show source in GimpIOBase.py:46](../../../gimpformats/GimpIOBase.py#L46)

#### Signature

```python
class CompositeSpace(Enum): ...
```



## CompressionMode

[Show source in GimpIOBase.py:64](../../../gimpformats/GimpIOBase.py#L64)

#### Signature

```python
class CompressionMode(Enum): ...
```



## GimpBlendMode

[Show source in GimpIOBase.py:71](../../../gimpformats/GimpIOBase.py#L71)

#### Signature

```python
class GimpBlendMode(Enum): ...
```



## GimpIOBase

[Show source in GimpIOBase.py:180](../../../gimpformats/GimpIOBase.py#L180)

#### Signature

```python
class GimpIOBase:
    def __init__(self, parent: Any = None) -> None: ...
```

### GimpIOBase().__repr__

[Show source in GimpIOBase.py:712](../../../gimpformats/GimpIOBase.py#L712)

Get a textual representation of this object.

#### Signature

```python
def __repr__(self) -> str: ...
```

### GimpIOBase().__str__

[Show source in GimpIOBase.py:708](../../../gimpformats/GimpIOBase.py#L708)

Get a textual representation of this object.

#### Signature

```python
def __str__(self) -> str: ...
```

### GimpIOBase()._colormapDecode

[Show source in GimpIOBase.py:340](../../../gimpformats/GimpIOBase.py#L340)

_colormapDecode_.

#### Arguments

- `data` - can be bytearray or an IO object

decode colormap/palette

#### Signature

```python
def _colormapDecode(self, data: bytearray | IO, index: int = 0) -> None: ...
```

### GimpIOBase()._guidelinesDecode

[Show source in GimpIOBase.py:288](../../../gimpformats/GimpIOBase.py#L288)

Decode guidelines.

#### Signature

```python
def _guidelinesDecode(self, data: bytearray) -> None: ...
```

### GimpIOBase()._itemPathDecode

[Show source in GimpIOBase.py:298](../../../gimpformats/GimpIOBase.py#L298)

Decode item path.

#### Signature

```python
def _itemPathDecode(self, data: bytearray) -> None: ...
```

### GimpIOBase()._parasitesDecode

[Show source in GimpIOBase.py:271](../../../gimpformats/GimpIOBase.py#L271)

Decode list of parasites.

#### Signature

```python
def _parasitesDecode(self, data: bytearray) -> int: ...
```

### GimpIOBase()._parasitesEncode

[Show source in GimpIOBase.py:281](../../../gimpformats/GimpIOBase.py#L281)

Encode list of parasites.

#### Signature

```python
def _parasitesEncode(self) -> bytearray: ...
```

### GimpIOBase()._propertiesDecode

[Show source in GimpIOBase.py:686](../../../gimpformats/GimpIOBase.py#L686)

Decode a list of properties.

#### Signature

```python
def _propertiesDecode(self, ioBuf: IO) -> int: ...
```

#### See also

- [IO](./binaryiotools.md#io)

### GimpIOBase()._propertiesEncode

[Show source in GimpIOBase.py:699](../../../gimpformats/GimpIOBase.py#L699)

Encode a list of properties.

#### Signature

```python
def _propertiesEncode(self) -> bytearray: ...
```

### GimpIOBase()._propertyDecode

[Show source in GimpIOBase.py:385](../../../gimpformats/GimpIOBase.py#L385)

Decode a single property.

Many properties are in the form
prop: one of PROP_
lengthOfData: 4
data: varies but is often ioBuf.32 or ioBuf.boolean

#### Signature

```python
def _propertyDecode(self, prop: int, data: bytearray) -> int: ...
```

### GimpIOBase()._propertyEncode

[Show source in GimpIOBase.py:496](../../../gimpformats/GimpIOBase.py#L496)

Encode a single property.

Many properties are in the form
prop: one of PROP_
lengthOfData: 4
data: varies but is often ioBuf.32 or ioBuf.boolean

If the property is the same as the default, or not specified, returns empty array

#### Signature

```python
def _propertyEncode(self, prop: int) -> bytearray: ...
```

### GimpIOBase()._samplePointsDecode

[Show source in GimpIOBase.py:373](../../../gimpformats/GimpIOBase.py#L373)

Decode a series of points.

#### Signature

```python
def _samplePointsDecode(self, data: bytearray) -> None: ...
```

### GimpIOBase()._userUnitsDecode

[Show source in GimpIOBase.py:367](../../../gimpformats/GimpIOBase.py#L367)

Decode a set of user-defined measurement units.

#### Signature

```python
def _userUnitsDecode(self, data: bytearray) -> None: ...
```

### GimpIOBase()._vectorsDecode

[Show source in GimpIOBase.py:308](../../../gimpformats/GimpIOBase.py#L308)

Decode vectors.

#### Signature

```python
def _vectorsDecode(self, data: bytearray) -> None: ...
```

### GimpIOBase().activeVector

[Show source in GimpIOBase.py:322](../../../gimpformats/GimpIOBase.py#L322)

Get the vector that is currently active.

#### Signature

```python
@property
def activeVector(self) -> GimpVector: ...
```

#### See also

- [GimpVector](./GimpVectors.md#gimpvector)

### GimpIOBase().doc

[Show source in GimpIOBase.py:249](../../../gimpformats/GimpIOBase.py#L249)

#### Signature

```python
@property
def doc(self) -> GimpIOBase: ...
```

### GimpIOBase().expanded

[Show source in GimpIOBase.py:327](../../../gimpformats/GimpIOBase.py#L327)

Is the group layer expanded.

#### Signature

```python
@property
def expanded(self) -> bool: ...
```

### GimpIOBase().expanded

[Show source in GimpIOBase.py:332](../../../gimpformats/GimpIOBase.py#L332)

Is the group layer expanded.

#### Signature

```python
@expanded.setter
def expanded(self, expanded: bool) -> None: ...
```

### GimpIOBase().full_repr

[Show source in GimpIOBase.py:723](../../../gimpformats/GimpIOBase.py#L723)

Get a textual representation of this object.

#### Signature

```python
def full_repr(self, indent: int = 0) -> str: ...
```

### GimpIOBase().pointerSize

[Show source in GimpIOBase.py:223](../../../gimpformats/GimpIOBase.py#L223)

Determine the size of the "pointer" datatype based on the document version.

NOTE: prior to version 11, it was 32-bit,
 since then it is 64-bit, thus supporting
 larger image files

#### Signature

```python
@property
def pointerSize(self) -> int: ...
```

### GimpIOBase().root

[Show source in GimpIOBase.py:256](../../../gimpformats/GimpIOBase.py#L256)

Get the root of the file object tree (Which is the same as self.doc).

#### Signature

```python
@property
def root(self) -> GimpIOBase: ...
```

### GimpIOBase().tattoo

[Show source in GimpIOBase.py:261](../../../gimpformats/GimpIOBase.py#L261)

Gimp nomenclature for the item's unique id.

#### Signature

```python
@property
def tattoo(self) -> Any | None: ...
```

### GimpIOBase().tattoo

[Show source in GimpIOBase.py:266](../../../gimpformats/GimpIOBase.py#L266)

Gimp nomenclature for the item's unique id.

#### Signature

```python
@tattoo.setter
def tattoo(self, tattoo: Any | None) -> None: ...
```



## GimpUserUnits

[Show source in GimpIOBase.py:800](../../../gimpformats/GimpIOBase.py#L800)

User-defined measurement units.

#### Signature

```python
class GimpUserUnits:
    def __init__(self) -> None: ...
```

### GimpUserUnits().__str__

[Show source in GimpIOBase.py:847](../../../gimpformats/GimpIOBase.py#L847)

Get a textual representation of this object.

#### Signature

```python
def __str__(self) -> str: ...
```

### GimpUserUnits().decode

[Show source in GimpIOBase.py:812](../../../gimpformats/GimpIOBase.py#L812)

Decode a byte buffer.

#### Arguments

----
 - `data` *bytearray* - data buffer to decode
 - `index` *int, optional* - index within the buffer to start at]. Defaults to 0.

#### Returns

-------
 - `int` - offset

#### Signature

```python
def decode(self, data: bytearray, index: int = 0) -> int: ...
```

### GimpUserUnits().encode

[Show source in GimpIOBase.py:835](../../../gimpformats/GimpIOBase.py#L835)

Convert this object to raw bytearray.

#### Signature

```python
def encode(self) -> bytearray: ...
```

### GimpUserUnits().full_repr

[Show source in GimpIOBase.py:851](../../../gimpformats/GimpIOBase.py#L851)

Get a textual representation of this object.

#### Signature

```python
def full_repr(self, indent: int = 0) -> str: ...
```



## ImageProperties

[Show source in GimpIOBase.py:136](../../../gimpformats/GimpIOBase.py#L136)

#### Signature

```python
class ImageProperties(Enum): ...
```



## TagColor

[Show source in GimpIOBase.py:52](../../../gimpformats/GimpIOBase.py#L52)

#### Signature

```python
class TagColor(Enum): ...
```



## Units

[Show source in GimpIOBase.py:32](../../../gimpformats/GimpIOBase.py#L32)

#### Signature

```python
class Units(Enum): ...
```



## camel_to_pascal_with_spaces

[Show source in GimpIOBase.py:21](../../../gimpformats/GimpIOBase.py#L21)

#### Signature

```python
def camel_to_pascal_with_spaces(val: str) -> str: ...
```