###### e-Yantra Innovation Challenge 2020-21

# Unmanned Aerial System for flood disaster emergency response and rescue management
<hr>

## Motivation: 

* Flood has been considered as one of the most recurring and frequent disaster in the world. Due to recurrent prevalence, the economic loss and life damage caused by the flood has put more burdens on economy than any other natural disaster. India also has continuously suffered by many flood events which claimed huge loss of life and economy. It has been found that the incidences of the flood are increasing very rapidly. Disaster management in India has very organised and structures programmes and policies but administration and implementation of these programs demand more efficiency. In last decade, flood damages more lives and economy than any other disasters [[1]](). 

* Flood in India has become one of the biggest disaster which has killed thousands of the people in last few years. The recurrence and intensity has amplified over the time which damaged life and economy at a great extent. Government of India has taken up many measures to lessen the damage caused by flood and other disasters, but there is a long way to go [[1]]().
* The objective is to introduce an unmanned aerial system for flood disaster emergency response and rescue management. Using drones, the system will be capable of sending the real time location of the people in flood affected area to rescue system using image processing and GPS system. The system scalable and multiple drones can be deployed in flood affected area for rescue. The system can be further developed into fully functional flood disaster emergency response system that will predict floods and automatically deploys drones for emergency response and rescue management.

<hr>

### Implementation:
1. This system is broadly divided into three parts – a) UAVs System with onboard image processing and GPS. b) Ground Control Base Station System. c) Web interface and rescue management system.
2. System Continuously Check for flood signal from sources such as Government site providing real time water level and flood status in particular region.
3. When there will be flood in region alert message will be send to the system then there will be Autonomous take-off of UAVs from Ground control station base located in nearby areas. 
4. Flood Affected Area is scanned by UAVs. This UAVs are using image processing and GPS to detect and identify the people in flood affected region and send back live location of people to the system server back.
5. This location database is available to rescue team to rescue the people from their respective location.
6. System block diagram is shown in following diagram

![System block diagram](img\systemWithserver.png)



<hr>

### User Interface:
1) There will be [web portal](https://sites.google.com/view/eyantra-team-fury/home) for Rescue Team showing location of humans and number of humans on that particular location.
2) Several other functionalities can be added to this portal such as number of people rescued and remaining people.

![UI](img\ui.png)

#### System Database 

![system database](img\databaseflowRescueXportal.png)

### Visit RescueXportal

* https://sites.google.com/view/eyantra-team-fury/home

<hr>

### Flow Chart

![Flow Chart](img\flow_chart.png)

<hr>

### Feasibility: 
1) In order to automate the entire process of human lives detection for rescue during and after floods and provide a more efficient and optimal solution for emergency response and rescue management, we decided to come up with the idea of drone system having real time human detection using image processing and sending their location to server for emergency response and rescue.
2) Using this system, we will be having advantage of less manpower consumption during disaster for flood disaster emergency response and rescue management.

<hr>

### References:
[1] Prakash Tripathi  “Flood Disaster in India: An Analysis of trend and Preparedness” https://www.researchgate.net/publication/292980782_Flood_Disaster_in_India_An_Analysis_of_trend_and_Preparedness

[2] India Commercial Drone Market (2020-2026): Market Forecast by Types, by Applications, by Regions, and Competitive Landscape
https://www.researchandmarkets.com/reports/5137116/india-commercial-drone-market-2020-2026-market?utm_source=GNOM&utm_medium=PressRelease&utm_code=fbddnc&utm_campaign=1432135+-+The+Indian+Commercial+Drone+Market+is+Projected+to+Grow+at+a+CAGR+of+12.4%25+during+2020-2026&utm_exec=cari18prd




