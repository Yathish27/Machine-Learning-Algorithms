# -*- coding: utf-8 -*-
"""
Created on Fri Mar 15 20:53:14 2019

@author: YATHISH N V
"""

from qiskit import IBMQ
from qiskit import QuantumRegister,ClassicalRegister,QuantumCircuit
first=input("Enter first binary number")
second=input("Enter second binary number")
l1=len(first)
l2=len(second)
num_bits=max(l1,l2)
creg=ClassicalRegister(num_bits)
qreg=QuantumRegister(num_bits)
circ=QuantumCircuit(creg,qreg)
a=QuantumRegister(num_bits)
b=QuantumRegister(num_bits+1)
c=QuantumRegister(num_bits)
d=QuantumRegister(num_bits+1)
cl=QuantumCircuit(a,b,c,d)
for i in range(l):
    if first[i]=='1':
        qc.x(a[l1-])
        


