#name - name of the exoplanet, 
#light_years_from_earth - This is the distance of this planet from Earth in light years. 1 light year is the distance light can travel in one year, and light it super fast. It can travel 9.461 Trillion km in 1 year.
#planet_mass - Mass of the planet with respect to Earth or Jupiter
#stellar_magnitude - Brightness of the host star of the planet when observed from Earth.
#discovery_date - Year of discovery exoplanet.
#planet_type - Type of the planet, eg. - Gas Giant, Neptune-like.
#planet_radius - Radius of the planet with respect to Earth or Jupiter.
#orbital_radius - This is the average distance of this exo-planet from its sun. Just like our solar system has 1 sun, there are multiple solar systems that contain many planets and sun(s).
#orbital_period - This is the time it takes to complete one orbit of it’s sun.
#eccentricity - This denotes how circular the orbit is. It might be oval in shape too. The lower the eccentricity, the more circular is the orbit.
#pl_hostname - The name of the host solar system.
#pl_letter - The letter given to this planet.
#pl_name - The name of this planet (short version).
#pl_discmethod - This is the discovery method which was used to find this exo-planet.
#pl_controvflag - This is a boolean (0, 1) which says if the existence of this planet is questioned or not. 
# pl_pnum - This is the number of planets that are there in its solar system. 
# pl_orbper - This is again, the orbital period in days.
#pl_orbperlim - This is again the radius of the orbit of the planet.
#pl_orbeccen - This is again the eccentricity of the planet.
#pl_orbincl - This is the orbital inclination, which means that it is the tilt of the exo-planet’s orbit when it revolves around its sun.
#pl_bmassj - This is again the mass of the planet. 
# pl_bmassprov - This is the unit to calculate the mass. 
# pl_radj - This is again, the radius of the planet. 
# pl_dens - This is the density of the planet. 
# pl_ttvflag - This is a flag that indicates if this planet's orbit exhibits any timing variations from other planets in the system. 
# pl_kepflag - This is a flag that tells if the solar system exhibits a planetary system (multiple planets) based on Kepler Field Mission. 
# pl_k2flag - This is a flag that tells if the solar system exhibits a planetary system based on the K2 Mission. 
# pl_nnotes - This is just the number of notes associated with the planet. 
# ra_str - This is the right ascension of the planetary system, which is the east-west coordinate by which the position of this planet is measured. 
# dec_str - This is the north-south coordinate by which the position of the planet is measured. 
# st_dist - This is again the distance of the planet from Earth. 
# gaia_dist - This is again the distance of the planet from Earth in Gaia Parallax. Gaia Parallax is the coordinate that is calculated with Trigonometry. 
# st_optmag - This is the Optical magnitude (discussed earlier). 
# st_optband - There are different bands in light. This is the band of the optical magnitude. 
# gaia_gmag - This is the magnitude of the host star of the planet measured in G-Band. 
# st_teff - This is the temperature of the host star in Kelvin. 
# st_mass - This is the amount of mass contained in the host star. 
# st_rad - This is the radius of the host star.
# rowupdate - This is the date of last update for this exo-planet. 
# pl_facility - Facility at which the planet was discovered (There are many facilities that are observing and looking for new planets/stars in our galaxy).
#temp_planet_date temp_planet_mass pl_letter pl_name pl_controvflag pl_pnum pl_orbper
#  pl_orbpererr1 pl_orbpererr2 pl_orbperlim pl_orbsmax pl_orbsmaxerr1 pl_orbsmaxerr2
#  pl_orbsmaxlim pl_orbeccen pl_orbeccenerr1 pl_orbeccenerr2 pl_orbeccenlim pl_orbinclerr1
#pl_orbinclerr2 pl_orbincllim pl_bmassj pl_bmassjerr1 pl_bmassjerr2 pl_bmassjlim
# pl_bmassprov pl_radj pl_radjerr1 pl_radjerr2 pl_radjlim pl_denserr1 pl_denserr2 
# pl_denslim pl_ttvflag pl_kepflag pl_k2flag pl_nnotes ra dec st_dist st_disterr1 st_disterr2 
# st_distlim gaia_dist gaia_disterr1 gaia_disterr2 gaia_distlim st_optmag st_optmagerr 
# st_optmaglim st_optband gaia_gmag gaia_gmagerr gaia_gmaglim st_tefferr1 st_tefferr2 
# st_tefflim st_masserr1 st_masserr2 st_masslim st_raderr1 st_raderr2
# st_radlim rowupdate pl_facility
import pandas as pd
import csv

df = pd.read_csv("final.csv")

del df["hyperlink"]
del df["temp_planet_date"]
del df["temp_planet_mass"]
del df["pl_letter"]
del df["pl_name"]
del df["pl_controvflag"]
del df["pl_pnum"]
del df["pl_orbper"]
del df["pl_orbpererr1"]
del df["pl_orbpererr2"]
del df["pl_orbperlim"]
del df["pl_orbsmax"]
del df["pl_orbsmaxerr1"]
del df["pl_orbsmaxerr2"]
del df["pl_orbsmaxlim"]
del df["pl_orbeccen"]
del df["pl_orbeccenerr1"]
del df["pl_orbeccenerr2"]
del df["pl_orbeccenlim"]
del df["pl_orbinclerr1"]
del df["pl_orbinclerr2"]
del df["pl_orbincllim"]
del df["pl_bmassj"]
del df["pl_bmassjerr1"]
del df["pl_bmassjerr2"]
del df["pl_bmassjlim"]
del df["pl_bmassprov"]
del df["pl_radj"]
del df["pl_radjerr1"]
del df["pl_radjerr2"]
del df["pl_radjlim"]
del df["pl_denserr1"]
del df["pl_denserr2"]
del df["pl_denslim"]
del df["pl_ttvflag"]
del df["pl_kepflag"]
del df["pl_k2flag"]
del df["pl_nnotes"]
del df["ra"]
del df["dec"]
del df["st_dist"]
del df["st_disterr1"]
del df["st_disterr2"]
del df["st_distlim"]
del df["gaia_dist"]
del df["gaia_disterr1"]
del df["gaia_disterr2"]
del df["gaia_distlim"]
del df["st_optmag"]
del df["st_optmagerr"]
del df["st_optmaglim"]
del df["st_optband"]
del df["gaia_gmag"]
del df["gaia_gmagerr"]
del df["gaia_gmaglim"]
del df["st_tefferr1"]
del df["st_tefferr2"]
del df["st_tefflim"]
del df["st_masserr1"]
del df["st_masserr2"]
del df["st_masslim"]
del df["st_raderr1"]
del df["st_raderr2"]
del df["st_radlim"]
del df["rowupdate"]
del df["pl_facility"]

df = df.rename({'pl_hostname': "solar_system_name",'pl_discmethod': 'planet_discovery_method',
'pl_orbincl': 'planet_orbital_inclanation',
'pl_dens': 'planet_density',
'ra_str': 'right_ascension',
'dec_str': 'declination',
'st_teff': 'host_temperature',
'st_mass': 'host_mass',
'st_rad': 'host_radius'}, axis = 'columns')

df.to_csv("main.csv")

print(list(df))
print(df.shape)
