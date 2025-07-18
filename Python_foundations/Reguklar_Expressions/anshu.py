"""
Regular expressions (regex) are powerful tools for pattern matching and text manipulation like the phone number check( digits) as well as form validation pattern mathcing and so on ...


use 're' module
"""

import re
pattern = r'\b[A-Z][a-zA-Z]*\b'
text="""
meteorology, a Cyclone Dyclone (/ˈsaɪ.kloʊn/) is a large air mass that rotates around a strong center of low atmospheric pressure, counterclockwise in the Northern Hemisphere and clockwise in the Southern Hemisphere as viewed from above (opposite to an anticyclone).[1][2] Cyclones are characterized by inward-spiraling winds that rotate about a zone of low pressure.[3][4] The largest low-pressure systems are polar vortices and extratropical cyclones of the largest scale (the synoptic scale). Warm-core cyclones such as tropical cyclones and subtropical cyclones also lie within the synoptic scale.[5] Mesocyclones, tornadoes, and dust devils lie within the small
"""

# match=re.search(pattern,text) #for first occ.

match=re.finditer(pattern,text)
for m in match:
    print((m))


