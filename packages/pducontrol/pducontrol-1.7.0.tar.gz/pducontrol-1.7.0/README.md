from selenium.webdriver.common.devtools.v117.web_authn import get_credentials

# pducontrol

pducontrol is a Python library to control a wide variety of PDUs
Currently we support the following models:

* SWH-1023J-08N1 (Dexlan, seems to be just an OEM rebadged unit)
* PDU81003 (CyberPower)
* NetIO 4C

## Installation

 You can install pducontrol from source:

```sh
make pip
pip install /dist/pducontrol-*.tar.gz
```
or just call the ``refresh_package.sh`` script

## Usage

This package provides both Python and CLI interfaces, here is how you can 
use them:

### In Python
You can either instantiate the class targeting your PDU, for instance for a
Dexlan unit:  

```python
from pducontrol import PDUControlREST
pdu = PDUControlREST("192.168.0.23")
print(pdu.get_all_names())
```
Or for more flexibility, you can let pducontrol choose the class to
instantiate:  

```python
from types import SimpleNamespace
from pducontrol import choose_pdu
pdu = choose_pdu(SimpleNamespace(ip_address="192.168.1.23"), {}, 5)
print(pdu.get_all_names())
```
### In CLI

```sh
pducontrol 192.168.1.23 get_name all
```

More information can be found using the `-h` argument. Some arguments even 
have submenus, for instance:
```sh
pducontrol 192.168.1.23 set -h
usage: pducontrol ip_address set [-h] outlets {on,off,reboot}

positional arguments:
  outlets          comma-separated list of outlets
  {on,off,reboot}  state to set the outlets to, can be one of [on, off,
                   reboot]

```

A configuration file named `pdu_settings.cfg`, containing IP addresses and
credentials can be added in`~/.config/pducontrol/` for ease of use and 
autocompletion. 

An example file is available in `config`.


## Contributing

Bug reports and comments are warmly welcome,
but contributions, such as pull requests and patches,
are not, for legal reasons only.
If that's bothering you, don't hesitate to tell, with enough pressure, we could
reconsider our position.

## License

pducontrol is released under LGPL v3

## Hacking

### Execute the program from the source directory

```sh
python3 -m pducontrol
```

### Generate a debian package

```sh
make debian
```

### Execute the unit tests

They are located in **tests/**.

```sh
make test
```

### Coding style

All python files should respect the PEP 8 coding style and shell scripts, the
shellcheck coding style.

### How to publish a release

1. put the repository on the release's revision
2. `make pip`
3. `twine upload dist/*`

