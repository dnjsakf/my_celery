import time
import random
 
from dochi_app import app
 
@app.task
def add( num1, num2 ):
    # time.sleep( random.randint(1, 10) )
    time.sleep( 1 )
    
    print( "{} + {} = {}".format( num1, num2, num1+num2 ) )
    
    return num1 + num2
 
@app.task
def callback( results ):
    return sum(results)