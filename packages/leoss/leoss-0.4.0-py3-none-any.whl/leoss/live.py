from .main import *
from .visual import *

import socket
from time import sleep


def RunServer(host: str, port: str, settings):
    HOST = ''                      # Symbolic name meaning all available interfaces
    PORT = 51515                   # Arbirtrary non-priviledged port

    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    while True:
        sleep(1);
        print("Looking for Clients...")
        s.bind((HOST, PORT))
        s.listen()
        conn, addr = s.accept()

        print('Connected to CLIENT. HOST: '+str(addr[0])+", PORT: "+str(addr[1]))
        message = 'Python Server Acknowledgement'
        conn.send(message.encode())

        system, spacecraft, recorder, time, timeStep, orbitPropOnly = settings()
        system.orbitPropOnly = orbitPropOnly

        sensors = system[0].getSensors()
        controllers = system[0].getControllers()
        actuators = system[0].getActuators()

        print(system[0].recorder.dataDict)

        simCounter = 0
        prev_simCounter = 0
        simStart = False
        simCheck = 0

        while True:
            data = conn.recv(1024)
            if not data: break

            if simStart == False:
                print("RCV:\t"+str(data))           

            if str(data.decode()) == "Connected to Processing Client":
                simStart = True
            
            if simStart and  str(data.decode()) != "Connected to Processing Client":
                datatoSend = "acknowledge:"+str(data.decode())+"\n"
                simCounter = int(data.decode())

                # print(simCounter)
                if simCounter*timeStep <= time:
                    simMultiple = simCounter - prev_simCounter
                    # print(simMultiple)
                    if system.time == 0:
                        simCheck = simMultiple
                    if simMultiple != simCheck:
                        # print("!!ERROR on data received!! "+str(simMultiple)+", "+str(simCheck)+", "+str(system.time))
                        if simMultiple > 0 and simMultiple <= 64:
                            simCheck = simMultiple
                        simMultiple = 0
                        
                    simTick = 0
                    while simTick < simMultiple:
                        system.advance1timestep(timeStep)
                        simTick = simTick + 1

                    prev_simCounter = simCounter  

                    position = system[0]['State'].position
                    velocity = system[0]['State'].velocity
                    quaternion = system[0]['State'].quaternion
                    bodyrate = system[0]['State'].bodyrate
                    location = system[0]['Location']
                    dateTime = system.datenow()
                    netforce = system[0]['Netforce']
                    nettorque = system[0]['Nettorque']
                    netmoment = system[0]['Netmoment']
                    sunlocation = system[0]['Sunlocation']
                    SpAngMom = system[0]['SpecificAngularMomentum']
                    SpMechEn = system[0]['SpecificMechanicalEnergy']
                    BdAngMom = system[0]['BodyAngularMomentum']

                    sysTime = f'{system.time}'
                    unixTime = int(calendar.timegm(dateTime.utctimetuple()))
                    unixValue = f'{unixTime}'
                    dateValue = dateTime.strftime('%Y, %m, %d, %H, %M, %S, %f')
                    positionValue = f'{position.x:.15f}, {position.y:.15f}, {position.z:.15f}'
                    velocityValue = f'{velocity.x:.15f}, {velocity.y:.15f}, {velocity.z:.15f}'
                    quaternionValue = f'{quaternion.w:.15f}, {quaternion.x:.15f}, {quaternion.y:.15f}, {quaternion.z:.15f}'
                    bodyrateValue = f'{bodyrate.x:.15f}, {bodyrate.y:.15f}, {bodyrate.z:.15f}'
                    locationValue = f'{location.x:.15f}, {location.y:.15f}, {location.z:.15f}'
                    netforceValue = f'{netforce.x:.15f}, {netforce.y:.15f}, {netforce.z:.15f}'
                    nettorqueValue = f'{nettorque.x:.15f}, {nettorque.y:.15f}, {nettorque.z:.15f}'
                    netmomentValue = f'{netmoment.x:.15f}, {netmoment.y:.15f}, {netmoment.z:.15f}'
                    sunlocationValue = f'{sunlocation.x:.15f}, {sunlocation.y:.15f}, {sunlocation.z:.15f}'
                    samValue = f'{SpAngMom:.15f}'   
                    smeValue = f'{SpMechEn:.15f}'
                    bamValue = f'{BdAngMom:.15f}'

                    sep = ", "

                    dataline = \
                        sysTime + sep +  \
                        str(simCounter) + sep + \
                        unixValue + sep + \
                        dateValue + sep +  \
                        positionValue + sep + \
                        velocityValue + sep + \
                        quaternionValue + sep + \
                        bodyrateValue  + sep + \
                        locationValue + sep +\
                        netforceValue + sep + \
                        nettorqueValue + sep + \
                        netmomentValue + sep + \
                        sunlocationValue + sep + \
                        samValue + sep +\
                        smeValue + sep +\
                        bamValue + sep + "EOF"

                    # conn.send(("Time:"+str(system.time)+", Counter:"+str(simCounter)+
                    #         #    ", Value1:"+str(system[0].state.bodyrate.x) +
                    #            ", Value1:"+str(sensors['mtm'].data.x) +
                    #         #    ", Value2:"+str(system[0].state.bodyrate.y) +
                    #         #    ", Value2:"+str(sensors['gyro'].data.x) +
                    #            ", Value2:"+str(sensors['ideal_MTM'].data.x) +
                    #         #    ", Value3:"+str(system[0].state.bodyrate.z) +
                    #            ", Value3:"+str(sensors['gyro'].data.x) +
                    #            ", EOF").encode())
                    
                    conn.send(dataline.encode())
        conn.close()
        print("Client Disconnected..")
        break;


