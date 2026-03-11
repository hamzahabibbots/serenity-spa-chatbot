# Home LAN Network Design - Cisco Packet Tracer

## Network Topology

```
                    ┌─────────────┐
                    │   ROUTER    │
                    │ (Cisco 2911)│
                    │ 192.168.1.1 │
                    └──────┬──────┘
                           │
                    ┌──────▼──────┐
                    │   SWITCH    │
                    │(Cisco 2960) │
                    └──────┬──────┘
                           │
    ┌──────┬──────┬────────┼────────┬──────┬──────┐
    │      │      │        │        │      │      │
  [PC]  [Laptop] [Printer] [Server] [TV] [Camera] [AP]
```

---

## IP Addressing Scheme

| Device | Type | IP Address | Subnet Mask | Gateway |
|--------|------|-----------|-------------|---------|
| Router | Gateway | 192.168.1.1 | 255.255.255.0 | - |
| Desktop-PC | PC | 192.168.1.10 | 255.255.255.0 | 192.168.1.1 |
| Laptop | Laptop | 192.168.1.11 | 255.255.255.0 | 192.168.1.1 |
| Tablet | Tablet | 192.168.1.12 | 255.255.255.0 | 192.168.1.1 |
| Printer | Printer | 192.168.1.20 | 255.255.255.0 | 192.168.1.1 |
| Home-Server | Server | 192.168.1.50 | 255.255.255.0 | 192.168.1.1 |
| Smart-TV | IoT | 192.168.1.30 | 255.255.255.0 | 192.168.1.1 |
| Security-Camera | IoT | 192.168.1.31 | 255.255.255.0 | 192.168.1.1 |
| Smartphone | Wireless | DHCP | - | 192.168.1.1 |

**Network:** 192.168.1.0/24  
**DHCP Range:** 192.168.1.100 - 192.168.1.200

---

## Device Inventory

| Category | Device | Model in Packet Tracer |
|----------|--------|------------------------|
| Infrastructure | Router | 2911 |
| Infrastructure | Switch | 2960-24TT |
| Infrastructure | Wireless AP | AccessPoint-PT |
| Computing | Desktop PC | PC-PT |
| Computing | Laptop | Laptop-PT |
| Computing | Tablet | Tablet-PC |
| Computing | Server | Server-PT |
| Peripheral | Printer | Printer-PT |
| IoT | Smart TV | End Devices → Home → TV |
| IoT | Security Camera | End Devices → Home → Webcam |
| Mobile | Smartphone | Smartphone-PT |

**Total: 11 devices**

---

## Cable Connections

| From | Port | To | Port | Cable |
|------|------|----|------|-------|
| Router | G0/0 | Switch | Fa0/1 | Straight |
| Switch | Fa0/2 | Desktop-PC | Fa0 | Straight |
| Switch | Fa0/3 | Laptop | Fa0 | Straight |
| Switch | Fa0/4 | Tablet | Fa0 | Straight |
| Switch | Fa0/5 | Printer | Fa0 | Straight |
| Switch | Fa0/6 | Home-Server | Fa0 | Straight |
| Switch | Fa0/7 | Smart-TV | Fa0 | Straight |
| Switch | Fa0/8 | Security-Camera | Fa0 | Straight |
| Switch | Fa0/9 | Wireless AP | Port0 | Straight |
| Wireless AP | Wireless | Smartphone | Wireless | WiFi |
