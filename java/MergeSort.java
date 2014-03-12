import java.util.Scanner;

public class MergeSort
{
	public static final int SENTINAL = 10000000;

	public static void main(String[] args){
		int i, j, n, array[];

			Scanner in = new Scanner(System.in);
			System.out.println("Enter number of elements");
			
			n = in.nextInt();
			array = new int[n];
		
			System.out.println("Enter " + n + " integers");
	
			for(i = 0; i < n; i++)
				array[i] = in.nextInt();

			/**
			 *Merge Sort
			 */
			mergeSort(array, 0, n-1);
			for(i= 0; i < n; i++)
				System.out.print(array[i]+ " ");

			System.out.println();
			
	}

	private static void mergeSort(int[] array, int idx_s, int idx_e)
	{
		if(idx_e <= idx_s){
			return;
		}
		int idx_m = (idx_e-idx_s) / 2 + idx_s;
		mergeSort(array, idx_s, idx_m);
		mergeSort(array, idx_m+1, idx_e);
		merge(array, idx_s, idx_e, idx_m);
	}

	private static void merge(int[] array, int idx_s, int idx_e, int idx_m)
	{
		int[] sub_array_1 = new int[idx_m - idx_s + 2]; //include the middle number and one more senital value
		int[] sub_array_2 = new int[idx_e - idx_m + 1]; //include one more senital value
		
		for(int i = 0; i < idx_m - idx_s + 1; i++)
		{
			sub_array_1[i] = array[idx_s + i];
		}
		sub_array_1[idx_m-idx_s + 1] = SENTINAL;

		for(int i = 0; i < idx_e - idx_m; i++)
		{
			sub_array_2[i] = array[idx_m + 1 + i];
		}
		sub_array_2[idx_e - idx_m] = SENTINAL;

		/**
		 *merge
		 */
		int i1 = 0;
		int i2 = 0;
		for(int i = idx_s ; i < idx_e + 1; i++)
		{
			if(sub_array_1[i1] < sub_array_2[i2]){
				array[i] = sub_array_1[i1];
				i1++;
			}else{
				array[i] = sub_array_2[i2];
				i2++;
			}
		}

	}
}
