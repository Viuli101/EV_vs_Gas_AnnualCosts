# -*- coding: utf-8 -*-
"""
Created on Fri Oct 18 17:06:11 2024
@author: vilde

Arbeidskrav 1 - Universitet i Sørøst-Norge.

Årlig totalkostnad for bensinbil vs. elektrisk bil.
"""
#Følgende variabler defineres:
    
D = 16000 #årlig kjøredistanse i km for både bensinbil og elbil
T = 365 #tid (dager)

Forsikring_el = 5000 # forsikring elbil (kr/år)
Forsikring_bensin = 7500 # forskring bensinbil (kr/år)

Forsikring_trafikk = 8.38 #trafikkforsikringsavgit for begge typer biler (kr/dag)

energi_el = 0.2 # energibruk for elbil per km (kWh/km) 
energi_el_pris = 2.0 #strømpris i enhet kr/kWh
energi_bensin = 1.0 #drivstoffbruk for bensinbil (kr/km)

Bom_el = 0.1 #Bomavgift elbil (kr/km)
Bom_bensin = 0.3 #Bomavgift bensinbil (kr/km)

#Det antas i tillegg at renter på billån og verditap er lik for begge typer biler"

total_C_el = Forsikring_el + (Forsikring_trafikk*T) + (energi_el*energi_el_pris*D) + (Bom_el*D) #Totale årlige kostnader for elektrisk bil.
total_C_bensin = Forsikring_bensin + (Forsikring_trafikk*T) + (energi_bensin*D) + (Bom_bensin*D) #Totale årlige kostnader for bensinbil.
 
if total_C_el > total_C_bensin:  #betingelse
    print(f"Total årlig kostnad for elektrisk bil er {total_C_el:.2f} kr, \n" 
          f"og total årlig kostnad for bensinbil er {total_C_bensin:.2f} kr.)\n"
          f"Det er derfor {total_C_el - total_C_bensin:.2f} kr dyrere å bruke elektrisk bil fremfor bensinbil.")    
    #Dersom årlige kostnader for elektrisk bil er høyere enn årlige kostnader for bensinbil, printes teksten ovenfor. 
    #Dersom betingelsen er usann, vil programmet undersøke neste betingelse 
    
elif total_C_bensin > total_C_el: #betingelse
    print(f"Total årlig kostnad for bensinbil er {total_C_bensin:.2f} kr, \n"
          f"og total årlig kostnad for elektrisk bil er {total_C_el:.2f} kr.\n"
          f"Det er derfor {total_C_bensin - total_C_el:.2f} kr dyrere å bruke bensinbil fremfor elbil.")
    #Dersom årlige kostnader for bensinbil er høyere enn årlige kostnader for elektrisk bil, printes teksten ovenfor. 
    #Dersom begge betingelsene ovenfor er usanne, printes teksten nedenfor.  
    
else:
    print(f"Total årlig kostnad for bensinbil er {total_C_bensin:.2f} kr, \n"
          f"og total årlig kostnad for elektrisk bil er {total_C_el:.2f} kr.\n"
          f"Årlige kostnader for bensinbil og elektrisk bil er de samme.")      #(Haugen&Lysaker,2023,s.208)

#Kilder: 
   #Haugen, F. A., & Lysaker, M. (2023). Python for realfag (3. utg.). Fagbokforlaget.  
     


