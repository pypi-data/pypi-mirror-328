# Binaryiotools

[Gimpformats Index](../README.md#gimpformats-index) / [Gimpformats](./index.md#gimpformats) / Binaryiotools

> Auto-generated documentation for [gimpformats.binaryiotools](../../../gimpformats/binaryiotools.py) module.

- [Binaryiotools](#binaryiotools)
  - [IO](#io)
    - [IO().__getitem__](#io()__getitem__)
    - [IO().__len__](#io()__len__)
    - [IO()._read](#io()_read)
    - [IO()._readUntil](#io()_readuntil)
    - [IO()._sz754](#io()_sz754)
    - [IO()._sz754set](#io()_sz754set)
    - [IO()._write](#io()_write)
    - [IO().addbytearray](#io()addbytearray)
    - [IO().beginContext](#io()begincontext)
    - [IO().bool16](#io()bool16)
    - [IO().bool16](#io()bool16-1)
    - [IO().bool32](#io()bool32)
    - [IO().bool32](#io()bool32-1)
    - [IO().bool64](#io()bool64)
    - [IO().bool64](#io()bool64-1)
    - [IO().bool8](#io()bool8)
    - [IO().bool8](#io()bool8-1)
    - [IO().boolean](#io()boolean)
    - [IO().boolean](#io()boolean-1)
    - [IO().byte](#io()byte)
    - [IO().byte](#io()byte-1)
    - [IO().cString](#io()cstring)
    - [IO().cString](#io()cstring-1)
    - [IO().cStringA](#io()cstringa)
    - [IO().cStringA](#io()cstringa-1)
    - [IO().cStringU](#io()cstringu)
    - [IO().cStringU](#io()cstringu-1)
    - [IO().cStringW](#io()cstringw)
    - [IO().cStringW](#io()cstringw-1)
    - [IO().data](#io()data)
    - [IO().data](#io()data-1)
    - [IO().double](#io()double)
    - [IO().double](#io()double-1)
    - [IO().dword](#io()dword)
    - [IO().dword](#io()dword-1)
    - [IO().endContext](#io()endcontext)
    - [IO().float32](#io()float32)
    - [IO().float32](#io()float32-1)
    - [IO().float32be](#io()float32be)
    - [IO().float32be](#io()float32be-1)
    - [IO().float32le](#io()float32le)
    - [IO().float32le](#io()float32le-1)
    - [IO().float64](#io()float64)
    - [IO().float64](#io()float64-1)
    - [IO().float64be](#io()float64be)
    - [IO().float64be](#io()float64be-1)
    - [IO().float64le](#io()float64le)
    - [IO().float64le](#io()float64le-1)
    - [IO().floating](#io()floating)
    - [IO().floating](#io()floating-1)
    - [IO().getbytearray](#io()getbytearray)
    - [IO().i16](#io()i16)
    - [IO().i16](#io()i16-1)
    - [IO().i16be](#io()i16be)
    - [IO().i16be](#io()i16be-1)
    - [IO().i16le](#io()i16le)
    - [IO().i16le](#io()i16le-1)
    - [IO().i32](#io()i32)
    - [IO().i32](#io()i32-1)
    - [IO().i32be](#io()i32be)
    - [IO().i32be](#io()i32be-1)
    - [IO().i32le](#io()i32le)
    - [IO().i32le](#io()i32le-1)
    - [IO().i64](#io()i64)
    - [IO().i64](#io()i64-1)
    - [IO().i64be](#io()i64be)
    - [IO().i64be](#io()i64be-1)
    - [IO().i64le](#io()i64le)
    - [IO().i64le](#io()i64le-1)
    - [IO().i8](#io()i8)
    - [IO().i8](#io()i8-1)
    - [IO().i8be](#io()i8be)
    - [IO().i8be](#io()i8be-1)
    - [IO().i8le](#io()i8le)
    - [IO().i8le](#io()i8le-1)
    - [IO().index](#io()index)
    - [IO().index](#io()index-1)
    - [IO().qword](#io()qword)
    - [IO().qword](#io()qword-1)
    - [IO().setbytearray](#io()setbytearray)
    - [IO().sz754](#io()sz754)
    - [IO().sz754](#io()sz754-1)
    - [IO().sz754A](#io()sz754a)
    - [IO().sz754A](#io()sz754a-1)
    - [IO().sz754U](#io()sz754u)
    - [IO().sz754U](#io()sz754u-1)
    - [IO().sz754W](#io()sz754w)
    - [IO().sz754W](#io()sz754w-1)
    - [IO().textLine](#io()textline)
    - [IO().textLine](#io()textline-1)
    - [IO().textLineA](#io()textlinea)
    - [IO().textLineA](#io()textlinea-1)
    - [IO().textLineU](#io()textlineu)
    - [IO().textLineU](#io()textlineu-1)
    - [IO().textLineW](#io()textlinew)
    - [IO().textLineW](#io()textlinew-1)
    - [IO().u16](#io()u16)
    - [IO().u16](#io()u16-1)
    - [IO().u16be](#io()u16be)
    - [IO().u16be](#io()u16be-1)
    - [IO().u16le](#io()u16le)
    - [IO().u16le](#io()u16le-1)
    - [IO().u32](#io()u32)
    - [IO().u32](#io()u32-1)
    - [IO().u32be](#io()u32be)
    - [IO().u32be](#io()u32be-1)
    - [IO().u32le](#io()u32le)
    - [IO().u32le](#io()u32le-1)
    - [IO().u64](#io()u64)
    - [IO().u64](#io()u64-1)
    - [IO().u64be](#io()u64be)
    - [IO().u64be](#io()u64be-1)
    - [IO().u64le](#io()u64le)
    - [IO().u64le](#io()u64le-1)
    - [IO().u8](#io()u8)
    - [IO().u8](#io()u8-1)
    - [IO().u8be](#io()u8be)
    - [IO().u8be](#io()u8be-1)
    - [IO().u8le](#io()u8le)
    - [IO().u8le](#io()u8le-1)
    - [IO().unsignedByte](#io()unsignedbyte)
    - [IO().unsignedByte](#io()unsignedbyte-1)
    - [IO().unsignedDword](#io()unsigneddword)
    - [IO().unsignedDword](#io()unsigneddword-1)
    - [IO().unsignedQword](#io()unsignedqword)
    - [IO().unsignedQword](#io()unsignedqword-1)
    - [IO().unsignedWord](#io()unsignedword)
    - [IO().unsignedWord](#io()unsignedword-1)
    - [IO().word](#io()word)
    - [IO().word](#io()word-1)

## IO

[Show source in binaryiotools.py:40](../../../gimpformats/binaryiotools.py#L40)

Class to handle i/o to a byte buffer or file-like object.

#### Signature

```python
class IO:
    def __init__(
        self,
        data: bytearray | bytes | None = None,
        idx: int = 0,
        littleEndian: bool = False,
        boolSize: int = 8,
        stringEncoding: str = "U",
    ) -> None: ...
```

### IO().__getitem__

[Show source in binaryiotools.py:72](../../../gimpformats/binaryiotools.py#L72)

Get data at a specific idx.

#### Signature

```python
def __getitem__(self, idx: int): ...
```

### IO().__len__

[Show source in binaryiotools.py:68](../../../gimpformats/binaryiotools.py#L68)

Length of data.

#### Signature

```python
def __len__(self) -> int: ...
```

### IO()._read

[Show source in binaryiotools.py:123](../../../gimpformats/binaryiotools.py#L123)

General formatted read.

#### Signature

```python
def _read(self, size: int, fmt: str) -> Any: ...
```

### IO()._readUntil

[Show source in binaryiotools.py:765](../../../gimpformats/binaryiotools.py#L765)

Read a sequence of chars in a set encoding until a set char.

#### Arguments

- `until` - must be within the ascii character set
- `encoding` - one of A (ascii), U (UTF-8) or W (UCS-2)

#### Signature

```python
def _readUntil(self, until: str, encoding: str = "A") -> str: ...
```

### IO()._sz754

[Show source in binaryiotools.py:697](../../../gimpformats/binaryiotools.py#L697)

Read the next string conforming to IEEE 754 and advance the index.

Note, string format is:
 uint32   n+1  Number of bytearray that follow, including the zero byte
 byte[n]  ...  String data in Unicode, encoded using UTF-8
 byte     0    Zero marks the end of the string.
or simply uint32=0 for empty string

#### Signature

```python
def _sz754(self, encoding: str) -> str: ...
```

### IO()._sz754set

[Show source in binaryiotools.py:719](../../../gimpformats/binaryiotools.py#L719)

_sz754set.

#### Signature

```python
def _sz754set(self, sz754: Any, _encoding: str) -> None: ...
```

### IO()._write

[Show source in binaryiotools.py:113](../../../gimpformats/binaryiotools.py#L113)

General formatted write.

#### Signature

```python
def _write(self, size: int, fmt: str, data: Any) -> None: ...
```

### IO().addbytearray

[Show source in binaryiotools.py:666](../../../gimpformats/binaryiotools.py#L666)

Add some raw bytearray and advance the index.

alias for setbytearray()

#### Arguments

- `bytearray` - can be a string, bytearray, or another IO object

#### Signature

```python
def addbytearray(self, iobytearray: Any) -> None: ...
```

### IO().beginContext

[Show source in binaryiotools.py:102](../../../gimpformats/binaryiotools.py#L102)

Start a new context where the index can be changed all you want...

and when endContext() is called, it will be restored to the current position

#### Signature

```python
def beginContext(self, newIndex: int) -> None: ...
```

### IO().bool16

[Show source in binaryiotools.py:180](../../../gimpformats/binaryiotools.py#L180)

Get bool16.

#### Signature

```python
@property
def bool16(self) -> bool: ...
```

### IO().bool16

[Show source in binaryiotools.py:185](../../../gimpformats/binaryiotools.py#L185)

Set bool16.

#### Signature

```python
@bool16.setter
def bool16(self, ioBool: bool) -> None: ...
```

### IO().bool32

[Show source in binaryiotools.py:190](../../../gimpformats/binaryiotools.py#L190)

Get bool32.

#### Signature

```python
@property
def bool32(self) -> bool: ...
```

### IO().bool32

[Show source in binaryiotools.py:195](../../../gimpformats/binaryiotools.py#L195)

Set bool32.

#### Signature

```python
@bool32.setter
def bool32(self, ioBool: bool) -> None: ...
```

### IO().bool64

[Show source in binaryiotools.py:200](../../../gimpformats/binaryiotools.py#L200)

Get bool64.

#### Signature

```python
@property
def bool64(self) -> bool: ...
```

### IO().bool64

[Show source in binaryiotools.py:205](../../../gimpformats/binaryiotools.py#L205)

Set bool64.

#### Signature

```python
@bool64.setter
def bool64(self, ioBool: bool) -> None: ...
```

### IO().bool8

[Show source in binaryiotools.py:170](../../../gimpformats/binaryiotools.py#L170)

Get bool8.

#### Signature

```python
@property
def bool8(self) -> bool: ...
```

### IO().bool8

[Show source in binaryiotools.py:175](../../../gimpformats/binaryiotools.py#L175)

Set a bool8.

#### Signature

```python
@bool8.setter
def bool8(self, ioBool: bool) -> None: ...
```

### IO().boolean

[Show source in binaryiotools.py:143](../../../gimpformats/binaryiotools.py#L143)

Return bool.

#### Signature

```python
@property
def boolean(self) -> bool: ...
```

### IO().boolean

[Show source in binaryiotools.py:156](../../../gimpformats/binaryiotools.py#L156)

Set bool.

#### Signature

```python
@boolean.setter
def boolean(self, ioBool: bool) -> None: ...
```

### IO().byte

[Show source in binaryiotools.py:210](../../../gimpformats/binaryiotools.py#L210)

Get byte.

#### Signature

```python
@property
def byte(self) -> Any: ...
```

### IO().byte

[Show source in binaryiotools.py:215](../../../gimpformats/binaryiotools.py#L215)

Set byte.

#### Signature

```python
@byte.setter
def byte(self, byte: Any) -> None: ...
```

### IO().cString

[Show source in binaryiotools.py:854](../../../gimpformats/binaryiotools.py#L854)

Read a sequence of chars until the next null byte.

#### Signature

```python
@property
def cString(self) -> str: ...
```

### IO().cString

[Show source in binaryiotools.py:859](../../../gimpformats/binaryiotools.py#L859)

Set a sequence of chars and add a null byte.

#### Signature

```python
@cString.setter
def cString(self, text: str) -> None: ...
```

### IO().cStringA

[Show source in binaryiotools.py:865](../../../gimpformats/binaryiotools.py#L865)

Read a sequence of chars until the next null byte in ascii.

#### Signature

```python
@property
def cStringA(self) -> str: ...
```

### IO().cStringA

[Show source in binaryiotools.py:870](../../../gimpformats/binaryiotools.py#L870)

Set a sequence of chars and add a null byte in ascii.

#### Signature

```python
@cStringA.setter
def cStringA(self, text: str) -> None: ...
```

### IO().cStringU

[Show source in binaryiotools.py:887](../../../gimpformats/binaryiotools.py#L887)

Read a sequence of chars until the next null byte in utf-8.

#### Signature

```python
@property
def cStringU(self) -> str: ...
```

### IO().cStringU

[Show source in binaryiotools.py:892](../../../gimpformats/binaryiotools.py#L892)

Set a sequence of chars and add a null byte in utf-8.

#### Signature

```python
@cStringU.setter
def cStringU(self, text: str) -> None: ...
```

### IO().cStringW

[Show source in binaryiotools.py:876](../../../gimpformats/binaryiotools.py#L876)

Read a sequence of chars until the next null byte in ucs-2.

#### Signature

```python
@property
def cStringW(self) -> str: ...
```

### IO().cStringW

[Show source in binaryiotools.py:881](../../../gimpformats/binaryiotools.py#L881)

Set a sequence of chars and add a null byte in ucs-2.

#### Signature

```python
@cStringW.setter
def cStringW(self, text: str) -> None: ...
```

### IO().data

[Show source in binaryiotools.py:76](../../../gimpformats/binaryiotools.py#L76)

Return data as a mutable bytearray.

#### Signature

```python
@property
def data(self) -> bytearray: ...
```

### IO().data

[Show source in binaryiotools.py:85](../../../gimpformats/binaryiotools.py#L85)

Set data.

#### Signature

```python
@data.setter
def data(self, data: bytearray) -> None: ...
```

### IO().double

[Show source in binaryiotools.py:610](../../../gimpformats/binaryiotools.py#L610)

Get a double.

#### Signature

```python
@property
def double(self) -> float: ...
```

### IO().double

[Show source in binaryiotools.py:615](../../../gimpformats/binaryiotools.py#L615)

Set a double.

#### Signature

```python
@double.setter
def double(self, floating: float) -> None: ...
```

### IO().dword

[Show source in binaryiotools.py:250](../../../gimpformats/binaryiotools.py#L250)

Get a dword.

#### Signature

```python
@property
def dword(self) -> Any: ...
```

### IO().dword

[Show source in binaryiotools.py:255](../../../gimpformats/binaryiotools.py#L255)

Set a dword.

#### Signature

```python
@dword.setter
def dword(self, dword: Any) -> None: ...
```

### IO().endContext

[Show source in binaryiotools.py:109](../../../gimpformats/binaryiotools.py#L109)

Restore the index to the previous location where it was when	beginContext() was called.

#### Signature

```python
def endContext(self) -> None: ...
```

### IO().float32

[Show source in binaryiotools.py:410](../../../gimpformats/binaryiotools.py#L410)

Get a float32.

#### Signature

```python
@property
def float32(self) -> float: ...
```

### IO().float32

[Show source in binaryiotools.py:417](../../../gimpformats/binaryiotools.py#L417)

Set a float32.

#### Signature

```python
@float32.setter
def float32(self, float32: float) -> None: ...
```

### IO().float32be

[Show source in binaryiotools.py:620](../../../gimpformats/binaryiotools.py#L620)

Read the next 32 bit float and advance the index.

#### Signature

```python
@property
def float32be(self) -> float: ...
```

### IO().float32be

[Show source in binaryiotools.py:625](../../../gimpformats/binaryiotools.py#L625)

Set a 32 bit float.

#### Signature

```python
@float32be.setter
def float32be(self, float32be: float) -> None: ...
```

### IO().float32le

[Show source in binaryiotools.py:630](../../../gimpformats/binaryiotools.py#L630)

Read the next 32 bit float and advance the index.

#### Signature

```python
@property
def float32le(self) -> float: ...
```

### IO().float32le

[Show source in binaryiotools.py:635](../../../gimpformats/binaryiotools.py#L635)

Set a 32 bit float.

#### Signature

```python
@float32le.setter
def float32le(self, float32le: float) -> None: ...
```

### IO().float64

[Show source in binaryiotools.py:425](../../../gimpformats/binaryiotools.py#L425)

Get a float64.

#### Signature

```python
@property
def float64(self) -> float: ...
```

### IO().float64

[Show source in binaryiotools.py:432](../../../gimpformats/binaryiotools.py#L432)

Set a float64.

#### Signature

```python
@float64.setter
def float64(self, float64: float) -> None: ...
```

### IO().float64be

[Show source in binaryiotools.py:640](../../../gimpformats/binaryiotools.py#L640)

Read the next 64 bit float and advance the index.

#### Signature

```python
@property
def float64be(self) -> float: ...
```

### IO().float64be

[Show source in binaryiotools.py:645](../../../gimpformats/binaryiotools.py#L645)

Set a 64 bit float.

#### Signature

```python
@float64be.setter
def float64be(self, float64be: float) -> None: ...
```

### IO().float64le

[Show source in binaryiotools.py:650](../../../gimpformats/binaryiotools.py#L650)

Read the next 64 bit float and advance the index.

#### Signature

```python
@property
def float64le(self) -> float: ...
```

### IO().float64le

[Show source in binaryiotools.py:655](../../../gimpformats/binaryiotools.py#L655)

Set a 64 bit float.

#### Signature

```python
@float64le.setter
def float64le(self, float64le: float) -> None: ...
```

### IO().floating

[Show source in binaryiotools.py:600](../../../gimpformats/binaryiotools.py#L600)

Get a float.

#### Signature

```python
@property
def floating(self) -> float: ...
```

### IO().floating

[Show source in binaryiotools.py:605](../../../gimpformats/binaryiotools.py#L605)

Set a float.

#### Signature

```python
@floating.setter
def floating(self, floating: float) -> None: ...
```

### IO().getbytearray

[Show source in binaryiotools.py:660](../../../gimpformats/binaryiotools.py#L660)

Grab some raw bytearray and advance the index.

#### Signature

```python
def getbytearray(self, nbytearray: int): ...
```

### IO().i16

[Show source in binaryiotools.py:320](../../../gimpformats/binaryiotools.py#L320)

Get an int16.

#### Signature

```python
@property
def i16(self) -> int: ...
```

### IO().i16

[Show source in binaryiotools.py:327](../../../gimpformats/binaryiotools.py#L327)

Set an int16.

#### Signature

```python
@i16.setter
def i16(self, i16: int) -> None: ...
```

### IO().i16be

[Show source in binaryiotools.py:510](../../../gimpformats/binaryiotools.py#L510)

Read the next signed int16 and advance the index.

#### Signature

```python
@property
def i16be(self) -> int: ...
```

### IO().i16be

[Show source in binaryiotools.py:515](../../../gimpformats/binaryiotools.py#L515)

Set the int16.

#### Signature

```python
@i16be.setter
def i16be(self, i16be: int) -> None: ...
```

### IO().i16le

[Show source in binaryiotools.py:500](../../../gimpformats/binaryiotools.py#L500)

Read the next signed int16 and advance the index.

#### Signature

```python
@property
def i16le(self) -> int: ...
```

### IO().i16le

[Show source in binaryiotools.py:505](../../../gimpformats/binaryiotools.py#L505)

Set the int16.

#### Signature

```python
@i16le.setter
def i16le(self, i16le: int) -> None: ...
```

### IO().i32

[Show source in binaryiotools.py:350](../../../gimpformats/binaryiotools.py#L350)

Get an int32.

#### Signature

```python
@property
def i32(self) -> int: ...
```

### IO().i32

[Show source in binaryiotools.py:357](../../../gimpformats/binaryiotools.py#L357)

Set an int32.

#### Signature

```python
@i32.setter
def i32(self, i32: int) -> None: ...
```

### IO().i32be

[Show source in binaryiotools.py:550](../../../gimpformats/binaryiotools.py#L550)

Read the next signed int32 and advance the index.

#### Signature

```python
@property
def i32be(self) -> int: ...
```

### IO().i32be

[Show source in binaryiotools.py:555](../../../gimpformats/binaryiotools.py#L555)

Set the int32.

#### Signature

```python
@i32be.setter
def i32be(self, i32be: int) -> None: ...
```

### IO().i32le

[Show source in binaryiotools.py:540](../../../gimpformats/binaryiotools.py#L540)

Read the next signed int32 and advance the index.

#### Signature

```python
@property
def i32le(self) -> int: ...
```

### IO().i32le

[Show source in binaryiotools.py:545](../../../gimpformats/binaryiotools.py#L545)

Set the int32.

#### Signature

```python
@i32le.setter
def i32le(self, i32le: int) -> None: ...
```

### IO().i64

[Show source in binaryiotools.py:380](../../../gimpformats/binaryiotools.py#L380)

Get an int64.

#### Signature

```python
@property
def i64(self) -> int: ...
```

### IO().i64

[Show source in binaryiotools.py:387](../../../gimpformats/binaryiotools.py#L387)

Set an int64.

#### Signature

```python
@i64.setter
def i64(self, i64: int) -> None: ...
```

### IO().i64be

[Show source in binaryiotools.py:590](../../../gimpformats/binaryiotools.py#L590)

Read the next signed int64 and advance the index.

#### Signature

```python
@property
def i64be(self) -> int: ...
```

### IO().i64be

[Show source in binaryiotools.py:595](../../../gimpformats/binaryiotools.py#L595)

Set the int64.

#### Signature

```python
@i64be.setter
def i64be(self, i64be: int) -> None: ...
```

### IO().i64le

[Show source in binaryiotools.py:580](../../../gimpformats/binaryiotools.py#L580)

Read the next signed int64 and advance the index.

#### Signature

```python
@property
def i64le(self) -> int: ...
```

### IO().i64le

[Show source in binaryiotools.py:585](../../../gimpformats/binaryiotools.py#L585)

Set the int64.

#### Signature

```python
@i64le.setter
def i64le(self, i64le: int) -> None: ...
```

### IO().i8

[Show source in binaryiotools.py:290](../../../gimpformats/binaryiotools.py#L290)

Get an int8.

#### Signature

```python
@property
def i8(self) -> int: ...
```

### IO().i8

[Show source in binaryiotools.py:297](../../../gimpformats/binaryiotools.py#L297)

Set an int8.

#### Signature

```python
@i8.setter
def i8(self, i8: int) -> None: ...
```

### IO().i8be

[Show source in binaryiotools.py:470](../../../gimpformats/binaryiotools.py#L470)

Read the next signed int8 and advance the index.

#### Signature

```python
@property
def i8be(self) -> int: ...
```

### IO().i8be

[Show source in binaryiotools.py:475](../../../gimpformats/binaryiotools.py#L475)

Set the int8.

#### Signature

```python
@i8be.setter
def i8be(self, i8be: int) -> None: ...
```

### IO().i8le

[Show source in binaryiotools.py:460](../../../gimpformats/binaryiotools.py#L460)

Read the next signed int8 and advance the index.

#### Signature

```python
@property
def i8le(self) -> int: ...
```

### IO().i8le

[Show source in binaryiotools.py:465](../../../gimpformats/binaryiotools.py#L465)

Set the int8.

#### Signature

```python
@i8le.setter
def i8le(self, i8le: int) -> None: ...
```

### IO().index

[Show source in binaryiotools.py:92](../../../gimpformats/binaryiotools.py#L92)

Return data.

#### Signature

```python
@property
def index(self) -> int: ...
```

### IO().index

[Show source in binaryiotools.py:97](../../../gimpformats/binaryiotools.py#L97)

Set index.

#### Signature

```python
@index.setter
def index(self, index: int) -> None: ...
```

### IO().qword

[Show source in binaryiotools.py:270](../../../gimpformats/binaryiotools.py#L270)

Get a qword.

#### Signature

```python
@property
def qword(self) -> Any: ...
```

### IO().qword

[Show source in binaryiotools.py:275](../../../gimpformats/binaryiotools.py#L275)

Set a qword.

#### Signature

```python
@qword.setter
def qword(self, qword: Any) -> None: ...
```

### IO().setbytearray

[Show source in binaryiotools.py:675](../../../gimpformats/binaryiotools.py#L675)

Add some raw bytearray and advance the index.

alias for addbytearray()

#### Arguments

- `iobytearray` - can be a string, bytearray, or another IO object

#### Signature

```python
def setbytearray(self, iobytearray: Any) -> None: ...
```

### IO().sz754

[Show source in binaryiotools.py:725](../../../gimpformats/binaryiotools.py#L725)

sz754.

#### Signature

```python
@property
def sz754(self) -> Any: ...
```

### IO().sz754

[Show source in binaryiotools.py:730](../../../gimpformats/binaryiotools.py#L730)

Set sz754.

#### Signature

```python
@sz754.setter
def sz754(self, sz754: Any) -> None: ...
```

### IO().sz754A

[Show source in binaryiotools.py:735](../../../gimpformats/binaryiotools.py#L735)

sz754A.

#### Signature

```python
@property
def sz754A(self) -> Any: ...
```

### IO().sz754A

[Show source in binaryiotools.py:740](../../../gimpformats/binaryiotools.py#L740)

Set sz754A.

#### Signature

```python
@sz754A.setter
def sz754A(self, sz754: Any) -> None: ...
```

### IO().sz754U

[Show source in binaryiotools.py:755](../../../gimpformats/binaryiotools.py#L755)

sz754U.

#### Signature

```python
@property
def sz754U(self) -> Any: ...
```

### IO().sz754U

[Show source in binaryiotools.py:760](../../../gimpformats/binaryiotools.py#L760)

Set sz754U.

#### Signature

```python
@sz754U.setter
def sz754U(self, sz754: Any) -> None: ...
```

### IO().sz754W

[Show source in binaryiotools.py:745](../../../gimpformats/binaryiotools.py#L745)

sz754W.

#### Signature

```python
@property
def sz754W(self) -> Any: ...
```

### IO().sz754W

[Show source in binaryiotools.py:750](../../../gimpformats/binaryiotools.py#L750)

Set sz754W.

#### Signature

```python
@sz754W.setter
def sz754W(self, sz754: Any) -> None: ...
```

### IO().textLine

[Show source in binaryiotools.py:794](../../../gimpformats/binaryiotools.py#L794)

Read a sequence of chars until the next new line char.

#### Signature

```python
@property
def textLine(self) -> str: ...
```

### IO().textLine

[Show source in binaryiotools.py:802](../../../gimpformats/binaryiotools.py#L802)

Set a sequence of chars until the next new line char.

#### Signature

```python
@textLine.setter
def textLine(self, text: str) -> None: ...
```

### IO().textLineA

[Show source in binaryiotools.py:809](../../../gimpformats/binaryiotools.py#L809)

Read a sequence of chars until the next new line char in ascii.

#### Signature

```python
@property
def textLineA(self) -> str: ...
```

### IO().textLineA

[Show source in binaryiotools.py:817](../../../gimpformats/binaryiotools.py#L817)

Set a sequence of chars until the next new line char in ascii.

#### Signature

```python
@textLineA.setter
def textLineA(self, text: str) -> None: ...
```

### IO().textLineU

[Show source in binaryiotools.py:839](../../../gimpformats/binaryiotools.py#L839)

Read a sequence of chars until the next new line char in utf-8.

#### Signature

```python
@property
def textLineU(self) -> str: ...
```

### IO().textLineU

[Show source in binaryiotools.py:847](../../../gimpformats/binaryiotools.py#L847)

Set a sequence of chars until the next new line char in utf-8.

#### Signature

```python
@textLineU.setter
def textLineU(self, text: str) -> None: ...
```

### IO().textLineW

[Show source in binaryiotools.py:824](../../../gimpformats/binaryiotools.py#L824)

Read a sequence of chars until the next new line char in ucs-2.

#### Signature

```python
@property
def textLineW(self) -> str: ...
```

### IO().textLineW

[Show source in binaryiotools.py:832](../../../gimpformats/binaryiotools.py#L832)

Set a sequence of chars until the next new line char in ucs-2.

#### Signature

```python
@textLineW.setter
def textLineW(self, text: str) -> None: ...
```

### IO().u16

[Show source in binaryiotools.py:335](../../../gimpformats/binaryiotools.py#L335)

Get an uint16.

#### Signature

```python
@property
def u16(self) -> int: ...
```

### IO().u16

[Show source in binaryiotools.py:342](../../../gimpformats/binaryiotools.py#L342)

Set an unint16.

#### Signature

```python
@u16.setter
def u16(self, u16: int) -> None: ...
```

### IO().u16be

[Show source in binaryiotools.py:480](../../../gimpformats/binaryiotools.py#L480)

Read the next uint16 and advance the index.

#### Signature

```python
@property
def u16be(self) -> int: ...
```

### IO().u16be

[Show source in binaryiotools.py:485](../../../gimpformats/binaryiotools.py#L485)

Set the uint16.

#### Signature

```python
@u16be.setter
def u16be(self, u16be: int) -> None: ...
```

### IO().u16le

[Show source in binaryiotools.py:490](../../../gimpformats/binaryiotools.py#L490)

Read the next uint16 and advance the index.

#### Signature

```python
@property
def u16le(self) -> int: ...
```

### IO().u16le

[Show source in binaryiotools.py:495](../../../gimpformats/binaryiotools.py#L495)

Set the uint16.

#### Signature

```python
@u16le.setter
def u16le(self, u16le: int) -> None: ...
```

### IO().u32

[Show source in binaryiotools.py:365](../../../gimpformats/binaryiotools.py#L365)

Get a uint32.

#### Signature

```python
@property
def u32(self) -> int: ...
```

### IO().u32

[Show source in binaryiotools.py:372](../../../gimpformats/binaryiotools.py#L372)

Set a unint32.

#### Signature

```python
@u32.setter
def u32(self, u32: int) -> None: ...
```

### IO().u32be

[Show source in binaryiotools.py:520](../../../gimpformats/binaryiotools.py#L520)

Read the next uint32 and advance the index.

#### Signature

```python
@property
def u32be(self) -> int: ...
```

### IO().u32be

[Show source in binaryiotools.py:525](../../../gimpformats/binaryiotools.py#L525)

Set the uint32.

#### Signature

```python
@u32be.setter
def u32be(self, u32be: int) -> None: ...
```

### IO().u32le

[Show source in binaryiotools.py:530](../../../gimpformats/binaryiotools.py#L530)

Read the next uint32 and advance the index.

#### Signature

```python
@property
def u32le(self) -> int: ...
```

### IO().u32le

[Show source in binaryiotools.py:535](../../../gimpformats/binaryiotools.py#L535)

Set the uint32.

#### Signature

```python
@u32le.setter
def u32le(self, u32le: int) -> None: ...
```

### IO().u64

[Show source in binaryiotools.py:395](../../../gimpformats/binaryiotools.py#L395)

Get a uint64.

#### Signature

```python
@property
def u64(self) -> int: ...
```

### IO().u64

[Show source in binaryiotools.py:402](../../../gimpformats/binaryiotools.py#L402)

Set a uint64.

#### Signature

```python
@u64.setter
def u64(self, u64: int) -> None: ...
```

### IO().u64be

[Show source in binaryiotools.py:560](../../../gimpformats/binaryiotools.py#L560)

Read the next uint64 and advance the index.

#### Signature

```python
@property
def u64be(self) -> int: ...
```

### IO().u64be

[Show source in binaryiotools.py:565](../../../gimpformats/binaryiotools.py#L565)

Set the uint64.

#### Signature

```python
@u64be.setter
def u64be(self, u64be: int) -> None: ...
```

### IO().u64le

[Show source in binaryiotools.py:570](../../../gimpformats/binaryiotools.py#L570)

Read the next uint64 and advance the index.

#### Signature

```python
@property
def u64le(self) -> int: ...
```

### IO().u64le

[Show source in binaryiotools.py:575](../../../gimpformats/binaryiotools.py#L575)

Set the uint64.

#### Signature

```python
@u64le.setter
def u64le(self, u64le: int) -> None: ...
```

### IO().u8

[Show source in binaryiotools.py:305](../../../gimpformats/binaryiotools.py#L305)

Get an unsigned int.

#### Signature

```python
@property
def u8(self) -> int: ...
```

### IO().u8

[Show source in binaryiotools.py:312](../../../gimpformats/binaryiotools.py#L312)

Set an unsigned int.

#### Signature

```python
@u8.setter
def u8(self, u8: int) -> None: ...
```

### IO().u8be

[Show source in binaryiotools.py:440](../../../gimpformats/binaryiotools.py#L440)

Read the next uint8 and advance the index.

#### Signature

```python
@property
def u8be(self) -> int: ...
```

### IO().u8be

[Show source in binaryiotools.py:445](../../../gimpformats/binaryiotools.py#L445)

Set the uint8.

#### Signature

```python
@u8be.setter
def u8be(self, u8be: int) -> None: ...
```

### IO().u8le

[Show source in binaryiotools.py:450](../../../gimpformats/binaryiotools.py#L450)

Read the next uint8 and advance the index.

#### Signature

```python
@property
def u8le(self) -> int: ...
```

### IO().u8le

[Show source in binaryiotools.py:455](../../../gimpformats/binaryiotools.py#L455)

Set the uint8.

#### Signature

```python
@u8le.setter
def u8le(self, u8le: int) -> None: ...
```

### IO().unsignedByte

[Show source in binaryiotools.py:220](../../../gimpformats/binaryiotools.py#L220)

Get unsigned byte.

#### Signature

```python
@property
def unsignedByte(self) -> Any: ...
```

### IO().unsignedByte

[Show source in binaryiotools.py:225](../../../gimpformats/binaryiotools.py#L225)

Set unsigned byte.

#### Signature

```python
@unsignedByte.setter
def unsignedByte(self, byte: Any) -> None: ...
```

### IO().unsignedDword

[Show source in binaryiotools.py:260](../../../gimpformats/binaryiotools.py#L260)

Get a unsigned dword.

#### Signature

```python
@property
def unsignedDword(self) -> Any: ...
```

### IO().unsignedDword

[Show source in binaryiotools.py:265](../../../gimpformats/binaryiotools.py#L265)

Set an unsigned dword.

#### Signature

```python
@unsignedDword.setter
def unsignedDword(self, unsignedDword: Any) -> None: ...
```

### IO().unsignedQword

[Show source in binaryiotools.py:280](../../../gimpformats/binaryiotools.py#L280)

Get an unsigned qword.

#### Signature

```python
@property
def unsignedQword(self) -> Any: ...
```

### IO().unsignedQword

[Show source in binaryiotools.py:285](../../../gimpformats/binaryiotools.py#L285)

Set an unsigned qword.

#### Signature

```python
@unsignedQword.setter
def unsignedQword(self, unsignedQword: Any) -> None: ...
```

### IO().unsignedWord

[Show source in binaryiotools.py:240](../../../gimpformats/binaryiotools.py#L240)

Get an unsigned word.

#### Signature

```python
@property
def unsignedWord(self) -> Any: ...
```

### IO().unsignedWord

[Show source in binaryiotools.py:245](../../../gimpformats/binaryiotools.py#L245)

Set an unsigned word.

#### Signature

```python
@unsignedWord.setter
def unsignedWord(self, unsignedWord: Any) -> None: ...
```

### IO().word

[Show source in binaryiotools.py:230](../../../gimpformats/binaryiotools.py#L230)

Get a word.

#### Signature

```python
@property
def word(self) -> Any: ...
```

### IO().word

[Show source in binaryiotools.py:235](../../../gimpformats/binaryiotools.py#L235)

Set a word.

#### Signature

```python
@word.setter
def word(self, word: Any) -> None: ...
```