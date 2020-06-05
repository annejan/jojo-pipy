RaspberyPi Python app FeedMe
==

©️ 2019-2020 Jolanda Versteeg and Anne Jan Brouwer

Choose some words, get a nice label 😄

Requirements
--

Python3 Qt5
```bash
sudo apt-get install python3 python3-pyqt5 qt5-qmake qt5-default
```

Manually if needed:
```bash
wget https://www.riverbankcomputing.com/static/Downloads/sip/4.19.21/sip-4.19.21.tar.gz
tar xvf sip-4.19.21.tar.gz
cd sip-4.19.21
python3 configure.py --sip-module=PyQt5.sip
make -j$(nproc)
sudo make install
wget https://netcologne.dl.sourceforge.net/project/pyqt/PyQt5/PyQt-5.7.1/PyQt5_gpl-5.7.1.tar.gz
tar xvf PyQt5_gpl-5.7.1.tar.gz
cd PyQt5_gpl-5.7.1
python3 configure.py
make -j$(nproc)
sudo make install
```
NB: This is assuming Qt 5.7.1

Also I patched the PyQt5_gpl-5.7.1 `configure.py`

Change:
```python
    argv = [quote(target_config.sip), '-w', '-f', sip_flags]
```
To:
```python
    argv = [quote(target_config.sip), '-w', '-f', sip_flags, '-n', mname]
```

And/or comment out:
```python
    argv.append('-B')
    argv.append('Qt_6_0_0')
```

Running
---

```bash
python3 main.py
```
