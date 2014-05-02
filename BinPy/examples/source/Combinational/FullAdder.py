from __future__ import print_function
from BinPy.Combinational.combinational import *
""" Examples for FullAdder class """
print ("\n---Initializing the FullAdder class--- ")
print ("\n---Input is of the form [Bit1, Bit2, Carry]")
print ("fa = FullAdder(0, 1, 0)")
fa = FullAdder(0, 1, 0)
print ("\n---Output of FullAdder")
print ("fa.output()")
print (fa.output())
print("Output is of the form [SUM, CARRY]")
print ("\n---Input changes---")
print ("fa.setInput(1, 0) #Input at index 1 is changed to 0")
fa.setInput(1, 0)
print ("\n---New Output of the FullAdder---")
print (fa.output())
print ("\n---Changing the number of inputs---")
print ("No need to set the number, just change the inputs")
print ("Input length must be three")
print ("fa.setInputs(1, 0, 1)")
fa.setInputs(1, 0, 1)
print ("\n---To get the input states---")
print ("fa.getInputStates()")
print (fa.getInputStates())
print ("\n---New output of FullAdder---")
print (fa.output())
print ("\n\n---Using Connectors as the input lines---")
print ("Take a Connector")
print ("conn = Connector()")
conn = Connector()
print ("\n---Set Output of Full Adder to Connector conn---")
print ("fa.setOutput(0, conn) # sets the conn at index 0 ")
fa.setOutput(0, conn)
print ("\n---Put this connector as the input to gate1---")
print ("gate1 = AND(conn, 0)")
gate1 = AND(conn, 0)
print ("\n---Output of the gate1---")
print ("gate1.output()")
print (gate1.output())
print ("Information about fa instance can be found by")
print ("fa")
print (fa)