package java01.array;

import java.util.Arrays;

public class frequancy {
	public static void main(String[] args) {
		int[] arr = {3, 2, 6, 6, 4, 3, 6, 7, 1, 1, 1, 5, 9};
		
		int[] used = new int[10];
		
		for(int num:arr) {
			used[num]++;
		}
		
		System.out.println(Arrays.toString(used));
	}
}
