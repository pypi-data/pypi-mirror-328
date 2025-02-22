#  pip  install  mccache

import  os
import  mccache
from    datetime  import  UTC
from    datetime  import  datetime  as  dt
from    pprint    import  pprint    as  pp


# Get a demo cache.
c = mccache.get_cache( 'demo' )
print( dict(c) )


# Insert a cache entry
k = os.environ.get( 'KEY1' ,'k1' )
c[ k ] = dt.now( UTC )
print(f"Inserted on {c[ k ]}")


# Update a cache entry
c[ k ] = dt.now( UTC )
print(f"Updated  on {c[ k ]}")
print(f"Metadata for key '{k}' is {c.metadata[ k ]}")


# Insert 2nd cache entry
k = os.environ.get( 'KEY1' ,'k2' )
c[ k ] = dt.now( UTC )
print(f"Inserted on {c[ k ]}")


# Insert 3rd cache entry
k = os.environ.get( 'KEY1' ,'k3' )
c[ k ] = dt.now( UTC )
print(f"Inserted on {c[ k ]}")


#
pp( mccache.get_local_metrics( 'demo' ))
