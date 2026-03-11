# Device Configurations

## Router (Cisco 2911)

```cisco
enable
configure terminal

hostname HOME-ROUTER

interface GigabitEthernet0/0
 description Home LAN
 ip address 192.168.1.1 255.255.255.0
 no shutdown

! DHCP for wireless/dynamic devices
ip dhcp pool HOME-LAN
 network 192.168.1.0 255.255.255.0
 default-router 192.168.1.1
 dns-server 8.8.8.8

! Exclude static IPs from DHCP
ip dhcp excluded-address 192.168.1.1 192.168.1.99

end
write memory
```

---

## Switch (Cisco 2960)

```cisco
enable
configure terminal
hostname HOME-SWITCH
end
write memory
```
> Switch works with default settings for basic connectivity.

---

## Wireless Access Point

1. Click on **Access Point** → **Config** tab
2. Set **SSID**: `HomeWiFi`
3. Set **Authentication**: WPA2-PSK
4. Set **Password**: `home1234`

---

## Static IP Devices

### Desktop-PC
| Setting | Value |
|---------|-------|
| IP Address | 192.168.1.10 |
| Subnet Mask | 255.255.255.0 |
| Gateway | 192.168.1.1 |
| DNS | 8.8.8.8 |

### Laptop
| Setting | Value |
|---------|-------|
| IP Address | 192.168.1.11 |
| Subnet Mask | 255.255.255.0 |
| Gateway | 192.168.1.1 |
| DNS | 8.8.8.8 |

### Tablet
| Setting | Value |
|---------|-------|
| IP Address | 192.168.1.12 |
| Subnet Mask | 255.255.255.0 |
| Gateway | 192.168.1.1 |
| DNS | 8.8.8.8 |

### Printer
| Setting | Value |
|---------|-------|
| IP Address | 192.168.1.20 |
| Subnet Mask | 255.255.255.0 |
| Gateway | 192.168.1.1 |

### Home-Server
| Setting | Value |
|---------|-------|
| IP Address | 192.168.1.50 |
| Subnet Mask | 255.255.255.0 |
| Gateway | 192.168.1.1 |
| DNS | 8.8.8.8 |

### Smart-TV
| Setting | Value |
|---------|-------|
| IP Address | 192.168.1.30 |
| Subnet Mask | 255.255.255.0 |
| Gateway | 192.168.1.1 |

### Security-Camera
| Setting | Value |
|---------|-------|
| IP Address | 192.168.1.31 |
| Subnet Mask | 255.255.255.0 |
| Gateway | 192.168.1.1 |

---

## DHCP Devices

### Smartphone
1. Click Smartphone → **Config** → **Wireless0**
2. Set SSID: `HomeWiFi`
3. Go to **Desktop** → **IP Configuration**
4. Select **DHCP**
5. Will get IP in range 192.168.1.100-200
