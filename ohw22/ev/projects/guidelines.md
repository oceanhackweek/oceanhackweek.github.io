<!-- 
++++++++++++++++++++++++++++++++++++++++++++++++++++
NOT USING THIS PAGE FOR OHW2020, CONSIDER REVIVING FOR LATER IN-PERSON EVENT. 
++++++++++++++++++++++++++++++++++++++++++++++++++++
-->



# Project Guidelines

## Project Template
Each project requires a brief project summary in the README.md of each GitHub project folder. Below is a template for the project summary.

### Project title

Brief title describing the proposed work.

### Collaborators on this project

List all participants on the project.

### The problem

What oceanographic data science problem are you going to explore? Try to focus on the data science/methodology problem first, followed by the location-specific oceanographic example afterwards. The project is likely more engaging for fellow hackers if it is centered around common data science problems. For example, the project could be to develop a workflow in Python to analyze CTD time series from multiple data sources, instead of emphasizing and focusing only on temperature variations in one very specific part of the ocean.

### Application example

Here is where you follow up with a location-specific example of where the data science methodology applies and list example datasets (size, format, how to access) that could be used for this exploration.

### Specific tasks

List the specific tasks you want to accomplish.

### Existing methods

How would you or others traditionally try to address this problem?

### Proposed methods/tools

Building from what you learn at Oceanhackweek, what new approaches would you like to try to implement?

### Background reading

Optional: links to manuscripts or technical documents for more in-depth analysis.



## Project Ideas
* Developing tutorials for using NASA data on the cloud.
* Working on an efficient open source matchup tutorial for satellite orbital data and in situ point or trajectory data.
* Developing an OSS algorithm development toolbox in Python to deal with a 400GB AMSR brightness temperature - in situ matchup database.
* [Argovis - a visualualization and API for accessing Argo data](https://argovis.colorado.edu/ng/home)
* [OHW18 Projects](https://oceanhackweek.github.io/projects.html)



## Project Data Storage

If your group needs to store data for project use during Oceanhackweek, depending on the volume, below is what we recommend:
- Whenever possible, public datasets like OOI, ARGO, satellite, etc. should be accessed remotely in the Jupyter notebook through standard protocols like OPeNDAP or other programmatic approaches.
- **Data that are <1 MB**: can be included directly in the project Github repository.
- **Data that are <10 GB**: can be stored in your home space on ocean.pangeo.io. When you are accessing data from the internet, it is often useful to have a cell in the notebook that downloads such data into your home space if those data are not there, otherwise do nothing if they are already there. You can also upload a local dataset through the pangeo interface. You can upload only one file as of now, so if you have multiple files you will need to zip them and unzip them later from the terminal. These are two ways to fetch and store larger datasets locally if they are not enormous. 
- **Data that are >10 GB**: are best stored in a cloud-optimized format. If you don't already have the data on the cloud, please talk to the instructors about your needs and how you anticipate using the data. We can help you prepare and upload the data to [cloud object storage](https://en.wikipedia.org/wiki/Cloud_storage) with Oceanhackweek support.
- Questions? Feel free post on Slack #project channel or email [oceanhkw@uw.edu](mailto:oceanhkw@uw.edu).
