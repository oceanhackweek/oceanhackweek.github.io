## Target Audience
Please specify the target audience for this tutorial. What does the audience need to know to be able to benefit from your tutorial? Can you eliminate unnecessary prerequisites? 

OceanHackWeek participants come from diverse technical backgrounds: while some may have basic scripting experience, others may have built complex applications within their domain, and still may be completely unfamiliar with libraries used in an adjacent domain.

## Learning Objectives
Please provide a few measurable learning objectives for your tutorial: those should be short statements of what participants will be able to do immediately after the tutorial. Consider learning objectives of varying complexity: some expect participants to be able to execute simple tasks, while others expect them to be able to develop new approaches to address a problem. You can use the [Bloom’s Taxonomy categorization](https://www.unmc.edu/facdev/_documents/teaching-docs/bloom-taxonomy.pdf) to structure your objectives. 

**Example:**

*After the lesson the learners will be able to*
* *Outline elements of ML pipelines*
* *List major differences between types of ML methods, and steps to proceed to evaluate their performance*
* *Identify contexts where deep learning can be useful*
* *Organize labeled datasets in a format expected by ML libraries*

Think about the balance of how your tutorial can be helpful to participants during the hackweek vs. afterwards throughout their careers.

## General Tips
Think of ways to engage the audience during the tutorial. That can also set the right tone of how much detail you need to provide. Remember the more experienced participants may be the more vocal ones so think of ways to hear from everybody without making them feel uncomfortable for not knowing a concept. Anonymous polls can be useful (such as [particifi](https://particify.de/en/)). 

Although the content of your tutorial may not seem a lot when presented as stand-alone, the participants are going through a sequence of tutorials during the week, and are also learning a lot of new things for their projects. 

* If using notebooks/code, be explicit whether you expect people to follow along running the cells/changing code on the fly, or they can just follow your demo, and dive into the notebook later.
* Scrolling through notebooks/code can become pretty confusing, so consider having sections in the notebook and hiding the code cells, only to reveal it when talking about a specific section
* Add a few key points after a section
* If there are steps for which participants need to navigate to specific places on a website, consider saving snapshots and circling the places they need to click to avoid them missing crucial steps after which they cannot navigate the lesson; pause to make sure people are at the right place
* Look through the tutorial and see what jargon/acronyms you are using:
  * Remove the ones not crucial for the tutorial
  * Spell out the ones that the participants need to know
  * If some are not important, be explicit that they are not important right now, and they are just there for future reference
 
## Tips for Use Case/Workflow Presentations

* While preparing your presentation, identify which of its components generalize outside of the use case; state those explicitly to help listeners focus on what can be relevant to them
* Share lessons learned: what worked well, what did not
* Did you have to pivot the project?

## Technical Setup

Oceanhackweek usualy provides a JupyterHub environment within which participants can run any interactive tutorials. As an instructor you will have to ensure that your tutorial can run within the environment. For that you will need to:
* provide your github username to the organizing team so that you get added to JupyterHub
* familiarize yourself with the JupyterHub environment ([JupyterHub Intro](https://github.com/valentina-s/oceanhackweek.github.io/blob/instructor-guide/resources/prep/jupyterhub.md))
* Identify which packages (and corresponding versions) you will need for the tutorial and provide them to the organizing team so that they are included into an image for building the JupyterHub (those can be PyPi, `conda`/`conda-forge`, R)
* Contribute your tutorial content to the corresponding OHWYY branch in [https://github.com/oceanhackweek/ohw-tutorials/](https://github.com/oceanhackweek/ohw-tutorials/)
* Ensure participants have access to the datasets used in the tutorial
  * If there is need to store some datasets on JupyterHub, let us know!
  * Make sure the datasets are reduced to a reasonable size to demonstrate the point, but not make the tutorial cumbersome to run
  * If the tutorial requires executing many expensive queries to a server, please, consider storing a local copy for the demonstration


