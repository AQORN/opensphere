# opensphere
OpenSphere is an open-source python-based project designed to replace the need for VMware ESX/vSphere cllent in simple lab use cases.

-- So far:
VMware offers a free license for 5 ESX servers and their own vSphere client to manage virtualization. It's easy to use and surprisingly there is no open-source alternative that focuses on making virtualization easy.

-- With OpenSphere:
This is a GUI written in Python3 that runs on Windows, Mac or Linux. The client connects to any Debian or RHEL system and coordinates KVM virtual machines and OpenvSwitch networking for the simple task of running and managing virtual machines easily without the need or use of VMware. In the future it will add support for OpenX - essentially vCenter but using OpenStack - for the purpose of managing multiple KVM hosts.

:: Some terminology equivalents
Linux replaces ESX
OpenSphere replaces vSphere
OpenX replaces vCenter (eventually)

While this is intended as a personal project being shared publicly for educational and non-commercial use, please let me know if you'd like to contribute at github@aqorn.com.

//adam

Disclaimer:
Any reference to proprietary product names are trademarks of their respective trademark holders.
