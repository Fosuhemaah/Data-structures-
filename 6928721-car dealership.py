#this script shows the brand of cars available and their respective prices
#list of cars under the brand Ford and their respective prices
FordGt=50000
FordExplorer=69000
FordTaurus=75600
FordKuga=95200
FordFlex=47000
FordFiesta=7000
#list of cars under the brand Ford
Ford=(FordGt,FordExplorer,FordTaurus,FordKuga,FordFlex,FordFiesta)
#list of cars under the brand Chevrolet and their respective prices
ChevroletTrax=87300
ChevroletSonic=25460
ChevroletEquinox=58000
ChevroletImpla=78000
Malibu=62000
ChevroletSpark=80000
#list of cars under the brand Chevrolet
Chevrolet=(ChevroletTrax,ChevroletSonic,ChevroletEquinox,ChevroletImpla,Malibu,ChevroletSpark)
#list of cars under the brand Audi with their respective prices
AudiA4=89000
AudiA3=43000
AudiA6=25600
AudiQ3=93000
AudiA8=38000
AudiA1=67000
#list of car under Audi 
Audi=(AudiA4 ,AudiA3, AudiA6, AudiQ3,AudiA8,AudiA1)
#list of cars under the brand Lexus and their respective prices
LexusUX=125000
LexusIS=900000
LexusCT=356000
LexusLC=240000
LexusGS=320000
LexusES=400000
#list of cars under the brand Lexus
Lexus=(LexusUX, LexusIS, LexusCT, LexusLC, LexusGS, LexusES)
#list of cars under the brand Honda and their respective prices
HondaPilot=48000
HondaAccord=24000
HondaCivic=93000
HondaCity=62000
HondaAmaze=71000
HondaClarity=962000
#list of cars under the brand Honda
Honda=(HondaPilot, HondaAccord, HondaCivic, HondaCity, HondaAmaze, HondaClarity)
print('You are welcomed to The Genesis Car Dealership')
CarBrand=(input('Please state the brand of car you want: '))
Ctype=(input('Please state the type of car you want: '))
if CarBrand == 'Ford':
   print('The brand of car stated is part of the available brands we have at our dealership')
elif CarBrand =='Chevrolet':
    print('The brand of car stated is part of the available brands we have at our dealership')
elif CarBrand =='Audi':
    print('The brand of car stated is part of the available brands we have at our dealership')
elif CarBrand =='Lexus':
    print('The brand of car stated is part of the available brands we have at our dealership')
elif CarBrand == 'Honda':
    print('The brand of car stated is part of the available brands we have at our dealership')
else:
    print('Sorry we do not have the car brand specified ')
print('The available brands are; Ford, Chevrolet, Audi, Lexus, Honda')
if Ctype == 'FordGt':
    print('The price of the car is 50000')
elif Ctype== 'FordExplorer':
    print('The price of the car is 69000')
elif Ctype== 'FordTaurus':
    print('The price of the car is 75600')
elif Ctype== 'FordKuga':
    print('The price of the car is 95200')
elif Ctype== 'FordFlex':
    print('The price of the car is 47000')    
elif Ctype== 'FordFiesta':
    print('The price of the car is 7000')    
elif Ctype== 'ChevroletTrax':
    print('The price of the car is 87300')
elif Ctype== 'ChevroletSonic':
      print('The price of the car is 25460')  
elif Ctype== 'ChevroletEquinox':
    print('The price of the car is 58000')    
elif Ctype== 'ChevroletImpla':
    print('The price of the car is 78000') 
elif Ctype== 'Malibu':
    print('The price of the car is 62000')    
elif Ctype== 'ChevroletSpark':
    print('The price of the car is 80000')
elif Ctype== 'AudiA4':
    print('The price of the car is 89000')    
elif Ctype== 'AudiA3':
    print('The price of the car is 43000')    
elif Ctype== 'AudiA6':
    print('The price of the car is 25600')    
elif Ctype== 'AudiQ3':
    print('The price of the car is 93000')    
elif Ctype== 'AudiA8':
    print('The price of the car is 38000')    
elif Ctype== 'AudiA1':
    print('The price of the car is 67000') 
elif Ctype== 'LexusUX':
    print('The price of the car is 125000')    
elif Ctype== 'LexusIS':
    print('The price of the car is 900000')    
elif Ctype== 'LexusCT':
    print('The price of the car is 356000')    
elif Ctype== 'LexusLC':
    print('The price of the car is 240000')    
elif Ctype== 'LexusGS':
    print('The price of the car is 320000')    
elif Ctype== 'LexusES':
    print('The price of the car is 400000') 
elif Ctype== 'HondaPilot':
    print('The price of the car is 48000')    
elif Ctype== 'HondaAccord':
    print('The price of the car is 24000')    
elif Ctype== 'HondaCivic':
    print('The price of the car is 93000')            
elif Ctype== 'HondaCity':
    print('The price of the car is 62000')            
elif Ctype== 'HondaAmaze':
    print('The price of the car is 71000')            
elif Ctype== 'HondaClarity':
    print('The price of the car is 962000')            
#https://github.com/Fosuhemaah                      