def RunServer2(host: str, port: str, settings):
    HOST = '127.0.0.1'        
    PORT = 55037       

    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    while True:
        sleep(1);
        print("Looking for Processing Client..")
        s.bind((HOST, PORT))
        s.listen(5)
        print("Server listening on {}:{}".format(HOST, PORT))

        conn, addr = s.accept()
        print("Connected to Client: "+str(addr))

        message = 'Python Server Acknowledgement'
        conn.send(message.encode())

        system, spacecraft, recorder, time, timeStep, orbitPropOnly = settings()
        system.orbitPropOnly = orbitPropOnly

        sensors = system[0].getSensors()
        controllers = system[0].getControllers()
        actuators = system[0].getActuators()

        print(system[0].recorder.dataDict.keys())

        recorderObj = system[0].recorder
        recorderKeys = list(system[0].recorder.dataDict.keys())

        channelList = []

        channelList.append("System Time")           #00
        channelList.append("Sim Counter")           #01
        channelList.append("UNIX Time")             #02
        channelList.append("Year")                  #03
        channelList.append("Month")                 #04
        channelList.append("Day")                   #05
        channelList.append("Hour")                  #06
        channelList.append("Minute")                #07
        channelList.append("Second")                #88
        channelList.append("Microsecond")           #09 
        channelList.append("ECI Position X")        #10
        channelList.append("ECI Position Y")        #11
        channelList.append("ECI Position Z")        #12
        channelList.append("ECI Velocity X")        #13
        channelList.append("ECI Velocity Y")        #14
        channelList.append("ECI Velocity Z")        #15
        channelList.append("ECI2Body Quaternion W") #16
        channelList.append("ECI2Body Quaternion X") #17
        channelList.append("ECI2Body Quaternion Y") #18
        channelList.append("ECI2Body Quaternion Z") #19
        channelList.append("Body Angular Rate X")   #20
        channelList.append("Body Angular Rate Y")   #21
        channelList.append("Body Angular Rate Z")   #22 
        channelList.append("RW Speed X")            
        channelList.append("RW Speed Y")
        channelList.append("RW Speed Z")
        channelList.append("Location Latitude")     #23
        channelList.append("Location Longitude")    #24
        channelList.append("Location Altitude")     #25
        channelList.append("Net Force X")           #26
        channelList.append("Net Force Y")           #27
        channelList.append("Net Force Z")           #28
        channelList.append("Net Torque X")          #29
        channelList.append("Net Torque Y")          #30
        channelList.append("Net Torque Z")          #31
        channelList.append("Net Momentum X")        #32
        channelList.append("Net Momentum Y")        #33
        channelList.append("Net Momentum Z")        #34
        channelList.append("ECI Sun Direction X")   #35
        channelList.append("ECI Sun Direction Y")   #36
        channelList.append("ECI Sun Direction Z")   #37
        channelList.append("Specific Angular Momentum")    #38
        channelList.append("Specific Mechanical Energy")   #39
        channelList.append("Body Angular Momentum")         #40

        for i in np.arange(10,len(recorderObj.dataDict)):
            key = recorderKeys[i]
            channelList.append(key+" X")
            channelList.append(key+" Y")
            channelList.append(key+" Z")


        channelList.append("EOF")   # end of frame
        channels = ",".join(channelList)

        # print(channels)

        while True:
            conn.recv(1024)
            message = conn.recv(1024)

            print("Client: "+message.decode())

            if str(message.decode()) == "Waiting for channel list":
                conn.send(channels.encode())       
    
            if str(message.decode()) == "Channel list acknowledged":
                conn.send("Running Simulation..".encode())
                print("Running Simulation..")
                break

        simCounter = 0
        prev_simCounter = 0
        simCheck = 0

        sleep(1)
        while True:

            # try: 
                data = conn.recv(1024)
                if not data: break
                simCounter = int(data.decode())
                # print(simCounter)

                if simCounter*timeStep <= time:
                    simMultiple = simCounter - prev_simCounter
                    # print(simMultiple)
                    if system.time == 0:
                        simCheck = simMultiple
                    if simMultiple != simCheck:
                        # print("!!ERROR on data received!! "+str(simMultiple)+", "+str(simCheck)+", "+str(system.time))
                        if simMultiple > 0 and simMultiple <= 64:
                            simCheck = simMultiple
                        simMultiple = 0
                        
                    simTick = 0
                    while simTick < simMultiple:
                        system.advance1timestep(timeStep)
                        simTick = simTick + 1

                    prev_simCounter = simCounter  

                    position = system[0]['State'].position
                    velocity = system[0]['State'].velocity
                    quaternion = system[0]['State'].quaternion
                    bodyrate = system[0]['State'].bodyrate
                    rwspeed = system[0]['State'].rwspeed
                    location = system[0]['Location']
                    dateTime = system.datenow()
                    netforce = system[0]['Netforce']
                    nettorque = system[0]['Nettorque']
                    netmoment = system[0]['Netmoment']
                    sunlocation = system[0]['Sunlocation']
                    SpAngMom = system[0]['SpecificAngularMomentum']
                    SpMechEn = system[0]['SpecificMechanicalEnergy']
                    BdAngMom = system[0]['BodyAngularMomentum']

                    sysTime = f'{system.time}'
                    unixTime = calendar.timegm(dateTime.utctimetuple())
                    unixValue = f'{str(unixTime)}'
                    dateValue = dateTime.strftime('%Y, %m, %d, %H, %M, %S, %f')
                    positionValue = f'{position.x:.9f}, {position.y:.9f}, {position.z:.9f}'
                    velocityValue = f'{velocity.x:.9f}, {velocity.y:.9f}, {velocity.z:.9f}'
                    quaternionValue = f'{quaternion.w:.9f}, {quaternion.x:.15f}, {quaternion.y:.9f}, {quaternion.z:.9f}'
                    bodyrateValue = f'{bodyrate.x*R2D:.9f}, {bodyrate.y*R2D:.9f}, {bodyrate.z*R2D:.9f}'
                    rwspeedValue = f'{rwspeed.x*R2D/6:.9f}, {rwspeed.y*R2D/6:.9f}, {rwspeed.z*R2D/6:.9f}'
                    locationValue = f'{location.x:.9f}, {location.y:.9f}, {location.z:.9f}'
                    netforceValue = f'{netforce.x:.9f}, {netforce.y:.9f}, {netforce.z:.9f}'
                    nettorqueValue = f'{nettorque.x:.9f}, {nettorque.y:.9f}, {nettorque.z:.9f}'
                    netmomentValue = f'{netmoment.x:.9f}, {netmoment.y:.9f}, {netmoment.z:.9f}'
                    sunlocationValue = f'{sunlocation.x:.9f}, {sunlocation.y:.9f}, {sunlocation.z:.9f}'
                    samValue = f'{SpAngMom:.9f}'   
                    smeValue = f'{SpMechEn:.9f}'
                    bamValue = f'{BdAngMom:.9f}'

                    sep = ", "

                    dataline = \
                        sysTime + sep +  \
                        str(simCounter) + sep + \
                        unixValue + sep + \
                        dateValue + sep +  \
                        positionValue + sep + \
                        velocityValue + sep + \
                        quaternionValue + sep + \
                        bodyrateValue  + sep + \
                        rwspeedValue + sep + \
                        locationValue + sep +\
                        netforceValue + sep + \
                        nettorqueValue + sep + \
                        netmomentValue + sep + \
                        sunlocationValue + sep + \
                        samValue + sep +\
                        smeValue + sep +\
                        bamValue + sep
                    
                    for i in np.arange(10,len(recorderObj.dataDict)):
                        key = recorderKeys[i]
                        if isinstance(system[0][key], Vector):
                            dataline = dataline + f'{system[0][key].x:.9f}' \
                                                + sep + f'{system[0][key].y:.9f}' \
                                                + sep + f'{system[0][key].z:.9f}' + sep
                            

                    dataline = dataline +  "EOF"
                    # print(dataline)

                    conn.send(dataline.encode())

                
            # except Exception as e:
            #     print({e})
            #     break
        if input("export data? (y/n): ") == "y":
            export(recorder['MULA'])

            