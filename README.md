# GOOSE Relay-Breaker Communication

Publisher-subscriber IEDs exchanging IEC 61850 GOOSE trip signals over the network, using `libiec61850` Python bindings.

## What it does

- `ied1_relay_publisher.py` - Publishes GOOSE trip messages (simulates a protection relay).
- `ied2_breaker_subscriber.py` - Subscribes to and prints GOOSE trip messages the moment they arrive (simulates a breaker).

Both scripts run independently and communicate over the network using multicast GOOSE frames - no shared state, no direct connection between them.

## How it works

The publisher constructs a GOOSE dataset and publishes it under a defined GoCbRef (`IED1LD0/LLN0$GO$gcbTrip`). The subscriber listens for messages matching the same reference and polls the message's StNum/SqNum fields to detect new trip events, printing the trip status the moment a new state is observed.

## Requirements

- Python 3.10+
- `libiec61850` with Python bindings (`pyiec61850`) - built from source, see the main [IEC 61850 Substation Automation](https://github.com/muhammadshahzaibshahzaib92-dev/iec61850-substation-automation) repo for build steps
- Root/sudo privileges (required for raw GOOSE socket access)

## Usage

Run the subscriber first, then the publisher, in two separate terminals:

    cd src
    sudo python3 ied2_breaker_subscriber.py

    # in a second terminal
    sudo python3 ied1_relay_publisher.py

## Tools

libiec61850, Python
