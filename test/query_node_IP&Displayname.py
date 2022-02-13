import sys
try:
    import orionsdk
except ImportError:
    print("Module orionsdk needs to be installed")
    print("pip install orionsdk")
    sys.exit()

#SwicClient("ServerIP/Name", "Username", "Password")
swis = orionsdk.SwisClient("192.168.21.39", "test", "Password01!!")
#Get Hostname/ IP / information  from Orion.Nodes if Vendor is Cisco
swis.query("SELECT DisplayName, IP FROM Orion.Nodes WHERE Vendor='Cisco' ")


"""
Reuulsts json format as below:

{'results': [{'NodeID': 2, 'DisplayName': 'N5K-1', 'IP': '192.168.20.13'},
  {'NodeID': 3, 'DisplayName': 'N5K-2', 'IP': '192.168.20.14'}]}
  
"""