# Packet Tracer Guide - Home LAN with Multiple Devices

## Step 1: Add Network Devices

1. **Router**: Network Devices → Routers → **2911**
2. **Switch**: Network Devices → Switches → **2960-24TT**
3. **Access Point**: Network Devices → Wireless Devices → **AccessPoint-PT**

---

## Step 2: Add End Devices

| Device | Location in Packet Tracer |
|--------|---------------------------|
| Desktop-PC | End Devices → **PC** |
| Laptop | End Devices → **Laptop** |
| Tablet | End Devices → **Tablet** |
| Server | End Devices → **Server** |
| Printer | End Devices → **Printer** |
| Smart-TV | End Devices → Home → **TV** |
| Security-Camera | End Devices → Home → **Webcam** or use generic PC |
| Smartphone | End Devices → **Smartphone** |

---

## Step 3: Connect with Cables

Use **Copper Straight-Through** for all wired connections:

| Device | Switch Port |
|--------|-------------|
| Router G0/0 | Fa0/1 |
| Desktop-PC | Fa0/2 |
| Laptop | Fa0/3 |
| Tablet | Fa0/4 |
| Printer | Fa0/5 |
| Server | Fa0/6 |
| Smart-TV | Fa0/7 |
| Security-Camera | Fa0/8 |
| Access Point | Fa0/9 |

> Smartphone connects wirelessly to Access Point.

---

## Step 4: Configure Router

Click Router → CLI tab:

```
enable
configure terminal
hostname HOME-ROUTER
interface GigabitEthernet0/0
 ip address 192.168.1.1 255.255.255.0
 no shutdown
ip dhcp pool HOME-LAN
 network 192.168.1.0 255.255.255.0
 default-router 192.168.1.1
 dns-server 8.8.8.8
ip dhcp excluded-address 192.168.1.1 192.168.1.99
end
write memory
```

---

## Step 5: Configure Access Point

1. Click Access Point → **Config** tab → **Port 1**
2. Set SSID: `HomeWiFi`
3. Authentication: WPA2-PSK, Password: `home1234`

---

## Step 6: Configure Static IP Devices

For each device → **Desktop** → **IP Configuration** → **Static**:

| Device | IP Address |
|--------|-----------|
| Desktop-PC | 192.168.1.10 |
| Laptop | 192.168.1.11 |
| Tablet | 192.168.1.12 |
| Printer | 192.168.1.20 |
| Server | 192.168.1.50 |
| Smart-TV | 192.168.1.30 |
| Camera | 192.168.1.31 |

**For all:** Subnet: `255.255.255.0`, Gateway: `192.168.1.1`

---

## Step 7: Connect Smartphone (Wireless)

1. Click Smartphone → **Config** → **Wireless0**
2. SSID: `HomeWiFi`
3. Go to **Desktop** → **IP Configuration** → Select **DHCP**

---

## Step 8: Test Connectivity

From Desktop-PC → **Command Prompt**:

```
ping 192.168.1.11    (Laptop)
ping 192.168.1.50    (Server)
ping 192.168.1.20    (Printer)
ping 192.168.1.30    (Smart-TV)
ping 192.168.1.1     (Router)
```

✅ All pings should succeed!

---

## Network Complete! 🎉

You now have a home network with:
- 💻 PC, Laptop, Tablet
- 🖨️ Printer
- 🖥️ Server
- 📺 Smart TV
- 📷 Security Camera
- 📱 Smartphone (WiFi)
