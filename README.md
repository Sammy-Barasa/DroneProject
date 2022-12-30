# DroneProject

### Drone Project API Backend for flight scheduling, user management service and flight data analyzer service


### System Block diagram
Consists of the transmitter module, communication module, receiver module and the web service (API and Interface) 

- **transmitter module** - Captures drone data (raw, pitch, yaw, latitude, longitude, height above ground) and sends to receiver for sending to the internet and web service.

- **communication module** - Long range communication module was used as drones can be upto 30km away from the receiving module and still send their data to the web service.

- **receiver module** - Long range receiver module equipped with capability to connect to the internet. Sends drone data to the web service for data analysis and visualization.

- **Web Service** - consists of an API and Web interface. API for data analysis and web interface for visualization.

![blockdiagram](/blockdiangram.png)

### System Flow Chart

![flow chart](/flowchart_ppt3.png)
