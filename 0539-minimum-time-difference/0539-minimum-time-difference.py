#Created by: Sebastián Felipe García Rojas

class Solution:
    def findMinDifference(self, timePoints: List[str]) -> int:

        lenArray = len(timePoints)
        minFormat = []
        i = 0
        minimumTimeDif = 24*60
        timeDif = 0

        for timePoint in timePoints:
            #Convertir hora en minutos del día
            # Convert the time point format to integer minutes
            if timePoint == "00:00":
                minFormat.append(1440)
            else:
                minutos = int(timePoint[0:2])*60 + int(timePoint[3:5])
                minFormat.append(minutos)

            #print(minutos)

        #Ordered the array in ascending order
        minFormat.sort()

        while i < lenArray:
            #                a.m       p.m       a.m (+1440)
            #Explanation |---------|---------|---------|
            #                     719       

            if minFormat[i] > 1 and minFormat[i] < 719:
                minFormat.append(minFormat[i]+1440)
                i += 1
            else:
                break

        #for minuto in minFormat:
        #    print(minuto)
        
        listLen = len(minFormat)
        print(listLen)

        i = 0
        while i < (listLen-1):
            if minFormat[i] == minFormat[i + 1]:
                return 0
                # Handle the exception for the time period between 23:59 and 00:00

            else:
                TimeDif = abs(minFormat[i] - minFormat[i+1]) 

                if TimeDif < minimumTimeDif:
                    minimumTimeDif = TimeDif

            i+=1

        return minimumTimeDif