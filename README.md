### Simulation Class Work 
------------

#### User Guide
-------

##### To configure
-------
* For https
	`git clone https://github.com/brijeshshah8174/pucsd2020-pp.git`
* For ssh
	`git clone git@github.com:brijeshshah8174/Simulation.git`

* After sucess of above instruction new folder named `Simulation` created.

* cd Simulation

##### How to run
----------
* In Order to plot scatter and histogram graph
	* `python my_plotter.py <filename> <interval>`
* In Order to Perform Chi Square Test
	* `python main.py`
		`Note : This program will prompt message to get file name and interval`

-------------------

#### Developer Guide
------------

* calulation.py
	* maxc :: [Integer] -> Integer
		* This function will find maximum from a list.
	* minc ::[Integer ]-> Integer
		* This function will find minimum from a list
 	* frequency_calc :: ([Integer]-> Integer) -> ([Integer],[Integer])
		* This function will take data and interval to return list of class and their frequency.
	* 

* reader.py
	* read_csv :: String filename -> [Float]
	* read_text :: String filename -> [Float]
	* print_tab :: Dist -> IO

* my_plotter.py
	* scatter
	* histogram

* data_set
	* `This folder contains all data set files.




###### Author
------------ 
* Name : Brijesh Shah
* Profession : Student

