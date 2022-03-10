---
layout: page
title: 2020 OceanHackWeek Projects
permalink: projects_2020.html
---

# OHW 2020 Projects

OceanHackWeek is not just about learning, it is also about using what is learned to create exciting new tools in collaboration with others. We strive to foster an inclusive and supportive learning environment based on the shared interests of all participants, and are proud to share outcome of the hack projects here.

---

### Project: Cloud-based Gap-free SST product

*A lot* of code is written to break down L4 analyses into RAM size pieces to run on local computers.  By starting to create a cloud-based code base, we can demonstrate how using cloud data could accelerate development in this area, and potentially others (ocean color, etc.) Tasks: Get different SST data; write additional filtering; write bias check; get land and sea ice masks, develop different blending (OI, etc.) algorithms, output in GDS2.0 L4.

**GitHub Page**: [https://github.com/oceanhackweek/ohw20-proj-gapfree-sst](https://github.com/oceanhackweek/ohw20-proj-gapfree-sst)<br>
**Presentation**: [video](https://www.youtube.com/watch?v=l5kgf1WfHJE&list=PLA6PlfxWZPLTPQ_OIr3dDPF9FRiHQXoVF&index=5)

### Project: Spatio-temporal Mapping of Argo data

GP regression to interpolate/map Argo profile data following the algorithm from Kuusela and Stein 2018. Optimal space-time interpolation of scattered oceanographic data in python; follows on methods from Kuusela and Stein (2018). Can use existing package to compute likelihood and mapping, focused on any fairly small region (~5-10-degree box) in the part of the global open ocean well-sampled by Argo. Import Argo T or S data from a specific region, fit the data to a mean function via least squares or loess and subtract the result from the data, and estimate autocovariance parameters for the resulting anomaly field via maximum likelihood estimation. Then use those parameters to estimate the anomaly field via "objective mapping". 

**Github Page**: [https://github.com/oceanhackweek/ohw20-proj-argo-mapping](https://github.com/oceanhackweek/ohw20-proj-argo-mapping)<br>
**Presentation**: [video](https://www.youtube.com/watch?v=QXQR03gyV48&list=PLA6PlfxWZPLTPQ_OIr3dDPF9FRiHQXoVF&index=8)

### Project: Visualizing the shelfbreak front in the northern Mid-Atlantic Bight with OOI data

The U.S. Ocean Observatories Initiative (OOI) provides data from moorings deployed in the Pioneer Array on the edge of the Northeast U.S. Shelf (NES) in the northern Mid-Atlantic Bight. Profiler moorings support wire-following profiling packages with a multidisciplinary sensor suite including temperature, conductivity (salinity), pressure (depth) and more. Although it may be straightforward to acquire and plot data from a single profile, or a single profiler over time, it is much more challenging to be able to visualize and analyze data from multiple profiler moorings. The goal of this project will be to develop flexible, scalable tools to assemble, plot, and analyze data from multiple moorings over time.

**Github Page**: [https://github.com/oceanhackweek/ohw20-proj-ooi-profiles-section](https://github.com/oceanhackweek/ohw20-proj-ooi-profiles-section)<br>
**Presentation**: [video](https://www.youtube.com/watch?v=Z3fJMPHRz6U&list=PLA6PlfxWZPLTPQ_OIr3dDPF9FRiHQXoVF&index=3)

### Project: Use the package pyXpcm to identify ocean regions

Building off of Rosso et al., 2020 and previous work ( Maze et al., 2017 and Jones et al., 2019 ), the goal is to construct a toolbox to apply the Profile Classification Model used in that paper and others to identify ocean mixing in a generalized context. Previous papers have focused on two regions, and are possibly hard coded in order to take in the data and run the unsupervised machine learning. We'd like to generalize the framework around the algorithms in order to look at ocean (possibly atmospheric) mixing anywhere in the world.

**Github Page**: [https://github.com/oceanhackweek/ohw20-proj-pyxpcm](https://github.com/oceanhackweek/ohw20-proj-pyxpcm)<br>

### Project: Ship track segmentor

Automatically segment GPS tracks based on sampling behavior patterns, compare data-driven vs rule-based approaches, and explore Geopandas and MovingPandas.

**Github Page**: [https://github.com/oceanhackweek/ohw20-proj-shiptrack](https://github.com/oceanhackweek/ohw20-proj-shiptrack)<br>
**Presentation**: [video](https://www.youtube.com/watch?v=xEQGq0LxzNE&list=PLA6PlfxWZPLTPQ_OIr3dDPF9FRiHQXoVF&index=4)

### Project: Species assemblages in marine protected areas and associated species distribution models

Using OBIS data and species distribution modeling, pull species occurrence data from the OBIS database and answer questions about species distributions.

**Github Page**: [https://github.com/oceanhackweek/ohw20-proj-species-marine-protected-areas](https://github.com/oceanhackweek/ohw20-proj-species-marine-protected-areas)<br>
**Presentation**: [video](https://www.youtube.com/watch?v=QoA3YD_NqwA&list=PLA6PlfxWZPLTPQ_OIr3dDPF9FRiHQXoVF&index=6)


### Project: Marine Heat Wave (MHW) analysis with xarray

This project aimed to apply the MHW definition of Hobday et al. (2016) using the capabilities of xarray and dask. The project was started as an Ocean Hack Week 2020 project with the following objectives: update E. Oliver's Marine Heat Waves (MHW) python code to take advantage of xarray, datetime, and dask, to adapt to use AWS MUR SST data, and to expand to regions (2D) analysis, as well as time series.

**Github Page**: [https://github.com/oceanhackweek/ohw20-proj-marine-heat-waves](https://github.com/oceanhackweek/ohw20-proj-marine-heat-waves)<br>
**Presentation**: [video](https://www.youtube.com/watch?v=za2xzc5XE9M&list=PLA6PlfxWZPLTPQ_OIr3dDPF9FRiHQXoVF&index=2&t=9s)


### Project: Co-locators expansion

Co-locate oceanographic data (served via ERDDAP) by establishing constraints to use as data server query filters. Submit the identical filter criteria to all ERDDAP servers indexed by the awesome-erddap project and visualize the results.

**Github Page**: [https://github.com/ioos/colocate](https://github.com/ioos/colocate)<br>
**Presentation**: [video](https://www.youtube.com/watch?v=2m1pxyRPoW4&list=PLA6PlfxWZPLTPQ_OIr3dDPF9FRiHQXoVF&index=7)
