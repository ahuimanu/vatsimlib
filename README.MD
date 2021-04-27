# VATSIMLIB

The VATSIMLIB library consumes VATSIM REST services and will store fetched records in a data backend. VATSIM exposes a number of data services via REST APIs.  Many of these have been updated in 2021.  

## VATSIM Services

Here are some of the services:

* [V3 Data Server JSON Feed](https://api.vatsim.dev/)
* [VATSIM API](https://api.vatsim.net/api/) - requires key

This library initially focuses on the data feed as metar and pilot lookups are provided within that API.

## Principal Components

The library consists of a reader, writer, and model component.

### Reader

Reader uses the requests library to obtain the JSON data from the VATSIM API.  The reader will translate this into a number of formats for the Writer.  The reader will call upon the Model component to utilize structured dataclass types.
