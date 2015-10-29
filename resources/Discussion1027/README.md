# Discussion 10/27/2015
with Rahul Bhalerao

## Thoughs
Build a logical relation between SDN controller, Hadoop controller and nodes (mapper and reducer);

Come up with how SDN really works. For example, in FlowComb`the controller dynamically minotors the bandwidth of nodes and paths. In general, when detecting some limitation putting off the data flow, the SDN controller sends messages to Hadoop controller and guide it to reschedule jobs to other mappers and reducers (Fat tree and other network structure may help when considering about rescheduling jobs to take full use of the network). 

## Todo

1. Build Hadoop system on some OVS (like Mininet).
2. Implement FlowComb or other strategy as the SDN controller part.
