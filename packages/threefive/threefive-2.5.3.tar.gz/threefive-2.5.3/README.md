 | [cli](#cli) | [lib](#lib) | [examples](#examples) | [hls](https://github.com/futzu/threefive/blob/master/hlsparse.md) | [encoding](#encoding) | [sixfix](https://github.com/futzu/SCTE35_threefive/blob/master/cli.md#sixfix) | [sidecar files](https://github.com/futzu/SCTE35_threefive/blob/master/sidecar.md) | [xml](https://github.com/futzu/SCTE35_threefive/blob/master/xml.md) | [iodisco.com/scte35 ](https://iodisco.com/cgi-bin/scte35parser) | 

# threefive is SCTE-35.
##### SCTE-35 Parser. SCTE-35 Decoder. SCTE-35 Encoder. MPEGTS SCTE-35 Packet Injection. HLS Manifest and Segment SCTE-35 Parser. HLS SCTE-35 Injection. SCTE-35 Xml and Xml+bin Decoder/ Encoder for DASH.

## Latest version is v2.4.97
* Updated to latest version of new_reader for Zero packet loss Multicast _(tested on OpenBSD and Debian)_.   
* [The cli has been Upgraded and tuned.]((https://github.com/futzu/threefive/blob/master/latest-cli.md))
* Xml Node Namespaces and attribute namespaces are now configurable.
* Turned SegmentationDescriptor.segmentation_message back on.
* Fix UMID upid encoding 
* Added a  [__Super Amazing__ HLS SCTE-35 Parser](https://github.com/futzu/threefive/blob/master/hlsparse.md)  to the __threefive cli.__. 
* Added a HLS SCTE-35 Encoder to the __threefive cli.__.
* MPEGTS Packet Injection added to the __threefive cli.__.
    * [Sidecar files explained](https://github.com/futzu/SCTE35_threefive/blob/master/sidecar.md)
* [sixfix](https://github.com/futzu/SCTE35_threefive/blob/master/newcli.md) : __ffmpeg__ turns SCTE-35 streams to __bin data (0x06)__, sixfix switches them back to SCTE-35 (0x86).
* [Xml](https://github.com/futzu/SCTE35-threefive/blob/master/latest-cli.md): Experimental support for [SCTE-35 xml as an input and output](https://github.com/futzu/SCTE35_threefive/blob/master/xml.md) ( DASH SCTE-214)


# Documentation
#### 
* _threefive is developed and tested on OpenBSD and Debian Sid._ 
    
#### Latest docs are always available in the python shell
```py3

>>>> from threefive import TimeSignal
>>>> help(TimeSignal)
```

### install
* python3
```py3
python3 -mpip install threefive
```
* pypy3
```py3
pypy3 -mpip install threefive
```

  
* [super cool examples](https://github.com/futzu/SCTE35-threefive/blob/master/examples/README.md)

* New! [threefive: more OO than you know](https://github.com/futzu/threefive/blob/master/oo.md)
   
* [answers to some common problems with ffmpeg and SCTE-35](https://github.com/futzu/SCTE35-threefive/blob/master/ffmpegscte35.md)

<details><summary>Versions and Releases</summary>

Every time I fix a bug or add a feature, I do a new release. <br>
This makes tracking down bugs and stuff much easier. <br>
Keep up, I do releases for reasons.
```lua
a@slow:~/threefive$ threefive version
2.4.81
a@slow:~/threefive$ 

```

* __Release__ versions are  __odd__.
* __Unstable__ testing versions are __even__.
---
![image](https://github.com/user-attachments/assets/caac5f33-204e-47c7-bcdb-1e2d05fdaefb)

</details>

## cli

* [The New Cli](https://github.com/futzu/threefive/blob/master/latest-cli.md)

*  [Decode SCTE-35 HLS](https://github.com/futzu/threefive/blob/master/newcli.md#hls-decode-scte-35)
*  [Encode SCTE-35 HLS](https://github.com/futzu/threefive/blob/master/newcli.md#hls-encode-scte-35)
*  [MPEGTS](https://github.com/futzu/threefive/blob/master/newcli.md#mpegts) (proy,pts,sidecar,sixfix,show,xml)

## lib
* New! [threefive: more OO than you know](https://github.com/futzu/threefive/blob/master/oo.md)
* [Parse SCTE-35 programmatically](https://github.com/futzu/scte35parser-threefive/blob/master/prog.md) with __threefive__ </i>(write some code)</i>
* [How to Use __threefive.Cue__](https://github.com/futzu/SCTE35_threefive/blob/master/basic.md)
* [Trigger on SCTE-35 __Events__](https://github.com/futzu/scte35parser-threefive/blob/master/trigger.md) using __threefive.Stream__

## online parser
* [iodisco.com/scte35 ](https://iodisco.com/cgi-bin/scte35parser) the only accurate online SCTE-35 parser (__powered by threefive__).

## examples
* SCTE-35 code [Examples](https://github.com/futzu/SCTE35-threefive/blob/master/examples/README.md)
  
## decryption
* Automatic __AES decryption__ with [threefive.Segment](https://github.com/futzu/SCTE35_threefive/blob/master/segment.md)

## webvtt
* Display SCTE-35 Data as [__WebVTT__ subtitles in Video](https://github.com/futzu/SCTE35_threefive/blob/master/examples/stream/cue2vtt.py)
      
## dash
* [A minimal Dash SCTE-35 mpd parser](https://github.com/futzu/SCTE35-threefive/blob/master/mpd_parser.md)
* [Experimental Dash SCTE-214 Support Now available in threefive 2.4.81 ](https://github.com/futzu/SCTE35-threefive/blob/master/dash.md) (_updated 10/15/2024_)

## encoding
*  [Encoding](https://github.com/futzu/scte35parser-threefive/blob/master/Encoding.md)
*  [Encoding | more_](https://github.com/futzu/scte35parser-threefive/blob/master/EncodingPipeMore.md)
*  [JSON to SCTE-35 Encoding](https://github.com/futzu/SCTE35_threefive/blob/master/cliencde.md)


</details>
 
 <details><summary>Cue Class</summary>

   *  src [cue.py](https://github.com/futzu/SCTE35-threefive/blob/master/threefive/cue.py)
   *  The __threefive.Cue__ class decodes a SCTE35 binary, base64, or hex encoded string.

 ![image](https://github.com/futzu/scte35-threefive/assets/52701496/5b8dbea3-1d39-48c4-8fbe-de03a53cc1dd)


```py3

class Cue(threefive.base.SCTE35Base)
 |  Cue(data=None, packet_data=None)

```
```js
 |  __init__(self, data=None, packet_data=None)
 |      data may be packet bites or encoded string
 |      packet_data is a instance passed from a Stream instance
```
* `Cue.decode()`
```js
 |  decode(self)
 |      Cue.decode() parses for SCTE35 data
```
* After Calling cue.decode() the __instance variables can be accessed via dot notation__.
```python3

    >>>> cue.command
    {'calculated_length': 5, 'name': 'Time Signal', 'time_specified_flag': True, 'pts_time': 21695.740089}

    >>>> cue.command.pts_time
    21695.740089

    >>>> cue.info_section.table_id

    '0xfc'
```

* `Cue.get()`
```js
 |  get(self)
 |      Cue.get returns the SCTE-35 Cue
 |      data as a dict of dicts.
```
> `Cue.get() Example`
```python3
>>> from threefive import Cue
>>> cue = Cue('0XFC301100000000000000FFFFFF0000004F253396')
>>> cue.decode()
True
>>> cue
{'bites': b'\xfc0\x11\x00\x00\x00\x00\x00\x00\x00\xff\xff\xff\x00\x00\x00O%3\x96',
'info_section': {'table_id': '0xfc', 'section_syntax_indicator': False, 'private': False, 'sap_type': '0x3',
'sap_details': 'No Sap Type', 'section_length': 17, 'protocol_version': 0, 'encrypted_packet': False,
'encryption_algorithm': 0, 'pts_adjustment_ticks': 0, 'pts_adjustment': 0.0, 'cw_index': '0x0', 'tier': '0xfff',
'splice_command_length': 4095, 'splice_command_type': 0, 'descriptor_loop_length': 0, 'crc': '0x4f253396'},
'command': {'command_length': None, 'command_type': 0, 'name': 'Splice Null'},
'descriptors': [], 'packet_data': None}
```
* Cue.get() omits cue.bites and empty values
```
>>> cue.get()
{'info_section': {'table_id': '0xfc', 'section_syntax_indicator': False,'private': False, 'sap_type': '0x3',
'sap_details': 'No Sap Type', 'section_length': 17, 'protocol_version': 0, 'encrypted_packet': False,
'encryption_algorithm': 0, 'pts_adjustment_ticks': 0, 'pts_adjustment': 0.0, 'cw_index': '0x0', 'tier': '0xfff',
'splice_command_length': 4095, 'splice_command_type': 0, 'descriptor_loop_length': 0, 'crc': '0x4f253396'},
'command': {'command_type': 0, 'name': 'Splice Null'},
'descriptors': []}
```

* `Cue.get_descriptors()`

```js
 |  get_descriptors(self)
 |      Cue.get_descriptors returns a list of
 |      SCTE 35 splice descriptors as dicts.
```
* `Cue.get_json()`
```js
 |  get_json(self)
 |      Cue.get_json returns the Cue instance
 |      data in json.
```
* `Cue.show()`
```js
 |  show(self)
 |      Cue.show prints the Cue as JSON
```
* `Cue.to_stderr()`
```js
 |  to_stderr(self)
 |      Cue.to_stderr prints the Cue
```
</details>


<details><summary>Stream Class</summary>




  * src [stream.py](https://github.com/futzu/SCTE35-threefive/blob/master/threefive/stream.py)
  * The threefive.__Stream__ class parses __SCTE35__ from __Mpegts__.
  * Supports:
     *  __File__ and __Http(s)__ and __Udp__ and __Multicast__ protocols.
  	 * __Multiple Programs__.
  	 * __Multi-Packet PAT, PMT, and SCTE35 tables__.

* threefive tries to include __pid__, __program__, anf  __pts__ of the SCTE-35 packet.

```js
class Stream(builtins.object)
 |  Stream(tsdata, show_null=True)
 |
 |  Stream class for parsing MPEG-TS data.
 ```
 ```py3
 |  __init__(self, tsdata, show_null=True)
 |
 |      tsdata is a file or http, https,
 |       udp or multicast url.
 |
 |      set show_null=False to exclude Splice Nulls

 ```

* `Stream.decode(func=show_cue)`
 ```py3
 |  decode(self, func=show_cue)
 |      Stream.decode reads self.tsdata to find SCTE35 packets.
 |      func can be set to a custom function that accepts
 |      a threefive.Cue instance as it's only argument.
 ```
 > `Stream.decode Example`

 ```python3
 import sys
 from threefive import Stream
 >>>> Stream('plp0.ts').decode()

```

   *   Pass in custom function

   *  __func__ should match the interface
  ``` func(cue)```

 > `Stream.decode with custom function Example`
```python3
import sys
import threefive

def display(cue):
   print(f'\033[92m{cue.packet_data}\033[00m')
   print(f'{cue.command.name}')

def do():
   sp = threefive.Stream(tsdata)
   sp.decode(func = display)

if __name__ == '__main__':
    do()
```

___

* `Stream.decode_next()`

 ```js
 |  decode_next(self)
 |      Stream.decode_next returns the next
 |      SCTE35 cue as a threefive.Cue instance.
 ```

> `Stream.decode_next Example`
```python3
"""
Stream.decode_next example.
decode_next returns the Cue every time a Cue is found.

This uses a while loop to pull the Cues from a mpegts stream.
When a Cue is found, if it's a Time Signal,
cue.command.command_type=6, print Cue.command.
You can filter on any var in the SCTE-35 Cue.
"""

import sys
import threefive
from new_reader import reader

def do():
    arg = sys.argv[1]
    with reader(arg) as tsdata:
        st = threefive.Stream(tsdata)
        while True:
            cue = st.decode_next()
            if not cue:
                return False
            if cue:
                if cue.command.command_type ==6:
                    print(cue.command)


if __name__ == "__main__":
    do()

```

* `Stream.proxy(func = show_cue)`

  *  Writes all packets to sys.stdout.

  *  Writes scte35 data to sys.stderr.

 ```js
 |  decode(self, func=show_cue_stderr)
 |      Stream.decode_proxy writes all ts packets are written to stdout
 |      for piping into another program like mplayer.
 |      SCTE-35 cues are printed to stderr.
 ```
> `Stream.proxy Example`
```python3

import threefive
sp = threefive.Stream('https://futzu.com/xaa.ts')
sp.decode_proxy()
```

* Pipe to mplayer
```bash
$ python3 proxy.py | mplayer -
```
___

* `Stream.show()`

```js
|  show(self)
|   List programs and streams and info for MPEGTS
```
> `Stream.show() Example`
```python3
>>>> from threefive import Stream
>>>> Stream('https://slo.me/plp0.ts').show()
```

```js
    Service:    fancy ˹
    Provider:   fu-corp
    Pcr Pid:    1051[0x41b]
    Streams:
                Pid: 1051[0x41b]        Type: 0x1b AVC Video
                Pid: 1052[0x41c]        Type: 0x3 MP2 Audio
                Pid: 1054[0x41e]        Type: 0x6 PES Packets/Private Data
                Pid: 1055[0x41f]        Type: 0x86 SCTE35 Data

```
</details>



<details><summary> Need to verify your splice points? </summary> 
 

 ![image](https://github.com/user-attachments/assets/2581053a-e373-434e-9e06-32ace453aa02)

 
* Try [cue2vtt.py](https://github.com/futzu/scte35-threefive/blob/master/examples/stream/cue2vtt.py) in the examples.

   * cue2vtt.py creates webvtt subtitles out of SCTE-35 Cue data
 
* use it like this 

 ```rebol
 pypy3 cue2vtt.py video.ts | mplayer video.ts -sub -
```




---

</details> 





<details><summary><b>threefive</b> is now <b>addressable TV</b> compatible</summary>


  ```smalltalk
             "tag": 2,
            "descriptor_length": 31,
            "name": "Segmentation Descriptor",
            "identifier": "CUEI",
            "components": [],
            "segmentation_event_id": "0x065eff",
            "segmentation_event_cancel_indicator": false,
            "segmentation_event_id_compliance_indicator": true,
            "program_segmentation_flag": true,
            "segmentation_duration_flag": false,
            "delivery_not_restricted_flag": true,
            "segmentation_message": "Call Ad Server",   < --- Boom
            "segmentation_upid_type": 12,
            "segmentation_upid_type_name": "MPU",
            "segmentation_upid_length": 16,
            "segmentation_upid": {
                "format_identifier": "ADFR",	<--- Boom
                "private_data": "0x0133f10134b04f065e060220",
                "version": 1,                            <---- Boom
                "channel_identifier": "0x33f1",                  <---- Boom
                "date": 20230223,                         <---- Boom
                "break_code": 1630,                       <---- Boom
                "duration": "0x602"                <---- Boom
            },
            "segmentation_type_id": 2,         <----  Boom
            "segment_num": 0,
            "segments_expected": 0
        },

  ```

---


</details>


<details><summary>Custom charsets for UPIDS aka upids.charset</summary>


`Specify a charset for Upid data by setting threefive.upids.charset` [`issue #55`](https://github.com/futzu/scte35-threefive/issues/55)

* default charset is ascii
* python charsets info [Here](https://docs.python.org/3/library/codecs.html)
* setting charset to None will return raw bytes.


#### Example Usage:

```lua
>>> from threefive import Cue,upids
>>> i="/DBKAAAAAAAAAP/wBQb+YtC8/AA0AiZDVUVJAAAD6X/CAAD3W3ACEmJibG5kcHBobkQCAsGDpQIAAAAAAAEKQ1VFSRSAIyowMljRk9c="

>>> upids.charset
'ascii'
>>> cue=Cue(i)
>>> cue.decode()
ascii
True
>>> cue.descriptors[0].segmentation_upid
'bblndpphnD\x02\x02���\x02\x00\x00'

>>> upids.charset="utf16"
>>> cue.decode()
utf16
True
>>> cue.descriptors[0].segmentation_upid
'扢湬灤桰䑮Ȃ菁ʥ\x00'
```

</details>

<details> <summary> Custom Private Splice Descriptors ( new! )</summary>


### threefive now supports custom private splice descriptors, right out the box. 
*  The first byte of the descriptor is read as an int for the Descriptor tag
* The second byte is read as an int for  the desciptor length
* The next four bytes are read as ASCII for the Identifier
* remanining bytes are returned as private data

```js
from threefive import Cue, TimeSignal
from threefive.descriptors import SpliceDescriptor
```
* make a Cue
```smalltalk
c = Cue()
```
* add a Time Signal
```smalltalk
c.command = TimeSignal()
c.command.time_specified_flag=True
c.command.pts_time=1234.567890
```
* add Splice Descriptor

```smalltalk
sd = SpliceDescriptor()
sd.tag = 47
sd.identifier ='fufu'
sd.private_data = b'threefive kicks ass'
c.descriptors.append(sd)
```
* encode
```smalltalk
c.encode()
'/DAvAAAAAAAAAP/wBQb+Bp9rxgAZLxdmdWZ1dGhyZWVmaXZlIGtpY2tzIGFzc1m+EsU='
```
* show

```smalltalk

c.show()
{
    "info_section": {
        "table_id": "0xfc",
        "section_syntax_indicator": false,
        "private": false,
        "sap_type": "0x03",
        "sap_details": "No Sap Type",
        "section_length": 47,
        "protocol_version": 0,
        "encrypted_packet": false,
        "encryption_algorithm": 0,
        "pts_adjustment_ticks": 0,
        "cw_index": "0x0",
        "tier": "0xfff",
        "splice_command_length": 5,
        "splice_command_type": 6,
        "descriptor_loop_length": 25,
        "crc": "0x59be12c5"
    },
    "command": {
        "command_length": 5,
        "command_type": 6,
        "name": "Time Signal",
        "time_specified_flag": true,
        "pts_time": 1234.56789,
        "pts_time_ticks": 111111110
    },
    "descriptors": [
        {
            "tag": 47,
            "descriptor_length": 23,
            "identifier": "fufu",
            "private_data": [
                116,
                104,
                114,
                101,
                101,
                102,
                105,
                118,
                101,
                32,
                107,
                105,
                99,
                107,
                115,
                32,
                97,
                115,
                115
            ]
        }
    ]
}
```
*  the custom Splice Descriptor
```js
c.descriptors[0]

{'tag': 47, 'descriptor_length': 23, 'name': None, 'identifier': 'fufu', 'bites': None, 'provider_avail_id': None, 'components': None, 'private_data': b'threefive kicks ass'}
```
* Cool dictionaary comprehension to print the Splice Descriptor with only relevant values
 
```js
{print(f'{k} = {v}') for k,v in vars(c.descriptors[0]).items() if v is not None}

tag = 47
descriptor_length = 23
identifier = fufu
private_data = b'threefive kicks ass'


```


</details>



 Powered by threefive
---

 
<br>⚡ [x9k3](https://github.com/futzu/x9k3): SCTE-35 HLS Segmenter and Cue Inserter.
<br>⚡ [m3ufu](https://github.com/futzu/m3ufu): SCTE-35 m3u8 Parser.
<br>⚡ [adbreak2](https://github.com/futzu/adbreak2) a cli tool that quickly and easily generates SCTE-35 Cues for HLS and stuff.
<br>⚡ [Ultra Mega Zoom Zoom](https://github.com/futzu/umzz) ABR HLS segmenter and SCTE-35 inserter. 
<br>⚡ [POIS Server](https://github.com/scunning1987/pois_reference_server) is Super Cool.
<br>⚡ [bpkio-cli](https://pypi.org/project/bpkio-cli/): A command line interface to the broadpeak.io APIs. 
<br>⚡ [amt-play ](https://github.com/vivoh-inc/amt-play) uses x9k3.


 threefive | more
 ---
 
<br>⚡ [Diagram](https://github.com/futzu/threefive/blob/master/cue.md) of a threefive SCTE-35 Cue.
<br>⚡ [ffmpeg and threefive](https://github.com/futzu/SCTE35-threefive/blob/master/threefive-ffmpeg.md) and SCTE35 and Stream Type 0x6 bin data.
<br>⚡ [Issues and Bugs and Feature Requests](https://github.com/futzu/scte35-threefive/issues) will be considered. Please don't make me regret it. 
<br>⚡ `NEW!` __threefive__ now has experimental DVB DAS Support `ETSI TS 103 752-1` <br><br>

 [![image](https://github.com/user-attachments/assets/ec5192f3-8484-4f85-87ab-f9d72374c666)](https://iodisco.com/scte35)




