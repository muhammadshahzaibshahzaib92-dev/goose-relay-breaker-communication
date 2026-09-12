import pyiec61850 as iec61850
import time

interface = "lo"

receiver = iec61850.GooseReceiver_create()
iec61850.GooseReceiver_setInterfaceId(receiver, interface)

subscriber = iec61850.GooseSubscriber_create("IED1LD0/LLN0$GO$gcbTrip", None)

iec61850.GooseReceiver_addSubscriber(receiver, subscriber)
iec61850.GooseReceiver_start(receiver)

print("Running:", iec61850.GooseReceiver_isRunning(receiver))
print("[IED-2] Listening for GOOSE trip messages... (DEBUG MODE - prints every 2 sec)")

try:
    count = 0
    while True:
        valid = iec61850.GooseSubscriber_isValid(subscriber)
        stNum = iec61850.GooseSubscriber_getStNum(subscriber)
        sqNum = iec61850.GooseSubscriber_getSqNum(subscriber)
        count += 1
        if count % 40 == 0:  # roughly every 2 seconds
            print(f"[DEBUG] isValid={valid} stNum={stNum} sqNum={sqNum}")
        time.sleep(0.05)
except KeyboardInterrupt:
    print("\nStopping...")

iec61850.GooseReceiver_stop(receiver)
iec61850.GooseReceiver_destroy(receiver)
