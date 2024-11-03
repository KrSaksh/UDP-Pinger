# UDP Pinger and Heartbeat Application

This project is a Python-based UDP Pinger and Heartbeat application developed for a computer networks assignment. It demonstrates fundamental socket programming concepts, packet loss simulation, and network diagnostics.

## Overview

The application simulates a simplified version of a standard `ping` tool, using UDP instead of ICMP for packet transmission between a client and server. The project is divided into two parts:

1. **UDP Pinger**: Calculates Round-Trip Time (RTT) for packets, simulates packet loss, and reports packet loss rates.
2. **UDP Heartbeat**: Checks server responsiveness by monitoring the server’s heartbeat signal and handles simulated packet loss to assess network reliability.

## Features

- **Client-Server Communication**: Utilizes UDP sockets for sending and receiving data.
- **RTT Calculation**: Measures and prints the round-trip time for each packet.
- **Packet Loss Simulation**: Randomly simulates packet loss to observe the effects on network communication.
- **Heartbeat Monitoring**: Tracks server responsiveness based on regular heartbeat signals.

## Requirements

- Python 3.x

## How to Run

1. Start the server by running `UDPPingerServer.py` and `UDPPingerServer_Part2.py`.
2. Run the client using the `UDPPingerClient_Part1.py` and `UDPPingerClient_Part2.py` to send packets and monitor RTT and packet loss.

## Usage

The client sends 10 pings to the server and waits up to one second for a response. It reports:
- Individual RTT for each packet.
- Minimum, maximum, and average RTT after all pings.
- Packet loss rate.

In **Heartbeat mode**, the client checks for server availability by sending periodic heartbeat packets. The client assumes the server is down if responses are missing for three consecutive attempts.

## Output Example

- **Ping Mode**: Displays RTT for each packet, timeout messages, and packet loss rate.
- **Heartbeat Mode**: Shows time difference for received heartbeats or missing responses.

## Notes

- This application was designed to help understand socket programming basics, packet loss effects, and network reliability checks using UDP.
