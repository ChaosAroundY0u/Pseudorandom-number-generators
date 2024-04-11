package first_element_sort;

//import java.util.ArrayList;
import java.util.Arrays;
import java.util.Random;
//import java.util.stream.IntStream;

public class Main {
	public static int[] concatenate(int[] a, int[] b, int[] c) {
        int aLen = a.length;
        int bLen = b.length;
        int cLen = c.length;
        int[] result = new int[aLen + bLen + cLen];
        System.arraycopy(a, 0, result, 0, aLen);
        System.arraycopy(b, 0, result, aLen, bLen);
        System.arraycopy(c, 0, result, aLen + bLen, cLen);
        return result;
	}
	
	public static int[] sort(int[] arr) {
		if (arr.length <= 1)
			return arr;
		
		int a = arr[0];
		int[] left = new int[arr.length];
        int leftSize = 0;
        int[] right = new int[arr.length];
        int rightSize = 0;
        
		for (int i = 1; i < arr.length; i++) {
            if (arr[i] > a) right[rightSize++] = arr[i];
            else left[leftSize++] = arr[i];   
        }
		
		int[] sortedLeft = Arrays.copyOfRange(left, 0, leftSize);
        int[] sortedRight = Arrays.copyOfRange(right, 0, rightSize);
		
		return concatenate(sort(sortedLeft), new int[]{a}, sort(sortedRight));
	}
	
	public static void main(String[] args) {
		Random rd = new Random();
		int[] array = new int[20];
		for (int i = 0; i < array.length; i++) {
			array[i] = rd.nextInt(100 + 100 + 1) - 100; // .nextInt(max - min + 1) + min; (creates number between max and min)
			System.out.print(array[i] + " ");
		}
		System.out.println();
		int[] sorted_array = sort(array);
		for (int j = 0; j < array.length; j++)
			System.out.print(sorted_array[j] + " ");
	}
}