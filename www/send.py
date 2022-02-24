import sys
import hashlib
import multicast_client
if sys.version_info < (3, 6):
    import sha3


if len(sys.argv)==3:
    macKeyPair=sys.argv[1]+"-"+sys.argv[2]
    macKeyPairEnc=macKeyPair.encode()
    macKeyPairSHA3_256=hashlib.sha3_256(macKeyPairEnc)
    multicast_client.sendToServer("REQ "+macKeyPairSHA3_256.hexdigest())
    print("Packet sent")
else:
    print("no args")