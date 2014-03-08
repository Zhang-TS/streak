import java.util.Scanner;

public class SelectionSort
{
	public static void main(String[] args){
		int i, j, n, array[];

		Scanner in = new Scanner(System.in);
		System.out.println("Enter number of elements");
	
		n = in.nextInt();
		array = new int[n];

		System.out.println("Enter " + n +" integers");

		for(i = 0; i < n; i++)
			array[i] = in.nextInt();
		
		/**
		 * selection sort
		 */
		//only need to sort the first n-1 number of elements
		//the last one is default to be the largest
		for(j = 0; j < n - 1; j++)
		{
			int key = array[j];
			int index = j;

			//find the smallest number in the remaining array
			for(i = j+1; i < n; i++)
			{
				if(array[i] < key){
					key = array[i];
					index = i;
				}
			}

			//exchange value at j with the found value at index
			array[index] = array[j];
			array[j] = key;
			
		}
	

		for(i = 0; i < n; i++)
			System.out.println(array[i]);
	}
}
	
