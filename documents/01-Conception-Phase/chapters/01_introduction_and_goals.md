# Introduction and Goals

This document outlines the architecture and design of HoppyBrew, a web-based application for managing brewing recipes and brews. The application is designed to be user-friendly and intuitive, with a clean and modern user interface. The application is also designed to be compatible with a wide range of devices and browsers, and to integrate with other brewing tools and services, such as `iSpindel`.

Note\! The terminology `brew` and `batch` are used interchangeably in this document to refer to the same thing, i.e. a single brewing process.

## Quality Goals

The top three quality goals for the architecture and design whose fulfillment is of highest importance to the major stakeholders of HoppyBrew have been identified as follows:

| **Priority**  | **Quality Goal** |
| -             | ------- |
| **1**         | **Usability:** The application should be easy to use and intuitive, with a clean and modern user interface. |
| **2**         | **Compatibility:** The application should be compatible with a wide range of devices and browsers. (mobile, desktop, tablet) |
| **3**         | **Integration:** The application should integrate with other brewing tools and services, such as `iSpindel`. |

The motivation behind these goals are to ensure that the application lives up to the expectations of the most important stakeholders, since they are the ones who will be the ones who influence the fundamental architecture and design decisions.

## Stakeholders

The following table lists all the stakeholders of HoppyBrew, along with their roles, contact information, and expectations. It is important to note that these stakeholders are the primary sources of requirements and constraints for the architecture and design of HoppyBrew.

| **Role/Name**             | **Contact Information** | **expectations**                                                                            |
| ------------------------- | ----------------------- | ------------------------------------------------------------------------------------------- |
| **Primary Stakeholder**   | Brewing Enthusiast      | Wants a user-friendly and intuitive application for managing brewing recipes and brew logs. |
| **Secondary Stakeholder** | Developer/Contributor   | Wants a high-quality, open-source application that is easy to maintain and extend.          |

## Requirements Overview

HoppyBrew is driven by the following essential features and functional requirements:

![UseCases](../images/Use-Case-Diagram-HoppyBrew.png)

![sds](/home/asbjorn/Nextcloud/repo/iu-project-software-engineering/documents/01-Conception-Phase/images/Use-Case-Diagram-HoppyBrew.png)

| **Id** | **Requirement**                                    | **Explanation**                                                                       |
| ------ | -------------------------------------------------- | ------------------------------------------------------------------------------------- |
| **F1** | **Manage and create brewing recipes**              | The application should allow users to manage and create brewing recipes.              |
| **F2** | **Manage and create brews and log their progress** | The application should allow users to manage and create brews and log their progress. |


And here is the file

![vignettes/test.png](../images/test.png)
