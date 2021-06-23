#include <fstream>
#include <iostream>
#include <sstream>

using namespace std;

int array[2000][2000]; // used for input image
int arr[2000][2000]; // used for output image
int hist[255];

int main()
{
	int i, row = 0, j = 0, col = 0, numrows = 0, numcols = 0, MAX = 0;
	
	// input image
	ifstream infile("saltpepper.pgm");
	stringstream ss;
	string inputLine = "";

	// First line : version
	getline(infile, inputLine);
	if (inputLine.compare("P2") != 0)
		cerr << "Version error" << endl;
	else
		cout << "Version : " << inputLine << endl;

	// Continue with a stringstream
	ss << infile.rdbuf();
	
	// Secondline : size
	ss >> numcols >> numrows >> MAX;
	
	// print total number of columns,
	// rows and maximum intensity of the image
	cout << numcols << " columns and " << numrows << " rows" << endl
		<< " Maximium Intesity " << MAX << endl;

	// Initialize a new array of
	// same size of the image with 0
	for (row = 0; row <= numrows; ++row)
		array[row][0] = 0;

	for (col = 0; col <= numcols; ++col)
		array[0][col] = 0;

	printf("****\n");
	
	// Following lines : data
	for (row = 1; row <= numrows; ++row) {
		for (col = 1; col <= numcols; ++col) {
			// original data store in new array
			ss >> array[row][col];
		}
	}

	for (row = 1; row <= numrows; ++row) {
		for (col = 1; col <= numcols; ++col) {
			
			// check if intensity is black or white
			if (array[row][col] == 0 || array[row][col] == 255)
			{
				// compute average of neighbours pixels
				// and store the pixel value in another
				// array for output image
				arr[row][col] = (array[row - 1][col] +
								array[row - 1][col - 1] +
								array[row - 1][col + 1] +
								array[row][col - 1] +
								array[row][col + 1] +
								array[row + 1][col + 1] +
								array[row + 1][col] +
								array[row + 1][col - 1]) / 8;
			}
			else {
				// store pixel value in another
				// array for output image
				arr[row][col] = array[row][col];
			}
		}
	}

	ofstream outfile;
	
	// new file open to store the output image
	outfile.open("salt and pepper.pgm");
	outfile << "P2" << endl;
	outfile << numcols << " " << numrows << endl;
	outfile << "255" << endl;

	for (row = 1; row <= numrows; ++row) {
		for (col = 1; col <= numcols; ++col) {
			
			// store resulatant pixel intensity to the output file
			outfile << arr[row][col] << " ";
		}
	}
	
	outfile.close();
	infile.close();
	return 0;
}
