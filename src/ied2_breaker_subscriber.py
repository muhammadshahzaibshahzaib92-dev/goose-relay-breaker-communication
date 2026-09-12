"""
ied2_breaker_subscriber.py
Day 12: Pehla GOOSE Subscriber (Breaker) Script
GOOSE trip messages ko "sunta" hai aur receive hote hi print karta hai.
"""

import pyiec61850 as iec61850
import time

def main():
    interface = "lo"

    receiver = iec61850.GooseReceiver_create()
    iec61850.GooseReceiver_setInterfaceId(receiver, interface)

    # goCbRef match karega jo Day 11 wali publisher script mein set kiya tha.
    # dstMac/appId set nahi kiya, isliye ye filter nahi karega un par.
    subscriber = iec61850.GooseSubscriber_create("IED1LD0/LLN0$GO$gcbTrip", None)

    iec61850.GooseReceiver_addSubscriber(receiver, subscriber)
    iec61850.GooseReceiver_start(receiver)

    if iec61850.GooseReceiver_isRunning(receiver):
        print("[IED-2] Listening for GOOSE trip messages...")

        lastStNum = -1
        try:
            while True:
                if iec61850.GooseSubscriber_isValid(subscriber):
                    stNum = iec61850.GooseSubscriber_getStNum(subscriber)
                    sqNum = iec61850.GooseSubscriber_getSqNum(subscriber)
                    if stNum != lastStNum:
                        lastStNum = stNum
                        print(f"[IED-2] GOOSE received! stNum={stNum} sqNum={sqNum} -> BREAKER TRIPPED")
                time.sleep(0.05)
        except KeyboardInterrupt:
            print("\n[IED-2] Stopping subscriber...")
    else:
        print("Failed to start GOOSE subscriber. Reason: interface na milna ya root permission chahiye.")

    iec61850.GooseReceiver_stop(receiver)
    iec61850.GooseReceiver_destroy(receiver)

if __name__ == "__main__":
    main()
