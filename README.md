# air-pollution-managment-system
Air Pollution Management System is a Python project that monitors, analyzes, and visualizes air quality data (NO₂, SO₂, RSPM) across Delhi. Built using Pandas and Matplotlib, it offers a menu-driven interface for data analysis, visualization, and easy manipulation of CSV-based datasets.
The Project entitled Air Pollution Management System consists of three built-in
modules as stated above and has been used together. The project monitors and
represents the data of Air pollution and levels of NO2, SO2 and RSPM in various
locations of Delhi as specified in the CSV file. The project also maintains a CSV file
to represent the record of location wise NO2, SO2 and RSPM levels.
The project has one user-defined module which is based on the menu-driven
approach to perform various manipulations on the csv and data.
The Main Menu of the project further has four submenus:
1- Data Visualization Menu which represents the data through line and bar
charts and plots the levels of NO2, SO2 and RSPM at different locations
respectively.
2- Data Manipulation Menu which manipulates the data by either adding or
deleting records or deleting a specific parameter of air in different locations.
3-Data Analysis Menu contains many options which retrieves data like printing top
or bottom records, printing specific or multiple columns or information and
displaying statistics as well as information of the data set.
4-Exit: To exit the System. And terminate the program.
The functions used in the project are described as follows:
1. Menuset():
This function displays the various menu options to the user so that the required
choice can be entered and the functions can be performed accordingly.
2. Display():
This function represents the data visualization menu and graphically displays
data through line chart and bar chart based on the user’s choice. The function
3
allows the user to represent data of SO2 and NO2 of specific location through line
chart and bar chart.
3. Manipulation()
This function displays the various sub-options available in the data manipulation
menu. It allows the user to enter his choice and perform various operations such
as adding area-wise air quality parameters, deleting details of air parameters and
deleting specific air parameters.
4. Analysis()
This function displays the various sub-options available in the data analysis
menu. It allows the user to enter his choice and perform various operations on
the data frame such as displaying specific records from top and bottom,
displaying specific single or multiple columns, displaying station details based
on the high NO2 and low rspm levels. The function also displays complete
statistics and complete information about the dataframe.
5. Bar_chart()
This function reads the data frame and retrieves only location column from it to
perform the required operation. This function displays date-wise SO2 and NO2
readings of a specific location through bar chart.
6. Bar_chart2()
This function reads the data frame and retrieves only location column from it to
perform the required operation. This function displays date-wise rspm readings
of a specific location through bar chart.
7. Line_chart()
4
This function reads the data frame and retrieves only location column from it to
perform the required operation. This function displays date-wise SO2 and NO2
readings of a specific location through line chart.
8. Line_chart2()
This function reads the data frame and retrieves only location column from it to
perform the required operation. This function displays date-wise SO2 and NO2
readings of a specific location through line chart.
9. Exit()
This function allows the user to exit the project once all options have been
successfully executed. 
