char *GetErrorString( int x )
{
	char errorString[20];
	/*
	*	This way of assigning errorString will not work in C. The compiler will
	*   tell you that arrays are not assignable. To set the value of a string
	*	you can make a call to the function strcopy(variable, string) to assign
	*	a string value to errorString.
	*/
	switch ( x )
	{
		case 0:
			errorString = "Success -- No error.";
			break;
		case 2:
			errorString = "Overflow!";
			break;
	}

	errorString[19] = 0;

	/*
	*	This is not really useful, because you are returning the address of 
	*	stack memory associated with errorStirng. Since the life-cycle of the 
	* 	errorString is scoped to this function, we are not guaranteed to find 
	*	something useful in the stack address returned by this function.
	*/
	return errorString;
}

/*
*	Usually C functions use int as a return type for the main method
*/
void main( void )
{
	int err = Do_Something();
	if ( err )
	{
		printf( "%s\n", GetErrorString( err ) );
	}
}